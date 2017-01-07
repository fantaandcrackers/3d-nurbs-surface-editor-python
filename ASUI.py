#ASUI

# http://noobtuts.com/python/opengl-introduction
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import main
import settings
import ASWindow


class knotWindow(QWidget):
   def __init__(self, parent = None):
      super(knotWindow, self).__init__(parent)
      layout = QVBoxLayout()

      self.uKnotEditing = []
      for i in range(len(settings.uKnots)):
         lineEdit = QLineEdit()
         lineEdit.setObjectName("u_" + str(i))
         lineEdit.setText(str(settings.uKnots[i]))
         self.uKnotEditing.append(lineEdit)


      self.vKnotEditing = []
      for i in range(len(settings.vKnots)):
         lineEdit = QLineEdit()
         lineEdit.setObjectName("u_" + str(i))
         lineEdit.setText(str(settings.vKnots[i]))
         self.vKnotEditing.append(lineEdit)

      uKnotBox = QHBoxLayout()
      for lineEdit in self.uKnotEditing:
         uKnotBox.addWidget(lineEdit)
      uButton = QPushButton('Update U Knots', self)
      uButton.clicked.connect(self.updateU)
      uKnotBox.addWidget(uButton)
      layout.addLayout(uKnotBox)

      vKnotBox = QHBoxLayout()
      for lineEdit in self.vKnotEditing:
         vKnotBox.addWidget(lineEdit)
      vButton = QPushButton('Update V Knots', self)
      vButton.clicked.connect(self.updateV)
      vKnotBox.addWidget(vButton)
      layout.addLayout(vKnotBox)

      self.setLayout(layout)

   def updateU(self):
      for i in range(len(self.uKnotEditing)):
         lineEdit = self.uKnotEditing[i]
         settings.uKnots[i] = float(lineEdit.text())
      main.draw()
     
   def updateV(self):
      for i in range(len(self.vKnotEditing)):
         lineEdit = self.vKnotEditing[i]
         settings.vKnots[i] = float(lineEdit.text())    
      main.draw()



