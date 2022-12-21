from colour import Color
from layout_elements import *
from new_colors import *


def apply_layout(self, layout: VGroup, table_of_contents: TableofContents = None, run_time=0.001, pause=False, tabula_rasa=False):
    """
    Applies a layout to the current scene.
    :param self: The current scene.
    :param layout: Layout to be applied.
    :param table_of_contents: The TableofContents object to manage the Slide Counter. Default is None.
    :param run_time: How long the animation should take. Default is 0.001 for instant application.
    :param pause: Whether the scene should pause after applying the layout. Default is False.
    :param tabula_rasa: Whether the scene should be cleared before applying the layout. Default is False.
    :return: None
    """
    if tabula_rasa:
        self.clear()
    table_of_contents.set_layout(layout)

    if table_of_contents is not None:
        table_of_contents.inc()

    self.play(Create(layout), run_time=run_time)
    self.wait()

    if pause:
        self.pause()


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


def table_of_contents_layout(color_of_frame=nc.COL_BACKGROUND, title="Table of Contents", table_of_contents: TableofContents = None) -> VGroup:
    """
    Creates a Table of Contents layout.
    :param color_of_frame: Background color of the slide. Default is ZUT_BLUE_DARK.
    :param title: Title of the slide. Default is "Table of Contents".
    :param table_of_contents: TableofContents object to manage the Slide Counter. Default is None.
    :return: Returns a Table of Contents layout VGroup.
    """
    elements = VGroup()

    elements.add(background_solid(color_of_frame))
    elements.add(Text(title, font="sans-serif", color=COL_ACCENT_1).scale(0.75).to_corner(UL, buff=0.55))  # Title

    if table_of_contents.get_chapters() is not None:
        for i in range(len(table_of_contents.get_chapters())):
            y_coord = (len(table_of_contents.get_chapters()) - 1) / 2 - i
            elements.add(
                    Text(str(i + 1) + ".", font="sans-serif", color=COL_ACCENT_1).scale(0.5).move_to([-5, y_coord, 0]))

        for i in range(len(table_of_contents.get_chapters())):
            elements.add(
                    Text(table_of_contents.get_chapters()[i], font="sans-serif", color=WHITE).scale(0.5).align_to(elements[2 + i], LEFT + UP).shift(
                        RIGHT * 0.5))

    return elements


def base_layout(color_of_frame=nc.COL_BACKGROUND, title="Title", table_of_contents: TableofContents = None) -> VGroup:
    """
    Creates a base layout for a slide.
    :param color_of_frame: Color of the background. Default is ZUT_BLUE_DARK.
    :param title: Title of the Slide.
    :param table_of_contents: TableofContents object to manage the Slide Counter. Default is None.
    :return: Returns a base layout VGroup.
    """
    elements = VGroup()

    elements.add(background_solid(color_of_frame))
    # elements.add(both_bars(color_of_frame)) # Bars are on hold for now, can be added if desired
    elements.add(Text(title, font="sans-serif", color=WHITE).scale(0.75).to_corner(UL, buff=0.55))  # Title

    if table_of_contents is not None:
        if table_of_contents.current_slide_num is not None and table_of_contents.max_slides is not None:
            elements.add(
                    Text(f"{table_of_contents.current_slide_num} / {table_of_contents.max_slides}", font="sans-serif", color=WHITE).scale(
                        0.33).to_corner(
                            DR, buff=0.55))
        elif table_of_contents.current_slide_num is not None:
            elements.add(Text(f"{table_of_contents.current_slide_num}", font="sans-serif", color=WHITE).scale(0.33).to_corner(DR, buff=0.55))

    return elements


def math_layout(title="Title", table_of_contents: TableofContents = None) -> VGroup:
    """
    Creates a layout for a slide with mathematical equations.
    :param title: Title of the slide.
    :param table_of_contents: TableofContents object to manage the Slide Counter. Default is None.
    :param tabula_rasa: Whether the slides should be cleared before the next slide is shown. Default is False.
    :return: Returns a layout VGroup.
    """
    elements = base_layout(title=title, table_of_contents=table_of_contents)
    elements.remove(elements[0])  # Remove background



    return elements
