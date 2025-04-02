import warnings
from typing import List

import numpy as np
from shapely.geometry import LinearRing, MultiPolygon, Polygon
from shapely.geometry.base import BaseGeometry

from .geometry_utils import calculate_azimuth_angle, calculate_distance
from .line_operations import (
    calculate_line_intersection,
    calculate_parallel_line_distance,
    create_line_equation,
    project_point_to_line,
)
from .rotation import rotate_point_clockwise, rotate_point_counterclockwise


def find_nearest_target_angle(
    current_azimuth: float, main_direction: float, allow_45_degree: bool
) -> float:
    """
    Finds the closest allowed target azimuth angle (0-360).
    """
    # Calculate angular difference relative to main_direction, normalize to [-180, 180]
    diff_angle = (current_azimuth - main_direction + 180) % 360 - 180

    # Define potential offsets from the main direction
    allowed_offsets = []
    if allow_45_degree:
        # Use offsets like 0, 45, 90, 135, 180, -45, -90, -135
        # Note: 180 and -180 are equivalent, 225 is -135, 270 is -90, 315 is -45
        allowed_offsets = [0.0, 45.0, 90.0, 135.0, 180.0, -45.0, -90.0, -135.0]
    else:
        # Use offsets 0, 90, 180, -90 (or 270)
        allowed_offsets = [0.0, 90.0, 180.0, -90.0]

    # Find the offset that minimizes the absolute difference to diff_angle
    best_offset = 0.0
    min_angle_dist = 181.0  # Start with a value larger than max possible diff (180)

    for offset in allowed_offsets:
        # Calculate the shortest angle between diff_angle and the current offset
        d = (diff_angle - offset + 180) % 360 - 180
        if abs(d) < min_angle_dist:
            min_angle_dist = abs(d)
            best_offset = offset

    # Calculate the final target azimuth by adding the best offset to the main direction
    # Normalize to [0, 360)
    target_azimuth = (main_direction + best_offset + 360) % 360
    return target_azimuth


def enforce_angles_post_process(
    points: List[np.ndarray],
    main_direction: float,
    allow_45_degree: bool,
    angle_tolerance: float = 0.1,  # Tolerance in degrees
    max_iterations: int = 2,  # Number of passes to allow adjustments to settle
) -> List[np.ndarray]:
    """
    Adjusts vertices iteratively to enforce target angles for each segment.
    Runs multiple iterations as adjusting one segment can affect adjacent ones.

    Parameters:
    -----------
    points : list[np.ndarray]
        List of numpy arrays representing polygon vertices. Assumed NOT closed
        (last point != first point). Length N >= 3.
    main_direction : float
        The main direction angle in degrees (0-360).
    allow_45_degree : bool
        Whether to allow 45-degree angles.
    angle_tolerance : float
         Allowable deviation from target angle in degrees.
    max_iterations : int
         Maximum number of full passes to adjust angles.

    Returns:
    --------
    list[np.ndarray]
        List of adjusted vertices (N points).
    """
    if len(points) < 3:
        return points  # Not enough points to form segments

    adjusted_points = [p.copy() for p in points]  # Work on a copy
    num_points = len(adjusted_points)

    for iteration in range(max_iterations):
        max_angle_diff_this_iter = 0.0
        changed = False  # Flag to track if any changes were made in this iteration

        for i in range(num_points):
            p1_idx = i
            p2_idx = (i + 1) % num_points  # Wrap around for the end point index

            p1 = adjusted_points[p1_idx]
            p2 = adjusted_points[p2_idx]

            # Avoid issues with coincident points before calculating angle
            dist = calculate_distance(p1, p2)
            if dist < 1e-7:
                # Coincident points have undefined angle, skip adjustment for this segment
                continue

            current_azimuth = calculate_azimuth_angle(p1, p2)
            target_azimuth = find_nearest_target_angle(
                current_azimuth, main_direction, allow_45_degree
            )

            # Calculate shortest rotation angle needed (positive for counter-clockwise)
            rotation_diff = (target_azimuth - current_azimuth + 180) % 360 - 180

            # Track the maximum deviation found in this iteration
            max_angle_diff_this_iter = max(max_angle_diff_this_iter, abs(rotation_diff))

            # Only rotate if the difference significantly exceeds tolerance
            # Use a slightly larger threshold for making changes to prevent jitter
            if abs(rotation_diff) > angle_tolerance:
                changed = True  # Mark that an adjustment was made
                # Rotate p2 around p1
                # Pass tuples to rotation functions (assuming they expect tuples)
                p1_rot = tuple(p1)
                p2_rot = tuple(p2)

                # Perform rotation (rotation_diff > 0 means counter-clockwise)
                if rotation_diff > 0:
                    new_p2_tuple = rotate_point_counterclockwise(
                        p2_rot, p1_rot, rotation_diff
                    )
                else:
                    new_p2_tuple = rotate_point_clockwise(
                        p2_rot, p1_rot, abs(rotation_diff)
                    )

                # Update the endpoint in the list for the *next* segment's calculation
                adjusted_points[p2_idx] = np.array(new_p2_tuple)

        # Check for convergence: If no points were adjusted significantly in this pass, stop.
        if not changed:
            # print(f"Angle enforcement converged after {iteration + 1} iterations.")
            break

    # Return the list of N adjusted unique points
    return adjusted_points


