from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sys
import pygame
import math
import time

# My Modules
import settings
import ASDrawing 
import ASUI
import ASMath
import ASWindow



# Set initial Screen
def refresh2d(width, height):
    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, width, 0.0, height, 0.0, 1.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

def setBackground(hexString):
  rgb = ASDrawing.getRgbTuple(hexString)
  glClearColor(rgb[0], rgb[1], rgb[2], 0.0)


# Interface
def addControlPoint(x,y):
    settings.points.append([x, y])

def getCurvePoint(t, drawLine):
    pointsCopy = settings.points
    resultArray = pointsCopy
    while len(resultArray) > 1:
        resultArray = calculateNextLevel(resultArray, t, drawLine)
    return resultArray[0]

knotWindow = None

def draw():
  glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

  points = settings.points
  weights = settings.weights

  uK = settings.uK
  vK = settings.vK

  global knotWindow

  if len(settings.uKnots) != uK + len(points[0]) + 1:
    settings.uKnots = ASMath.generateKnots(points[0], uK)
    if knotWindow != None:
      knotWindow.hide()
      knotWindow = None

  if len(settings.vKnots) != vK + len(points) + 1:
    settings.vKnots = ASMath.generateKnots([row[0] for row in points], vK)
    if knotWindow != None:
      knotWindow.hide()
      knotWindow = None

  if knotWindow == None:
    knotWindow = ASUI.knotWindow()
    knotWindow.show()





  ASDrawing.drawSurface(points, uK, vK, settings.uKnots, settings.vKnots, weights)

  for row in points:
    print row

  glutSwapBuffers()




# Point Array Manipulation Functions
def getClosestPointIndex(x, y, points):
  minDistance = 8
  closestPointIndex = None
  if len(points) >= 1:
    for i in range(0, len(points)):
      if ASMath.distancePoints(x, y, points[i][0], points[i][1]) < minDistance:
        closestPointIndex = i
        minDistance = ASMath.distancePoints(x, y, points[i][0], points[i][1])
  return closestPointIndex



# Mouse Functions
lastMouseDown = None
currentDraggedPoint = None
selectedPointIndex = None
controlPointSelected = False
vectorSelected = False

currentKey = 0

def on_keyboard(key, x, y):
  global currentKey
  currentKey = 1 if key == "1" else (2 if key == "2" else (3 if key == "3" else (4 if key == "4" else 0)))
  print currentKey

savedIndex = None

def on_click(button, state, x, y):
  global savedIndex
  if button == GLUT_LEFT_BUTTON and state == GLUT_DOWN:
    y = settings.height - y
    minDistance = 8
    savedIndex = None
    print(x, y)
    for j in range(len(settings.points)):
      row = settings.points[j]
      for i in range(len(row)):
        p1 = [row[i][0], row[i][1]]
        if ASMath.distancePoints2D(p1, [x, y]) < minDistance:
          savedIndex = [j, i]
          minDistance = ASMath.distancePoints2D(p1, [x, y])
          print(savedIndex)


previousY = 0

def on_drag(x, y):
  global savedIndex, previousY
  if savedIndex != None:
    i, j = savedIndex
    if currentKey > 0:
      offset = y - previousY
      adder = 1 if offset < 0 else -1
      previousY = y
      if currentKey == 1:
        settings.points[i][j][0] += adder
      elif currentKey == 2:
        settings.points[i][j][1] += adder
      elif currentKey == 3:
        settings.points[i][j][2] += adder
      elif currentKey == 4:
        settings.weights[i][j] += adder
      draw()


def main():
  settings.init()
  glutInit()
  ASWindow.setupWindow()
  glutMouseFunc(on_click)
  glutMotionFunc(on_drag)
  glutKeyboardFunc(on_keyboard)
  glutDisplayFunc(draw)
   # glutIdleFunc(draw)
  app = QApplication(sys.argv)
  ex = ASUI.sliderdemo()
  ex.show()
  glutMainLoop()

if __name__ == "__main__": main()
