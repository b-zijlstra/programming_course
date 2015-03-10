#
# Author: Ivo Filot
#
# 3D perspective
#

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import sys

ESCAPE = '\033'

# Number of the glut window.
window = 0
rtri = 0.0
rquad = 0.0
rotate_x = 0
rotate_y = 0

# A general OpenGL initialization function.  Sets all of the initial parameters. 
def InitGL(Width, Height):              # We call this right after our OpenGL window is created.
    glClearColor(1.0, 1.0, 1.0, 0.0)    # This Will Clear The Background Color To Black
    glClearDepth(1.0)                   # Enables Clearing Of The Depth Buffer
    glDepthFunc(GL_LESS)                # The Type Of Depth Test To Do
    glEnable(GL_DEPTH_TEST)             # Enables Depth Testing
    glShadeModel(GL_SMOOTH)             # Enables Smooth Color Shading
    
    glMatrixMode(GL_PROJECTION)
    glPolygonMode( GL_FRONT_AND_BACK, GL_LINE );
    glLoadIdentity()                    # Reset The Projection Matrix
                                        # Calculate The Aspect Ratio Of The Window
    gluPerspective(45.0, float(Width)/float(Height), 0.1, 100.0)

    glMatrixMode(GL_MODELVIEW)

# The function called when our window is resized (which shouldn't happen if you enable fullscreen, below)
def ReSizeGLScene(Width, Height):
    if Height == 0:                     # Prevent A Divide By Zero If The Window Is Too Small 
        Height = 1

    glViewport(0, 0, Width, Height)     # Reset The Current Viewport And Perspective Transformation
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45.0, float(Width)/float(Height), 0.1, 100.0)
    glMatrixMode(GL_MODELVIEW)

# The main drawing function. 
def DrawGLScene():
    global rotate_y, rotate_x

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT); # Clear The Screen And The Depth Buffer
    glLoadIdentity();                   # Reset The View
    glTranslatef(0.0,0.0,-12.0);        # Move Left And Into The Screen

    # draw carbon
    glColor3f(0.1,0.1,0.1);             # Set The Color To Grey
    glutSolidSphere(0.9,40,40)

    # draw the four hydrogen at the vertices of a tetrahedron
    glPushMatrix()
    glRotatef(rotate_x, 0, 1.0, 0.0)
    glRotatef(rotate_y, 1.0, 0, 0.0)
    glColor3f(0.9,0.9,0.9);
    glTranslatef(-1.0, -1.0, -1.0)
    glutSolidSphere(0.5,40,40)
    glPopMatrix()

    glPushMatrix()
    glRotatef(rotate_x, 0, 1.0, 0.0)
    glRotatef(rotate_y, 1.0, 0, 0.0)
    glColor3f(0.9,0.9,0.9);
    glTranslatef(1.0, 1.0, -1.0)
    glutSolidSphere(0.5,40,40)
    glPopMatrix()

    glPushMatrix()
    glRotatef(rotate_x, 0, 1.0, 0.0)
    glRotatef(rotate_y, 1.0, 0, 0.0)
    glColor3f(0.9,0.9,0.9);
    glTranslatef(1.0, -1.0, 1.0)
    glutSolidSphere(0.5,40,40)
    glPopMatrix()

    glPushMatrix()
    glRotatef(rotate_x, 0, 1.0, 0.0)
    glRotatef(rotate_y, 1.0, 0, 0.0)
    glColor3f(0.9,0.9,0.9);
    glTranslatef(-1.0, 1.0, 1.0)
    glutSolidSphere(0.5,40,40)
    glPopMatrix()

    glPushMatrix()
    glLoadIdentity();
    glRotatef(rotate_x, 0, 1.0, 0.0)
    glRotatef(rotate_y, 1.0, 0, 0.0)
    glColor3f(1.0, 0.0, 0.0);
    glTranslatef(0.0, 0.0, -15.0)
    glutSolidSphere(0.5,40,40)
    glPopMatrix()

    #  since this is double buffered, swap the buffers to display what just got drawn. 
    glutSwapBuffers()

# The function called whenever a key is pressed. Note the use of Python tuples to pass in: (key, x, y)  
def keyPressed(*args):
    global rotate_x, rotate_y
    # If escape is pressed, kill everything.
    if args[0] == ESCAPE:
        sys.exit()
    if args[0] == 'a':
        rotate_x -= 2
    if args[0] == 'd':
        rotate_x += 2
    if args[0] == 's':
        rotate_y -= 2
    if args[0] == 'w':
        rotate_y += 2

def main():
    global window
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
    glutInitWindowSize(640, 480)
    glutInitWindowPosition(0, 0)
    window = glutCreateWindow("IMC Rules!")
    glutDisplayFunc(DrawGLScene)
    glutIdleFunc(DrawGLScene)
    glutReshapeFunc(ReSizeGLScene)
    glutKeyboardFunc(keyPressed)
    InitGL(640, 480)
    glutMainLoop()

print "Hit ESC key to quit."
main()