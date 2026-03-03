from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *

class Dashboard(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("MIS Student Dashboard")

        central_widget = QWidget()
        layout = QVBoxLayout()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        self.section_box = SectionBox()
        layout.addWidget(self.section_box)

        self.dashboard_toolbar()

    
    def dashboard_toolbar(self):
        toolbar = QToolBar("Dashboard Toolbar")
        toolbar.setMovable(False)
        self.addToolBar(Qt.ToolBarArea.LeftToolBarArea, toolbar)

        container = QWidget()
        c_layout = QVBoxLayout()
        c_layout.setSpacing(30)
        container.setLayout(c_layout)

        user_icon = QToolButton()
        user_icon.setIcon(QIcon("images/usericon"))
        user_icon.setText("Bennett Steg")
        user_icon.setIconSize(QSize(150,150))
        user_icon.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)
        c_layout.addWidget(user_icon)

        # Each button has a name, icon, and a callback function
        buttons = [
            ("Home","images/homebutton.png", self.go_home),
            ("Teams","images/teams.png", self.open_teams),
            ("Outlook","images/outlook.png", self.open_outlook),
            ("Blackboard","images/blackboard.png", self.open_blackboard),
            ("Calendar","images/calendar.png", self.open_calendar)
        ]

        for name, image_path, func in buttons:
            btn = QToolButton()
            btn.setIcon(QIcon(image_path))
            btn.setIconSize(QSize(50, 50))
            btn.setText(name)
            btn.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextBesideIcon)
            btn.setAutoRaise(True)
            btn.clicked.connect(func)
            c_layout.addWidget(btn)

        c_layout.addStretch()
        toolbar.addWidget(container)

        # Example functions
    def go_home(self):
        print("Home button pressed")

    def open_teams(self):
        print("Teams button pressed")

    def open_outlook(self):
        print("Outlook button pressed")

    def open_blackboard(self):
        print("Blackboard button pressed")

    def open_calendar(self):
        print("Calendar button pressed")


class SectionBox(QGroupBox):
    def __init__(self):
        super().__init__("Student Overview")

        self.layout = QGridLayout()
        self.setLayout(self.layout)

        self.create_child_boxes()

    def create_child_boxes(self):
        for i in range(4):
            child_group = QGroupBox(f"Section {i+1}")
            child_layout = QVBoxLayout()
            child_group.setLayout(child_layout)

            child_layout.addWidget(QLabel(f"Label in Section {i+1}"))
            child_layout.addWidget(QPushButton("Button"))

            row = i // 2
            col = i % 2
            self.layout.addWidget(child_group, row, col)



