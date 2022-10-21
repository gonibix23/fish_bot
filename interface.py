import sys
import core_functions as cf
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton

# Subclass QMainWindow to customize your application's main window
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Where is my water!")

        button = QPushButton("Press Me!")

        self.setFixedSize(QSize(800, 500))

        # Set the central widget of the Window.
        self.setCentralWidget(button)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()