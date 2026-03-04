class DashboardModel:
    def __init__(self):
        self.gpa = 3.75
        self.assignments_due = 3
        self.next_event = "MIS Exam"
        self.notifications = 2

    def get_gpa(self):
        return self.gpa

    def get_assignments(self):
        return self.assignments_due

    def get_next_event(self):
        return self.next_event

    def get_notifications(self):
        return self.notifications

    def increment_notifications(self):
        self.notifications += 1