# 导入OpenGL的库
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
# from numpy import *
import sys

from contextlib import contextmanager

import logging as log
import itertools

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
timerSecs = 2000

width = 300
high = 300
xmin = -5
xmax = 5
ymin = -5
ymax = 5
dnear = -100
dfar = 100
x0 = 0
y0 = 0
red = 0
green = 1
blue = 0
lookfx = 0
lookfy = 0
lookfz = 10
looktx = 0
lookty = 0
looktz = -10
anglex = 0
angley = 0
anglez = 0
movex = 0
movey = 0
movez = 0
angle1 = 31
angle2 = -11
leg1 = False
leg2 = True

z_dis = 0
scaleLevel = 1

GLUT_WHEEL_UP  = 3
GLUT_WHEEL_DOWN  = 4

# tag: basic setting here


# done: complate the argvs of these funcs
# note: this is all Callback Registration func of glut


def DisplayFunc():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glClearColor(1, 1, 1, 0)
    glMatrixMode( GL_MODELVIEW )
    glLoadIdentity()
    gluLookAt(lookfx,lookfy,lookfz,looktx,lookty,looktz,0,1,0)
    glColor3f(red, green, blue)
    glRotatef(anglex, 1, 0, 0)
    glRotatef(angley, 0, 1, 0)
    glRotatef(anglez, 0, 0, 1)
    glTranslatef(movex, movey, movez)

    # tag: display 系数
    # // 设置光源
    setLight()

    glScale(scaleLevel,scaleLevel,scaleLevel)
    glRotate(30,1,2,0)
    # glLoadIdentity()
    # 绘制
    draw_world_base_line()
    glTranslate(0,0,z_dis)
    draw_body()
    draw_head()
    draw_left_leg()
    draw_right_leg()
    draw_left_arm()
    draw_right_arm()

    glutSwapBuffers()

    # tag: add draw func above

    # glutSwapBuffers()


def OverlayDisplayFunc():
    pass


def ReshapeFunc(width, height):
    # global windowWidth, windowHeight
    # windowHeight = height
    # windowWidth = width
    # glutPostRedisplay()
    pass


def KeyboardFunc(key, x, y):
    global anglex, angley, anglez,movex,movey,movez
    # qe
    if key == b'e' or key == b'E':
        angley += 10
    if key == b'q' or key == b'Q':
        angley -= 10

    # wasd
    if key == b'w' or key == b'W':
        movey -= 0.3
    elif key == b's' or key == b'S':
        movey += 0.3
    elif key == b'a' or key == b'A':
        movex += 0.3
    elif key == b'd' or key == b'D':
        movex -= 0.3
    
    

    

        
    
    glutPostRedisplay()
    # tag: 键盘交互 函数
    # done: basic view move


def MouseFunc(button, state, x, y):
    global isMoving, oldx, oldy,scaleLevel
    log.debug((button,state,x,y))

    # tag: 滚轮放大缩小功能
    if button == GLUT_WHEEL_DOWN and state == GLUT_DOWN:
        log.debug(scaleLevel)
        if scaleLevel>=0.1:
            scaleLevel-=0.1
    
    if button == GLUT_WHEEL_UP and state == GLUT_DOWN:
        log.debug(scaleLevel)
        scaleLevel+=0.1
    

    glutPostRedisplay()
    # tag: 鼠标交互 函数


def MotionFunc(x, y):
    # global oldx, oldy
    # if isMoving:

    #     if oldx == None and oldy == None:
    #         glTranslate(((x-windowWidth/2)/windowWidth)*5,
    #                     ((windowHeight/2-y)/windowHeight)*5, 0)
    #     else:
    #         glTranslate(((x-oldx)/windowWidth)*5,
    #                     ((oldy-y)/windowHeight)*5, 0)

    # oldx = x
    # oldy = y
    # glutPostRedisplay()
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
    # glRotate(1, 1, 1, 1)
    pass


