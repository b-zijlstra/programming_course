#
# pyopengl.py
#
# Basic example Python OpenGL implementation
# Draws a red triangle and a blue rectangle
#
# Author: Ivo Filot
#
# Reference: This tut is based on Lesson 2 from the NeHe tutorials
#

# start by importing some libraries
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import sys

ESCAPE = '\033' # ESC button
window = 0

# A general OpenGL initialization function.  Sets all of the initial parameters. 
def InitGL(Width, Height):				# We call this right after our OpenGL window is created.
    glClearColor(1.0, 1.0, 1.0, 0.0)	# This Will Clear The Background Color To White
    glClearDepth(1.0)					# Enables Clearing Of The Depth Buffer
    glDepthFunc(GL_LESS)				# The Type Of Depth Test To Do
    glEnable(GL_DEPTH_TEST)				# Enables Depth Testing
    glShadeModel(GL_SMOOTH)				# Enables Smooth Color Shading
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()					# Reset The Projection Matrix
										# Calculate The Aspect Ratio Of The Window
    gluPerspective(45.0, float(Width)/float(Height), 0.1, 100.0)

    glMatrixMode(GL_MODELVIEW)

# The function called when our window is resized (which shouldn't happen if you enable fullscreen, below)
def ReSizeGLScene(Width, Height):
    if Height == 0:						# Prevent A Divide By Zero If The Window Is Too Small 
	    Height = 1

    glViewport(0, 0, Width, Height)		# Reset The Current Viewport And Perspective Transformation
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45.0, float(Width)/float(Height), 0.1, 100.0)
    glMatrixMode(GL_MODELVIEW)

# The main drawing function. 
def DrawGLScene():
	# Clear The Screen And The Depth Buffer
	glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
	glLoadIdentity()			# Reset The View 

	# Move Left 1.5 units and into the screen 6.0 units.
	glTranslatef(-1.5, 0.0, -6.0)

	# Draw a triangle
	glBegin(GL_POLYGON)                 # Start drawing a polygon
	glColor3f(1.0, 0.0, 0.0)            # Red
	glVertex3f(0.0, 1.0, 0.0)           # Top
	glVertex3f(1.0, -1.0, 0.0)          # Bottom Right
	glVertex3f(-1.0, -1.0, 0.0)         # Bottom Left
	glEnd()                             # We are done with the polygon

	# Move Right 3.0 units.
	glTranslatef(3.0, 0.0, 0.0)

	# Draw a square (quadrilateral)
	glBegin(GL_QUADS)                   # Start drawing a 4 sided polygon
	glColor3f(0.0, 0.0, 1.0)            # Blue
	glVertex3f(-1.0, 1.0, 0.0)          # Top Left
	glVertex3f(1.0, 1.0, 0.0)           # Top Right
	glVertex3f(1.0, -1.0, 0.0)          # Bottom Right
	glVertex3f(-1.0, -1.0, 0.0)         # Bottom Left
	glEnd()                             # We are done with the polygon

	#  since this is double buffered, swap the buffers to display what just got drawn. 
	glutSwapBuffers()

# exit the program when ESC is pressed
def keyPressed(*args):
    if args[0] == ESCAPE:
	    sys.exit()

def main():
	global window
	glutInit(sys.argv)
	glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
	glutInitWindowSize(640, 480)
	glutInitWindowPosition(0, 0)
	window = glutCreateWindow("IMC rules!")
	glutDisplayFunc(DrawGLScene)
	glutIdleFunc(DrawGLScene)
	glutReshapeFunc(ReSizeGLScene)
	glutKeyboardFunc(keyPressed)
	InitGL(640, 480)
	glutMainLoop()

# Print message to console, and kick off the main to get it rolling.
print "Hit ESC key to quit."
main()