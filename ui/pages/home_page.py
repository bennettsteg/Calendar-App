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


class HomePage(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setStyleSheet(""" QGroupBox { font-size: 16px; font-weight: bold; } """)
        
        self.setup_ui()

    def setup_ui(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        self.central_layout = QVBoxLayout()
        central_widget.setLayout(self.central_layout)

        self.student_overview = self.create_student_overview()
        self.central_layout.addWidget(self.student_overview)

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