# ASDrawing
from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *

import ASMath
import settings

  
# Colors
def getRgbTuple(hexString):
  h = hexString.lstrip('#')
  return tuple(float(int(h[i:i+2], 16))/255 for i in (0, 2 ,4))

def setHex(hexString):
  rgb = getRgbTuple(hexString)
  glColor3f(rgb[0], rgb[1], rgb[2])


# Low Level Drawing Functions
def drawPoint(point):
    glColor3f(1,1,1)
    glPointSize(3)
    glBegin(GL_POINTS)
    glVertex3f(point[0], point[1], point[2])
    glEnd();

def drawPointHighlighted(point):
    setHex('FC354C')
    glPointSize(10);
    glBegin(GL_POINTS);
    glVertex3f(point[0], point[1], point[2])
    glEnd();

def drawLine(point0, point1):
    glColor3f(1,1,1)
    glLineWidth(1)
    glBegin(GL_LINES)
    glVertex3f(point0[0], point0[1], point0[2])
    glVertex3f(point1[0], point1[1], point1[2])
    glEnd()


# Higher Level Drawing Functions
def drawControlPoints(points, highlighted):
    n = len(points) # Number of rows
    m = len(points[0]) # Number of columns
    for i in range(n):
      for j in range(m):
        if highlighted:
          drawPointHighlighted(points[i][j])
        else:
          drawPoint(points[i][j])

def drawControlPolygon(points):
    n = len(points) # Number of rows
    m = len(points[0]) # Number of columns
    for i in range(n-1):
      for j in range(m):
        drawLine(points[i][j], points[i+1][j])
    for i in range(n):
      for j in range(m-1):
        drawLine(points[i][j], points[i][j+1])   

def drawSurface(points, uK, vK, uKnots, vKnots, weights):
    drawControlPolygon(points)
    drawControlPoints(points, True)

    nurbsPoints = ASMath.nurbsSurface(uK, vK, uKnots, vKnots, points, weights)
    drawControlPolygon(nurbsPoints)
    drawControlPoints(nurbsPoints, False)



