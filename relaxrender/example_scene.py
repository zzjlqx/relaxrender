import numpy as np
import relaxrender.utah_teapot.teapot_data as teapot

from .scene import Scene
from .camera import PerspectiveCamera
from .mesh import Mesh
from .texture import Texture, PlaneLightSource, UniformReflection
from .triangle import Triangles
from .points import Point3D, Point2D
from .triangle import Triangle, Triangles
from .color import Color, Red, White, Black, Green, Blue, Grey

__all__ = ['cornell_box']


def make_cornell_box():
    tris = Triangles()
    texs = []
    tex_pos = []

    # add light
    tris.append_rct(np.array([0.5, 0.999, -0.5]),
                    np.array([-0.5, 0.999, -0.5]),
                    np.array([-0.5, 0.999, -1.5]),
                    np.array([0.5, 0.999, -1.5]))

    texs.append(PlaneLightSource())
    texs.append(PlaneLightSource())

    tex_pos.append(None)
    tex_pos.append(None)

    # add ceilling, wall, floor
    # ceiling
    tris.append_rct(np.array([1, 1, 0]),
                    np.array([-1, 1, 0]),
                    np.array([-1, 1, -2]),
                    np.array([1, 1, -2]))

    texs.append(UniformReflection(Grey))
    texs.append(UniformReflection(Grey))

    tex_pos.append(None)
    tex_pos.append(None)

    # left wall
    tris.append_rct(np.array([-1, 1, 0]),
                    np.array([-1, -1, 0]),
                    np.array([-1, -1, -2]),
                    np.array([-1, 1, -2]))

    texs.append(UniformReflection(Red))
    texs.append(UniformReflection(Red))

    tex_pos.append(None)
    tex_pos.append(None)

    # right wall
    tris.append_rct(np.array([1, 1, 0]),
                    np.array([1, 1, -2]),
                    np.array([1, -1, -2]),
                    np.array([1, -1, 0]))

    texs.append(UniformReflection(Green))
    texs.append(UniformReflection(Green))

    tex_pos.append(None)
    tex_pos.append(None)

    # floor
    tris.append_rct(np.array([-1, -1, 0]),
                    np.array([1, -1, 0]),
                    np.array([1, -1, -2]),
                    np.array([-1, -1, -2]))

    texs.append(UniformReflection(Grey))
    texs.append(UniformReflection(Grey))

    tex_pos.append(None)
    tex_pos.append(None)

    # back
    tris.append_rct(np.array([1, 1, -2]),
                    np.array([-1, 1, -2]),
                    np.array([-1, -1, -2]),
                    np.array([1, -1, -2]))

    texs.append(UniformReflection(Grey))
    texs.append(UniformReflection(Grey))

    tex_pos.append(None)
    tex_pos.append(None)
    
    # teapot
    """
    对每一部分的所有点进行3层遍历, 将所有的三角形组合加入到 tris 中
    """
    points = teapot.t_pos
    for point in points:
        point = [x/4 for x in point]
        point.reverse()
    for piece in teapot.t_patch:
        length = len(piece)
        for i in range(length):
            for j in range(length):
                if i >= j:
                    continue
                for k in range(length):
                    if i >= k or j >= k:
                        continue
                    tris.append_tri(points[i], points[j], points[k])
                    # 茶壶取白色
                    texs.append(UniformReflection(White))

                    tex_pos.append(None)
    # todo

    mesh = Mesh(tris, texs, tex_pos)
    
    c_pos = np.array([0.0, 0.0, 1.0])
    c_up = np.array([0.0, 1.0, 0])
    c_right = np.array([1.0, 0.0, 0])
    camera = PerspectiveCamera(c_pos, c_up, c_right, np.pi/2, np.pi/2)

    ret = Scene(mesh, camera)

    return ret

cornell_box = make_cornell_box()
