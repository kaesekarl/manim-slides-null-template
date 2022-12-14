from manim import *
from manim_presentation import *
from colour import Color, HSL
from constants import *
import newColors as nc


def top_bar(color_of_frame=nc.mainColor):
    return Rectangle(height=0.5, width=FRAME_WIDTH, color=color_of_frame, fill_color=color_of_frame, fill_opacity=1).to_edge(UP, buff=0)


def bottom_bar(color_of_frame=nc.mainColor):
    return Rectangle(height=0.5, width=FRAME_WIDTH, color=color_of_frame, fill_color=color_of_frame, fill_opacity=1).to_edge(DOWN, buff=0)


def both_bars(color_of_frame=nc.mainColor):
    return VGroup(top_bar(color_of_frame), bottom_bar(color_of_frame))


def center_bar(color_of_frame=nc.mainColor):
    return Rectangle(height=4, width=2/3*FRAME_WIDTH, color=color_of_frame, fill_color=color_of_frame, fill_opacity=1).to_edge(LEFT, buff=0)
