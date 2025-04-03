import numpy as np
import pyproj
import requests
import time
from typing import Dict, Any, Tuple, Optional, Union, List, Callable

# Constants
DEG_TO_RAD = np.pi / 180.0
RAD_TO_DEG = 180.0 / np.pi
WGS84_ELLIPSOID = pyproj.Geod(ellps='WGS84')
USGS_EPQS_URL = "https://epqs.nationalmap.gov/v1/json"


def fov_to_focal_length(fov_degrees: float, sensor_dimension: float) -> float:
    """
    Convert a field of view angle to focal length.
    
    Args:
        fov_degrees: Field of view angle in degrees
        sensor_dimension: Relevant sensor dimension in the same unit as the desired focal length
        
    Returns:
        Focal length in the same unit as sensor_dimension
    """
    fov_rad = fov_degrees * DEG_TO_RAD
    return sensor_dimension / (2 * np.tan(fov_rad / 2))


def camera_matrix_from_fov(h_fov_degrees: float, v_fov_degrees: float, 
                         principal_point_x: float, principal_point_y: float,
                         image_width: int, image_height: int) -> np.ndarray:
    """
    Build the camera intrinsic matrix from field of view angles.
    
    Args:
        h_fov_degrees: Horizontal field of view in degrees
        v_fov_degrees: Vertical field of view in degrees
        principal_point_x: X-coordinate of the principal point in pixels
        principal_point_y: Y-coordinate of the principal point in pixels
        image_width: Width of the image in pixels
        image_height: Height of the image in pixels
        
    Returns:
        3x3 camera intrinsic matrix
    """
    # Calculate focal length in pixels
    fx = image_width / (2 * np.tan(h_fov_degrees * DEG_TO_RAD / 2))
    fy = image_height / (2 * np.tan(v_fov_degrees * DEG_TO_RAD / 2))
    
    return np.array([
        [fx, 0, principal_point_x],
        [0, fy, principal_point_y],
        [0, 0, 1]
    ])


def rotation_matrix(roll: float, pitch: float, yaw: float) -> np.ndarray:
    """
    Build rotation matrix from roll, pitch, yaw angles (in degrees).
    
    Args:
        roll: Roll angle in degrees (rotation around x-axis)
        pitch: Pitch angle in degrees (rotation around y-axis)
        yaw: Yaw angle in degrees (rotation around z-axis)
        
    Returns:
        3x3 rotation matrix
    """
    # Convert to radians
    roll_rad = roll * DEG_TO_RAD
    pitch_rad = pitch * DEG_TO_RAD
    yaw_rad = yaw * DEG_TO_RAD
    
    # Build rotation matrices for each axis
    R_roll = np.array([
        [1, 0, 0],
        [0, np.cos(roll_rad), -np.sin(roll_rad)],
        [0, np.sin(roll_rad), np.cos(roll_rad)]
    ])
    
    R_pitch = np.array([
        [np.cos(pitch_rad), 0, np.sin(pitch_rad)],
        [0, 1, 0],
        [-np.sin(pitch_rad), 0, np.cos(pitch_rad)]
    ])
    
    R_yaw = np.array([
        [np.cos(yaw_rad), -np.sin(yaw_rad), 0],
        [np.sin(yaw_rad), np.cos(yaw_rad), 0],
        [0, 0, 1]
    ])
    
    # Combine rotations: R = R_yaw * R_pitch * R_roll
    # Note: The order matters and depends on the convention used
    R = R_yaw @ R_pitch @ R_roll
    
    return R


def pixel_to_ray(pixel_x: float, pixel_y: float, K_inv: np.ndarray, R: np.ndarray) -> np.ndarray:
    """
    Convert a pixel coordinate to a ray direction in world space.
    
    Args:
        pixel_x: X-coordinate of the pixel
        pixel_y: Y-coordinate of the pixel
        K_inv: Inverse of the camera intrinsic matrix
        R: Rotation matrix representing camera orientation
        
    Returns:
        3D ray direction vector (normalized)
    """
    # Convert pixel to normalized camera coordinates
    p_cam = np.array([pixel_x, pixel_y, 1.0])
    ray_cam = K_inv @ p_cam
    
    # Rotate ray to world space
    ray_world = R @ ray_cam
    
    # Normalize ray direction
    ray_world = ray_world / np.linalg.norm(ray_world)
    
    return ray_world


