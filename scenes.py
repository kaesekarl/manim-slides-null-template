from manim import *
from manim_slides import *
from colour import Color
from constants import *
from layout_elements import *
from new_colors import *
from layouts import *

TOC_CHAPTERS = ["Basic Slide", "Test 1"]

TOC = TableofContents(TOC_CHAPTERS, max_slides=3)


class Title(Slide):

    def construct(self):
        self.play(Create(title_layout(title="Title", subtitle="Subtitle", author="Author"), run_time=0.001))
        self.pause()
        self.wait()


class TableOfContents(Slide):

    def construct(self):
        self.play(Create(table_of_contents_layout(title="Table of Contents", table_of_contents=TOC), run_time=0.001))
        self.pause()
        self.wait()


class BasicSlide(Slide):

    def construct(self):
        self.play(Create(title_layout(title="Titel", subtitle="Subtitle", author="Author"), run_time=0.001))
        self.pause()
        self.wait()


class Intro(Slide):

    def construct(self):
        apply_layout(self, title_layout(title="Titel", subtitle="Subtitle", author="Author"), table_of_contents=TOC, pause=True)

        apply_layout(self, table_of_contents_layout(title="Table of Contents", table_of_contents=TOC), pause=True)
        self.wait()


class Parabola(Slide):

    def construct(self):
        apply_layout(self, base_layout(title="Parabel", table_of_contents=TOC))

        grid = NumberPlane(x_range=[-25, 25, 5], y_range=[0, 5, 1], x_length=FRAME_WIDTH, y_length=FRAME_HEIGHT)

        parabolas = VGroup()
        for i in range(1, 5):
            parabolas += grid.plot(lambda x: i/5 * x ** 2, color=WHITE)

        self.pause()
        self.play(Create(parabolas))

        self.wait()
