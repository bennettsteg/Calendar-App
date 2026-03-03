from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *

class Dashboard(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("MIS Student Dashboard")

        central_widget = QWidget()
        layout = QVBoxLayout()

        label = QLabel("Welcome to Your Dashboard")
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        layout.addWidget(label)

        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        self.dashboard_toolbar()
    
    def dashboard_toolbar(self):
        toolbar = QToolBar("Dashboard Toolbar")
        toolbar.setMovable(False)
        self.addToolBar(Qt.ToolBarArea.LeftToolBarArea, toolbar)

        container = QWidget()
        c_layout = QVBoxLayout()
        c_layout.setSpacing(40)
        container.setLayout(c_layout)

        # Each button has a name, icon, and a callback function
        buttons = [
            ("Home", "images/homebutton.png", self.go_home),
            ("Teams", "images/teams.png", self.open_teams),
            ("Outlook", "images/outlook.png", self.open_outlook),
            ("Blackboard", "images/blackboard.png", self.open_blackboard),
            ("Calendar", "images/calendar.png", self.open_calendar)
        ]

        for name, image_path, func in buttons:
            btn = QToolButton()
            btn.setText(name)
            btn.setIcon(QIcon(image_path))
            btn.setIconSize(QSize(50, 50))
            btn.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)
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