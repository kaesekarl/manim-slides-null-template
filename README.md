# Documentation for Manim-Slides-Framework
**Author:** Kaesekarl  
This is a framework to create slides with Manim. It uses the [manim CE library](https://github.com/ManimCommunity/manim/) 
to render the Animations and Slides. 
It also uses the [manim-slides](https://github.com/jeertmans/manim-slides) library to create the Presentation itself.
The Design is heavily influenced by [karlosos LaTeX-Beamer Template](https://github.com/karlosos/zut-fibeamer).

## Installation
Please follow the instructions for Manim and Manim-Slides. This framework comes with pipenv-files, so you can use 
pipenv to install the dependencies.


## Usage
In the `layouts.py` are some example layouts. These are created with the `layout_elements.py` components. To apply a 
layout to a slide, you can use the `apply_layout` function. The `apply_layout` function takes a layout (as a VGroup)
and applies it to the slide. Some more parameters are available:

- `table_of_contents`: Use a TableOfContents-Object for to manage the automated values for the slides. 
- `run_time`: The run_time for the animations. Normally a very short time is used, so the animations are not visible.
- `wait_for_content`: Wait before the first piece of Content is displayed on the slide. This is useful, if you want to 
  show the slide title first.
- `tabula_rasa`: Remove all other content from the slide before adding the layout on top. 

After the layout is applied, you can add content to the slide normally with manim.
