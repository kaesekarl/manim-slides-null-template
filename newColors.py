from manim import *
from manim_presentation import *
from colour import Color, HSL


def color_creator(rgb_array: list) -> Color:
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


MAIN_COLOR_BLUE_0 = color_creator([43, 46, 52])