def regularize_coordinate_array(
    coordinates: np.ndarray,
    parallel_threshold: float = 3,
    allow_45_degree: bool = True,
    angle_enforcement_tolerance: float = 0.1,  # Add tolerance parameter
) -> np.ndarray:
    """
    Regularize polygon coordinates by aligning edges to be either parallel
    or perpendicular (or 45 deg) to the main direction, with a
    post-processing step to enforce angles.

    Parameters:
    -----------
    coordinates : numpy.ndarray
        Array of coordinates for a polygon ring (shape: n x 2).
        Assumed closed (first point == last point).
    parallel_threshold : float
        Distance threshold for considering parallel lines as needing connection.
    allow_45_degree : bool
        If True, allows 45-degree orientations relative to the main direction.
    angle_enforcement_tolerance : float
        Maximum allowed deviation (degrees) from target angle in the final output.

    Returns:
    --------
    numpy.ndarray
        Regularized coordinates array (n x 2), closed (first == last).
    """
    if (
        len(coordinates) < 4
    ):  # Need at least 3 unique points + closing point for a polygon
        warnings.warn("Not enough coordinates to regularize. Returning original.")
        return coordinates

    # Remove duplicate closing point for processing, if present
    if np.allclose(coordinates[0], coordinates[-1]):
        processing_coords = coordinates[:-1]
    else:
        processing_coords = coordinates  # Assume it wasn't closed

    if len(processing_coords) < 3:
        warnings.warn(
            "Not enough unique coordinates to regularize. Returning original."
        )
        return coordinates  # Return original closed coords

    # Analyze edges to find properties and main direction
    # Use the non-closed version for edge analysis
    edge_data = analyze_edges(processing_coords)

    # Orient edges based on main direction
    oriented_edges, edge_orientations = orient_edges(
        processing_coords, edge_data, allow_45_degree=allow_45_degree
    )

    # Connect and regularize edges
    # This returns a list of np.ndarray points, likely NOT closed
    initial_regularized_points = connect_regularized_edges(
        oriented_edges, edge_orientations, parallel_threshold
    )

    if not initial_regularized_points or len(initial_regularized_points) < 3:
        warnings.warn("Regularization resulted in too few points. Returning original.")
        # Decide what to return: maybe the simplified input or original?
        # Returning original for safety:
        return coordinates

    # *** NEW: Post-processing step to enforce angles ***
    final_regularized_points_list = enforce_angles_post_process(
        initial_regularized_points,
        edge_data["main_direction"],
        allow_45_degree,
        angle_tolerance=angle_enforcement_tolerance,
    )

    if not final_regularized_points_list or len(final_regularized_points_list) < 3:
        warnings.warn(
            "Angle enforcement resulted in too few points. Returning original."
        )
        return coordinates

    # Convert list of arrays back to a single numpy array and ensure closure
    final_coords_array = np.array([p for p in final_regularized_points_list])
    # Ensure the final array is explicitly closed for Shapely
    closed_final_coords = np.vstack([final_coords_array, final_coords_array[0]])

    return closed_final_coords  # Return the closed array


