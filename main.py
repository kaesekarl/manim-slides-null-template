import manim_slides

from scenes import *
from manim import *

SCENES_IN_ORDER = [Intro(), Parabola()]

for scene in SCENES_IN_ORDER:
    scene.render()

