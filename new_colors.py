from colour import Color, HSL


def color_creator_rgb(rgb_array: list) -> Color:
    """
    Creates a Color object from a list of RGB values.
    :param rgb_array: Array of length 3 containing RGB values (0-255).
    :return: returns a Color object.
    """

    for i in range(len(rgb_array)):
        rgb_array[i] = rgb_array[i] / 255

    new_color = Color()
    new_color.rgb = rgb_array
    return new_color


def color_creator_hex(hex_string: str) -> Color:
    """
    Creates a Color object from a hex string.
    :param hex_string: Hex string of the color.
    :return: returns a Color object.
    """

    new_color = Color()
    new_color.hex = hex_string
    return new_color


ZUT_BLUE_DARK = COL_BACKGROUND = color_creator_rgb([43, 46, 52])  # ZUT_BLUE_DARK
ZUT_BLUE_LIGHT = COL_ACCENT_1 = color_creator_hex("#6daddf")  # ZUT_BLUE_LIGHT
ZUT_TAN = color_creator_hex("#f3eee1")  # ZUT_TAN

