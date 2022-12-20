from manim import *
from manim_slides import *
from colour import Color
from constants import *
from layout_elements import *
from new_colors import *
from layouts import *

TOC_CHAPTERS = ["Title", "Table of Contents", "Basic Slide", "Test 1"]

TOC = TableofContents(TOC_CHAPTERS)



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


class Test1(Slide):
    def construct(self):
        self.play(Create(title_layout(title="Title", subtitle="Subtitle", author="Author")))
        self.wait()
        self.pause()
        self.play(Create(table_of_contents_layout(title="Table of Contents", table_of_contents=TOC)))
        self.wait()
        self.pause()
        self.play(Create(base_layout(color_of_frame=nc.COL_BACKGROUND, title="Title")))
        self.wait()
        self.pause()

        self.wait()



