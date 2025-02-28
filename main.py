import io
import sys
import random

from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtGui import QPainter, QColor
from PyQt6.QtWidgets import QWidget, QApplication

template = """<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>MainWindow</class>
 <widget class="QMainWindow" name="MainWindow">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>800</width>
    <height>600</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>MainWindow</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <widget class="QPushButton" name="pb_create_circle">
    <property name="geometry">
     <rect>
      <x>300</x>
      <y>200</y>
      <width>181</width>
      <height>28</height>
     </rect>
    </property>
    <property name="text">
     <string>Создать окружности</string>
    </property>
   </widget>
  </widget>
  <widget class="QStatusBar" name="statusbar"/>
 </widget>
 <resources/>
 <connections/>
</ui>
"""


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        f = io.StringIO(template)
        uic.loadUi(f, self)

        self.flag_draw = False
        self.window_width, self.window_height = 750, 500

        self.circle_color = QColor(255, 255 ,0)
        self.circle_radius_range = [10, 100]
        circle_delta_coords = 50
        self.circle_x_range = [circle_delta_coords, self.window_width - circle_delta_coords]
        self.circle_y_range = [circle_delta_coords, self.window_height - circle_delta_coords]
        self.circle_count_range = [10, 30]

        self.initUI()

    def initUI(self):
        self.setGeometry(100, 100, self.window_width, self.window_height)
        self.setFixedSize(self.window_width, self.window_height)
        self.setWindowTitle('Git и желтые окружности')
        self.pb_create_circle.clicked.connect(self.create_circles)

    def create_circles(self):
        self.flag_draw = True
        self.update()

    def paintEvent(self, event):
        if self.flag_draw:
            qp = QPainter()
            qp.begin(self)
            self.draw_flag(qp)
            qp.end()

    def draw_flag(self, qp):
        for _ in range(random.randint(*self.circle_count_range)):
            qp.setBrush(QColor(255, 255, 0))
            circle_radius = random.randint(*self.circle_radius_range)
            qp.drawEllipse(random.randint(*self.circle_x_range), random.randint(*self.circle_y_range), circle_radius, circle_radius)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Window()
    ex.show()
    sys.exit(app.exec())