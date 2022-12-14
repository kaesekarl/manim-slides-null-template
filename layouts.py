from manim import *
from manim_presentation import *
from colour import Color, HSL
from constants import *
from layout_elements import *
from newColors import *


def title_layout(color_of_frame=nc.MAIN_COLOR_BLUE_0, title="Title", subtitle="Subtitle", author="Author"):
    """
    Creates a Title Slide with a title, subtitle and author.
    :param Color color_of_frame: Color of the background. Default is MAIN_COLOR_BLUE_0.
    :param str title: Title of the Presentation.
    :param str subtitle: Subtitle of the Presentation.
    :param str author: Author of the Presentation.
    :return: returns a Title Slide VGroup.
    """
    elements = VGroup()

    elements.add(background_solid(color_of_frame))

    elements.add(both_bars(color_of_frame))
    elements.add(Text(title, font="sans-serif", color=WHITE).scale(0.75).to_corner(UL, buff=0.55))                  # Title
    elements.add(Text(subtitle, font="sans-serif", color=WHITE).scale(0.5).next_to(elements[1], DOWN, buff=0.5))    # Subtitle
    elements.add(Text(author, font="sans-serif", color=WHITE).scale(0.33).next_to(elements[2], DOWN, buff=0.5))     # Author

    return elements



def base_layout(color_of_frame=nc.MAIN_COLOR_BLUE_0, title="Title", page=None, total_pages=None):
    """
    Creates a base layout for a slide.
    :param color_of_frame: Color of the background. Default is MAIN_COLOR_BLUE_0.
    :param title: Title of the Slide.
    :param page: Current page of the presentation. Default is None. Can be used independent of total_pages.
    :param total_pages: Total number of pages in the presentation. Default is None.
    :return: Returns a base layout VGroup.
    """
    elements = VGroup()

    elements.add(background_solid(color_of_frame))
    elements.add(both_bars(color_of_frame))
    elements.add(Text(title, font="sans-serif", color=WHITE).scale(0.75).to_corner(UL, buff=0.55))  # Title

    if page is not None and total_pages is not None:
        elements.add(Text(f"{page} / {total_pages}", font="sans-serif", color=WHITE).scale(0.33).to_corner(DR, buff=0.55))
    elif page is not None:
        elements.add(Text(f"{page}", font="sans-serif", color=WHITE).scale(0.33).to_corner(DR, buff=0.55))

    return elements

