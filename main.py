from manim import *
from manim_presentation import *
from colour import Color, HSL
from constants import *
from layoutbars import *
from newColors import *
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


class Test1(Slide):
    def construct(self):
        layouts.base_layout(self, title="Test für einen Titel", page=1, total_pages=3)


class Test2(Slide):
    def construct(self):
        layouts.title_layout(self, title="Titel", subtitle="Subtitle", author="Author")


class Closer(Slide):
    def construct(self):
        headline = Text("Thank you for watching!", font="Arial", color=WHITE).scale(1.5)
        self.wait()

        self.play(Write(headline))

        self.pause()
        self.wait()