class USGSElevationService:
    """
    Class for querying elevation data from USGS Elevation Point Query Service (EPQS).
    """
    
    def __init__(self, default_height: float = 0.0, cache_size: int = 100, max_retries: int = 2, timeout: int = 3):
        """
        Initialize the USGS elevation service.
        
        Args:
            default_height: Default height to return if the USGS service fails
            cache_size: Maximum number of elevation points to cache
            max_retries: Maximum number of retry attempts for failed requests
            timeout: Timeout in seconds for the API request
        """
        self.default_height = default_height
        self.max_retries = max_retries
        self.timeout = timeout
        self.cache = {}  # Simple cache for elevation data
        self.cache_size = cache_size
        self.connection_error = False  # Flag to indicate if there was a connection error
    
    def get_elevation(self, lat: float, lon: float) -> float:
        """
        Get the elevation at a given latitude and longitude.
        
        Args:
            lat: Latitude in degrees
            lon: Longitude in degrees
            
        Returns:
            Elevation in meters, or default_height if service fails
        """
        # Round to 5 decimal places for caching (about 1.1 meters precision)
        cache_key = (round(lat, 5), round(lon, 5))
        
        # Check if elevation is already in cache
        if cache_key in self.cache:
            return self.cache[cache_key]
        
        # Prepare API request
        params = {
            "x": lon,
            "y": lat,
            "units": "Meters",
            "output": "json"
        }
        
        elevation = self.default_height
        
        # Try to get elevation from USGS service with retries
        for attempt in range(self.max_retries + 1):
            try:
                response = requests.get(USGS_EPQS_URL, params=params, timeout=self.timeout)
                
                if response.status_code == 200:
                    # Parse response
                    data = response.json()
                    
                    # Check if the response contains elevation data
                    if "value" in data:
                        elevation = float(data["value"])
                        break
            except (requests.RequestException, ValueError, KeyError) as e:
                print(f"USGS elevation service error (attempt {attempt+1}/{self.max_retries+1}): {str(e)}")
                
                # If this is the last attempt, mark connection error
                if attempt == self.max_retries:
                    self.connection_error = True
                
                # Wait before retry (exponential backoff)
                if attempt < self.max_retries:
                    time.sleep(0.5 * (2 ** attempt))
        
        # Add elevation to cache
        if len(self.cache) >= self.cache_size:
            # Remove a random entry if cache is full
            self.cache.pop(next(iter(self.cache)))
        
        self.cache[cache_key] = elevation
        
        return elevation
    
    def close(self):
        """
        Clean up resources.
        """
        # No need to close anything for the USGS service
        pass


def ray_ground_intersection(camera_pos: np.ndarray, ray_dir: np.ndarray, 
                          elevation_service: USGSElevationService,
                          ref_lat: float, ref_lon: float,
                          max_distance: float = 100000.0,
                          step_size: float = 100.0,
                          fine_step_size: float = 1.0) -> Optional[np.ndarray]:
    """
    Calculate the intersection of a ray with the ground using elevation data.
    
    Args:
        camera_pos: Camera position in ENU coordinates
        ray_dir: Ray direction (normalized)
        elevation_service: Service to get elevation data
        ref_lat: Reference latitude for ENU coordinate system
        ref_lon: Reference longitude for ENU coordinate system
        max_distance: Maximum distance to search for intersection
        step_size: Initial step size for ray marching
        fine_step_size: Fine step size for precise intersection
        
    Returns:
        Intersection point in ENU coordinates, or None if no intersection found
    """
    # Check if ray is pointing upward
    if ray_dir[2] >= 0:
        return None
    
    # Initialize distance along ray
    distance = 0.0
    
    # Create transformers for coordinate conversions
    transformer_to_lla = pyproj.Transformer.from_crs(
        {"proj": "tmerc", "lat_0": ref_lat, "lon_0": ref_lon},
        "epsg:4326",
        always_xy=True
    )
    
    # Coarse search
    while distance < max_distance:
        # Calculate point along ray
        point = camera_pos + distance * ray_dir
        
        # Convert ENU to geodetic (lon, lat, alt)
        lon, lat, _ = transformer_to_lla.transform(point[0], point[1], 0)
        
        # Get elevation at this point
        elevation = elevation_service.get_elevation(lat, lon)
        
        # Check if point is below ground
        if point[2] <= elevation:
            # Back up one step
            distance -= step_size
            break
        
        # Increment distance
        distance += step_size
    
    # Check if we've exceeded max distance
    if distance >= max_distance:
        return None
    
    # Fine search
    for _ in range(int(step_size / fine_step_size)):
        # Increment distance
        distance += fine_step_size
        
        # Calculate point along ray
        point = camera_pos + distance * ray_dir
        
        # Convert ENU to geodetic
        lon, lat, _ = transformer_to_lla.transform(point[0], point[1], 0)
        
        # Get elevation at this point
        elevation = elevation_service.get_elevation(lat, lon)
        
        # Check if point is below ground
        if point[2] <= elevation:
            # Adjust z-coordinate to ground level
            point[2] = elevation
            return point
    
    # If no intersection found in fine search, return the last point
    point = camera_pos + distance * ray_dir
    lon, lat, _ = transformer_to_lla.transform(point[0], point[1], 0)
    elevation = elevation_service.get_elevation(lat, lon)
    point[2] = elevation
    
    return point


