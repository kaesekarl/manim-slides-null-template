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


def table_of_contents_layout(color_of_frame=nc.COL_BACKGROUND, title="Table of Contents", TOC: TableofContents = None) -> VGroup:
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

    if TOC.get_chapters() is not None:
        for i in range(len(TOC.get_chapters())):
            y_coord = (len(TOC.get_chapters()) - 1) / 2 - i
            elements.add(
                    Text(str(i + 1) + ".", font="sans-serif", color=COL_ACCENT_1).scale(0.5).move_to([-5, y_coord, 0]))

        for i in range(len(TOC.get_chapters())):
            elements.add(
                    Text(TOC.get_chapters()[i], font="sans-serif", color=WHITE).scale(0.5).align_to(elements[2 + i], LEFT + UP).shift(RIGHT * 0.5))

    return elements


def base_layout(color_of_frame=nc.COL_BACKGROUND, title="Title", toc: TableofContents = None) -> VGroup:
    """
    Creates a base layout for a slide.
    :param color_of_frame: Color of the background. Default is ZUT_BLUE_DARK.
    :param title: Title of the Slide.
    :param toc: TableofContents object to manage the Slide Counter. Default is None.
    :return: Returns a base layout VGroup.
    """
    elements = VGroup()

    elements.add(background_solid(color_of_frame))
    # elements.add(both_bars(color_of_frame)) # Bars are on hold for now, can be added if desired
    elements.add(Text(title, font="sans-serif", color=WHITE).scale(0.75).to_corner(UL, buff=0.55))  # Title

    if toc.current_slide_num is not None and toc.max_slides is not None:
        elements.add(
                Text(f"{toc.current_slide_num} / {toc.max_slides}", font="sans-serif", color=WHITE).scale(0.33).to_corner(DR, buff=0.55))
    elif toc.current_slide_num is not None:
        elements.add(Text(f"{toc.current_slide_num}", font="sans-serif", color=WHITE).scale(0.33).to_corner(DR, buff=0.55))

    return elements
