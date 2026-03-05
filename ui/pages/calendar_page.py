from PySide6.QtWidgets import *
from PySide6.QtCore import Qt


class CalendarPage(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setup_ui()

    def setup_ui(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Create layout
        layout = QVBoxLayout()
        central_widget.setLayout(layout)

        # Title
        self.title = QLabel("Calendar")
        self.title.setStyleSheet("font-size: 24px; font-weight: bold;")

        # Full calendar widget
        self.calendar = QCalendarWidget()
        self.calendar.setGridVisible(True)

        # Create text box
        self.notes_box = QTextEdit()

        # Add widgets to layout
        layout.addWidget(self.title)
        layout.addWidget(self.calendar)
        layout.addWidget(self.notes_box)
