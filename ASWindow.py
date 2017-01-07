#ASWindow.py
from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
import settings
import ASDrawing 
import time
import math

def setupWindow():
	glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_ALPHA | GLUT_DEPTH)
	glutInitWindowSize(settings.width, settings.height)
	glutInitWindowPosition(0, 0)
	settings.window = glutCreateWindow("Arthur Shir")
	refresh2d(settings.width, settings.height)
	setBackground('29221F')

def setBackground(hexString):
	rgb = ASDrawing.getRgbTuple(hexString)
	glClearColor(rgb[0], rgb[1], rgb[2], 0.0)


def refresh2d(width, height):
	glViewport(0, 0, width, height)
	glMatrixMode(GL_PROJECTION)
	glLoadIdentity()
	glOrtho(0.0, width, 0.0, height, 0.0, 3000.0)
	# gluLookAt(0, 0, 1000, 0, 0, 0, 0, 1, 0)
	glMatrixMode(GL_MODELVIEW)
	glLoadIdentity()

	glTranslatef(0.0, 0.0, -1000)

def changeCameraAngle(degrees, axis):
	glTranslatef(settings.width/2, settings.height/2, 0);
	glRotatef(float(degrees*15), axis[0], axis[1], axis[2]);
	glTranslatef(-settings.width/2, -settings.height/2, 0);