# In regularization.py


def analyze_edges(coordinates: np.ndarray):  # Expects unclosed coordinates (N x 2)
    """
    Analyze edges to find their lengths, angles, and identify the main direction
    based on angle distribution, optimized for buildings where most lines are
    perpendicular or parallel.

    Handles wrap-around for the segment connecting the last point to the first.

    Parameters:
    -----------
    coordinates : numpy.ndarray
        Polygon coordinates (shape: N x 2), assumed NOT closed.

    Returns:
    --------
    dict
        Dictionary containing edge data including lengths, angles, indices, and main direction
    """
    edge_lengths = []
    azimuth_angles = []
    edge_indices = []
    num_points = len(coordinates)

    if num_points < 3:
        # Return empty or default data if not enough points for a polygon
        return {
            "edge_lengths": [],
            "azimuth_angles": [],
            "edge_indices": [],
            "longest_edge_index": -1,
            "main_direction": 0,
            "angle_distribution": [],
        }

    for i in range(num_points):
        current_idx = i
        next_idx = (i + 1) % num_points  # Handles wrap-around: N-1 -> 0

        current_point = coordinates[current_idx]
        next_point = coordinates[next_idx]

        edge_length = calculate_distance(current_point, next_point)
        # Check for coincident points before calculating azimuth
        if edge_length < 1e-9:  # Use a small tolerance
            # Optionally skip this edge or handle as needed
            warnings.warn(
                f"Skipping zero-length edge between index {current_idx} and {next_idx}"
            )
            continue  # Skip this degenerate edge

        azimuth = calculate_azimuth_angle(current_point, next_point)

        # Only include edges with meaningful length
        # if edge_length > 0.001: # Keep your original threshold or adjust
        edge_lengths.append(edge_length)
        azimuth_angles.append(azimuth)
        # Store the indices used for this edge
        edge_indices.append([current_idx, next_idx])

    # --- Rest of the angle analysis logic remains the same ---
    # (Using the collected azimuth_angles and edge_lengths)

    # Handle case where no valid edges were found
    if not edge_lengths:
        return {
            "edge_lengths": [],
            "azimuth_angles": [],
            "edge_indices": [],
            "longest_edge_index": -1,
            "main_direction": 0,
            "angle_distribution": [],
        }

    # Normalize angles...
    normalized_angles = [angle % 180 for angle in azimuth_angles]
    orthogonal_angles = [angle % 90 for angle in normalized_angles]

    # Create histogram bins...
    bin_size = 5
    num_bins = int(90 // bin_size)
    angle_bins = [0] * num_bins

    # Count angles...
    for angle, length in zip(orthogonal_angles, edge_lengths):
        # Ensure bin_index is within bounds (can happen if angle is exactly 90)
        bin_index = min(int(angle // bin_size), num_bins - 1)
        angle_bins[bin_index] += length

    # Find dominant direction...
    # Check if angle_bins is empty or all zeros
    if not angle_bins or all(count == 0 for count in angle_bins):
        main_direction = 0  # Default direction if no clear signal
        warnings.warn("Could not determine main direction from angle distribution.")
    else:
        main_bin = np.argmax(angle_bins)
        raw_main_direction = (main_bin * bin_size) + (bin_size / 2)

        # Determine final main direction (0-90 or 90-180 range)...
        direction1 = raw_main_direction
        direction2 = (raw_main_direction + 90) % 180
        support1 = 0
        support2 = 0
        for angle, length in zip(normalized_angles, edge_lengths):
            dist1 = min(
                abs(angle - direction1),
                abs(angle - direction1 - 180),
                abs(angle - direction1 + 180),
            )
            dist2 = min(
                abs(angle - direction2),
                abs(angle - direction2 - 180),
                abs(angle - direction2 + 180),
            )
            if dist1 <= dist2:  # Give slight preference to dir1 in case of tie
                support1 += length
            else:
                support2 += length
        main_direction = direction1 if support1 >= support2 else direction2

    # Find longest edge index (relative to the filtered edge_lengths list)
    longest_edge_idx_in_list = np.argmax(edge_lengths) if edge_lengths else -1
    # The actual index pair can be retrieved using edge_indices[longest_edge_idx_in_list] if needed

    return {
        "edge_lengths": edge_lengths,
        "azimuth_angles": azimuth_angles,
        "edge_indices": edge_indices,  # These indices now correctly refer to the input 'coordinates' array
        "longest_edge_index": longest_edge_idx_in_list,  # Index within the 'edge_lengths' list
        "main_direction": main_direction,
        "angle_distribution": list(
            zip([i * bin_size + bin_size / 2 for i in range(num_bins)], angle_bins)
        ),
    }


def orient_edges(
    simplified_coordinates: np.ndarray,
    edge_data: dict,
    allow_45_degree: bool = True,
    diagonal_threshold_reduction: float = 15.0,
):
    """
    Orient edges to be parallel or perpendicular (or optionally 45 degrees)
    to the main direction determined by angle distribution analysis.

    Parameters:
    -----------
    simplified_coordinates : numpy.ndarray
        Simplified polygon coordinates (shape: n x 2, assumed closed).
    edge_data : dict
        Dictionary containing edge analysis data ('azimuth_angles', 'edge_indices',
        'main_direction').
    allow_45_degree : bool, optional
        If True, allows edges to be oriented at 45-degree angles relative
        to the main direction. Defaults to True.
    diagonal_threshold_reduction : float, optional
        Angle in degrees to subtract from the 45-degree snapping thresholds,
        making diagonal (45°) orientations less likely. Defaults to 15.0.

    Returns:
    --------
    tuple
        Tuple containing:
        - oriented_edges (numpy.ndarray): Array of [start, end] points for each oriented edge.
        - edge_orientations (list): List of orientation codes for each edge.
          - 0: Parallel or anti-parallel (0, 180 deg relative to main_direction)
          - 1: Perpendicular (90, 270 deg relative to main_direction)
          - 2: Diagonal (45, 135, 225, 315 deg relative to main_direction) - only if allow_45=True.
    """

    # edge_data =
    oriented_edges = []
    # Orientation codes: 0=Parallel/AntiParallel, 1=Perpendicular, 2=Diagonal(45deg)
    edge_orientations = []

    azimuth_angles = edge_data["azimuth_angles"]
    edge_indices = edge_data["edge_indices"]
    main_direction = edge_data["main_direction"]

    # Small tolerance for floating point comparisons
    tolerance = 1e-9

    for i, (azimuth, (start_idx, end_idx)) in enumerate(
        zip(azimuth_angles, edge_indices)
    ):
        # Calculate the shortest angle difference from edge azimuth to main_direction
        # Result is in the range [-180, 180]
        diff_angle = (azimuth - main_direction + 180) % 360 - 180

        target_offset = (
            0.0  # The desired angle relative to main_direction (0, 45, 90 etc.)
        )
        orientation_code = 0

        if allow_45_degree:
            # Calculate how close we are to each of the key orientations
            dist_to_0 = min(abs(diff_angle % 180), abs((diff_angle % 180) - 180))
            dist_to_90 = min(abs((diff_angle % 180) - 90), abs((diff_angle % 180) - 90))
            dist_to_45 = min(
                abs((diff_angle % 180) - 45), abs((diff_angle % 180) - 135)
            )

            # Apply down-weighting to 45-degree angles
            # This effectively shrinks the zone where angles snap to 45 degrees
            if dist_to_45 <= (22.5 - diagonal_threshold_reduction):
                # Close enough to 45/135/225/315 degrees (accounting for down-weighting)
                angle_mod = diff_angle % 90
                if angle_mod < 45:
                    target_offset = (diff_angle // 90) * 90 + 45
                else:
                    target_offset = (diff_angle // 90 + 1) * 90 - 45

                # Determine which diagonal direction we're closer to
                # Use modulo 180 to differentiate between 45/225 and 135/315
                normalized_angle = (main_direction + target_offset) % 180
                if 0 <= normalized_angle < 90:
                    # This is closer to 45 degrees
                    orientation_code = 2  # 45/225 degrees
                else:
                    # This is closer to 135 degrees
                    orientation_code = 3  # 135/315 degrees
            elif dist_to_0 <= dist_to_90:
                # Closer to 0/180 degrees
                target_offset = round(diff_angle / 180.0) * 180.0
                orientation_code = 0
            else:
                # Closer to 90/270 degrees
                target_offset = round(diff_angle / 90.0) * 90.0
                if abs(target_offset % 180) < tolerance:
                    # If rounding diff_angle/90 gave 0 or 180, force to 90 or -90
                    target_offset = 90.0 if diff_angle > 0 else -90.0
                orientation_code = 1

        else:  # Original logic (refined): Snap only to nearest 90 degrees
            if abs(diff_angle) < 45.0:  # Closer to parallel/anti-parallel (0 or 180)
                # Snap to 0 or 180, whichever is closer
                target_offset = round(diff_angle / 180.0) * 180.0
                orientation_code = 0
            else:  # Closer to perpendicular (+90 or -90/270)
                # Snap to +90 or -90, whichever is closer
                target_offset = round(diff_angle / 90.0) * 90.0
                # Ensure it's not actually 0 or 180 (should be handled above, but safety check)
                if abs(target_offset % 180) < tolerance:
                    # If rounding diff_angle/90 gave 0 or 180, force to 90 or -90
                    target_offset = 90.0 if diff_angle > 0 else -90.0
                orientation_code = 1

        # Calculate the rotation angle needed to achieve the target orientation
        # Calculate shortest rotation angle
        rotation_angle = (main_direction + target_offset - azimuth + 180) % 360 - 180

        # Perform rotation
        start_point = np.array(simplified_coordinates[start_idx], dtype=float)
        end_point = np.array(simplified_coordinates[end_idx], dtype=float)

        # Rotate the edge to align with the target orientation
        rotated_edge = rotate_edge(start_point, end_point, rotation_angle)

        oriented_edges.append(rotated_edge)
        edge_orientations.append(orientation_code)

    return np.array(oriented_edges, dtype=object), edge_orientations


def rotate_edge(start_point: np.ndarray, end_point: np.ndarray, rotation_angle: float):
    """
    Rotate an edge around its midpoint by the given angle

    Parameters:
    -----------
    start_point : numpy.ndarray
        Start point of the edge
    end_point : numpy.ndarray
        End point of the edge
    rotation_angle : float
        Angle to rotate by in degrees

    Returns:
    --------
    list
        List containing the rotated start and end points
    """
    midpoint = (start_point + end_point) / 2

    if rotation_angle > 0:
        rotated_start = rotate_point_counterclockwise(
            start_point, midpoint, np.abs(rotation_angle)
        )
        rotated_end = rotate_point_counterclockwise(
            end_point, midpoint, np.abs(rotation_angle)
        )
    elif rotation_angle < 0:
        rotated_start = rotate_point_clockwise(
            start_point, midpoint, np.abs(rotation_angle)
        )
        rotated_end = rotate_point_clockwise(
            end_point, midpoint, np.abs(rotation_angle)
        )
    else:
        rotated_start = start_point
        rotated_end = end_point

    return [np.array(rotated_start), np.array(rotated_end)]


#     return regularized_points
def connect_regularized_edges(
    oriented_edges: np.ndarray, edge_orientations: list, parallel_threshold: float
):
    """
    Connect oriented edges to form a regularized polygon

    Parameters:
    -----------
    oriented_edges : numpy.ndarray
        Array of oriented edges
    edge_orientations : list
        List of edge orientations (0=parallel, 1=perpendicular)
    parallel_threshold : float
        Distance threshold for considering parallel lines as needing connection

    Returns:
    --------
    list
        List of regularized points forming the polygon
    """
    regularized_points = []

    # Process all edges including the connection between last and first edge
    for i in range(len(oriented_edges)):
        current_index = i
        next_index = (i + 1) % len(oriented_edges)  # Wrap around to first edge

        current_edge_start = oriented_edges[current_index][0]
        current_edge_end = oriented_edges[current_index][1]
        next_edge_start = oriented_edges[next_index][0]
        next_edge_end = oriented_edges[next_index][1]

        current_orientation = edge_orientations[current_index]
        next_orientation = edge_orientations[next_index]

        if current_orientation != next_orientation:
            # Handle perpendicular edges
            regularized_points.append(
                handle_perpendicular_edges(
                    current_edge_start, current_edge_end, next_edge_start, next_edge_end
                )
            )
        else:
            # Handle parallel edges
            new_points = handle_parallel_edges(
                current_edge_start,
                current_edge_end,
                next_edge_start,
                next_edge_end,
                parallel_threshold,
                next_index,
                oriented_edges,
            )
            regularized_points.extend(new_points)

    return regularized_points


def handle_perpendicular_edges(
    current_edge_start, current_edge_end, next_edge_start, next_edge_end
):
    """
    Handle intersection of perpendicular edges

    Parameters:
    -----------
    current_edge_start : numpy.ndarray
        Start point of current edge
    current_edge_end : numpy.ndarray
        End point of current edge
    next_edge_start : numpy.ndarray
        Start point of next edge
    next_edge_end : numpy.ndarray
        End point of next edge

    Returns:
    --------
    numpy.ndarray
        Intersection point of the two edges
    """
    line1 = create_line_equation(current_edge_start, current_edge_end)
    line2 = create_line_equation(next_edge_start, next_edge_end)

    intersection_point = calculate_line_intersection(line1, line2)
    if intersection_point:
        # Convert to numpy array if not already
        return np.array(intersection_point)
    else:
        # If lines are parallel (shouldn't happen with perpendicular check)
        # add the end point of current edge
        return current_edge_end


def handle_parallel_edges(
    current_edge_start,
    current_edge_end,
    next_edge_start,
    next_edge_end,
    parallel_threshold,
    next_index,
    oriented_edges,
):
    """
    Handle connection between parallel edges

    Parameters:
    -----------
    current_edge_start : numpy.ndarray
        Start point of current edge
    current_edge_end : numpy.ndarray
        End point of current edge
    next_edge_start : numpy.ndarray
        Start point of next edge
    next_edge_end : numpy.ndarray
        End point of next edge
    parallel_threshold : float
        Distance threshold for considering parallel lines as needing connection
    next_index : int
        Index of the next edge
    oriented_edges : numpy.ndarray
        Array of all oriented edges

    Returns:
    --------
    list
        List of points to add to the regularized polygon
    """
    line1 = create_line_equation(current_edge_start, current_edge_end)
    line2 = create_line_equation(next_edge_start, next_edge_end)
    line_distance = calculate_parallel_line_distance(line1, line2)

    new_points = []

    if line_distance < parallel_threshold:
        # Shift next edge to align with current edge
        projected_point = project_point_to_line(
            next_edge_start[0],
            next_edge_start[1],
            current_edge_start[0],
            current_edge_start[1],
            current_edge_end[0],
            current_edge_end[1],
        )
        # Ensure projected_point is a numpy array
        new_points.append(np.array(projected_point))

        # Update next edge starting point
        oriented_edges[next_index][0] = np.array(projected_point)
        oriented_edges[next_index][1] = np.array(
            project_point_to_line(
                next_edge_end[0],
                next_edge_end[1],
                current_edge_start[0],
                current_edge_start[1],
                current_edge_end[0],
                current_edge_end[1],
            )
        )
    else:
        # Add connecting segment between edges
        midpoint = (current_edge_end + next_edge_start) / 2
        connecting_point1 = project_point_to_line(
            midpoint[0],
            midpoint[1],
            current_edge_start[0],
            current_edge_start[1],
            current_edge_end[0],
            current_edge_end[1],
        )
        connecting_point2 = project_point_to_line(
            midpoint[0],
            midpoint[1],
            next_edge_start[0],
            next_edge_start[1],
            next_edge_end[0],
            next_edge_end[1],
        )
        # Convert points to numpy arrays
        new_points.append(np.array(connecting_point1))
        new_points.append(np.array(connecting_point2))

    return new_points


def regularize_single_polygon(
    polygon: Polygon,
    parallel_threshold: float = 3,
    allow_45_degree: bool = True,
    allow_circles: bool = True,
    circle_threshold: float = 0.90,
) -> Polygon:
    """
    Regularize a Shapely polygon by aligning edges to principal directions

    Parameters:
    -----------
    polygon : shapely.geometry.Polygon
        Input polygon to regularize
    parallel_threshold : float
        Distance threshold for parallel line handling

    Returns:
    --------
    shapely.geometry.Polygon
        Regularized polygon
    """

    # Handle exterior ring

    exterior_coordinates = np.array(polygon.exterior.coords)
    # append the first point to the end to close the polygon

    # print(exterior_coordinates)
    regularized_exterior = regularize_coordinate_array(
        exterior_coordinates,
        parallel_threshold=parallel_threshold,
        allow_45_degree=allow_45_degree,
    )
    # print(regularized_exterior)
    if allow_circles:
        area = polygon.area
        centroid = polygon.centroid
        radius = np.sqrt(area / np.pi)
        perfect_circle = centroid.buffer(radius, resolution=42)
        # Check if the polygon is close to a circle using iou
        iou = (
            perfect_circle.intersection(polygon).area
            / perfect_circle.union(polygon).area
        )
        if iou > circle_threshold:
            # If the polygon is close to a circle, return the perfect circle
            regularized_exterior = np.array(
                perfect_circle.exterior.coords, dtype=object
            )

    # Handle interior rings (holes)
    regularized_interiors: List[np.ndarray] = []
    for interior in polygon.interiors:
        interior_coordinates = np.array(interior.coords)
        regularized_interior = regularize_coordinate_array(
            interior_coordinates,
            parallel_threshold=parallel_threshold,
            allow_45_degree=allow_45_degree,
        )
        regularized_interiors.append(regularized_interior)

    # Create new polygon
    try:
        # Convert coordinates to LinearRings
        exterior_ring = LinearRing(regularized_exterior)
        interior_rings = [LinearRing(r) for r in regularized_interiors]

        # Create regularized polygon
        regularized_polygon = Polygon(exterior_ring, interior_rings)
        return regularized_polygon
    except Exception as e:
        # If there's an error creating the polygon, return the original
        warnings.warn(f"Error creating regularized polygon: {e}. Returning original.")
        return polygon


def process_geometry(
    geometry: BaseGeometry,
    parallel_threshold: float,
    allow_45_degree: bool,
    allow_circles: bool,
    circle_threshold: float,
) -> BaseGeometry:
    """
    Process a single geometry, handling different geometry types

    Parameters:
    -----------
    geometry : shapely.geometry.BaseGeometry
        Input geometry to regularize
    parallel_threshold : float
        Distance threshold for parallel line handling

    Returns:
    --------
    shapely.geometry.BaseGeometry
        Regularized geometry
    """
    if isinstance(geometry, Polygon):
        return regularize_single_polygon(
            polygon=geometry,
            parallel_threshold=parallel_threshold,
            allow_45_degree=allow_45_degree,
            allow_circles=allow_circles,
            circle_threshold=circle_threshold,
        )
    elif isinstance(geometry, MultiPolygon):
        regularized_parts = [
            regularize_single_polygon(
                polygon=part,
                parallel_threshold=parallel_threshold,
                allow_45_degree=allow_45_degree,
                allow_circles=allow_circles,
                circle_threshold=circle_threshold,
            )
            for part in geometry.geoms
        ]
        return MultiPolygon(regularized_parts)
    else:
        # Return unmodified if not a polygon
        warnings.warn(
            f"Unsupported geometry type: {type(geometry)}. Returning original."
        )
        return geometry
