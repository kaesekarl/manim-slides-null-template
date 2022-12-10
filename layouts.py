from manim import *
from manim_presentation import *
from colour import Color, HSL
from constants import *
from layoutbars import *
from newColors import *


def baselayout(self, colorOfFrames=nc.mainColor):
    bothbars(self, colorOfFrames)
    self.wait()

