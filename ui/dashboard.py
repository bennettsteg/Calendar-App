from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from ui.pages.home_page import HomePage
from ui.pages.calendar_page import CalendarPage
from ui.pages.teams_page import TeamsPage
from ui.pages.outlook_page import OutlookPage
from ui.pages.blackboard_page import BlackboardPage


class Dashboard(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("MIS Student Dashboard")
        self.showMaximized()

        self.stacked_widget = QStackedWidget()

        self.home_page_frame = HomePage()
        self.teams_page_frame = TeamsPage()
        self.outlook_page_frame = OutlookPage()
        self.blackboard_page_frame = BlackboardPage()
        self.calendar_page_frame = CalendarPage()

        self.stacked_widget.addWidget(self.home_page_frame)
        self.stacked_widget.addWidget(self.teams_page_frame)
        self.stacked_widget.addWidget(self.outlook_page_frame)
        self.stacked_widget.addWidget(self.blackboard_page_frame)
        self.stacked_widget.addWidget(self.calendar_page_frame)

        main_layout = QHBoxLayout()
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)
        main_layout.addWidget(self.create_toolbar())
        main_layout.addWidget(self.stacked_widget)
        self.setLayout(main_layout)

    def switch_frame(self, index):
        self.stacked_widget.setCurrentIndex(index)

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
            ("Home","resources/images/homebutton.png", lambda: self.switch_frame(0)),
            ("Teams", "resources/images/teams.png", lambda: self.switch_frame(1)),
            ("Outlook", "resources/images/outlook.png", lambda: self.switch_frame(2)),
            ("Blackboard", "resources/images/blackboard.png", lambda: self.switch_frame(3)),
            ("Calendar", "resources/images/calendar.png", lambda: self.switch_frame(4))
        ]

        for name, png_path, command in buttons:
            btn = QToolButton()
            btn.setText(name)
            btn.setIcon(QIcon(png_path))
            btn.setIconSize(QSize(40,40))
            btn.setAutoRaise(True)
            btn.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextBesideIcon)
            # Emits signal for controller
            btn.clicked.connect(command)
            layout.addWidget(btn)

        layout.addStretch()
        toolbar.addWidget(container)

        return toolbar
