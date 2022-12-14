from manim import *
from manim_presentation import *
from colour import Color, HSL
from constants import *
import new_colors as nc


def background_solid(color_of_frame=nc.ZUT_BLUE_DARK):
    """
    Creates a solid background for the slide.
    :param color_of_frame: Color of the background. Default is MAIN_COLOR_BLUE_0.
    :return: returns a solid color background.
    """
    return Rectangle(height=FRAME_HEIGHT, width=FRAME_WIDTH, color=color_of_frame, fill_color=color_of_frame, fill_opacity=1)

def top_bar(color_of_frame=nc.ZUT_BLUE_DARK):
    return Rectangle(height=0.5, width=FRAME_WIDTH, color=color_of_frame, fill_color=color_of_frame, fill_opacity=1).to_edge(UP, buff=0)


def bottom_bar(color_of_frame=nc.ZUT_BLUE_DARK):
    return Rectangle(height=0.5, width=FRAME_WIDTH, color=color_of_frame, fill_color=color_of_frame, fill_opacity=1).to_edge(DOWN, buff=0)


def both_bars(color_of_frame=nc.ZUT_BLUE_DARK) -> VGroup:
    """
    Creates both top and bottom bars.
    :param Color color_of_frame: color of the bars. Default is MAIN_COLOR_BLUE_0.
    :return: VGroup of both bars.
    """
    return VGroup(top_bar(color_of_frame), bottom_bar(color_of_frame))


def center_bar(color_of_frame=nc.ZUT_BLUE_DARK):
    return Rectangle(height=4, width=2/3*FRAME_WIDTH, color=color_of_frame, fill_color=color_of_frame, fill_opacity=1).to_edge(LEFT, buff=0)
