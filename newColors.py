from manim import *
from manim_presentation import *
from colour import Color, HSL


def color_creator(hex_value):
    newcolor = Color()
    newcolor.hex = f'#{hex_value}'
    return newcolor


mainColor = color_creator(212529)
