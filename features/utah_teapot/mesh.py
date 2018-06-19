import numpy as np

from features.utah_teapot.texture import Texture
from features.utah_teapot.triangle import Triangles

__all__ = ['Mesh']

class Mesh:
    def __init__(self, triangles=None, texs=None, tex_pos=None):
        self.triangles = triangles
        self.textures = texs
        self.texture_pos = tex_pos

    def verify(self):
        pass
        
