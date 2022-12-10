from manim import *
from manim_presentation import *
from colour import Color, HSL




def colorCreator(hexValue):
    newcolor = Color()
    newcolor.hex = f'#{hexValue}'
    return newcolor


mainColor = colorCreator(212529)