def ecef_to_geodetic(x: float, y: float, z: float) -> Tuple[float, float, float]:
    """
    Convert ECEF coordinates to geodetic coordinates.
    
    Args:
        x: ECEF X coordinate
        y: ECEF Y coordinate
        z: ECEF Z coordinate
        
    Returns:
        Tuple of (latitude, longitude, altitude)
    """
    transformer = pyproj.Transformer.from_crs("epsg:4978", "epsg:4326", always_xy=True)
    lon, lat, alt = transformer.transform(x, y, z)
    return lat, lon, alt


def geodetic_to_ecef(lat: float, lon: float, alt: float) -> Tuple[float, float, float]:
    """
    Convert geodetic coordinates to ECEF coordinates.
    
    Args:
        lat: Latitude in degrees
        lon: Longitude in degrees
        alt: Altitude in meters
        
    Returns:
        Tuple of (ECEF X, ECEF Y, ECEF Z)
    """
    transformer = pyproj.Transformer.from_crs("epsg:4326", "epsg:4978", always_xy=True)
    x, y, z = transformer.transform(lon, lat, alt)
    return x, y, z


def enu_to_geodetic(enu_coords: np.ndarray, ref_lat: float, ref_lon: float, ref_alt: float) -> np.ndarray:
    """
    Convert ENU coordinates to geodetic coordinates.
    
    Args:
        enu_coords: ENU coordinates (East, North, Up) as a numpy array
        ref_lat: Reference latitude in degrees
        ref_lon: Reference longitude in degrees
        ref_alt: Reference altitude in meters
        
    Returns:
        Numpy array of [latitude, longitude, altitude]
    """
    # First, convert reference point to ECEF
    ref_x, ref_y, ref_z = geodetic_to_ecef(ref_lat, ref_lon, ref_alt)
    
    # Create rotation matrix for ENU to ECEF
    ref_lat_rad = ref_lat * DEG_TO_RAD
    ref_lon_rad = ref_lon * DEG_TO_RAD
    
    sin_lat = np.sin(ref_lat_rad)
    cos_lat = np.cos(ref_lat_rad)
    sin_lon = np.sin(ref_lon_rad)
    cos_lon = np.cos(ref_lon_rad)
    
    R = np.array([
        [-sin_lon, -sin_lat * cos_lon, cos_lat * cos_lon],
        [cos_lon, -sin_lat * sin_lon, cos_lat * sin_lon],
        [0, cos_lat, sin_lat]
    ])
    
    # Convert ENU to ECEF
    ecef_offset = R @ enu_coords
    ecef_coords = np.array([ref_x + ecef_offset[0], ref_y + ecef_offset[1], ref_z + ecef_offset[2]])
    
    # Convert ECEF to geodetic
    transformer_to_lla = pyproj.Transformer.from_crs("epsg:4978", "epsg:4326", always_xy=True)
    lon, lat, alt = transformer_to_lla.transform(ecef_coords[0], ecef_coords[1], ecef_coords[2])
    
    return np.array([lat, lon, alt])


