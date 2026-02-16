import sys
from win11toast import toast
from PyQt6.QtWidgets import QApplication, QLabel, QWidget

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        # setGeometry(x_pos, y_pos, width, height)
        self.setGeometry(100, 100, 400, 300) 
        self.setWindowTitle("PyQt Geometry Example")
        self.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())