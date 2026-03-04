# controller.py

class DashboardController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

        self.connect_signals()
        self.refresh_view()

    def connect_signals(self):
        self.view.home_clicked.connect(self.handle_home)
        self.view.teams_clicked.connect(self.handle_teams)
        self.view.outlook_clicked.connect(self.handle_outlook)
        self.view.blackboard_clicked.connect(self.handle_blackboard)
        self.view.calendar_clicked.connect(self.handle_calendar)

    def refresh_view(self):
        self.view.update_gpa(self.model.get_gpa())
        self.view.update_assignments(self.model.get_assignments())
        self.view.update_calendar(self.model.get_next_event())
        self.view.update_notifications(self.model.get_notifications())

    # Handlers
    def handle_home(self):
        print("Home pressed")

    def handle_teams(self):
        print("Teams pressed")

    def handle_outlook(self):
        print("Outlook pressed")

    def handle_blackboard(self):
        print("Blackboard pressed")

    def handle_calendar(self):
        print("Calendar pressed")