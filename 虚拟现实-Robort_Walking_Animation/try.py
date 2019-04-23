#导入OpenGL的库
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
#from numpy import *
import sys

# # assimp to load model
# from pyassimp import *

no_mat = [ 1.0, 1.0, 0.0, 1.0 ];
mat_ambient = [ 1.0, 0.5, 1.0, 1.0 ];
mat_ambient_color = [ 1.0, 1.0, 1.0, 1.0 ];
mat_diffuse = [ 1.0, 1.0, 1.0, 1.0 ];
mat_specular = [ 0.0, 0.6, 0.5, 1.0 ];
no_shininess = [ 0.1 ];
low_shininess = [ 5.0 ];
high_shininess = [ 100.0 ];
mat_emission = [ 0.3, 0.2, 0.2, 0.0 ];

angle = 0
neck = 0
lshoulder = -5
lelbow = -10
rshoulder = 5
relbow = 10
lhips = 5
rhips = -5
lfoot = 10
rfoot = -10
flagneck = 0
flaglshoulder = 0
flaglelbow = 0
flagrshoulder = 0
flagrelbow = 0
flaglhips = 0
flagrhips = 0
flaglfoot = 0
flagrfoot = 0
 
def init():
    ambient = [ 0.0, 0.0, 0.0, 1.0 ]
    diffuse = [ 1.0, 1.0, 1.0, 1.0 ]
    position = [ 0.0, 5.0, 10.0, 0.0 ]
    lmodel_ambient = [ 0.4, 0.4, 0.4, 1.0 ]
    local_view = [ 0.0 ]

    glClearColor(0, 0, 0, 0);

    glLight(GL_LIGHT0, GL_AMBIENT, ambient);
    glLight(GL_LIGHT0, GL_DIFFUSE, diffuse);
    glLight(GL_LIGHT0, GL_POSITION, position);
    glLightModelfv(GL_LIGHT_MODEL_AMBIENT, lmodel_ambient);
    glLightModelfv(GL_LIGHT_MODEL_LOCAL_VIEWER, local_view);

    glShadeModel(GL_SMOOTH);
    glEnable(GL_DEPTH_TEST);
    glEnable(GL_LIGHTING);
    glEnable(GL_LIGHT0);
 
def plotfunc():
    glClear(GL_COLOR_BUFFER_BIT)
    glPointSize(5.0)
    
    #绘制坐标系
    glColor3f(1.0, 1.0, 0.0)
    glBegin(GL_LINES) #画线
    glVertex2f(-5.0, 0.0)
    glVertex2f(5.0, 0.0)
    glVertex2f(0.0, 5.0)
    glVertex2f(0.0, -5.0)
    glEnd()
 
    #绘制y = x*x*x (-5.0 < x < 5.0) 的图像
    glColor3f(0.0, 0.0, 0.0)
    glBegin(GL_LINES)#画线
    #for x in arange(-5.0, 5.0, 0.1):
    for x in (i * 0.1 for i in range(-50, 50)):
        y = x * x * x
        glVertex2f(x, y) #绘制每个0.1个步长的点
    glEnd()
 
    glFlush()

def draw_body():
    glPushMatrix();
    glTranslatef(0, 1.5, 0);
    glScalef(0.5, 1, 0.4);
    glMaterialfv(GL_FRONT, GL_AMBIENT, mat_ambient_color);
    glMaterialfv(GL_FRONT, GL_DIFFUSE, mat_diffuse);
    glMaterialfv(GL_FRONT, GL_SPECULAR, mat_specular);
    glMaterialfv(GL_FRONT, GL_SHININESS, high_shininess);
    glMaterialfv(GL_FRONT, GL_EMISSION, no_mat);
    glutSolidCube(4);
    glPopMatrix();

def draw_leye():
    glPushMatrix();

    glColor3f(0, 0, 0);
    glTranslatef(-0.2, 4, 0.5);
    glRotatef(neck, 0, 0, 1);
    glTranslatef(-0.2, 0.5, 0.5);

    glutWireSphere(0.2, 100, 300);

    glPopMatrix();

def draw_try():
    glPushMatrix();

    glColor3f(0, 0, 12);
    # glTranslatef(-0.2, 4, 0.5);
    # glRotatef(neck, 0, 0, 1);
    # glTranslatef(-0.2, 0.5, 0.5);

    glutSolidCube(2);

    glPopMatrix();


angle = 0

def idle():
    pass


def display():
    global angle
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    glRotatef(angle, 0, 1, 0)
    angle += 1

    # glPushMatrix()
    # glRotatef(angle, 0, 1, 0)
    # glTranslatef(0, 4, 0)
    draw_body()
    draw_leye()

    draw_try()


    # draw_reye()
    # draw_mouth()
    # draw_head()
    # draw_leftshoulder()
    # draw_rightshoulder()
    # draw_leftfoot()
    # draw_rightfoot()
    # glPopMatrix()
    glutSwapBuffers()

def reshape(w,h):
    glViewport(0, 0, w, h);
    glMatrixMode(GL_PROJECTION);
    glLoadIdentity();
    gluPerspective(74.0, w / h, 1.0, 1000.0);
    # glOrtho(-8,8,-8,8,-10,10);
    glMatrixMode(GL_MODELVIEW);
    glLoadIdentity();
    gluLookAt(0.0, 4.0, 10, 0.0, 4, 0.0, 0.0, 1.0, 0.0);
 
def main():
    print("按键’W’,'A',’S’,'D'为向上，向左，向下，向右");
    print("按键’Q’,'E'为向前，向后");
    print("按键’1’,’2’为整体旋转");
    print("按键’3’为头部旋转");
    print("按键’4’,’5’,’6’,’7’为手臂旋转");
    print("按键’8’,’9’,’a’,’b’为腿部旋转");

    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowPosition(50,50)
    glutInitWindowSize(400,400)
    glutCreateWindow("robot animation")
    
    init()
    glutDisplayFunc(display)
    glutReshapeFunc(reshape)
    glutIdleFunc(idle)
    # glutKeyboardFunc(keyboard)
    glutMainLoop()
 
if __name__ == "__main__":
    main()
