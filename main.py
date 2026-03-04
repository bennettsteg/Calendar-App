# main.py

import sys
from PySide6.QtWidgets import QApplication
from view.dashboard_view import DashboardView
from model.dashboard_model import DashboardModel
from controller.dashboard_controller import DashboardController

def main():
    app = QApplication(sys.argv)

    model = DashboardModel()
    view = DashboardView()
    controller = DashboardController(model, view)

    view.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()