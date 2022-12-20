from manim import *
from colour import Color, HSL
from constants import *
import new_colors as nc


def background_solid(color_of_frame=nc.COL_BACKGROUND):
    """
    Creates a solid background for the slide.
    :param color_of_frame: Color of the background. Default is MAIN_COLOR_BLUE_0.
    :return: returns a solid color background.
    """
    return Rectangle(height=FRAME_HEIGHT, width=FRAME_WIDTH, color=color_of_frame, fill_color=color_of_frame, fill_opacity=1)


def top_bar(color_of_frame=nc.COL_BACKGROUND):
    return Rectangle(height=0.5, width=FRAME_WIDTH, color=color_of_frame, fill_color=color_of_frame, fill_opacity=1).to_edge(UP, buff=0)


def bottom_bar(color_of_frame=nc.COL_BACKGROUND):
    return Rectangle(height=0.5, width=FRAME_WIDTH, color=color_of_frame, fill_color=color_of_frame, fill_opacity=1).to_edge(DOWN, buff=0)


def both_bars(color_of_frame=nc.COL_BACKGROUND) -> VGroup:
    """
    Creates both top and bottom bars.
    :param Color color_of_frame: color of the bars. Default is MAIN_COLOR_BLUE_0.
    :return: VGroup of both bars.
    """
    return VGroup(top_bar(color_of_frame), bottom_bar(color_of_frame))


def center_bar(color_of_frame=nc.COL_BACKGROUND):
    return Rectangle(height=4, width=2/3*FRAME_WIDTH, color=color_of_frame, fill_color=color_of_frame, fill_opacity=1).to_edge(LEFT, buff=0)


class TableofContents:

    def __init__(self, chapters: list = None, initial_slide_num=0, max_slides: int = None):
        """
        Creates a slide counter to keep track of slide numbers
        :param chapters: list of chapters. Form is ["Chapter 1", "Chapter 2, ...]. Default is None.
        """
        self.current_slide_num = initial_slide_num
        self.max_slides = max_slides
        self.max_chapters = len(chapters)
        self.chapters = chapters
        self.current_chapter = 0

    def set(self, page):
        self.current_slide_num = page

    def inc(self):
        self.current_slide_num += 1

    def dec(self):
        self.current_slide_num -= 1

    def slide_num(self):
        return self.current_slide_num


    def inc_chapter(self):
        self.current_chapter += 1

    def set_chapter(self, chapter_num):
        self.current_chapter = chapter_num

    def get_chapter(self, chapter_num=None):
        if chapter_num is None:
            return self.chapters[self.current_chapter]
        return self.chapters[chapter_num]

    def get_chapters(self):
        return self.chapters
