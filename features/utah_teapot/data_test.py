import math
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import relaxrender.utah_teapot.teapot_data as teapot


points = teapot.t_pos
for piece in [teapot.t_patch[5]]:
    for p in piece:
        point = points[p]
        x, y, z = point[0], point[1], point[2]
        # diff = y/math.sqrt(2)
        plt.plot(x, y, 'o')
        plt.text(x, y, str(p))
    plt.show()
    pass
plt.xlim([-4, 4])
plt.ylim([0, 4])
"""
plt.savefig("xz.png")

plt.figure()
for piece in teapot.t_patch:
    for p in piece:
        point = points[p]
        x, y, z = point[0], point[1], point[2]
        # diff = y/math.sqrt(2)
        plt.plot(x, y, 'o')
        plt.text(x, y, str(p))
    # plt.show()
plt.xlim([-4, 4])
# plt.ylim([, 4])
plt.savefig("xy.png")

plt.figure()
for piece in teapot.t_patch:
    for p in piece:
        point = points[p]
        x, y, z = point[0], point[1], point[2]
        # diff = y/math.sqrt(2)
        plt.plot(y, z, 'o')
        plt.text(y, z, str(p))
    # plt.show()
# plt.xlim([-4, 4])
# plt.ylim([, 4])
plt.savefig("yz.png")


plt.xlim([-5, 5])
plt.ylim([-1, 5])
plt.show()
"""
# np.arange()

"""
x = np.matrix([p[0] for p in teapot.t_pos])
y = np.matrix([p[1] for p in teapot.t_pos])
z = np.matrix([p[2] for p in teapot.t_pos])
"""

for piece in teapot.t_patch:
    x, y, z = [], [], []
    fig = plt.figure()
    ax = Axes3D(fig)
    for p in piece:
        x += [teapot.t_pos[p][0]]
        y += [teapot.t_pos[p][1]]
        z += [teapot.t_pos[p][2]]
        ax.text(x[-1], y[-1], z[-1], str(p))

    x = np.matrix(x)
    y = np.matrix(y)
    z = np.matrix(z)

    ax.scatter(x, y, z)
    ax.set_xlabel('X Label')
    ax.set_ylabel('Y Label')
    ax.set_zlabel('Z Label')
    ax.set_xlim([-4, 4])
    ax.set_ylim([-2, 0])
    ax.set_zlim([0, 4])
    # plt.savefig("teapot.png")
    plt.show()

    fig = plt.figure()
    ax = Axes3D(fig)
    ax.plot_wireframe(x, y, z)
    ax.set_xlabel('X Label')
    ax.set_ylabel('Y Label')
    ax.set_zlabel('Z Label')
    ax.set_xlim([-4, 4])
    ax.set_ylim([-2, 0])
    ax.set_zlim([0, 4])
    # plt.savefig("teapot1.png")
    plt.show()
    pass

fig = plt.figure()
ax = Axes3D(fig)
surf = ax.plot_surface(x, y, z)
ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')
# plt.savefig("teapot2.png")
plt.show()