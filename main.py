# main.py

import sys
from PySide6.QtWidgets import QApplication
from dashboard.dashboard import Student_Dashboard

def main():
    app = QApplication(sys.argv)

    main_window = Student_Dashboard()
    main_window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()