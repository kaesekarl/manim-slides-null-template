from manim import *
from manim_slides import *
from colour import Color
from constants import *
from layout_elements import *
from new_colors import *
from layouts import *


sc = SlideCounter(0)

for i in range(1, 10):
    sc.inc()
    print(sc.get(), "of", sc.max_slides)
