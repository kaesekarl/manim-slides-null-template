from manim import *
from manim_presentation import *
from colour import Color, HSL
from constants import *
from layoutbars import *
from newColors import *
import layouts


class title(Slide):
    def construct(self):
        Headline = Text("Title", font="Arial", color=WHITE).scale(1.5).to_edge(LEFT, buff=1).shift(UP)
        Subtitle = Text("Subtitle", font="Arial", color=WHITE).scale(1).next_to(Headline, DOWN)

        self.wait()

        self.add(Headline)
        self.play(Write(Subtitle))

        self.pause()
        self.wait()


class tableofcontents(Slide):
    def construct(self):
        Headline = Text("Table of Contents", font="Arial", color=WHITE).scale(1.5).to_corner(UL, buff=1)

        self.wait()
        self.add(Headline)

        self.pause()
        self.wait()


class test1(Slide):
    def construct(self):
        layouts.baselayout(self, title="Test für einen Titel", page=1, totalpages=3)

class test2(Slide):
    def construct(self):
        layouts.titlelayout(self, title="Titel", subtitle="Subtitle", author="Author")
class closer(Slide):
    def construct(self):
        Headline = Text("Thank you for watching!", font="Arial", color=WHITE).scale(1.5)
        self.wait()

        self.play(Write(Headline))

        self.pause()
        self.wait()
