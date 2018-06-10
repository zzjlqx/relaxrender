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
    1.0 (共5041个, 待改正) 对每一部分的所有点进行3层遍历, 将所有的三角形组合加入到 tris 中
    2.0 
    """

    def mapping(point):
        point = [x / 4 for x in point]
        point[1:].reverse()
        point[1] = -point[1]
        point[2] -= 0.5
        return point

    points = teapot.t_pos
    points = [mapping(p) for p in points]
    tmp = 1
    for piece in teapot.t_patch:
        length = len(piece)
        for i in range(length):
            for j in range(length):
                if i >= j:
                    continue
                for k in range(length):
                    if i >= k or j >= k:
                        continue
                    p1, p2, p3 = points[piece[i]], points[piece[j]], points[piece[k]]
                    if (p1 is p2) or (p2 is p3) or (p1 is p3):
                        continue
                    if abs(p1[2]-p2[2]) >= 0.1 or abs(p2[2]-p3[2]) >= 0.1 or abs(p1[2]-p3[2]) >= 0.1 or \
                            p1[0] == p2[0] or p1[1] == p2[1] or p1[2] == p2[2] or \
                            p2[0] == p3[0] or p2[1] == p3[1] or p2[2] == p3[2] or \
                            p1[0] == p3[0] or p1[1] == p3[1] or p1[2] == p3[2] :
                        continue
                    tmp += 1

                    tris.append_tri(points[piece[i]], points[piece[j]], points[piece[k]])
                    # 茶壶取白色
                    texs.append(UniformReflection(White))

                    tex_pos.append(None)
    # todo

    mesh = Mesh(tris, texs, tex_pos)

    c_pos = np.array([0.0, 0.0, 1.0])
    c_up = np.array([0.0, 1.0, 0])
    c_right = np.array([1.0, 0.0, 0])
    camera = PerspectiveCamera(c_pos, c_up, c_right, np.pi / 2, np.pi / 2)

    ret = Scene(mesh, camera)

    return ret


cornell_box = make_cornell_box()
