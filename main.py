from manim import *
from manim_slides import *
from colour import Color
from constants import *
from layout_elements import *
from new_colors import *
import layouts


class Title(Slide):
    def construct(self):
        self.add(layouts.title_layout(title="Title", subtitle="Subtitle", author="Author"))


class TableOfContents(Slide):
    def construct(self):
        TOC = layouts.table_of_contents_layout(title="Table of Contents", chapters=["Chapter 1", "Chapter 2", "Chapter 3"])
        self.add(TOC)


class Test2(Slide):
    def construct(self):
        self.play(Create(layouts.title_layout(title="Titel", subtitle="Subtitle", author="Author")))
        self.pause()
        self.wait()

