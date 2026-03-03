import sys
from PyQt6.QtWidgets import QApplication
from ui.dashboard import Dashboard

def main():
    app = QApplication(sys.argv)
    window = Dashboard()
    window.showMaximized()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()