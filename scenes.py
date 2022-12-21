from manim import *
from manim_slides import *
from colour import Color
from constants import *
from layout_elements import *
from new_colors import *
from layouts import *
import math as m

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


class SinCos(Slide):

    def construct(self):
        # apply_layout(self, base_layout(title="Parabel"))

        axes = Axes(x_range=[-5, 5, 1], y_range=[-2, 2, 1], x_length=CONTENT_WIDTH, y_length=CONTENT_HEIGHT, axis_config={"stroke_color": WHITE})
        labels = axes.get_axis_labels(x_label="x", y_label=MathTex("f(x)"))
        self.play(Create(axes), Create(labels))
        self.wait()
        elements = VGroup()

        singraph = axes.plot(lambda x: m.sin(x), color=RED)
        sinlabel = MathTex("f(x) = \\sin(x)", color=RED).next_to(singraph, UP).shift(RIGHT*2)
        elements.add(singraph, sinlabel)

        cosgraph = axes.plot(lambda x: m.cos(x), color=BLUE)
        coslabel = MathTex("f(x) = \\cos(x)", color=BLUE).next_to(cosgraph, UP).shift(LEFT*2)
        elements.add(cosgraph, coslabel)
        self.play(Create(elements, run_time=2))
        self.wait()

