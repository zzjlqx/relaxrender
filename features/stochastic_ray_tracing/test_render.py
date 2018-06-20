import unittest

import numpy as np

from relaxrender.color import Color, Red, White, Black, Green, Blue, Grey
from relaxrender.texture import Texture, PlaneLightSource, UniformReflection
from stochastic_ray_tracing.render import get_shadow
from stochastic_ray_tracing.render import make_shadow_cornell_box
import relaxrender.raycasting as raycasting
import relaxrender.context as ctx
import relaxrender.screenwriter as sw
from relaxrender.points import Point3D

class TestRender(unittest.TestCase):

    def test_make_shadow_cornell_box(self):
        cornell_box = make_shadow_cornell_box()