def TimerFunc(value):
    global angle1, angle2, leg1, leg2, anglex, angley, anglez,z_dis
    # anglex += 5
    # angley += 5
    # anglez += 5
    z_dis+=0.03
    if z_dis>30:
        z_dis = 0
    if angle1>=30:
        leg1=False # 向后
    elif angle1<=-10:
        leg1=True

    if -20<angle1<=0:
        dis = 0.2
    elif 0<angle1<60:
        dis = 0.6

    if leg1:
        angle1+=dis
    else:
        angle1-=dis



    if angle2>=30:
        leg2=False # 向后
    elif angle2<=-10:
        leg2=True

    if -20<angle2<=0:
        dis = 0.2
    elif 0<angle2<60:
        dis = 0.6

    if leg2:
        angle2+=dis
    else:
        angle2-=dis

    # tag: 定时器 函数
    glutPostRedisplay()
    glutTimerFunc(timerSecs, TimerFunc, 0)

    # glRotate(2, 1, 1, 1)
    # glutPostRedisplay()
    # glutTimerFunc(50, TimerFunc, value)

################################


def init():
    glClearColor(0, 0, 0, 0)
    glViewport(x0, y0, windowWidth, windowHeight)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(xmin, xmax, ymin, ymax, dnear, dfar)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    glEnable(GL_DEPTH_TEST)
    glShadeModel(GL_SMOOTH)


def draw_world_base_line():
    with freeze():
        # glTranslate(0.1, 0, 0)
        # glRotate(300, 1, 0, 0)
        # glRotate(270, 0, 0, 1)
        # glScale(0.1, 0.1, 0.1)

        # note: red is x,green is y, blue is z

        setMaterial(rgb(255, 0, 0))  # red x
        glLineWidth(10)
        with connect(GL_LINES):
            glVertex3fv([0.0, 0.0, 0.0])
            glVertex3fv([10.0, 0.0, 0.0])

        glLineWidth(10)
        setMaterial(rgb(0, 255, 0))
        with connect(GL_LINES):
            glVertex3fv([0.0, 0.0, 0.0])
            glVertex3fv([0.0, 10.0, 0.0])
        glLineWidth(10)
        setMaterial(rgb(0, 0, 255))
        with connect(GL_LINES):
            glVertex3fv([0.0, 0.0, 0.0])
            glVertex3fv([0.0, 0.0, 10.0])


def draw_body():
    """draw_body
    """
    with freeze():
        create_cube(-2,2,0,6,-0.5,0.5)


def draw_head():
    with freeze():
        setMaterial(rgb(0, 0, 0))
        glTranslate(0, 7.5, 0)
        glutSolidSphere(1.5, 20, 20)


def draw_left_leg():
    """draw_left_leg
    """
    leg_dis = -1.5
    leg_length = 2

    with freeze():
        glTranslate(leg_dis, 0, 0)
        glRotate(angle1,-1,0,0)
        create_cube(-0.5,0.5,-leg_length,0,-0.5,0.5)

        glTranslate(0, -leg_length-0.5, 0)
        glutSolidSphere(0.5, 20, 20)

        glTranslate(0, -0.5, 0)
        if angle1>0:glRotate(-angle1,-1,0,0)
        create_cube(-0.5,0.5,-leg_length*2,0,-0.5,0.5)


def draw_right_leg():
    """draw_right_leg
    """
    leg_dis = 1.5
    leg_length = 2

    with freeze():
        glTranslate(leg_dis, 0, 0)
        glRotate(angle2,-1,0,0)
        create_cube(-0.5,0.5,-leg_length,0,-0.5,0.5)

        glTranslate(0, -leg_length-0.5, 0)
        glutSolidSphere(0.5, 20, 20)

        glTranslate(0, -0.5, 0)
        if angle2>0:glRotate(-angle2,-1,0,0)
        create_cube(-0.5,0.5,-leg_length*2,0,-0.5,0.5)


def draw_left_arm():
    """draw_left_arm
    """
    dis = [-2.5,6,0]
    leg_length = 2
    with freeze():
        glTranslate(*dis)
        glRotate(angle2,-1,0,0)
        create_cube(-0.5,0.5,-leg_length,0,-0.5,0.5)

        glTranslate(0, -leg_length-0.5, 0)
        glutSolidSphere(0.5, 20, 20)

        glTranslate(0, -0.5, 0)
        create_cube(-0.5,0.5,-leg_length*2,0,-0.5,0.5)



