import sys
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Side Toolbar Example")
        self.setGeometry(100, 100, 400, 300)

        # Set the central widget (the main area of your application)
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        self._create_toolbars()

    def _create_toolbars(self):
        # Create the left-side toolbar
        left_toolbar = QToolBar("Left Toolbar")
        # Add the toolbar to the left toolbar area
        self.addToolBar(Qt.ToolBarArea.LeftToolBarArea, left_toolbar)
        
        # Make the toolbar immovable if desired (optional)
        # left_toolbar.setMovable(False) 

        # Add actions (buttons) to the toolbar
        # You'll need an icon file (e.g., 'icon.png') in your directory for this to work
        # If you don't have one, you can just use text: QAction("Action 1", self)
        action1 = QAction(QIcon('icon.png'), "Action 1", self)
        action1.triggered.connect(self.on_action1_triggered)
        left_toolbar.addAction(action1)

        action2 = QAction(QIcon('icon.png'), "Action 2", self)
        action2.triggered.connect(self.on_action2_triggered)
        left_toolbar.addAction(action2)
        
        # Add a separator
        left_toolbar.addSeparator()

        action3 = QAction(QIcon('icon.png'), "Action 3", self)
        action3.triggered.connect(self.on_action3_triggered)
        left_toolbar.addAction(action3)

    def on_action1_triggered(self):
        print("Action 1 triggered")

    def on_action2_triggered(self):
        print("Action 2 triggered")
        
    def on_action3_triggered(self):
        print("Action 3 triggered")

# Main application logic
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
