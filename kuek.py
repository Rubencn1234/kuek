import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QStackedWidget, QMessageBox,
    QTableWidget, QTableWidgetItem, QHeaderView
)
from PyQt5.QtCore import pyqtSignal, Qt

class LoginWidget(QWidget):
    login_successful = pyqtSignal(str)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Inicio de sesion")
        self.failed_attempts = 0
        self.max_attempts = 3

        layout = QVBoxLayout(self)
        layout.setContentsMargins(50, 50, 50, 50)
        layout.setSpacing(15)

        self.title_label = QLabel("<h1>Sistema de notas escolar</h1>")
        self.title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.username_label = QLabel("Usuario:")
        self.username_input = QLineEdit()
        self.username_input.setPlaceholderText("Ingrese usuario (admin o estudiante)")
        self.password_label = QLabel("Contraseña:")
        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText("Ingrese contraseña (contra123 o pass)")
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)
        self.login_button = QPushButton("Iniciar Sesion")
        self.login_button.clicked.connect(self.attempt_login)
        self.password_input.returnPressed.connect(self.attempt_login)

        layout.addWidget(self.title_label)
        layout.addSpacing(20)
        user_layout = QHBoxLayout()
        user_layout.addWidget(self.username_label)
        user_layout.addWidget(self.username_input)
        layout.addLayout(user_layout)
        pass_layout = QHBoxLayout()
        pass_layout.addWidget(self.password_label)
        pass_layout.addWidget(self.password_input)
        layout.addLayout(pass_layout)
        layout.addSpacing(20)
        layout.addWidget(self.login_button, alignment=Qt.AlignmentFlag.AlignCenter)
        layout.addStretch()

    def attempt_login(self):
        username = self.username_input.text()
        password = self.password_input.text()

        user_role = None 

        if username == "admin" and password == "contra123":
            print("Inicio de sesion de admin correcto")
            user_role = "admin"
        elif username == "estudiante" and password == "pass":
             print("Inicio de sesion de estudiante correcto!")
             user_role = "student"

        if user_role: 
            self.failed_attempts = 0
            self.login_successful.emit(user_role)
        else: 
            self.failed_attempts += 1
            print(f"Login Fallido! Intento {self.failed_attempts} de {self.max_attempts}")
            if self.failed_attempts >= self.max_attempts:
                QMessageBox.critical(self, "Login Bloquado",
                                     f"Demasiados intentos de inicio de sesion ({self.max_attempts}). Login bloquado.")
                self.username_input.setEnabled(False)
                self.password_input.setEnabled(False)
                self.login_button.setEnabled(False)
            else:
                remaining_attempts = self.max_attempts - self.failed_attempts
                QMessageBox.warning(self, "Login Fallido",
                                    f"Clave o usuario invalido. {remaining_attempts} intentos restantes.")
                self.password_input.clear()
                self.username_input.setFocus()

    def reset_login_state(self):
        self.failed_attempts = 0
        self.username_input.setEnabled(True)
        self.password_input.setEnabled(True)
        self.login_button.setEnabled(True)
        self.username_input.clear() 
        self.password_input.clear()
        self.username_input.setFocus()

class AdminWidget(QWidget): 
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Tablero del admin") 

        layout = QVBoxLayout(self)
        layout.setContentsMargins(20, 20, 20, 20)
        layout.setSpacing(10)

        self.title_label = QLabel("<h2>Admin - Administracion de notas</h2>")
        self.title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.grade_table = QTableWidget()
        self.grade_table.setColumnCount(3)
        self.grade_table.setHorizontalHeaderLabels(["Student", "Subject", "Grade"])
        self.grade_table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.grade_table.setEditTriggers(QTableWidget.EditTrigger.NoEditTriggers)

        self.logout_button = QPushButton("Cerrar sesion")

        layout.addWidget(self.title_label)
        layout.addWidget(self.grade_table)
        layout.addWidget(self.logout_button, alignment=Qt.AlignmentFlag.AlignRight)

        self.load_grades()

    def load_grades(self):
        grades_data = [
            ("Alicia Perez", "Matematicas", "7"),
            ("Benjamin Contreras", "Matematicas", "6"),
            ("Carlos Jara", "Matematicas", "6.5"),
            ("Diego Montes", "Matematicas", "5.5"),
            ("Elena Reyes", "Matematicas", "5"),
            ("Felipe Parra", "Matematicas", "6.5"),
        ]
        self.grade_table.setRowCount(len(grades_data))
        for row_idx, (student, subject, grade) in enumerate(grades_data):
            self.grade_table.setItem(row_idx, 0, QTableWidgetItem(student))
            self.grade_table.setItem(row_idx, 1, QTableWidgetItem(subject))
            self.grade_table.setItem(row_idx, 2, QTableWidgetItem(grade))


class StudentWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Tablero del estudiante")

        layout = QVBoxLayout(self)
        layout.setContentsMargins(30, 30, 30, 30)
        layout.setSpacing(15)

        self.title_label = QLabel("<h2>Tus Notas</h2>")
        self.title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.info_label = QLabel("Bienvenido Carlos\n\n Tu promedio es: 6.5")
        self.info_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.info_label.setStyleSheet("font-size: 14px;") 

        self.logout_button = QPushButton("Cerrar sesion")

        layout.addWidget(self.title_label)
        layout.addWidget(self.info_label)
        layout.addStretch() 
        layout.addWidget(self.logout_button, alignment=Qt.AlignmentFlag.AlignRight)



class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Aplicacion escolar")
        self.setMinimumSize(500, 400)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.stacked_widget = QStackedWidget(self.central_widget)

        self.login_screen = LoginWidget()
        self.student_screen = StudentWidget()
        self.admin_screen = AdminWidget()

        self.login_screen_index = self.stacked_widget.addWidget(self.login_screen)
        self.student_screen_index = self.stacked_widget.addWidget(self.student_screen)
        self.admin_screen_index = self.stacked_widget.addWidget(self.admin_screen)

        main_layout = QVBoxLayout(self.central_widget)
        main_layout.addWidget(self.stacked_widget)
        main_layout.setContentsMargins(0,0,0,0)

        self.login_screen.login_successful.connect(self.handle_login_success)

        self.student_screen.logout_button.clicked.connect(self.show_login_screen)
        self.admin_screen.logout_button.clicked.connect(self.show_login_screen)

        self.show_login_screen() 

    def handle_login_success(self, role):
        print(f"Login de: {role}")
        if role == "admin":
            self.stacked_widget.setCurrentIndex(self.admin_screen_index)
            self.setWindowTitle("Aplicacion Escolar - Tablero del admin")
            self.resize(600, 500) 
        elif role == "student":
            self.stacked_widget.setCurrentIndex(self.student_screen_index)
            self.setWindowTitle("Aplicacion Escolar - Tablero del estudiante")
            self.resize(450, 350)
        else:
            QMessageBox.error(self, "Error", f"Rol desconocido: {role}")
            self.show_login_screen()


    def show_login_screen(self):
        self.login_screen.reset_login_state()
        self.stacked_widget.setCurrentIndex(self.login_screen_index)
        self.setWindowTitle("Aplicacion Escolar - Inicio de sesion")
        self.resize(500, 400) 


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec())