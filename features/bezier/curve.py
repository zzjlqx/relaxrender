from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import numpy as np
import ctypes
import math

ctrlPoints=np.array([[[-1.5, -1.5, 2.0], [-0.5, -1.5, 2.0], [0.5, -1.5, -1.0],[1.5,-1.5,2.0]],
                     [[-1.5, -0.5, 1.0], [-0.5, 1.5, 2.0], [0.5, 0.5, 1.0],[1.5,-0.5,-1.0]],
                     [[-1.5, 0.5, 2.0], [-0.5, 0.5, 1.0], [0.5, 0.5, 3.0],[1.5,-1.5,1.5]],
                     [[-1.5,1.5,-2.0],[-0.5,1.5,-2.0],[0.5,0.5,1.0],[1.5,1.5,-1.0]]],dtype='float32')
Scale=0.0
def initLight():
    glDepthFunc(GL_LESS)
    #glShadeModel(GL_SMOOTH)
    ambient=[0.4, 0.6, 0.2, 1.0];
    position=[0.0, 1.0, 3.0, 1.0];
    mat_diffuse=[0.2, 0.4, 0.8, 1.0];
    mat_specular=[1.0, 1.0, 1.0, 1.0];
    mat_shininess=[80.0];
    glEnable(GL_LIGHTING);
    glEnable(GL_LIGHT0);
    glLightfv(GL_LIGHT0, GL_AMBIENT, ambient);
    glLightfv(GL_LIGHT0, GL_POSITION, position);
    glMaterialfv(GL_FRONT, GL_DIFFUSE, mat_diffuse);
    glMaterialfv(GL_FRONT, GL_SPECULAR, mat_specular);
    glMaterialfv(GL_FRONT, GL_SHININESS, mat_shininess);

    glEnable(GL_DEPTH_TEST)
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)

def Reshape(w,h):
    glViewport(0,0,w,h)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    if w<=h:
        glOrtho(-5.0,5.0,-5.0*h/w,5.0*h/w,-5.0,5.0)
    else:
        glOrtho(-5.0*w/h,5.0*w/h,-5.0,5.0,-5.0,5.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

def DrawPoints():
    glColor3f(1.0, 0.0, 0.0)
    #glPointSize(5.0)
    glBegin(GL_POINTS)
    for i in range(3):
        for j in range(3):
            glVertex3fv(ctrlPoints[i][j])
    glEnd()

def Draw():
    global Scale
    Scale=Scale+0.0001
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    glMatrixMode(GL_MODELVIEW)#设置模型参数
    #glPushMatrix()
    #glRotatef(45.0, 0.0, 1.0, 0.0)
    #glRotatef(60.0, 1.0, 0.0, 0.0)
    glRotatef(0.03,0.0,1.0,1.0)
    glColor3f(0.0, 1.0, 0.0)
    glMap2f(GL_MAP2_VERTEX_3, 0.0, 1.0, 0.0, 1.0, ctrlPoints)#曲线创建映射
    glEnable(GL_MAP2_VERTEX_3)
    glMapGrid2f(20, 0.0, 1.0, 20, 0.0, 1.0)
    #glEvalMesh2(GL_LINE, 0, 10, 0, 10)#网格
    glEvalMesh2(GL_FILL, 0, 20, 0, 20)#光滑平面
    #DrawPoints()
    #glPopMatrix()
    glutSwapBuffers()


def main():
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowSize(500, 500)
    glutInitWindowPosition(50, 50)
    glutCreateWindow("curve")
    glutDisplayFunc(Draw)
    glutIdleFunc(Draw)
    glutReshapeFunc(Reshape)
    glClearColor(0.0, 0.0, 0.0, 1.0)#背景光
    #glEnable(GL_AUTO_NORMAL)
    #glEnable(GL_NORMALIZE)
    initLight()
    glutMainLoop()

if __name__ == '__main__':
    main()
