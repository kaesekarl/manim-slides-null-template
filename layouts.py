from manim import *
from manim_presentation import *
from colour import Color, HSL
from constants import *
from layoutbars import *
from newColors import *


def title_layout(self, color_of_frame=nc.mainColor, title="Title", subtitle="Subtitle", author="Author"):
    self.add(center_bar(color_of_frame))
    self.add(Text(title, font="sans-serif", color=WHITE).scale(0.75).to_edge(LEFT).shift(UP))
    self.add(Text(subtitle, font="sans-serif", color=WHITE).scale(0.66).to_edge(LEFT).shift(DOWN))

    author = VGroup(Text(author, font="sans-serif", color=WHITE).scale(0.66).to_corner(DR, buff=0.5))
    self.add(author)
    # self.add(Rectangle(height=0.5, width=3, color=colorOfFrames, fill_color=colorOfFrames, fill_opacity=1).to_edge(
    # DOWN).shift(UP*0.5).to_edge(RIGHT, buff=0))


def base_layout(self, color_of_frame=nc.mainColor, title="Title", page=None, total_pages=None):
    self.add(both_bars(color_of_frame))
    self.add(Text(title, font="sans-serif", color=WHITE).scale(0.75).to_corner(UL, buff=0.55))

    if page is not None and total_pages is not None:
        self.add(Text(f"{page} / {total_pages}", font="sans-serif", color=WHITE).scale(0.33).to_corner(DR, buff=0.55))