class sliderdemo(QWidget):
   def __init__(self, parent = None):
      super(sliderdemo, self).__init__(parent)
      layout = QVBoxLayout()


      self.resetViewButton = QPushButton('Reset View', self)
      self.resetViewButton.clicked.connect(self.resetView)
      layout.addWidget(self.resetViewButton)


      self.uResLabel = QLabel("uRes = " + str(settings.uRes))
      self.uResLabel.setAlignment(Qt.AlignCenter)

      self.uResSlider = QSlider(Qt.Horizontal)
      self.uResSlider.setMinimum(3)
      self.uResSlider.setMaximum(30)
      self.uResSlider.setValue(3)
      self.uResSlider.setTickPosition(QSlider.TicksBelow)
      self.uResSlider.setTickInterval(1)
      self.uResSlider.valueChanged.connect(self.uResValueChange)

      uResBox = QHBoxLayout()
      uResBox.addStretch(1)
      uResBox.addWidget(self.uResLabel)
      uResBox.addWidget(self.uResSlider)
      layout.addLayout(uResBox)

      self.vResLabel = QLabel("vRes = " + str(settings.vRes))
      self.vResLabel.setAlignment(Qt.AlignCenter)

      self.vResSlider = QSlider(Qt.Horizontal)
      self.vResSlider.setMinimum(3)
      self.vResSlider.setMaximum(30)
      self.vResSlider.setValue(3)
      self.vResSlider.setTickPosition(QSlider.TicksBelow)
      self.vResSlider.setTickInterval(1)
      self.vResSlider.valueChanged.connect(self.vResValueChange)

      vResBox = QHBoxLayout()
      vResBox.addStretch(1)
      vResBox.addWidget(self.vResLabel)
      vResBox.addWidget(self.vResSlider)
      layout.addLayout(vResBox)




      self.colNumLabel = QLabel("Columns = " + str(len(settings.points[0])))
      self.colNumAddButton = QPushButton('+', self)
      self.colNumSubButton = QPushButton('-', self)
      self.colNumSubButton.clicked.connect(self.colNumSub)
      self.colNumAddButton.clicked.connect(self.colNumAdd)
      colNumBox = QHBoxLayout()
      colNumBox.addStretch(1)
      colNumBox.addWidget(self.colNumLabel)
      colNumBox.addWidget(self.colNumSubButton)
      colNumBox.addWidget(self.colNumAddButton)
      layout.addLayout(colNumBox)

      self.rowNumLabel = QLabel("Rows = " + str(len(settings.points)))
      self.rowNumAddButton = QPushButton('+', self)
      self.rowNumSubButton = QPushButton('-', self)
      self.rowNumSubButton.clicked.connect(self.rowNumSub)
      self.rowNumAddButton.clicked.connect(self.rowNumAdd)
      rowNumBox = QHBoxLayout()
      rowNumBox.addStretch(1)
      rowNumBox.addWidget(self.rowNumLabel)
      rowNumBox.addWidget(self.rowNumSubButton)
      rowNumBox.addWidget(self.rowNumAddButton)
      layout.addLayout(rowNumBox)


      self.uKLabel = QLabel("uK = " + str(settings.uK))
      self.uKAddButton = QPushButton('+', self)
      self.uKSubButton = QPushButton('-', self)
      self.uKSubButton.clicked.connect(self.uKSub)
      self.uKAddButton.clicked.connect(self.uKAdd)
      uKBox = QHBoxLayout()
      uKBox.addStretch(1)
      uKBox.addWidget(self.uKLabel)
      uKBox.addWidget(self.uKSubButton)
      uKBox.addWidget(self.uKAddButton)
      layout.addLayout(uKBox)

      self.vKLabel = QLabel("vK = " + str(settings.vK))
      self.vKAddButton = QPushButton('+', self)
      self.vKSubButton = QPushButton('-', self)
      self.vKSubButton.clicked.connect(self.vKSub)
      self.vKAddButton.clicked.connect(self.vKAdd)
      vKBox = QHBoxLayout()
      vKBox.addStretch(1)
      vKBox.addWidget(self.vKLabel)
      vKBox.addWidget(self.vKSubButton)
      vKBox.addWidget(self.vKAddButton)
      layout.addLayout(vKBox)



      self.lx = QLabel("Rotate X")
      self.lx.setAlignment(Qt.AlignCenter)

      self.cameraSliderX = QSlider(Qt.Horizontal)
      self.cameraSliderX.setMinimum(0)
      self.cameraSliderX.setMaximum(360)
      self.cameraSliderX.setValue(0)
      self.cameraSliderX.setTickPosition(QSlider.TicksBelow)
      self.cameraSliderX.setTickInterval(1)
      self.cameraSliderX.valueChanged.connect(self.cameraXValueChange)

      xBox = QHBoxLayout()
      xBox.addStretch(1)
      xBox.addWidget(self.lx)
      xBox.addWidget(self.cameraSliderX)
      layout.addLayout(xBox)


      self.ly = QLabel("Rotate Y")
      self.ly.setAlignment(Qt.AlignCenter)

      self.cameraSliderY = QSlider(Qt.Horizontal)
      self.cameraSliderY.setMinimum(0)
      self.cameraSliderY.setMaximum(360)
      self.cameraSliderY.setValue(0)
      self.cameraSliderY.setTickPosition(QSlider.TicksBelow)
      self.cameraSliderY.setTickInterval(1)
      self.cameraSliderY.valueChanged.connect(self.cameraYValueChange)

      xBox = QHBoxLayout()
      xBox.addStretch(1)
      xBox.addWidget(self.ly)
      xBox.addWidget(self.cameraSliderY)
      layout.addLayout(xBox)

      self.setLayout(layout)

      self.previousX = 0
      self.previousY = 0

   def resetView(self):
      ASWindow.refresh2d(settings.width, settings.height)
      main.draw()


   def uResValueChange(self):
      settings.uRes = self.uResSlider.value()
      self.uResLabel.setText("uRes = " + str(settings.uRes))
      main.draw()

   def vResValueChange(self):
      settings.vRes = self.vResSlider.value()
      self.vResLabel.setText("vRes = " + str(settings.vRes))
      main.draw()


   def uKAdd(self):
      settings.uK += 1
      self.uKLabel.setText("uK = " + str(settings.uK))
      main.draw()

   def uKSub(self):
      settings.uK -= 1
      self.uKLabel.setText("uK = " + str(settings.uK))
      main.draw()

   def vKAdd(self):
      settings.vK += 1
      self.vKLabel.setText("vK = " + str(settings.vK))
      main.draw()

   def vKSub(self):
      settings.vK -= 1
      self.vKLabel.setText("vK = " + str(settings.vK))
      main.draw()


   def rowNumAdd(self):
      settings.points.append([])
      for point in settings.points[-2]:
         newPoint = [point[0] + 100, point[1], point[2]]
         settings.points[-1].append(newPoint)
      settings.weights.append([2 for i in range(len(settings.points[0]))])
      self.rowNumLabel.setText("Rows = " + str(len(settings.points)))
      main.draw()

   def rowNumSub(self):
      del settings.points[-1]
      self.rowNumLabel.setText("Rows = " + str(len(settings.points)))
      main.draw()

   def colNumAdd(self):
      for row in settings.points:
         point = row[-1]
         row.append([point[0], point[1] + 100, point[2]])
      for row in settings.weights:
         row.append(2)
      self.colNumLabel.setText("Col = " + str(len(settings.points[0])))
      main.draw()

   def colNumSub(self):
      for row in settings.points:
         del row[-1]
      for row in settings.weights:
         del row[-1]
      self.colNumLabel.setText("Col = " + str(len(settings.points[0])))
      main.draw()



   def cameraXValueChange(self):
      degree = 1 if self.previousX < self.cameraSliderX.value() else -1
      self.previousX = self.cameraSliderX.value()
      ASWindow.changeCameraAngle(degree, [1, 0, 0])
      main.draw()

   def cameraYValueChange(self):
      degree = 1 if self.previousY < self.cameraSliderY.value() else -1
      self.previousY = self.cameraSliderY.value()
      ASWindow.changeCameraAngle(degree, [0, 1, 0])
      main.draw()