def calculate_target_coordinates(config: Dict[str, Any]) -> Dict[str, Any]:
    """
    Calculate the real-world coordinates of a target from a camera image.
    
    Args:
        config: Configuration dictionary
        
    Returns:
        Dictionary with calculated target coordinates
    """
    # Extract camera parameters
    camera_lat = config["camera"]["position"]["latitude"]
    camera_lon = config["camera"]["position"]["longitude"]
    camera_alt = config["camera"]["position"]["altitude"]
    camera_heading = config["camera"]["position"]["heading"]
    
    roll = config["camera"]["orientation"]["roll"]
    pitch = config["camera"]["orientation"]["pitch"]
    yaw = config["camera"]["orientation"]["yaw"]
    
    # Apply heading to yaw if needed
    effective_yaw = yaw + camera_heading
    
    # Extract field of view parameters
    h_fov = config["camera"]["intrinsics"]["field_of_view"]["horizontal_degrees"]
    v_fov = config["camera"]["intrinsics"]["field_of_view"]["vertical_degrees"]
    
    principal_x = config["camera"]["intrinsics"]["principal_point"]["x"]
    principal_y = config["camera"]["intrinsics"]["principal_point"]["y"]
    
    image_width = config["camera"]["intrinsics"]["sensor_size"]["width"]
    image_height = config["camera"]["intrinsics"]["sensor_size"]["height"]
    
    # Extract target parameters
    target_pixel_x = config["target"]["pixel_coordinates"]["x"]
    target_pixel_y = config["target"]["pixel_coordinates"]["y"]
    
    # Use hardcoded default height for USGS fallback
    DEFAULT_HEIGHT = 0.0
    
    # Initialize USGS elevation service with good defaults for reliability
    usgs_service = USGSElevationService(
        default_height=DEFAULT_HEIGHT,
        cache_size=200,      # Larger cache to avoid repeat queries
        max_retries=3,       # More retries for better reliability
        timeout=5            # Longer timeout for slower connections
    )
    
    # Calculate camera rotation matrix with heading applied to yaw
    # For photogrammetry purposes, we need to adapt the coordinate system
    # In photogrammetry typically:
    # - Z-axis points in viewing direction (down the optical axis)
    # - X-axis points to the right
    # - Y-axis points down
    R = rotation_matrix(roll, pitch, effective_yaw)
    
    # Calculate camera intrinsic matrix and its inverse from field of view
    K = camera_matrix_from_fov(h_fov, v_fov, principal_x, principal_y, image_width, image_height)
    K_inv = np.linalg.inv(K)
    
    # For a camera pointing straight down, we can directly compute the ray
    # by using a simpler approach to ensure it points downward
    if abs(pitch + 90) < 1e-6:  # Check if pitch is -90 degrees (pointing straight down)
        # For a downward-pointing camera, we can calculate the ray directly
        # Calculate normalized image coordinates
        norm_x = (target_pixel_x - principal_x) / (image_width / 2)
        norm_y = (target_pixel_y - principal_y) / (image_height / 2)
        
        # Calculate ray direction with z pointing down
        ray_dir = np.array([
            np.tan(norm_x * np.tan(h_fov * DEG_TO_RAD / 2)),
            np.tan(norm_y * np.tan(v_fov * DEG_TO_RAD / 2)),
            -1.0
        ])
        ray_dir = ray_dir / np.linalg.norm(ray_dir)
    else:
        # Use the standard pixel-to-ray calculation
        ray_dir = pixel_to_ray(target_pixel_x, target_pixel_y, K_inv, R)
    
    # Convert camera position to cartesian coordinates (approximation for small areas)
    # We're using ENU (East-North-Up) as local coordinate system
    camera_enu = np.array([0, 0, camera_alt])  # Origin of ENU is at (camera_lat, camera_lon, 0)
    
    # Calculate intersection with ground
    try:
        target_enu = ray_ground_intersection(camera_enu, ray_dir, usgs_service, camera_lat, camera_lon)
        
        # If we got a None result, it means the ray doesn't intersect - this shouldn't happen
        # in normal usage, but we'll handle it gracefully
        if target_enu is None:
            print("Warning: Ray does not intersect with terrain. This may indicate incorrect camera parameters.")
            print("Using simplified intersection calculation with default height.")
            
            # Use simple geometry for a flat plane at default height
            # This is just a fallback that should rarely be needed
            t = (DEFAULT_HEIGHT - camera_enu[2]) / ray_dir[2]
            if t <= 0:
                return {
                    "success": False,
                    "error": "Camera is below ground or ray points upward. Check camera parameters."
                }
            target_enu = camera_enu + t * ray_dir
    except Exception as e:
        print(f"Error during ray-ground intersection with USGS data: {str(e)}")
        print("Using simplified intersection calculation with default height.")
        
        # Use simple geometry for a flat plane as fallback
        t = (DEFAULT_HEIGHT - camera_enu[2]) / ray_dir[2]
        if t <= 0:
            return {
                "success": False,
                "error": f"Ray-ground intersection failed: {str(e)}"
            }
        target_enu = camera_enu + t * ray_dir
    
    # Clean up resources
    usgs_service.close()
    
    # Convert target ENU coordinates to geodetic coordinates
    target_geodetic = enu_to_geodetic(target_enu, camera_lat, camera_lon, 0)
    
    result = {
        "success": True,
        "target": {
            "latitude": float(target_geodetic[0]),
            "longitude": float(target_geodetic[1]),
            "altitude": float(target_geodetic[2])
        }
    }
    
    # Add a warning if USGS service had connectivity issues
    if usgs_service.connection_error:
        result["warning"] = "USGS elevation service connectivity issues detected. Calculation performed with approximate elevation data."
    
    return result 