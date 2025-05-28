import random
import time

logged = bool(True)
teacher = False
student = False
t_name = str("Eduardo Parker")
t_user = str("e.parker")
t_passwd = int(1234)
s_name = str("Carlos Jara")
s_user = str("c.jara")
s_passwd = int(1234)

student_1 = "Alicia Perez"
student_2 = "Bodoque Contreras"
student_3 = "Carlos Jara"
student_4 = "Diego Montes"
student_5 = "Elena Reyes"
student_6 = "Felipe Parra"
student_7 = "Guillermo Olmedo"
student_8 = "Hugo Muños"
student_9 = "Ivan Rojas"
student_10 = "Juan Perez"
student_11 = "Kevin Diaz"
student_12 = "Manuel Soto"
student_13 = "Nicolas Silva"


op_1 = 0
op_2 = 0
op_3 = 0
op_4 = 0
op_5 = 0
op_6 = 0
op_7 = 0
student_grades_1 = [7.0, 6.5, 6.0, 6.6]
student_grades_2 = [6.0, 5.5, 6.2, 6.5]
student_grades_3 = [6.5, 6.8, 5.9, 6.0]
student_grades_4 = [5.2, 5.0, 6.0, 4.7]
student_grades_5 = [5.0, 5.1, 4.9, 5.6]
student_grades_6 = [6.5, 5.2, 5.9, 6.1]
student_grades_7 = [4.0, 3.2, 5.5, 6.2]
student_grades_8 = [6.3, 6.5, 3.3, 5.0]
student_grades_9 = [2.5, 2.1, 5.5, 1.8]
student_grades_10 = [2.1, 6.4, 2.9, 5.5]
student_grades_11 = [1.7, 1.4, 1.0, 4.7]
student_grades_12 = [4.8, 5.6, 6.4, 7.0]
student_grades_13 = [1.5, 5.7, 2.2, 5.7]




def asistance():
    print()

def grades():
    print(f"{student_1}, {student_grades_1}")
    print(f"{student_2}, {student_grades_2}")
    print(f"{student_3}, {student_grades_3}")
    print(f"{student_4}, {student_grades_4}")
    print(f"{student_5}, {student_grades_5}")
    print(f"{student_6}, {student_grades_6}")
    print(f"{student_7}, {student_grades_7}")
    print(f"{student_8}, {student_grades_8}")
    print(f"{student_9}, {student_grades_9}")
    print(f"{student_10}, {student_grades_10}")
    print(f"{student_11}, {student_grades_11}")
    print(f"{student_12}, {student_grades_12}")
    print(f"{student_13}, {student_grades_13}")



def teacher_menu():
    print('''Seleccione una ipción:
          1. Ver Asistencia
          2. Ver Calificaciones
          3. Ver Anotaciones
          4. Salir
''')
    op_1 = int(input(""))
    match op_1:

        case 1:
            print("Cargando Asistencia...")
            asistance()
        case 2:
            print("Cargando Calificaciones...")
            grades()













def student_menu():
    print("")










user = str(input("Ingrese su usuario: "))
passwd = int(input("Ingrese su contraseña: "))
if user == t_user and passwd == t_passwd:
        logged = True
        teacher = True
        print(f"Sesión iniciada como el profesor {t_name}")
        print("Cargando menu...")
        time.sleep (2)
        teacher_menu()




while logged == False:
    print("Contraseña y/o usuario incorrecto/s")
    user = str(input("Ingrese su usuario: "))
    passwd = int(input("Ingrese su contraseña: ")) 
    if user == t_user and passwd == t_passwd:
        logged = True
        teacher = True
        print(f"Sesión iniciada como el profesor {t_name}")
        print("Cargando menu...")
        time.sleep (2)
        teacher_menu()

    elif user == s_user and passwd == s_passwd:
        logged = True
        student = True
        print(f"Sesión iniciada como el estudiante {s_name}")
        print("Cargando menu...")
        time.sleep (2)
        student_menu()


