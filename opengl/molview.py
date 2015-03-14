#
# Author: Bart Zijlstra (Based on script by Ivo Filot)
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

data_C = ("C",0.9,0.1,0.1,0.1) #Name,Size,R,G,B
data_H = ("H",0.5,0.8,0.8,0.8) #Name,Size,R,G,B

class Atom:
    """Defines an atom"""
    def __init__(self,Name,Size,R,G,B):
        self.name = Name
        self.size = Size
        self.r = R
        self.g = G
        self.b = B
        self.x = 0.0
        self.y = 0.0
        self.z = 0.0
    def SetLocation(self,X,Y,Z):
        self.x = float(X)
        self.y = float(Y)
        self.z = float(Z)
    def Translate(self,X,Y,Z):
        self.x += float(X)
        self.y += float(Y)
        self.z += float(Z)
    def Invert(self,X,Y,Z):
        self.x *= -1.0
        self.y *= -1.0
        self.z *= -1.0
    def DrawSelf(self,Tx=0.0,Ty=0.0,Tz=0.0,Rx=0.0,Ry=0.0,Rz=0.0):
        glPushMatrix()
        glRotatef(Rx, 0, 1.0, 0.0)
        glRotatef(Ry, 1.0, 0, 0.0)
        glColor3f(self.r,self.g,self.b)
        glTranslatef(self.x+Tx, self.y+Ty, self.z+Tz)
        glutSolidSphere(self.size,40,40)
        glPopMatrix()


class Alkane:
    """Defines an alkane"""
    def __init__(self,Size):
        self.size = Size
        self.atoms = []
        self.BuildAlkane(Size)
    def BuildAlkane(self,Size=None):
        self.atoms = []
        if Size==None:
            Size = self.size

        # draw start hydrogen
        atom = Atom(*data_H)
        atom.SetLocation( -1.0, 1.0, 1.0)
        self.atoms.append(atom)
        sign = -1.0
        for i in range(0,Size): # make CH2 group
            origin = (i, (1.0+sign)/2, -i)
            # add carbon
            atom = Atom(*data_C)
            atom.SetLocation(*origin)
            self.atoms.append(atom)

            # add the two hydrogens
            atom = Atom(*data_H)
            position = (i+1.0, (1.0+sign)/2+sign, -i+1.0)
            atom.SetLocation(*position)
            self.atoms.append(atom)

            atom = Atom(*data_H)
            position = (i-1.0, (1.0+sign)/2+sign, -i-1.0)
            atom.SetLocation(*position)
            self.atoms.append(atom)

            # switch if hydrogens are above or below carbon
            sign *= -1.0

        # draw end hydrogen
        atom = Atom(*data_H)
        atom.SetLocation((Size-1)+1.0,  (1.0+sign)/2,  -(Size-1)-1.0)
        self.atoms.append(atom)
    def FindCenter(self):
        x = 0.0
        y = 0.0
        z = 0.0
        for atom in self.atoms:
            x += atom.x
            y += atom.y
            z += atom.z
        x /= len(self.atoms)
        y /= len(self.atoms)
        z /= len(self.atoms)
        return (x,y,z)
    def DrawSelf(self,Tx=0.0,Ty=0.0,Tz=0.0,Rx=0.0,Ry=0.0,Rz=0.0):
        for atom in self.atoms:
            atom.DrawSelf(Tx,Ty,Tz,Rx,Ry,Rz)



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
    global rotate_y, rotate_x, scene

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT); # Clear The Screen And The Depth Buffer
    glLoadIdentity();                   # Reset The View
    glTranslatef(0.0,0.0,-12.0);        # Move Left And Into The Screen

    center = scene.FindCenter()
    scene.DrawSelf(-center[0],-center[1],-center[2],rotate_x,rotate_y,0.0)

    # Stuff to help see how the system is oriented
    # glPushMatrix()
    # glLoadIdentity();
    # glRotatef(rotate_x, 0, 1.0, 0.0)
    # glRotatef(rotate_y, 1.0, 0, 0.0)
    # glColor3f(1.0, 0.0, 0.0);
    # glTranslatef(0.0, 0.0, -15.0)
    # glutSolidSphere(0.5,40,40)
    # glPopMatrix()

    # glPushMatrix()
    # glRotatef(rotate_x, 0, 1.0, 0.0)
    # glRotatef(rotate_y, 1.0, 0, 0.0)
    # glColor3f(1.0, 0.0, 0.0);
    # glTranslatef(1.0, 0.0, 0.0)
    # glutSolidSphere(0.1,40,40)
    # glPopMatrix()

    # glPushMatrix()
    # glRotatef(rotate_x, 0, 1.0, 0.0)
    # glRotatef(rotate_y, 1.0, 0, 0.0)
    # glColor3f(0.0, 1.0, 0.0);
    # glTranslatef(0.0, 1.0, 0.0)
    # glutSolidSphere(0.2,40,40)
    # glPopMatrix()

    # glPushMatrix()
    # glRotatef(rotate_x, 0, 1.0, 0.0)
    # glRotatef(rotate_y, 1.0, 0, 0.0)
    # glColor3f(0.0, 0.0, 1.0);
    # glTranslatef(0.0, 0.0, 1.0)
    # glutSolidSphere(0.3,40,40)
    # glPopMatrix()

    #  since this is double buffered, swap the buffers to display what just got drawn. 
    glutSwapBuffers()

# Function to create a carbon.
def DrawCarbon(Xin,Yin,Zin,Rot_x=0,Rot_y=0):
    glPushMatrix()
    glRotatef(Rot_x, 0, 1.0, 0.0)
    glRotatef(Rot_y, 1.0, 0, 0.0)
    glColor3f(0.1,0.1,0.1); # Set The Color To Grey
    glTranslatef(Xin, Yin, Zin)
    glutSolidSphere(0.9,40,40)
    glPopMatrix()

# Function to create a hydrogen.
def DrawHydrogen(Xin,Yin,Zin,Rot_x=0,Rot_y=0):
    glPushMatrix()
    glRotatef(Rot_x, 0, 1.0, 0.0)
    glRotatef(Rot_y, 1.0, 0, 0.0)
    glColor3f(0.9,0.9,0.9);
    glTranslatef(Xin, Yin, Zin)
    glutSolidSphere(0.5,40,40)
    glPopMatrix()

# The function called whenever a key is pressed. Note the use of Python tuples to pass in: (key, x, y)  
def keyPressed(*args):
    global rotate_x, rotate_y, scene
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
    if args[0] == 'q':
        scene.size -= 1
        scene.BuildAlkane()
    if args[0] == 'e':
        scene.size += 1
        scene.BuildAlkane()

def main():
    global window
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
    glutInitWindowSize(640, 480)
    glutInitWindowPosition(0, 0)
    window = glutCreateWindow("IMC Rules!")
    global scene
    scene = Alkane(1)
    glutDisplayFunc(DrawGLScene)
    glutIdleFunc(DrawGLScene)
    glutReshapeFunc(ReSizeGLScene)
    glutKeyboardFunc(keyPressed)
    InitGL(640, 480)
    glutMainLoop()

print "Hit ESC key to quit."
main()