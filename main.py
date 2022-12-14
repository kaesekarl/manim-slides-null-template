from manim import *
from manim_slides import *
from colour import Color, HSL
from constants import *
from layout_elements import *
from new_colors import *
import layouts


class Title(Slide):
    def construct(self):
        headline = Text("Title", font="Arial", color=WHITE).scale(1.5).to_edge(LEFT, buff=1).shift(UP)
        subtitle = Text("Subtitle", font="Arial", color=WHITE).scale(1).next_to(headline, DOWN)

        self.wait()

        self.add(headline)
        self.play(Write(subtitle))

        self.pause()
        self.wait()


class TableOfContents(Slide):
    def construct(self):
        headline = Text("Table of Contents", font="Arial", color=WHITE).scale(1.5).to_corner(UL, buff=1)

        self.wait()
        self.add(headline)

        self.pause()
        self.wait()



class Test2(Slide):
    def construct(self):
        self.add(layouts.title_layout(title="Titel", subtitle="Subtitle", author="Author"))




