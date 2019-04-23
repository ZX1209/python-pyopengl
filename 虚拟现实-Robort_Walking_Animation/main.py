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


isMoving = False
oldx = None
oldy = None
windowWidth = 800
windowHeight = 800
timerSecs = 100
# tag: basic setting here


# done: complate the argvs of these funcs
# note: this is all Callback Registration func of glut


def DisplayFunc():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    with freeze():
        # glRotate(300, 1, 0, 0)
        # glRotate(270, 0, 0, 1)
        draw_world_base_line()
        glScale(0.1, 0.1, 0.1)

        draw_body()

    # tag: add draw func above

    glutSwapBuffers()


def OverlayDisplayFunc():
    pass


def ReshapeFunc(width, height):
    # global windowWidth, windowHeight
    # windowHeight = height
    # windowWidth = width
    # glutPostRedisplay()
    pass


def KeyboardFunc(key, x, y):
    if key == b'x' or key == b'X':
        glRotate(5, 1, 0, 0)
        glutPostRedisplay()
    elif key == b'y' or key == b'Y':
        glRotate(5, 0, 1, 0)
        glutPostRedisplay()
    elif key == b'z' or key == b'Z':
        glRotate(5, 0, 0, 1)
        glutPostRedisplay()
    # done: basic view move


def MouseFunc(button, state, x, y):
    global isMoving, oldx, oldy
    if button == GLUT_RIGHT_BUTTON and state == GLUT_DOWN:
        isMoving = True
        log.debug((oldx, oldy, x, y))
    elif button == GLUT_RIGHT_BUTTON and state == GLUT_UP:
        isMoving = False
        oldx = None
        oldy = None
        glLoadIdentity()

    glutPostRedisplay()
    # tag: mouse deal


def MotionFunc(x, y):
    global oldx, oldy
    if isMoving:

        if oldx == None and oldy == None:
            glTranslate(((x-windowWidth/2)/windowWidth)*5,
                        ((windowHeight/2-y)/windowHeight)*5, 0)
        else:
            glTranslate(((x-oldx)/windowWidth)*5,
                        ((oldy-y)/windowHeight)*5, 0)

    oldx = x
    oldy = y
    glutPostRedisplay()


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
    # glRotate(1, 1, 1, 1)
    pass


def TimerFunc(value):
    glRotate(2, 1, 1, 1)
    glutPostRedisplay()
    glutTimerFunc(50, TimerFunc, value)

################################


def init():
    pass


def draw_world_base_line():
    with freeze():
        # glTranslate(0.1, 0, 0)
        # glRotate(300, 1, 0, 0)
        # glRotate(270, 0, 0, 1)
        # glScale(0.1, 0.1, 0.1)

        # note: red is x,green is y, blue is z
        glColor(rgb(255, 0, 0))  # red x

        glLineWidth(2.0)
        with connect(GL_LINES):
            glVertex3fv([0.0, 0.0, 0.0])
            glVertex3fv([10.0, 0.0, 0.0])

        glColor(rgb(0, 255, 0))
        with connect(GL_LINES):
            glVertex3fv([0.0, 0.0, 0.0])
            glVertex3fv([0.0, 10.0, 0.0])

        glColor(rgb(0, 0, 255))
        with connect(GL_LINES):
            glVertex3fv([0.0, 0.0, 0.0])
            glVertex3fv([0.0, 0.0, 10.0])


def draw_body():
    """draw_body
    """
    with freeze():
        glTranslatef(0, 1.5, 0)
        glScalef(1, 1, 2)
        glutSolidCube(1)

# tag: add you function here


def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    glutInitWindowPosition(50, 50)
    glutInitWindowSize(windowWidth, windowHeight)
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
    timerSecs = 10
    value = 10
    glutTimerFunc(timerSecs, TimerFunc, value)
    """Usage
    void glutTimerFunc(unsigned int msecs,
                   void (*func)(int value), value);
    """

    glutMainLoop()


if __name__ == "__main__":
    main()
