from manim import *
from manim_presentation import *
from colour import Color, HSL
from constants import *
import newColors as nc




def topbar(self, colorOfFrame=nc.mainColor):
    quader = Rectangle(height=0.5, width=FRAME_WIDTH, color=colorOfFrame, fill_color=colorOfFrame, fill_opacity=1).to_edge(UP, buff=0)
    self.add(quader)


def bottombar(self, colorOfFrame=nc.mainColor):
    quader = Rectangle(height=0.5, width=FRAME_WIDTH, color=colorOfFrame, fill_color=colorOfFrame, fill_opacity=1).to_edge(DOWN, buff=0)
    self.add(quader)


def bothbars(self, colorOfFrame=nc.mainColor):
    topbar(self, colorOfFrame)
    bottombar(self, colorOfFrame)

def centerbar(self, colorOfFrame=nc.mainColor):
    quader = Rectangle(height=4, width=2/3*FRAME_WIDTH, color=colorOfFrame, fill_color=colorOfFrame, fill_opacity=1).to_edge(LEFT, buff=0)
    self.add(quader)
