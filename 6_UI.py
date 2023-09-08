"""
Задание 6 [Ui]
Создайте диалоговое окно
В этом окне два кастомных виджета
Эти два виджета должны быть экземплярами одного и того же класса. 
Они должны быть подсвечены так, чтобы они выделялись на фоне диалогового окна.
Задача - при клике мышью на одном виджете другой виджет должен поменять цвет на рандомный.
"""
import random
from PySide2 import QtWidgets, QtGui, QtCore

exempl = []

# Custom widget class
class CustomWidget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(CustomWidget, self).__init__(parent)
        self.setAutoFillBackground(True)
        self.setMouseTracking(True)
        self.setMinimumSize(100, 100)
        self.randomize_color()

    def randomize_color(self):
        # Random color generation
        color = QtGui.QColor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        palette = self.palette()
        palette.setColor(QtGui.QPalette.Background, color)
        self.setPalette(palette)

    def enterEvent(self, event):
        # Highlight on mouse hover
        self.setStyleSheet("border: 2px solid orange;")

    def leaveEvent(self, event):
        # Remove highlighting when the mouse cursor leaves the widget
        self.setStyleSheet("")

    def mousePressEvent(self, event):
        # When you click on a widget, the color of the second widget changes
        for i in exempl:
            if i != self:
                i.randomize_color()
     
# Create a dialog box
class Dialog(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(Dialog, self).__init__(parent)
        self.setWindowTitle("Custom Widgets Demo")
        self.setMinimumSize(400, 200)
        layout = QtWidgets.QVBoxLayout()

        # Generating custom widget instances
        num_widgets = 3
        for i in range(num_widgets):
            widget = CustomWidget(self)
            exempl.append(widget)
            layout.addWidget(widget)

        self.setLayout(layout)


dialog = Dialog()
dialog.show()
