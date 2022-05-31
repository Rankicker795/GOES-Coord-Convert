import numpy as np


def rad2cartesian(x_rad: np.ndarray, y_rad: np.ndarray, sat_height: float,
                  sat_longitude: float, semi_major_axis: float,
                  semi_minor_axis: float) -> Tuple[np.ndarray, np.ndarray]:
    """
    Convert X,Y radians to Lon/Lat Cartesian 
    :param x_rad: X Radians array
    :param y_rad: Y Radians array
    :param sat_height: Satellite Height
    :param sat_longitude: Satellite Longitude
    :param semi_major_axis: Semi Major Axis of Satellite Orbit
    :param semi_minor_axis: Semi Minor Axis of Satellite Orbit
    :return: Tuple of Lon/Lat values
    """
    H = sat_height + semi_major_axis
    sat_angle = np.deg2rad(sat_longitude)
    x_rad_sin = np.sin(x_rad)
    x_rad_cos = np.cos(x_rad)
    y_rad_sin = np.sin(y_rad)
    y_rad_cos = np.cos(y_rad)
    a = np.square(x_rad_sin) + (np.square(x_rad_cos) * (np.square(y_rad_cos) +
         (((semi_major_axis ** 2.0) / (semi_minor_axis ** 2.0)) *
         np.square(y_rad_sin))))

    b = -2.0 * H * y_rad_cos * x_rad_cos
    c = (H ** 2.0) - (semi_major_axis ** 2.0)

    disc = b ** 2 - 4.0 * a * c
    r = (-b - np.sqrt(disc)) / (2.0 * a)

    s_x = r * y_rad_cos * x_rad_cos
    s_y = - r * x_rad_sin
    s_z = r * x_rad_cos * y_rad_sin

    lats = np.rad2deg(np.arctan(
        ((semi_major_axis ** 2) / (semi_minor_axis ** 2)) * (s_z / np.sqrt(
            ((H - s_x) * (H - s_x)) + (s_y * s_y)
        ))
    ))
    lons = np.rad2deg(sat_angle - np.arctan(s_y / (H - s_x)))
    return lons, lats
