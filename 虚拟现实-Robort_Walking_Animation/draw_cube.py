#导入OpenGL的库
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
#from numpy import *
import sys

times = 0
rotate = 0

 
def renderScene():
    global times,rotate
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);
    
    glMatrixMode(GL_MODELVIEW); 
    glPushMatrix();
 
    #glTranslatef(-0.2, 0, 0); # 平移
 
    #glScalef(2, 1, 1);    # 缩放
 
 
    times+=1;
    if times > 100:
        times = 0;
 
    if times % 100 == 0:
        rotate += 0.3;
    
    # glRotatef(rotate, 0, 1, 0);
    glRotatef(rotate, 1, 1, 0);
 
    glColor3f(0, 0, 100);

    glutSolidCube(4)
 
    glPopMatrix();
    glutSwapBuffers();
 
def main():
    glutInit(sys.argv);
    glutInitDisplayMode(GLUT_DEPTH | GLUT_DOUBLE | GLUT_RGBA);
    glutInitWindowPosition(100,100);
    glutInitWindowSize(500, 500);
    glutCreateWindow("GLDemo");
    glutDisplayFunc(renderScene);
    glutIdleFunc(renderScene);
    glutMainLoop();



if __name__ == "__main__":
    main()