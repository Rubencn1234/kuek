import random
import time

has_logged = False
logged = bool(True)
teacher = False
student = False
t_name = str("Eduardo Parker")
t_user = str("e.parker")
t_passwd = int(1234)
s_name = str("Carlos Jara")
s_user = str("c.jara")
s_passwd = int(1234)
actual = ""
actual_2 = ""
h = 0
students = ['Alicia Perez', 'Bodoque Contreras', 'Carlos Jara', 'Diego Montes', 'Elena Reyes', 'Felipe Parra', 'Guillermo Olmedo', 'Hugo Muños', 'Ivan Rojas', 'Juan Perez', 'Kevin Diaz', 'Manuel Soto', 'Nicolas Silva'] 
student_count = len(students)
ausentes = 0
presentes = 0

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

student_asistencia_1 = []
student_asistencia_2 = []
student_asistencia_3 = []
student_asistencia_4 = []
student_asistencia_5 = []
student_asistencia_6 = []
student_asistencia_7 = []
student_asistencia_8 = []
student_asistencia_9 = []
student_asistencia_10 = []
student_asistencia_11 = []
student_asistencia_12 = []
student_asistencia_13 = []

op_1 = 0
op_2 = 0
op_3 = 0
op_4 = 0
op_5 = 0
op_6 = 0
op_7 = 0
student_grades_0 = [0, 0, 0, 0]
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

student_prom_1 = sum(student_grades_1) / len(student_grades_1)
student_prom_2 = sum(student_grades_2) / len(student_grades_2)
student_prom_3 = sum(student_grades_3) / len(student_grades_3)
student_prom_4 = sum(student_grades_4) / len(student_grades_4)
student_prom_5 = sum(student_grades_5) / len(student_grades_5)
student_prom_6 = sum(student_grades_6) / len(student_grades_6)
student_prom_7 = sum(student_grades_7) / len(student_grades_7)
student_prom_8 = sum(student_grades_8) / len(student_grades_8)
student_prom_9 = sum(student_grades_9) / len(student_grades_9)
student_prom_10 = sum(student_grades_10) / len(student_grades_10)
student_prom_11 = sum(student_grades_11) / len(student_grades_11)
student_prom_12 = sum(student_grades_12) / len(student_grades_12)
student_prom_13 = sum(student_grades_13) / len(student_grades_13)

class_total = student_prom_1 + student_prom_2 + student_prom_3 + student_prom_4 + student_prom_5 + student_prom_6 + student_prom_7 + student_prom_8 + student_prom_9 + student_prom_10 + student_prom_11 + student_prom_12 + student_prom_13

class_prom = round(class_total / student_count, 1)

def status():
    global student_count
    print("----------------------------------------------------------------------------")
    for i in range (1, student_count+1):
        print


def asistance():
    global logged, student_count, students, presentes, ausentes, porc_asistencia
    while logged == True:
        print(f"-----Pasando Lista-----")
        print(f'''Ingrese "s" para confirmar asistencia, ingrese "n" para confirmar inasistencia.''')
        for i in range (student_count):
            asistencia = input(str(f"{i+1}. {students[i]}: "))
            if asistencia == "s":
                print(f"{students[i]} esta presente")
                exec(f'''student_asistencia_{i+1}.append("True") ''')
                presentes += 1

            elif asistencia == "n":
                print(f"{students[i]} esta ausente")
                exec(f'''student_asistencia_{i+1}.append("False")''')
                ausentes += 1

        porc_asistencia =  (presentes / student_count) * 100
        print(f"Porcentaje de asistencia: {round(porc_asistencia, 1)}%")
        print(f"Presentes: {presentes}")
        print(f"Ausentes: {ausentes}")
        print("Volviendo al menu...")
        time.sleep(2)
        teacher_menu()