def draw_right_arm():
    """draw_right_arm
    """
    dis = [2.5,6,0]
    leg_length = 2
    with freeze():
        glTranslate(*dis)
        glRotate(angle1,-1,0,0)
        create_cube(-0.5,0.5,-leg_length,0,-0.5,0.5)

        glTranslate(0, -leg_length-0.5, 0)
        glutSolidSphere(0.5, 20, 20)

        glTranslate(0, -0.5, 0)
        create_cube(-0.5,0.5,-leg_length*2,0,-0.5,0.5)


def create_cube(xl,xr,yu,yd,zb,zf):
    vertex_list = []
    for z,y,x in itertools.product([zb,zf],[yu,yd],[xl,xr]):
        vertex_list.append([x,y,z])

    index_list = [
        [0, 2, 3, 1],
        [0, 4, 6, 2],
        [0, 1, 5, 4],
        [4, 5, 7, 6],
        [1, 3, 7, 5],
        [2, 6, 7, 3]
    ]

    with connect(GL_POLYGON):
        for i in range(6):
            for j in range(4):
                glVertex3fv(vertex_list[index_list[i][j]])



# tag: write draw_parts function here


def setLight():
    position = [1.0, 1.0, 1.0, 0.0]
    position1 = [-1.0, -1.0, 1.0, 0.0]
    ambient = [0.2, 0.2, 0.2, 0.2]
    diffuse = [0.5, 0.5, 0.2, 0.2]
    specular = [0.5, 0.5, 0.5, 0.2]

    # tag: 设置光照参数

    glLight(GL_LIGHT0, GL_POSITION, position)
    """
    GL_POSITION属性。表示光源所在的位置。由四个值（X, Y, Z, W）表示。
    方向性光源（Directional Light） 第四个值W为零，则表示该光源位于无限远处，
    前三个值表示了它所在的方向。
    通常，太阳可以近似的被认为是方向性光源。
    """
    glLight(GL_LIGHT0, GL_AMBIENT, ambient)
    glLight(GL_LIGHT0, GL_DIFFUSE, diffuse)
    glLight(GL_LIGHT0, GL_SPECULAR, specular)

    glEnable(GL_LIGHT0)

    glLight(GL_LIGHT1, GL_POSITION, position1)
    """
    GL_POSITION属性。表示光源所在的位置。由四个值（X, Y, Z, W）表示。
    方向性光源（Directional Light） 第四个值W为零，则表示该光源位于无限远处，
    前三个值表示了它所在的方向。
    通常，太阳可以近似的被认为是方向性光源。
    """
    glLight(GL_LIGHT1, GL_AMBIENT, ambient)
    glLight(GL_LIGHT1, GL_DIFFUSE, diffuse)
    glLight(GL_LIGHT1, GL_SPECULAR, specular)

    glEnable(GL_LIGHT1)

    glEnable(GL_LIGHTING)
    glEnable(GL_DEPTH_TEST)


def setMaterial(rgb):
    material_ambient = [rgb[0], rgb[1], rgb[2], 1.0]
    material_diffuse = [0.0, 0.0, 0.5, 1.0]
    material_specular = [0.0, 0.0, 1.0, 1.0]
    material_emission = [0.0, 0.0, 0.0, 1.0]
    material_shininess = [30.0]

    glMaterialfv(GL_FRONT, GL_AMBIENT, material_ambient)
    glMaterialfv(GL_FRONT, GL_DIFFUSE, material_diffuse)
    glMaterialfv(GL_FRONT, GL_SPECULAR, material_specular)
    glMaterialfv(GL_FRONT, GL_EMISSION, material_emission)
    glMaterialfv(GL_FRONT, GL_SHININESS, material_shininess)

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
                   void (*func)(int value), value)
    """

    glutMainLoop()


if __name__ == "__main__":
    main()
