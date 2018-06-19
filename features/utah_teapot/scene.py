
from features.utah_teapot.mesh import *
from features.utah_teapot.camera import *

__all__ = ['Scene']

class Scene:
    def __init__(self, mesh, camera):
        self.mesh = mesh
        self.camera = camera

