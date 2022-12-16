from colour import Color
from layout_elements import *
from new_colors import *


def title_layout(color_of_frame=nc.COL_BACKGROUND, title="Title", subtitle="Subtitle", author="Author") -> VGroup:
    """
    Creates a Title Slide with a title, subtitle and author.
    :param Color color_of_frame: Color of the background. Default is ZUT_BLUE_DARK.
    :param str title: Title of the Presentation.
    :param str subtitle: Subtitle of the Presentation.
    :param str author: Author of the Presentation.
    :return: returns a Title Slide VGroup.
    """
    elements = VGroup()

    elements.add(background_solid(color_of_frame))  # Background

    elements.add(DashedLine(color=COL_ACCENT_1, start=[-6, 1, 0], end=[6, 1, 0]))  # Underline of Title
    elements.add(Text(title, weight=BOLD, font="sans-serif", color=COL_ACCENT_1).scale(0.75).align_to(elements[1],
                                                                                                      LEFT + UP).shift(UP * 0.66))  # Title
    elements.add(Text(subtitle, weight=BOLD, font="sans-serif", color=WHITE).scale(0.5).align_to(elements[1],
                                                                                                 DOWN + LEFT).shift(DOWN))  # Subtitle
    elements.add(Text(author, weight=BOLD, font="sans-serif", color=ZUT_TAN).scale(0.33).align_to(elements[3],
                                                                                                  DOWN + LEFT).shift(DOWN * 0.66))  # Author

    return elements


def table_of_contents_layout(color_of_frame=nc.COL_BACKGROUND, title="Table of Contents",
                             chapters: list = None) -> VGroup:
    """
    Creates a Table of Contents layout.
    :param color_of_frame: Background color of the slide. Default is ZUT_BLUE_DARK.
    :param title: Title of the slide. Default is "Table of Contents".
    :param chapters: list of chapter-titles. Default is None. List should be in the format ["Chapter 1", "Chapter 2", ...]
    :return: Returns a Table of Contents layout VGroup.
    """
    elements = VGroup()

    elements.add(background_solid(color_of_frame))
    elements.add(Text(title, font="sans-serif", color=COL_ACCENT_1).scale(0.75).to_corner(UL, buff=0.55))  # Title

    if chapters is not None:
        for i in range(len(chapters)):
            y_coord = (len(chapters) - 1) / 2 - i
            elements.add(
                Text(str(i + 1) + ".", font="sans-serif", color=COL_ACCENT_1).scale(0.5).move_to([-5, y_coord, 0]))

        for i in range(len(chapters)):
            elements.add(
                Text(chapters[i], font="sans-serif", color=WHITE).scale(0.5).align_to(elements[2 + i], LEFT + UP).shift(
                    RIGHT * 0.5))

    return elements


def base_layout(color_of_frame=nc.COL_BACKGROUND, title="Title", page=None, total_pages=None) -> VGroup:
    """
    Creates a base layout for a slide.
    :param color_of_frame: Color of the background. Default is ZUT_BLUE_DARK.
    :param title: Title of the Slide.
    :param page: Current page of the presentation. Default is None. Can be used independent of total_pages.
    :param total_pages: Total number of pages in the presentation. Default is None. Can only be used if page is not None.
    :return: Returns a base layout VGroup.
    """
    elements = VGroup()

    elements.add(background_solid(color_of_frame))
    # elements.add(both_bars(color_of_frame)) # Bars are on hold for now, can be added if desired
    elements.add(Text(title, font="sans-serif", color=WHITE).scale(0.75).to_corner(UL, buff=0.55))  # Title

    if page is not None and total_pages is not None:
        elements.add(
            Text(f"{page} / {total_pages}", font="sans-serif", color=WHITE).scale(0.33).to_corner(DR, buff=0.55))
    elif page is not None:
        elements.add(Text(f"{page}", font="sans-serif", color=WHITE).scale(0.33).to_corner(DR, buff=0.55))

    return elements
