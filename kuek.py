import time
import sys
from PyQt5.QtWidgets import (QApplication, QLabel, QWidget, QVBoxLayout, QHBoxLayout, QGridLayout, QLineEdit, QPushButton)
from PyQt5.QtGui import QIcon

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(700, 300, 500, 500)
        self.setWindowIcon(QIcon())
        self.user_input = QLineEdit(self)
        self.pasw_input = QLineEdit(self)
        self.sign_in = QPushButton("Ingresar", self)
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Promediador de notas")
        vbox = QVBoxLayout()
        vbox.addWidget(self.user_input)
        vbox.addWidget(self.pasw_input)
        vbox.addWidget(self.sign_in)

        self.setLayout(vbox)

        self.user_input.setAlignment()


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()




# tries = int(0)
# signed = int(0)
# tuser = "admin"
# tpassw = "admin"
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

