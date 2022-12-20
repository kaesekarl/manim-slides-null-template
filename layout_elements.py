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

    def __init__(self, chapters: list = None):
        """
        Creates a slide counter to keep track of slide numbers
        :param chapters: list of chapters. Form is ["None", "Chapter 1", Chapter 1", Chapter 2", "Chapter 3", "Chapter 3"] to have each entry be a
        page matching a chapter. Default is None.
        """
        self.current_slide_num = 0
        self.max_slides = len(chapters)
        self.chapters = chapters

    def set(self, page):
        self.current_slide_num = page

    def inc(self):
        self.current_slide_num += 1

    def dec(self):
        self.current_slide_num -= 1

    def get_slide_num(self):
        return self.current_slide_num

    def max(self):
        return self.max_slides

    def get_chapter(self, slide_num=None):
        if slide_num is None:
            return self.chapters[self.current_slide_num]
        return self.chapters[slide_num]

    def get_chapters(self):
        return self.chapters
