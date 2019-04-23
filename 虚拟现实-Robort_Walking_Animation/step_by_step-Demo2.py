#导入OpenGL的库
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
#from numpy import *
import sys

angle = 0.0


# /**
#  * 渲染回调函数
#  */
def RenderScenceCB():
    global angle
    # 清空颜色缓存
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);
    # 交换前后缓存

    glPushMatrix();

    glRotate(angle,2.0,1.0,3.0);

    glBegin(GL_TRIANGLES);

    glVertex3f(-0.5,-0.5,0.0);

    glVertex3f(0.5,0.0,0.0);

    glVertex3f(0.0,0.5,0.0);
    glVertex3f(0.0,0.5,1.0);

    glEnd();

          
    glPopMatrix();


    glutSwapBuffers();

    angle+=1

# /**
#  * 主函数
#  */
def main():

    # 初始化GLUT
    glutInit(sys.argv);

    # 显示模式：双缓冲、RGBA
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA);

    # 窗口设置
    glutInitWindowSize(480, 320);      # 窗口尺寸
    glutInitWindowPosition(100, 100);  # 窗口位置
    glutCreateWindow("Tutorial 01");   # 窗口标题

    # 开始渲染
    glutDisplayFunc(RenderScenceCB);

    glutReshapeFunc(reshape)
    # glutKeyboardFunc(keyboard)

    # 缓存清空后的颜色值
    glClearColor(100, 0.0, 0.0, 0.0);

    # 通知开始GLUT的内部循环
    glutMainLoop();


if __name__ == "__main__":
    main()