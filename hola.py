import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QStackedWidget, QMessageBox,
    QTableWidget, QTableWidgetItem, QHeaderView
)
from PyQt5.QtCore import pyqtSignal, Qt

# --- 1. Login Widget ---
class LoginWidget(QWidget):
    # Signal emitted when login is successful
    login_successful = pyqtSignal()
    # Signal emitted when login fails (optional, can use QMessageBox directly)
    # login_failed = pyqtSignal(str)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Login") # Title for the widget itself (if shown standalone)

        layout = QVBoxLayout(self)
        layout.setContentsMargins(50, 50, 50, 50) # Add some padding
        layout.setSpacing(15) # Space between widgets

        self.title_label = QLabel("<h1>School Grade System Login</h1>")
        self.title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.username_label = QLabel("Username:")
        self.username_input = QLineEdit()
        self.username_input.setPlaceholderText("Enter your username (e.g., admin)")

        self.password_label = QLabel("Password:")
        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText("Enter your password (e.g., password123)")
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password) # Hide password

        self.login_button = QPushButton("Login")
        self.login_button.clicked.connect(self.attempt_login)
        # Allow pressing Enter in password field to trigger login
        self.password_input.returnPressed.connect(self.attempt_login)

        # Add widgets to layout
        layout.addWidget(self.title_label)
        layout.addSpacing(20) # Extra space after title

        # Use QHBoxLayout for label + input pairs for better alignment (optional)
        user_layout = QHBoxLayout()
        user_layout.addWidget(self.username_label)
        user_layout.addWidget(self.username_input)
        layout.addLayout(user_layout)

        pass_layout = QHBoxLayout()
        pass_layout.addWidget(self.password_label)
        pass_layout.addWidget(self.password_input)
        layout.addLayout(pass_layout)

        layout.addSpacing(20) # Space before button
        layout.addWidget(self.login_button, alignment=Qt.AlignmentFlag.AlignCenter)
        layout.addStretch() # Push everything up

    def attempt_login(self):
        username = self.username_input.text()
        password = self.password_input.text()

        # --- !!! IMPORTANT: Hardcoded credentials for demonstration ONLY ---
        # --- In a real application, NEVER do this. Use secure authentication. ---
        if username == "admin" and password == "password123":
            print("Login Successful!")
            self.login_successful.emit() # Signal success
        elif username == "student" and password == "pass":
             print("Login Successful!")
             self.login_successful.emit() # Signal success for another user
        else:
            print("Login Failed!")
            QMessageBox.warning(self, "Login Failed", "Invalid username or password.")
            # Optionally clear fields or just let the user try again
            # self.password_input.clear()

# --- 2. Grade System Widget ---
class GradeSystemWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Grade System")

        layout = QVBoxLayout(self)
        layout.setContentsMargins(20, 20, 20, 20)
        layout.setSpacing(10)

        self.title_label = QLabel("<h2>Student Grades</h2>")
        self.title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.grade_table = QTableWidget()
        self.grade_table.setColumnCount(3) # Student, Subject, Grade
        self.grade_table.setHorizontalHeaderLabels(["Student", "Subject", "Grade"])
        # Make table columns resize nicely
        self.grade_table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        # Make table read-only for this example
        self.grade_table.setEditTriggers(QTableWidget.EditTrigger.NoEditTriggers)


        self.logout_button = QPushButton("Logout")
        # We need to connect this back to the main window to switch back
        # We'll do the connection in MainWindow

        layout.addWidget(self.title_label)
        layout.addWidget(self.grade_table)
        layout.addWidget(self.logout_button, alignment=Qt.AlignmentFlag.AlignRight)

        self.load_grades() # Load dummy data

    def load_grades(self):
        # --- Dummy Data: In a real app, fetch this based on logged-in user ---
        grades_data = [
            ("Alice Smith", "Math", "A"),
            ("Bob Johnson", "Math", "B"),
            ("Alice Smith", "Physics", "A-"),
            ("Charlie Brown", "History", "C+"),
            ("Bob Johnson", "Physics", "C"),
            ("Alice Smith", "Chemistry", "B+"),
        ]

        self.grade_table.setRowCount(len(grades_data))

        for row_idx, (student, subject, grade) in enumerate(grades_data):
            self.grade_table.setItem(row_idx, 0, QTableWidgetItem(student))
            self.grade_table.setItem(row_idx, 1, QTableWidgetItem(subject))
            self.grade_table.setItem(row_idx, 2, QTableWidgetItem(grade))

# --- 3. Main Window ---
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("School Application")
        self.setMinimumSize(500, 400) # Set a reasonable minimum size

        # Central widget to hold the stacked layout
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        # Stacked widget to switch between screens
        self.stacked_widget = QStackedWidget(self.central_widget)

        # Create the individual screen widgets
        self.login_screen = LoginWidget()
        self.grade_screen = GradeSystemWidget()

        # Add screens to the stacked widget
        # Keep track of indices for easier switching
        self.login_screen_index = self.stacked_widget.addWidget(self.login_screen)
        self.grade_screen_index = self.stacked_widget.addWidget(self.grade_screen)

        # Main layout for the central widget
        main_layout = QVBoxLayout(self.central_widget)
        main_layout.addWidget(self.stacked_widget)
        main_layout.setContentsMargins(0,0,0,0) # Use full space

        # Connect signals
        self.login_screen.login_successful.connect(self.show_grade_system)
        # Connect the logout button from the grade screen
        self.grade_screen.logout_button.clicked.connect(self.show_login_screen)


        # Start on the login screen
        self.show_login_screen()

    def show_login_screen(self):
        self.stacked_widget.setCurrentIndex(self.login_screen_index)
        # Optional: Clear password field on logout/return to login
        self.login_screen.password_input.clear()
        self.login_screen.username_input.setFocus() # Set focus to username field
        self.setWindowTitle("School Application - Login") # Update window title
        self.resize(500, 400) # Reset to a decent login size

    def show_grade_system(self):
        # Optional: Could reload grades here if they depend on the user
        # self.grade_screen.load_grades() # For now, data is static
        self.stacked_widget.setCurrentIndex(self.grade_screen_index)
        self.setWindowTitle("School Application - Grade System") # Update window title
        self.resize(600, 500) # Maybe resize for the table view

# --- Application Entry Point ---
if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec())