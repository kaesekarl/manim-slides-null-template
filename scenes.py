from manim import *
from manim_slides import *
from colour import Color
from constants import *
from layout_elements import *
from new_colors import *
from layouts import *
import math as m

TOC_CHAPTERS = ["Basic Slide", "Test 1"]

TOC = TableOfContents(TOC_CHAPTERS, max_slides=3)



class Title(Slide):

    def construct(self):
        apply_layout(self, title_layout(title="Title", subtitle="Subtitle", author="Author"), table_of_contents=TOC)
        self.wait()


class TableOfContents(Slide):

    def construct(self):
        apply_layout(self, table_of_contents_layout(title="Table of Contents", table_of_contents=TOC), table_of_contents=TOC)
        self.wait()


class BasicSlide(Slide):

    def construct(self):
        self.play(Create(title_layout(title="Titel", subtitle="Subtitle", author="Author"), run_time=0.001))
        self.pause()
        self.wait()


class Intro(Slide):

    def construct(self):
        apply_layout(self, title_layout(title="Titel", subtitle="Subtitle", author="Author"), wait_for_content=True)

        apply_layout(self, table_of_contents_layout(title="Table of Contents", table_of_contents=TOC), wait_for_content=True)
        self.wait()


class SinCos(Slide):

    def construct(self):
        axes = Axes(x_range=[-PI, PI, PI/4], y_range=[-1.5, 1.5, 1], x_axis_config=dict(stroke_color=WHITE,
                                                                                      include_numbers=True,
                                                                                      label_constructor=MathTex,
                                                                                       ))
        labels = axes.get_axis_labels(x_label="x", y_label=MathTex("f(x)"))
        self.play(Create(axes), Create(labels))
        self.pause()
        self.wait()


        elements = VGroup()

        singraph = axes.plot(lambda x: m.sin(x), color=RED)
        sinlabel = MathTex("f(x) = \\sin(x)", color=RED).next_to(singraph, UP).shift(RIGHT*2)
        elements.add(singraph, sinlabel)

        cosgraph = axes.plot(lambda x: m.cos(x), color=BLUE)
        coslabel = MathTex("f(x) = \\cos(x)", color=BLUE).next_to(cosgraph, UP).shift(LEFT*2)
        elements.add(cosgraph, coslabel)

        for element in elements:
            self.play(Create(element))
        self.wait()


        vt = ValueTracker(0)
        dot_on_sin = Dot().add_updater(lambda d: d.move_to(singraph.point_from_proportion(vt.get_value())))

        #val = DecimalNumber().add_updater(lambda d: d.next_to(dot_on_sin, UP).set_value())
        self.play(Create(dot_on_sin))
        #self.play(Create(val))
        self.wait()
        self.play(vt.animate.set_value(1), run_time=3)
        self.wait()

        self.wait(2)

class ValueTrackerExample(Scene):

    def construct(self):
                number_line = NumberLine()
                pointer = Vector(DOWN)
                label = MathTex("x").add_updater(lambda m: m.next_to(pointer, UP))

                tracker = ValueTracker(0)
                pointer.add_updater(
                        lambda m: m.next_to(
                                number_line.n2p(tracker.get_value()),
                                UP
                        )
                )
                self.add(number_line, pointer, label)
                tracker += 1.5
                self.wait(1)
                tracker -= 4
                self.wait(0.5)
                self.play(tracker.animate.set_value(5)),
                self.wait(0.5)
                self.play(tracker.animate.set_value(3))
                self.play(tracker.animate.increment_value(-2))
                self.wait(0.5)


class TestTriangle(Scene):
    def construct(self):

        vt = ValueTracker(0)

        points = VGroup()
        p1 = Dot()
        p2 = Dot()
        p3 = Dot()
        positions = [UP, LEFT*2/3+DOWN*1/3, RIGHT*2/3+DOWN*1/3]
        points.add(p1, p2, p3)

        self.play(Create(points))
        for pos , i in zip(positions, range(3)):
            self.play(points[i].animate.move_to(pos), run_time=0.5)
        p1.add_updater(lambda d: d.shift(vt.get_value()*UP))
        self.wait()


        triangle = Polygon(p1.get_center(), p2.get_center(), p3.get_center()).set_z_index(-1).add_updater(lambda p: p.become(Polygon(p1.get_center(), p2.get_center(), p3.get_center()).set_z_index(-1)))
        self.play(Create(triangle))
        self.wait()


        circle = Circle.from_three_points(p1.get_center(), p2.get_center(), p3.get_center()).set_z_index(-1).add_updater(lambda c: c.become(Circle.from_three_points(p1.get_center(), p2.get_center(), p3.get_center()).set_z_index(-1)))
        self.play(Create(circle))

        self.play(vt.animate.set_value(0.2), run_time=0.5)
        self.wait()

        self.wait()

class test1(Slide):

        def construct(self):
            apply_layout(self, title_layout(title="Brüning Stinkt", subtitle="Subtitle", author="Author"))
            self.pause()
            self.wait()


class LayoutTransitionTest(Slide):
    def construct(self):
        layout1 = title_layout(title="Brüning Stinkt", subtitle="Subtitle", author="Author")
        layout2 = table_of_contents_layout(title="Table of Contents", table_of_contents=TOC)

        apply_layout(self, layout1)
        self.pause()
        self.wait()
        self.play(Transform(layout1, layout2))
        self.pause()
        self.wait()
