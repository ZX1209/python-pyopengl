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


x1 = -0.25
y1 = -0.25
width = 0.5
height = 0.5
xMin = -1.0
xMax = 1.0
yMin = -1.0
yMax = 1.0
widthWindows = 400
heightWindows = 400
colorR = 0.5
colorG = 0.5
colorB = 0.5


# tag: basic setting here

# with tag("h1"):
#     print("hello")
#     print("world")


# done: complate the argvs of these funcs
# note: this is Callback Registration func of glut


def DisplayFunc():
    glClearColor(0, 0, 0, 0)
    glClearDepth(1)
    glClear(GL_COLOR_BUFFER_BIT)

    glColor(colorR, colorG, colorB)
    glRectf(x1, y1, x1+width, y1+height)
    glFlush()

    # tag: add draw func above

    # glutSwapBuffers()


def OverlayDisplayFunc():
    pass


def ReshapeFunc(width, height):
    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(xMin, xMax, yMin, yMax, 0.0, 10.0)


def KeyboardFunc(key, x, y):
    global y1, x1
    # log.debug(key)

    if key == b'w' or key == b'W':
        y1 += 0.1
        if y1 >= yMax-height:
            y = yMax-height
        glutPostRedisplay()
    elif key == b's' or key == b'S':
        y1 -= 0.1
        if y1 < yMin:
            y = yMin
        glutPostRedisplay()
    elif key == b'd' or key == b'D':
        x1 += 0.1
        if x1 >= xMax-height:
            x = xMax-height
        glutPostRedisplay()
    elif key == b'a' or key == b'A':
        x1 -= 0.1
        if x1 < xMin:
            x = xMin
        glutPostRedisplay()


def MouseFunc(button, state, x, y):
    global colorR, colorG, colorB
    if state == GLUT_DOWN:
        if button == GLUT_LEFT_BUTTON:
            colorR += 0.1
            if colorR > 1:
                colorR = 0
            glutPostRedisplay()
        elif button == GLUT_MIDDLE_BUTTON:
            colorG += 0.1
            if colorG > 1:
                colorG = 0
            glutPostRedisplay()
        elif button == GLUT_RIGHT_BUTTON:
            colorB += 0.1
            if colorB > 1:
                colorB = 0
            glutPostRedisplay()


def MotionFunc(x, y):
    global x1, y1
    x1 = x/widthWindows*(xMax-xMin)+xMin-width/2
    y1 = (heightWindows-y) / heightWindows*(yMax-yMin)+yMin-width/2
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
    pass


def TimerFunc(value):
    pass

################################


def init():
    pass


def draw_teapot():
    glClearColor(1.0, 1.0, 1.0, 1.0,)
    glClearDepth(1.0)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glEnable(GL_COLOR_MATERIAL)
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    glEnable(GL_AUTO_NORMAL)
    glEnable(GL_NORMALIZE)
    glEnable(GL_DEPTH_TEST)
    glDepthFunc(GL_LESS)

    # 设置模型变换矩阵
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

    # 设置光源参数
    position = [1.0, 1.0, 1.0, 0.0]
    ambient = [0.2, 0.2, 0.2, 0.2]
    diffuse = [0.5, 0.5, 0.2, 0.2]
    specular = [0.5, 0.5, 0.5, 0.2]

    glLight(GL_LIGHT0, GL_POSITION, position)
    glLight(GL_LIGHT0, GL_AMBIENT, ambient)
    glLight(GL_LIGHT0, GL_DIFFUSE, diffuse)
    glLight(GL_LIGHT0, GL_SPECULAR, specular)

    material_ambient = [0.2, 0.2, 0.2, 0.2]
    material_diffuse = [0.2, 0.8, 0.4, 0.8]
    material_specular = [0.2, 0.8, 0.4, 0.8]
    material_emission = [0.2, 0.2, 0.2, 1.0]
    material_shininess = [10.0]

    glMaterialfv(GL_BACK, GL_AMBIENT, material_ambient)
    glMaterialfv(GL_BACK, GL_DIFFUSE, material_diffuse)
    glMaterialfv(GL_BACK, GL_SPECULAR, material_specular)
    glMaterialfv(GL_BACK, GL_EMISSION, material_emission)
    glMaterialfv(GL_BACK, GL_SHININESS, material_shininess)

    glColor(rgb(1, 0, 0))
    glRotated(60, 1, 1, 1)
    glutSolidTeapot(0.5)

    glutSwapBuffers()


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
    glutInitDisplayMode(GLUT_SINGLE)
    glutInitWindowPosition(100, 100)
    glutInitWindowSize(400, 400)
    glutCreateWindow("pyopengl demo")

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