def see_grades():
    global logged
    while logged == True:
        print(f"{student_1}: {student_grades_1}")
        print(f"{student_2}: {student_grades_2}")
        print(f"{student_3}: {student_grades_3}")
        print(f"{student_4}: {student_grades_4}")
        print(f"{student_5}: {student_grades_5}")
        print(f"{student_6}: {student_grades_6}")
        print(f"{student_7}: {student_grades_7}")
        print(f"{student_8}: {student_grades_8}")
        print(f"{student_9}: {student_grades_9}")
        print(f"{student_10}: {student_grades_10}")
        print(f"{student_11}: {student_grades_11}")
        print(f"{student_12}: {student_grades_12}")
        print(f"{student_13}: {student_grades_13}")
        op_4 = int(input(f"1. Volver al menu, 2. Salir: "))
        if op_4 == 1:
            teacher_menu()
        elif op_4 == 2:
            print("Saliendo...")
            time.sleep(3)
            logged = False


def anotations():
    global logged
    while logged == True:
        print("kuek")
        print("Volviendo al menu...")
        time.sleep(3)
        teacher_menu()


def edit_grades():
    global logged, actual, student_grades_1, student_grades_2, student_grades_3, student_grades_4, student_grades_5, student_grades_6, student_grades_7, student_grades_8, student_grades_9, student_grades_10, student_grades_11, student_grades_12, student_grades_13
    while logged == True:
        print(f'''Alumnos en el curso: 
    1.{student_1}
    2. {student_2}
    3. {student_3}
    4. {student_4}
    5. {student_5}
    6. {student_6}
    7. {student_7}
    8. {student_8}
    9. {student_9}
    10. {student_10}
    11. {student_11}
    12. {student_12}
    13. {student_13}''')
        op_2 = int(input(f"Ingrese el numero de lista del estudiante a editar la nota, ingrese cero para volver al menu: "))
        if op_2 == 0:
            teacher_menu()
        exec(f"actual = student_grades_{op_2}")
        actual_2 = actual
        print(f"alo: {actual_2}")
        print("----------------------------------------------------------------------------")
        for i, val in range(actual):
            print(f"Nota {i+1}: {val}")
        op_3 = int(input(f"Ingrese el numero de nota que desea editar, ingrese 0 para salir al menu: "))
        if op_3 == 0:
            teacher_menu()





def teacher_menu():
    global logged
    while logged == True:
        print(f"Cantidad de estudiantes: {student_count}")
        print(f"Promedio de la clase: {class_prom}")
        print('''Seleccione una opción:
            1. Pasar Asistencia
            2. Ver Calificaciones
            3. Modificar Calificaciones
            4. Ver Anotaciones
            5. Salir
    ''')
        op_1 = int(input(""))
        match op_1:

            case 1:
                print("Cargando Asistencia...")
                asistance()
            case 2:
                print("Cargando Calificaciones...")
                see_grades()

            case 3:
                print("Cargando Calificaciones...")
                edit_grades()

            case 4:
                print("Cargando anotaciones...")
                anotations()


            case 5:
                print("Saliendo...")
                login()














def student_menu():
    global logged
    while logged == True:
        print(f"Bienvenido {student_3}")
        print(f"Tu promedio es de: {student_prom_3}")
        print(f"Tus Calificaciones son: {student_grades_3}")
        print(f"Tu porcentaje de asistencia es de: ")
        input("")
        print("Saliendo...")
        time.sleep(2)
        login()










def login():
    print("--------Bienvenido al sistema de notas y asistencia.--------")
    user = str(input("Ingrese su usuario: "))
    try:
        passwd = int(input("Ingrese su contraseña: "))
    except ValueError:
        print("Error, la contraseña es un numero. Intente nuevamente.")
        login()
    if user == t_user and passwd == t_passwd:
            logged = True
            has_logged = True
            while logged == True:
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

    else:
        print("Usuario y/o contraseña no validos, vuelva a intentar.")
        logged = False
        has_logged = False




def login_again():
    while logged == False and has_logged == False:
        print("Contraseña y/o usuario incorrecto/s")
        user = str(input("Ingrese su usuario: "))
        try:
            passwd = int(input("Ingrese su contraseña: ")) 
        except ValueError:
            print("Error, la contraseña es un numero. Intente nuevamente.")
            login()
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


login()