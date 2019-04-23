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


# todo: complate the argvs of these funcs
# note: this is Callback Registration func of glut


def DisplayFunc():
    draw_world_base_line()

    # tag: add draw func above

    glutSwapBuffers()


def OverlayDisplayFunc():
    pass


def ReshapeFunc(width, height):
    pass


def KeyboardFunc(key, x, y):
    pass


def MouseFunc(button, state, x, y):
    pass


def MotionFunc(x, y):
    pass


def PassiveMotionFunc(x, y):
    pass


def VisibilityFunc(state):
    pass


def EntryFunc(state):
    pass


def SpecialFunc(key, x, y):
    pass


def SpaceballMotionFunc(x, y, z):
    pass


def SpaceballRotateFunc(x, y, z):
    pass


def SpaceballButtonFunc(button, state):
    pass


def ButtonBoxFunc(button, state):
    pass


def DialsFunc(dial, value):
    pass


def TabletMotionFunc(x, y):
    pass


def TabletButtonFunc(button, state, x, y):
    pass


def MenuStatusFunc(status, x, y):
    pass


def IdleFunc():
    pass


def TimerFunc(value):
    pass

################################


def init():
    pass

# tag: add you function here


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


def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowPosition(50, 50)
    glutInitWindowSize(400, 400)
    glutCreateWindow("opengl demo")

    init()

    # glut callback function regist ignore it
    glutDisplayFunc(DisplayFunc)
    glutOverlayDisplayFunc(OverlayDisplayFunc)
    glutReshapeFunc(ReshapeFunc)
    glutKeyboardFunc(KeyboardFunc)
    glutMouseFunc(MouseFunc)
    glutMotionFunc(MotionFunc)
    glutPassiveMotionFunc(PassiveMotionFunc)
    glutVisibilityFunc(VisibilityFunc)
    glutEntryFunc(EntryFunc)
    glutSpecialFunc(SpecialFunc)
    glutSpaceballMotionFunc(SpaceballMotionFunc)
    glutSpaceballRotateFunc(SpaceballRotateFunc)
    glutSpaceballButtonFunc(SpaceballButtonFunc)
    glutButtonBoxFunc(ButtonBoxFunc)
    glutDialsFunc(DialsFunc)
    glutTabletMotionFunc(TabletMotionFunc)
    glutTabletButtonFunc(TabletButtonFunc)
    glutMenuStatusFunc(MenuStatusFunc)
    glutIdleFunc(IdleFunc)

    # fro glutTimerFunc
    msecs = 10
    value = 10
    glutTimerFunc(msecs, TimerFunc, value)
    """Usage
    void glutTimerFunc(unsigned int msecs,
                   void (*func)(int value), value);
    """

    glutMainLoop()


if __name__ == "__main__":
    main()
