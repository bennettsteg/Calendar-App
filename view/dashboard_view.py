from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
import os

class SectionBox(QGroupBox):
    def __init__(self, title):
        super().__init__(title)
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

    def add_widget(self, widget):
        self.layout.addWidget(widget)


class DashboardView(QMainWindow):

    # Creates Signals 
    home_clicked = Signal()
    teams_clicked = Signal()
    outlook_clicked = Signal()
    blackboard_clicked = Signal()
    calendar_clicked = Signal()

    def __init__(self):
        super().__init__()

        self.setStyleSheet(""" QGroupBox { font-size: 16px; font-weight: bold; } """)

        self.setWindowTitle("MIS Student Dashboard")
        self.showMaximized()

        self.setup_ui()

    def setup_ui(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        self.central_layout = QVBoxLayout()
        central_widget.setLayout(self.central_layout)

        self.student_overview = self.create_student_overview()
        self.central_layout.addWidget(self.student_overview)

        self.addToolBar(Qt.ToolBarArea.LeftToolBarArea,self.create_toolbar())

    def create_student_overview(self):
        group = QGroupBox("Student Overview")
        layout = QGridLayout()
        group.setLayout(layout)

        self.gpa_section = SectionBox("GPA")
        self.gpa_label = QLabel()
        self.gpa_section.add_widget(self.gpa_label)

        self.assignment_section = SectionBox("Assignments")
        self.assignment_label = QLabel()
        self.assignment_section.add_widget(self.assignment_label)

        self.calendar_section = SectionBox("Calendar")
        self.calendar = QCalendarWidget()
        self.calendar.setGridVisible(True)
        self.calendar_section.add_widget(self.calendar)

        self.notification_section = SectionBox("Notifications")
        self.notification_label = QLabel()
        self.notification_section.add_widget(self.notification_label)

        for widget in [self.gpa_section,self.assignment_section,self.calendar_section,self.notification_section]:
            widget.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        layout.addWidget(self.gpa_section, 0, 0)
        layout.addWidget(self.assignment_section, 0, 1)
        layout.addWidget(self.calendar_section, 1, 0)
        layout.addWidget(self.notification_section, 1, 1)

        return group

    def create_toolbar(self):
        toolbar = QToolBar("Dashboard Toolbar")
        toolbar.setMovable(False)

        container = QWidget()
        layout = QVBoxLayout()
        container.setLayout(layout)
        layout.setSpacing(40)

        # User icon created beforehand due to unique sizing
        user_icon = QToolButton()
        user_icon.setIcon(QIcon("resources/images/usericon.png"))
        user_icon.setText("Bennett Steg")
        user_icon.setIconSize(QSize(150, 150))
        user_icon.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)
        layout.addWidget(user_icon)

        buttons = [
            ("Home","resources/images/homebutton.png", self.home_clicked),
            ("Teams", "resources/images/teams.png", self.teams_clicked),
            ("Outlook", "resources/images/outlook.png", self.outlook_clicked),
            ("Blackboard", "resources/images/blackboard.png", self.blackboard_clicked),
            ("Calendar", "resources/images/calendar.png", self.calendar_clicked)
        ]

        for name, png_path, signal in buttons:
            btn = QToolButton()
            btn.setText(name)
            btn.setIcon(QIcon(png_path))
            btn.setIconSize(QSize(40,40))
            btn.setAutoRaise(True)
            btn.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextBesideIcon)
            # Emits signal for controller
            btn.clicked.connect(signal.emit)
            layout.addWidget(btn)

        layout.addStretch()
        toolbar.addWidget(container)

        return toolbar    


    # Methods Controller will call
    def update_gpa(self, value):
        self.gpa_label.setText(f"Current GPA: {value}")

    def update_assignments(self, value):
        self.assignment_label.setText(f"{value} assignments due")

    def update_calendar(self, event):
        pass

    def update_notifications(self, value):
        self.notification_label.setText(f"{value} unread notifications")