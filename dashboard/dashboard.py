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


class Student_Dashboard(QMainWindow):
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
            btn.clicked.connect(signal)
            layout.addWidget(btn)

        layout.addStretch()
        toolbar.addWidget(container)

        return toolbar 

    def home_clicked(self):
        pass
    def teams_clicked(self):
        pass
    def outlook_clicked(self):
        pass
    def blackboard_clicked(self):
        pass
    def calendar_clicked(self):
        pass

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
        self.calendar = DashboardCalendar()
        self.calendar_section.add_widget(self.calendar)

        self.notification_section = SectionBox("Notifications")
        self.notification_label = QLabel()
        self.notification_section.add_widget(self.notification_label)

        # Ensure all widgets are evenly sized 
        for widget in [self.gpa_section,self.assignment_section,self.calendar_section,self.notification_section]:
            widget.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        layout.addWidget(self.gpa_section, 0, 0)
        layout.addWidget(self.assignment_section, 0, 1)
        layout.addWidget(self.calendar_section, 1, 0)
        layout.addWidget(self.notification_section, 1, 1)

        return group

class DashboardCalendar(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout(self)

        self.calendar = QCalendarWidget()
        self.calendar.setGridVisible(True)
        #self.calendar.clicked.connect(self.date_clicked.emit)

        layout.addWidget(self.calendar)

    def show_message(self, date, text):
        QMessageBox.information(self, f"Note for {date.toString('yyyy-MM-dd')}", text)