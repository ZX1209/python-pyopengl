# 导入OpenGL的库
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
# from numpy import *
import sys

from contextlib import contextmanager

import logging as log

# tag: add module above


log.basicConfig(level=log.DEBUG)


def rgb(r, g, b):
    """for colorize of vscode extention
    """
    return r, g, b


@contextmanager
def freeze():
    """context manager for opengl's push and pop matrix 
    like a freeze magic freeze the above behaviour
    let the change be local
    """
    glPushMatrix()
    yield
    glPopMatrix()


@contextmanager
def connect(name):
    """context manager for opengl's draw things 
    just start point points
    """
    glBegin(name)
    yield
    glEnd()

# tag: basic setting here

# with tag("h1"):
#     print("hello")
#     print("world")


def init():
    pass


angle = 0.0


def draw_cube2():
    glPushMatrix()

    glTranslate(-0.5, 1, 1)

    glutSolidCube(1)
    glPopMatrix()


def draw_cube():
    global angle

    glPushMatrix()

    glTranslate(1, 1, 1)

    glutSolidCube(1)

    draw_cube2()
    glPopMatrix()

    angle += 0.1


def draw_body():

    glPushMatrix()

    glPopMatrix()


def draw_world_base_line():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    with freeze():
        # glTranslate(0.1, 0, 0)
        glRotate(300, 1, 0, 0)
        glRotate(270, 0, 0, 1)
        glScale(0.1, 0.1, 0.1)

        # note: red is x,green is y, blue is z
        glColor(rgb(255, 0, 0))  # red x

        glLineWidth(2.0)
        with connect(GL_LINES):
            glVertex3fv([0.0, 0.0, 0.0])
            glVertex3fv([1.0, 0.0, 0.0])

        glColor(rgb(0, 255, 0))
        with connect(GL_LINES):
            glVertex3fv([0.0, 0.0, 0.0])
            glVertex3fv([0.0, 1.0, 0.0])

        glColor(rgb(0, 0, 255))
        with connect(GL_LINES):
            glVertex3fv([0.0, 0.0, 0.0])
            glVertex3fv([0.0, 0.0, 1.0])

# tag: def draw func here


def display():
    draw_world_base_line()

    # tag: add draw func above

    glutSwapBuffers()


def keyboard(key, x, y):
    log.debug((key, x, y))
    if key == b'x':
        glRotate(10, 1, 0, 0)
    elif key == b'y':
        glRotate(10, 0, 1, 0)
    elif key == b'z':
        glRotate(10, 0, 0, 1)

    glutPostRedisplay()

    # tag: key handle


def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowPosition(50, 50)
    glutInitWindowSize(400, 400)
    glutCreateWindow("robot animation")

    init()
    glutDisplayFunc(display)
    glutIdleFunc(display)
    # glutReshapeFunc(reshape)
    # glutIdleFunc(idle)
    glutKeyboardFunc(keyboard)
    glutMainLoop()


if __name__ == "__main__":
    main()
