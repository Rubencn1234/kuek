import time
import sys 
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import (QApplication, QLabel, QWidget, QVBoxLayout, QHBoxLayout, QGridLayout, QLineEdit, QPushButton)
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt


max_tries = int(3)
signed = bool(False)
teacher_user = "admin"
teacher_passw = "admin"
student_user = "user"
student_passw = "user"
is_teacher = bool(False)
trying = bool(False)
nota_1 = float(0)
nota_2 = float(0)
nota_3 = float(0)
nota_4 = float(0)



class Promediador(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(700, 300, 600, 300)
        self.setWindowIcon(QIcon())
        self.tries = 3
        self.title_label = QLabel("Sistema de notas", self)
        self.subtitle_label = QLabel("Por favor, Ingrese sus credenciales", self)
        self.user_label = QLabel("Ingrese usuario", self)
        self.user_input = QLineEdit(self)
        self.pasw_label = QLabel("Ingrese contraseña", self)
        self.pasw_input = QLineEdit(self)
        self.signin_button = QPushButton("Ingresar", self)
        self.welcome_label = QLabel("", self)
        self.text1_label = QLabel("", self)
        self.text2_label = QLabel("", self)
        self.text3_label = QLabel("", self)        
        self.text4_label = QLabel("", self)
        
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Sistema de notas")
        vbox = QVBoxLayout()
        vbox.addWidget
        vbox.addWidget(self.title_label)
        vbox.addWidget(self.subtitle_label)
        vbox.addWidget(self.user_label)
        vbox.addWidget(self.user_input)
        vbox.addWidget(self.pasw_label)
        vbox.addWidget(self.pasw_input)
        vbox.addWidget(self.signin_button)
        vbox.addWidget(self.welcome_label)

        self.timer = QtCore.QTimer(self)
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.update_counter)
        self.counter = 0

        

        self.setLayout(vbox)

        self.title_label.setAlignment(Qt.AlignCenter)
        self.subtitle_label.setAlignment(Qt.AlignCenter)
        self.user_input.setAlignment(Qt.AlignCenter)
        self.user_label.setAlignment(Qt.AlignCenter)
        self.pasw_input.setAlignment(Qt.AlignCenter)
        self.pasw_label.setAlignment(Qt.AlignCenter)
        self.welcome_label.setAlignment(Qt.AlignCenter)

        self.user_label.setObjectName("user_label")
        self.user_input.setObjectName("user_input")
        self.pasw_label.setObjectName("pasw_label")
        self.pasw_input.setObjectName("pasw_input")
        self.welcome_label.setObjectName("welcome_label")
        self.title_label.setObjectName("title_label")
        self.subtitle_label.setObjectName("subtitle_label")
        self.signin_button.setObjectName("signin_button")

        self.setStyleSheet("""
            QLabel, QPushButton{
                font-family: Arial
            }
            QLabel#title_label{
                font-size: 30px;
                font-weight: bold;
            }
            QLabel#subtitle_label{
                font-size: 25px;
            }
            QLabel#user_label{
                font-size: 20px;
            }
            QLineEdit#user_input{
                font-size: 20px;
            }
            QLabel#pasw_label{
                font-size: 20px;
            }
            QLineEdit#pasw_input{
                font-size: 20px;
            }
        """)


        self.signin_button.clicked.connect(self.sign_in)

    def update_counter(self):
        self.counter += 1
        print(f"Reloj interno, Contador: {self.counter}")



    def sign_in(self):
        user = self.user_input.text()
        passw = self.pasw_input.text()
        self.tries -= 1
        signed = False
        trying = True



        if user==teacher_user and passw==teacher_passw and self.tries>=1:
            signed = True
            is_teacher = True
            trying = False
            print("Teacher",user, passw)
            self.welcome_label.setText(f"Bienvenido {user} al sistema de notas (profesor)")
            self.signin_button.deleteLater()
            self.user_label.deleteLater()
            self.user_input.deleteLater()
            self.pasw_label.deleteLater()
            self.pasw_input.deleteLater()
            self.title_label.deleteLater()
            self.subtitle_label.deleteLater()
            self.welcome_label.setAlignment(Qt.AlignCenter)


        elif user==student_user and passw==student_passw and self.tries>=1:
            signed = True
            trying = False
            print("Student", user, passw)
            self.welcome_label.setText(f"Bienvenido {user} al sistema de notas (Estudiante)")



        elif self.tries>=0:
            trying  = False
            print("Clave y/o usuario invalido/a")
            print("Le quedan", self.tries, "intentos")
            self.welcome_label.setText(f"Clave y/o usuario invalido/a, Le quedan {self.tries} intentos ")
        else:
            print("Intentos maximos superados")
            self.welcome_label.setText(f"Intentos maximos alcanzados, espere 1 minuto para volver a intentar")
            self.timer.start()
            if self.counter >= 3:
                self.timer.stop()
                self.tries = 3
                self.welcome_label.setText(f"Clave y/o usuario invalido/a, Le quedan {self.tries} intentos ")
                

                
    def stop_repeating_timer(self):
        if self.timer.isActive():
            self.timer.stop()
            print("Repeating timer stopped.")
                
        
        
        

    def closeEvent(self, event):
        print("Deteniendo reloj interno.")
        self.stop_repeating_timer()
        event.accept()






    def sistema_notas_profe(self):
        print ("alo (profe)")







    def sistema_notas_student(self):
        print("olo (estudiante)")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Promediador()
    window.show()
    sys.exit(app.exec_())





# for i in range (0, 3):
#     if tries<3:
#         user = str(input("Ingrese usuario: "))
#         passw = str(input("Ingrese la contraseña: "))
#         if user==tuser and passw==tpassw:
#             print("Bienvenido al sistema", user, ".")
#             signed= int(1)
#             break
#         else:
#             tries += 1
#             print("Clave invalida")




# if signed==1:
#     hora = time.localtime
#     print("Hora Actual:", hora)

