
# def votaciones():
#     voto = int(0)
#     op1 = int(0)
#     p1 = str("Piñera")
#     op2 = int(0)
#     p2 = str("Bachelet")
#     op3 = int(0)
#     p3 = str("Nulo")
#     win = int(1)
#     winner = str("Nadie")
#     votantes = int(input("Ingrese numero de votantes: "))

#     for i in range (0, votantes):
#         voto = int(input("1. Piñera, 2. Bachelet, Cualquier otra opcion cuenta como nulo: "))
#         if voto == 1:
#             op1 +=1
#         elif voto == 2:
#             op2 +=1
#         else:
#             op3 +=1

#     if op1>op2:
#         winner = p1
#     elif op1<op2:
#         winner = p2
#     elif op1==op2:
#         win = 0

#     print("Fin de las elecciones")
#     print("La cantidad de votos totales es:", votantes)
#     if win==0:
#         print("Las elecciones terminaron en empate")
#     else:
#         print("El ganador de las elecciones fue:", winner)

#     print("La cantidad de votos nulos fue:", op3)

#----------------------------------------------------------------------------

# palabra = str(input("Ingrese una palabra: "))
# long = len(palabra)
# print("La palabra consiste de", long, "letras")

#----------------------------------------------------------------------------

# word=input("Ingrese palabra: ")
# car=0
# for i in word:
#     car+=1
#     print(i)
# print("Cantidad de caracteres:", car)

#----------------------------------------------------------------------------

# word=input("Ingrese palabra: ")
# car=0
# vow=0
# cons=0
# for i in word:
#     if i=="a" or i=="e" or i=="i" or i=="o" or i=="u":
#         vow+=1
#     else:
#         cons+=1
#     car+=1
#     print(i)
# print("Cantidad de caracteres:", car)
# print("Cantidad de vocales: ", vow)
# print("Cantidad de consonantes:", cons)

#----------------------------------------------------------------------------

# num=0
# while num<=5:
#     print(num)
#     num+=1

#----------------------------------------------------------------------------

# import time
# num=10

# while num>=0:
#     print(num)
#     time.sleep(1)
#     num-=1

#----------------------------------------------------------------------------

# ans="no"

# while ans!="si":
#     ans=str(input("Si o no?: "))

#----------------------------------------------------------------------------

# pasw=1234
# tries=0
# maxtries=3
# valid=0

# contraseña=int(input("Ingrese su contraseña: "))
# while contraseña!=pasw:
#     print("Error, Clave incorrecta")
#     tries +=1
#     contraseña=int(input("Ingrese su contraseña: "))


# print("Clave correcta")

#----------------------------------------------------------------------------

# carrito=str()
# obj=0
# cant=0
# compras=int(input("Ingrese la cantidad de cosas que desea comprar: "))
# while cant<=compras:
#     print("Ingrese el objeto que desea llevar: ")
#     obj=input("1.Arroz, 2.Fideos, 3.Palta, 4.Velas, 5.Neumaticos, 6.Latas de atun, 7.Queso")
#     if obj==1:
#         carrito+="Arroz, "
#     elif obj==2:
#         carrito+="Fideos"
#     elif obj==3:
#         carrito+="Palta"
#     elif obj==4:
#         carrito+="Velas"
#     elif obj==5:
#         carrito+="Neumaticos"
#     elif obj==6:
#         carrito+="Latas de atun"

        


#----------------------------------------------------------------------------

# total=0
# pares=0
# impares=0
# num=-1
# print("Ver si un numero es par o impar, ingrese 0 para salir.")
# num=int(input("Ingrese numero: "))
# while num!=0:
#     if  num % 2:
#         print("Impar")
#         impares+=1
#         total+=1
#     else:
#         print("Par")
#         pares+=1
#         total+=1
#     num=num=int(input("Ingrese numero: "))

# print("La cantidad de numeros pares:", pares)
# print("La cantidad de numeros impares:", impares)

#----------------------------------------------------------------------------

# total=0
# num=int
# sum=0
# pares=0
# impares=0
# while num!=0:
#     num=int(input("Ingrese un numero: "))
#     sum+=num
#     print("La suma actual es:", sum)
#     if  num % 2:
#         print("Impar")
#         impares+=1
#         total+=1
#     else:
#         print("Par")
#         pares+=1
#         total+=1

# print("Suma total:", sum)
# print("Cantidad de pares: ", pares)
# print("Cantidad de impares: ", impares)

#----------------------------------------------------------------------------

# import random
# import time
# turn=random.randint(1,2)
# lp1=50
# lp2=50
# winner=str("Nadie")
# p1 = str(input("Ingrese el nombre del jugador 1: "))
# p2 = str(input("Ingrese el nombre del jugador 2: "))
# while lp1>=0 or lp2>=0:
#     time.sleep(1)
#     if turn==1:
#         print("Turno de", p1)
#         dam=random.randint(1,10)
#         print(p1,"le a hecho", dam, "de daño a ", p2)
#         lp2-=dam
#         if lp2>0:
#             print("A ", p2, "le quedan", lp2, "de vida")
#         else:
#             print(p2, "a sido derrotado")
#             winner=p1
#             break
#         turn=2
#     else:
#         print("Turno de", p2)
#         dam=random.randint(1,10)
#         print(p2, "le a hecho", dam, "de daño a ", p1)
#         lp1-=dam
#         if lp1>0:
#             print("A ", p1, "le quedan", lp1, "de vida")
#         else:
#             print(p1, "a sido derrotado")
#             winner=(p2)
#             break
#         turn=1

# print("El ganador es:", winner)

#----------------------------------------------------------------------------

# for i in range (1,10,3):
#     print(i)

#----------------------------------------------------------------------------

# aux=0
# while (aux!=3):
#     print("1-$1000")
#     print("2-$500")
#     print("3- salir")    
#     aux = int(input("Input: "))
#     if (aux==1):
#         print("1")

#----------------------------------------------------------------------------

# edad=-1
# while (edad <0 or edad>100):
#     edad=int(input("Ingrese edad: "))
#     if (edad<0 or edad>100):
#         print("Error, edad fuera de rango.")

# print("Edad ingresada correctamente.")

#----------------------------------------------------------------------------

# par=0
# impar=0

# n1 = int(input("Ingrese un numero: "))

# for i in range(n1):
#     if i % 2:
#         print(i, "Impar")
#     else:
#         print(i, "Par")

#----------------------------------------------------------------------------

# sum=0
# num=int(input("[Ingrese 0 para salir] Ingrese un numero a sumar: "))
# while num!=0:
#     sum+=num
#     print("Suma actual:", sum)
#     num=int(input("[Ingrese 0 para salir] Ingrese un numero a sumar: "))


# print("Cantidad de numeros ingresados:", total)
# print("Suma de numeros ingresados:", sum)

#----------------------------------------------------------------------------

# import random
# mul=random.randint(2,8)
# n1 = int(input("Ingrese un numero: "))
# print("El multiplicador es:", mul)
# resul=n1*mul
# print("Su resultado es:", resul)
# if resul>50:
#     print("Si")
# else:
#     print("No")

#----------------------------------------------------------------------------

# n1=input("Ingrese un numero: ")
# if n1<0:
#     print("negativo")
# elif n1>0:
#     print("Positivo")

# else:
#     print(0)

#----------------------------------------------------------------------------

# import random

# botella = int(10)
# sed = True
# rellenar = ""
# tomar = False
# trago = random.randint(30, 60)

# while botella >= 0:
#     if sed == True:
#         print("Tienes sed")
#         ans = str(input("Desea tomar agua?: "))
#         if ans=="si":
#             botella = botella-trago
#             tomar = True
#             print(f"Has tomado agua, a la botella le quedan {botella}ml")
#         elif ans=="no":
#             print("No has tomado agua")

# while botella <= 0:
#     print("Botella vacia")
#     rellenar = str(input("Rellenar botella?: "))
#     if rellenar=="si":
#         botella=1000
#         print("Has rellenado la botella")
#     elif rellenar=="no":
#         print("No has rellenado la botella")



#----------------------------------------------------------------------------

# import time
# e_level = float(1)
# nacionalidad=0
# points=float(0)
# sueldo=float(0)

# print("Calculadora de puntaje crediticio.")
# income = int(input("Ingrese cuales son sus ingresos mensuales: "))
# if income < 500000:
#     print("Ingresos menores a $500.000")
#     sueldo=100000

# elif income>=500000 and income<1000000:
#     print("Ingresos mayores a $500.000 y menores a $1.000.000")
#     sueldo=300000

# elif income>1000000 and income<1500000:
#     print("Ingresos mayores a $1.000.000 ")
#     sueldo=650000
# elif income>1500000:
#     print("Ingresos mayores a 1.500.000")
#     sueldo=1000000


# ans1 = int(input("Ingrese su nivel de educación. 1: Basico, 2: Medio, 3: Superior "))

# if ans1==1:
#     print("Su nivel de educacion es basico")
#     e_level=1

# elif ans1==2:
#     print("Su nivel de educacion es medio")
#     e_level=1.3

# elif ans1==3:
#     print("Su nivel de educacion es superior")
#     e_level=1.5

# print("Su nacionalidad es chilena o extranjera? 1. Chileno, 2. Extranjero")
# nacionalidad=int(input())

# print("Calculando puntaje")
# points=sueldo*e_level

# if nacionalidad == 1:
#     points += 300000

# print(f"Su puntaje crediticio es: {points}")

#----------------------------------------------------------------------------

# ▄ (alt+220)

#----------------------------------------------------------------------------

# import random

# n1 = int(input("Ingrese un numero: "))
# n2 = int(input("Ingrese otro numero: "))
# resul = float(0)

# if n2<n1:
#     print("El segundo numero debe ser mayor al primero, intente nuevamente")
#     n1 = int(input("Ingrese un numero: "))
#     n2 = int(input("Ingrese otro numero: "))

# resul = random.randint(n1, n2)
# print(resul)


# print("▄"*resul)

#----------------------------------------------------------------------------


# def suma():
#     n1=int(input("Ingrese el primer numero: "))
#     n2=int(input("Ingrese el segundo numero: "))
#     print(f"El resultado de la suma es: {n1+n2} ")

# def resta():
#     n1=int(input("Ingrese el primer numero: "))
#     n2=int(input("Ingrese el segundo numero: "))
#     print(f"El resultado de la resta es: {n1-n2} ")

# def multiplicar():
#     n1=int(input("Ingrese el primer numero: "))
#     n2=int(input("Ingrese el segundo numero: "))
#     print(f"El resultado de la multiplicacion es: {n1*n2} ")

# def dividir():
#     n1=int(input("Ingrese el primer numero: "))
#     n2=int(input("Ingrese el segundo numero: "))
#     print(f"El resultado de la division es: {n1/n2} ")
    


# def calc():
#     while True:
#         op = int(input('''Seleccionar opcion:
#                     1. suma
#                     2. resta
#                     3. multiplicar
#                     4. dividir
#                     5. Salir
#                     '''))

#         match op:
#             case 1:
#                 print("suma")
#                 suma()

#             case 2:
#                 print("resta")
#                 resta()

#             case 3:
#                 print("multiplicar")
#                 multiplicar()
#             case 4:
#                 print("Dividir")
#                 try:
#                     dividir()
#                 except ZeroDivisionError as Division_cero:
#                     print(f"Se produjo un error: {Division_cero}")
                
#             case 5:
#                 print("Saliendo")
#                 break
#             case _:
#                 print("Invalido")


# while True:
#     print("Bienvenido al menu")
#     menu=int(input('''Seleccione una opcion:
#                    1. Calculadora
#                    2. Contador de votos
#                    '''))

#     match menu:
#         case 1:
#             print("Ingresando a calculadora")
#             calc()

#         case 2:
#             print("Ingresando a Contador de votos")

#----------------------------------------------------------------------------

# sub_prom = float(0)
# prom = float(0)
# prom_seccion = float(0)
# n_actual = 0
# a_actual = 0
# a_aprueban = int(0)
# a_reprueban = int(0)
# print("Bienvenido al sistema de notas")
# n_alumnos = int(input("Ingrese la cantidad de alumnos de la sección: "))
# while a_actual < n_alumnos:
#     for h in  range (0, n_alumnos):
#         n_notas = int(input(f"Ingrese la cantidad de notas del alumno {h+1}: "))
#         for i in range (0, n_notas):
#             sub_prom += float(input(f"Ingrese la nota {i+1} del alumno {h+1}: "))
#             prom = sub_prom/(i+1)

#         prom_seccion += prom
#         print(f"El promedio del alumno {h+1} es de: {prom}")
#         if prom < 4:
#             print(f"El alumno {h+1} reprobo con un: {prom}")
#             a_reprueban += 1

#         else:
#             print(f"El alumno {h+1} aprobo con un: {prom}")
#             a_aprueban += 1
#         prom = 0

# print(f"El promedio de la seccion fue de: {prom_seccion}")
# print(f"La cantidad de alumnos que aprobaron fue de: {a_aprueban} ")
# print(f"La cantidad de alumnos que reprobo fue de: {a_reprueban}")

#----------------------------------------------------------------------------

# import random

# dog_count = int(0)
# bunny = int(0)
# bunny_cuota = int(3)
# awarded = int(0)
# not_awarded = int(0)
# success_rate = float(0)

# while True:
#     try: 
#         dog_count = int(input("Ingrese la cantidad de perros que van a cazar: "))
#         while dog_count<1:
#             print("Solo ingrese numeros enteros positivos")
#             dog_count = int(input("Ingrese la cantidad de perros que van a cazar: "))
#         for i in range (1, dog_count + 1):
#             bunny = random.randint (0,6)
#             if bunny >= bunny_cuota:
#                 print(f"El perro {i} tiene premio")
#                 awarded += 1

#             else:
#                 print(f"El perro {i} no tiene premio")
#                 not_awarded += 1

#         print(f"{awarded} perros cumplieron la cuota y merecen premio")
#         print(f"{not_awarded} perros no cumplieron la cuota y requieren confinamiento solitario")
#         success_rate = (dog_count/100)*awarded  
#         print(f"La tasa de exito de los perros fue de: {success_rate}%")
#         break
#     except Exception as Error:
#         print("Ingrese solo numeros enteros positivos")

#----------------------------------------------------------------------------

# import time
# import random

# cars = int(0)
# full_wash = int(0)
# standard_wash = int(0)
# basic_wash = int(0)
# sales = int(0)
# income = int(0)
# highest_payment = int(0, )
# menu = int(0)
# menu_2 = int(0)

# while True:
#     menu = int(input('''----------------------------------------------------------------------------
#                      Bienvenido al autolavado, Seleccione una opción:
#                      1. Cursar pago del lavado
#                      2. Ver ventas diarias
#                      3. Salir
#                      '''))
#     match menu:
#         case 1:
#             print("----------------------------------------------------------------------------")
#             print('''Precios: 
#                   1. Servicio Full: $15.000
#                   2. Servicio Standard: $10.000
#                   3. Servicio Basico: $7.000
#                   ----------------------------------------------------------------------------''')
#             menu_2 = int(input("Seleccione el servicio: "))
#             match menu_2:
#                 case 1:
#                     print("Servicio Full")
#                     income += 15000
#                     cars += 1
#                     if 15000 > highest_payment:
#                         highest_payment = 15000
#                     print("Lavando auto...")
#                     time.sleep (2)

#                 case 2:
#                     print("Servicio Standard")
#                     income += 10000
#                     cars += 1
#                     if 10000 > highest_payment:
#                         highest_payment = 10000
#                     print("Lavando auto...")
#                     time.sleep (2)

#                 case 3:
#                     print("Servicio Basico")
#                     income += 7000
#                     cars += 1
#                     if 7000 > highest_payment:
#                         highest_payment = 7000
#                     print("Lavando auto...")
#                     time.sleep (2)

#         case 2:
#             print("----------------------------------------------------------------------------")
#             print(f'''Resumen Financiero:
# Autos Lavados: {cars}
# Ingresos: ${income}
# Venta mas alta: ${highest_payment}
# ----------------------------------------------------------------------------''')

#         case 3:
#             print("----------------------------------------------------------------------------")
#             print("Saliendo...")
#             time.sleep (2)
#             break


#----------------------------------------------------------------------------

# import random, time

# tries = 0
# max_tries = 3
# cupo = int(200000)
# deuda = int(100000)
# saldo = int(500000)
# ahorro = int(5000000)
# deposito = int(0)
# retiro = int(0)
# pago = int(0)
# s_user = int(20512096)
# s_passw = int(1234)
# signed = False

# while True:
#     while tries <= max_tries:
#         print("Bienvenido al pago de deudas de su tarjeta masterplop")
#         user = int(input("Ingrese su usuario: "))
#         passw = int(input("Ingrese su pin numerico: "))
#         while user == s_user and passw == s_passw:
#             print("Datos correctos, Cargando sistema.")
#             signed = True
#             time.sleep (2)
#             while signed == True:
#                 op2 = int(input(f'''Seleccione un producto:
#                     1. Tarjeta de credito
#                     2. Cuenta Corriente
#                     3. Cuenta de ahorro
#                     4. Cerrar sesión'''))
#                 match op2:

#                     case 1:
#                         print("----Tarjeta de Credito----")
#                         print(f"Cupo total: ${cupo}")
#                         print(f"Cupo restante: ${cupo-deuda}")
#                         print(f"Deuda Pendiente: ${deuda}")
#                         print("")
#                         op3 = int(input(f'''Seleccione una opción:
#                             1. Pagar (deuda restante: {deuda})
#                             2. Volver al menu'''))
#                         if op3 == 1:
#                             print(f"El saldo de su cuenta corriente es de: ${saldo}")
#                             pago = int(input("Ingrese el monto que quiere pagar de su tarjeta: "))
#                             if pago <=0:
#                                 print("Ingrese un monto valido de pago")
#                                 pago = int(input("Ingrese el monto que quiere pagar de su tarjeta: "))
#                             else:
#                                 op4 = input('''Escriba "confirmo" para confirmar el pago de su tarjeta de credito: ''')
#                                 if op4 == "confirmo":
#                                     deuda = deuda - pago
#                                     saldo = saldo - pago
#                                     print(f"La deuda de su tarjeta a sido pagada correctamente, su deuda a quedado en: ${deuda}")
#                                     print(f"El saldo restante en su cuenta corriente es de: ${saldo}")


#                                 else:
#                                     break

#                     case 2:
#                         print("----Cuenta Corriente----")
#                         print(f"Saldo Actual: ${saldo}")
#                         op5 = int(input('''Seleccione una opción:
#                                         1. Ver la ultima compra
#                                         2. Volver al menu'''))




#                     case 3:
#                         print("----Cuenta de Ahorro----")
#                         print(f"Saldo Actual: ${ahorro}")
#                         op6 = int(input('''Seleccione una opción: 
#                         1. Depositar monto
#                         2. Retirar monto
#                         3. Volver al menu'''))

#                         match op6:
#                             case 1:
#                                 deposito = int(input("Ingrese un monto a depositar: "))
#                                 if deposito <=0:
#                                     deposito = int(input("Ingrese un monto valido a depositar: "))
#                                     ahorro += deposito
#                                     print(f"El saldo de su cuenta de ahorro es: ${ahorro}")


#                             case 2:
#                                 retiro = int(input("Ingrese el monto a retirar: "))
#                                 if retiro <= 0:
#                                     retiro = int(input("Ingrese un monto valido a retirar: "))
#                                     ahorro = ahorro - retiro
#                                     print(f"El saldo de su cuenta de ahorro es: ${ahorro}")


#                             case 3:
#                                 print("Volviendo al menu...")
#                                 time.sleep (2)
#                                 break



#         else:
#             print("Datos incorrectos, intente nuevamente")
#             tries +=1



#----------------------------------------------------------------------------

# import random
# # with open('texto.txt', 'w') as writer:
# #     for aloooo in range (1, 5):
# #             writer.write('''
# # 1
# # 2
# # 3
# # 4
# # 5
# # ''')

# notas = []


# for i in range (1,4):

#     notas = random.randint(10, 70)


# print(notas)

#----------------------------------------------------------------------------
# import time
# from os import system

# lista = ['a', 'b', 'c','d']
# op1 = int
# op2 = int
# p_totales = len(lista)
# p_eliminados = int(0)
# p_added = int(0)
# p_last_added = int

# def add_product():
#     system("cls")
#     print(f"Numero actual de productos: {p_totales}")
#     lista.append(input("Producto a añadir: "))
#     p_added += 1
#     p_last_added = lista[p_totales]
#     print(f'''Se a añadido el producto "{p_last_added}" ''')
#     print("Volviendo al menu...")
#     time.sleep(1)
#     menu()

# def delete_product():
#     system("cls")
#     print(f"Productos actuales: {lista}")
#     print(f"Productos totales: {p_totales+1}")
#     op2 = int(input("Ingrese el producto que desea eliminar: "))
#     if op2 < p_totales+1 or op2 > p_totales+1:
#         print("No existe ese producto, Intente nuevamente.")
#         print("Volviendo al menu...")
#         time.sleep(1)
#         menu()

#     lista.pop(op2-1)
#     p_eliminados += 1
#     print(f"Se a eliminado exitosamente el producto {op2}")
#     print(f"Productos actuales: {lista}")
#     print("Volviendo al menu...")
#     time.sleep(2)
#     menu()


# def ver_productos():
#     system("cls")
#     print(f"Productos actuales: {lista}")
#     print("Volviendo al menu...")
#     time.sleep(1)
#     menu()




# def menu():
#     print('''Seleccione una opcion:
#         1. Añadir un producto
#         2. Eliminar un producto
#         3. Ver todos los productos
#         4. Salir''')
#     try:
#         op1 = int(input("Ingrese una opción: "))
#         match op1:
#             case 1:
#                 print("Cargando...")
#                 time.sleep(1)
#                 add_product()

#             case 2:
#                 print("Cargando...")
#                 time.sleep(1)
#                 delete_product()

#             case 3:
#                 print("Cargando...")
#                 time.sleep(1)
#                 ver_productos()

#             case 4:
#                 print("Saliendo...")
#                 time.sleep(1)
#     except Exception as Error:
#         print(f"Ocurrio un error inesperado: {Error}")
#         print("Intente nuevamente.")
#         menu()

# menu()

#----------------------------------------------------------------------------

# import time


# op1 = int
# op2 = int
# op3 = int
# nombre_completo = str

# nombres_completos = []
# nombres = []
# apellidos = []

# def nom_ape():
#     print("Ingreso de nombre y apellido (singular)")
#     nombre_completo = str(input("Ingrese nombre y apellido: "))
#     nombres_completos.append(nombre_completo)
#     print(f"a {nombres_completos}")
#     op2 = nombre_completo.split( )
#     nombre = op2[0]
#     apellido = op2[1]
#     nombres.append(nombre)
#     apellidos.append(apellido)
#     print(f"El nombre ingresado es: {nombre}")
#     print(f"El apellido ingresado es: {apellido}")
#     print("Volviendo al menu...")
#     time.sleep(1)
#     menu()
    

# def see_nom_apes():
#     print("Mostrando nombres y apellidos ingresados")
#     print(f"Nombres: {nombres}")
#     print(f"Apellidos: {apellidos}")
#     print("Volviendo al menu...")
#     time.sleep(1)
#     menu()
    

# def search_nom_apes():
#     print("Buscar nombre")
#     op3 = str(input("Ingrese el nombre a buscar: "))
#     if op3 in nombres:
#         print(f"El nombre {op3} si se encontro en la lista")
#     else:
#         print(f"El nombre {op3} no se encontro en la lista")
#     print("Volviendo al menu...")
#     time.sleep(1)
#     menu()



# def menu():
#     print('''Opciones:
#         1.Ingresar nombre y apellido
#         2.Mostrar nombres y apellidos
#         3.Buscar nombre
#         4.Salir
#         ''')
#     op1 = int(input("Seleccione una opcion: "))
#     match op1:
#         case 1:
#             print("Cargando...")
#             time.sleep(1)
#             nom_ape()

#         case 2:
#             print("Cargando...")
#             time.sleep(1)
#             see_nom_apes()
            

#         case 3:
#             print("Cargando...")
#             time.sleep(1)
#             search_nom_apes()

#         case 4:
#             print("Saliendo...")
#             time.sleep(3)





# menu()


#----------------------------------------------------------------------------

# import time
# import random

# op1 = int
# op2 = int
# op3 = int

# stock = [10, 10, 10, 20, 20, 20, 10, 5]
# stock_nom = ['Manzanas', 'Peras', 'Naranjas', 'Harina', 'Arroz', 'Atun', 'Coca-cola', 'Cinta-Adesiva']
# carrito = []
# boleta = []

# def comprar():
#     while True:
#         if len(carrito) == 0:
#             print("El carrito esta vacio")
#         else:
#             print(f"El carrito contiene {len(carrito)} productos")
#         print(f'''Opciones de compra:
#             1. Manzanas, stock: {stock[0]}
#             2. Peras, stock: {stock[1]}
#             3. Naranjas, stock: {stock[2]}
#             4. Harina, stock: {stock[3]}
#             5. Arroz, stock: {stock[4]}
#             6. Atun, stock: {stock[5]}
#             7. Coca-cola, stock: {stock[6]}
#             8. Cinta adesiva, stock: {stock[7]}''')
#         op2 = int(input("Ingrese una opcion, ingrese 0 para salir: "))
#         match op2:
#             case 0:
#                 print("Volviendo al menu...")
#                 time.sleep(2)
#                 menu()

#             case 1:
#                 print(f"Añadiendo 1 {stock_nom[0]} al carrito...")
#                 carrito.append(stock_nom[0])
#                 stock[0] -= 1

#             case 2:
#                 print(f"Añadiendo 1 {stock_nom[1]} al carrito")
#                 carrito.append(stock_nom[1])
#                 stock[1] -=1

#             case 3:
#                 print(f"Añadiendo 1 {stock_nom[2]} al carrito")
#                 carrito.append(stock_nom[2])
#                 stock[2] -= 1

#             case 4:
#                 print(f"Añadiendo 1 {stock_nom[3]} al carrito")
#                 carrito.append(stock_nom[3])
#                 stock[3] -= 1

#             case 5:
#                 print(f"Añadiendo 1 {stock_nom[4]} al carrito")
#                 carrito.append(stock_nom[4])
#                 stock[4] -= 1

#             case 6:
#                 print(f"Añadiendo 1 {stock_nom[5]} al carrito")
#                 carrito.append(stock_nom[5])
#                 stock[5] -= 1

#             case 7:
#                 print(f"Añadiendo 1 {stock_nom[6]} al carrito")
#                 carrito.append(stock_nom[6])
#                 stock[6] -= 1

#             case 8:
#                 print(f"Añadiendo 1 {stock_nom[7]} al carrito")
#                 carrito.append(stock_nom[7])
#                 stock[7] -= 1






# def menu():
#     print('''Bienvenido al carrito de compras, seleccione una opcion:
#         1. Ingresar productos
#         2. Comprar
#         3. Crear boleta
#         4. Salir''')
#     op1 = int(input("Seleccione una opcion: "))
#     match op1:
#         case 1:
#             print("Cargando...")
#             time.sleep(1)

#         case 2:
#             print("Cargando...")
#             time.sleep(1)
#             comprar()

#         case 3:
#             print("Cargando...")
#             time.sleep(1)

#         case 4:
#             print("Cargando...")
#             time.sleep(1)


# menu()

#----------------------------------------------------------------------------

# diccionario = {
#     "nombre":"kuek",
#     "numero":123456789,
#     "alo":True,
# }

# for key, value in diccionario.items():
#     print(f"{key}:{value}")


# diccionario["ciudad"]="Talca"

# for key, value in diccionario.items():
#     print(f"{key}:{value}")

#----------------------------------------------------------------------------

# frutas={
#     "manzana":1000,
#     "pera":1200,
#     "naranja":1300
# }

# op1 = input("Elija una fruta: ")

# op2 = frutas.get(op1)

# print(op2)

#----------------------------------------------------------------------------

# frutas={
#     "naranja":1200,
#     "pera":1200
# }

# op1 = input("Ingrese una fruta: ")
# op2 = int(input("Ingrese el precio: "))

# frutas[op1]=op2

# print(frutas)

#----------------------------------------------------------------------------
# import time

# carrito=[]
# total=0

# frutas={
#     "manzana":1000,
#     "pera":1200,
#     "naranja":1300,
#     "sandia":3000
# }


# def ingresar():
#     n_add = input("Ingrese el nombre de la fruta a ingresar: ")
#     p_add = int(input("Ingrese el precio de la fruta a ingresar: "))
#     frutas[n_add]=p_add
#     print(f"Se a añadido {n_add} a ${p_add} exitosamente")
#     print("Volviendo al menu...")
#     time.sleep(1)
#     menu()

# def actualizar_p():
#     n_edit=input("Ingrese el nombre de la fruta a actualizar: ")
#     p_edit=int(input(f"Ingrese el nuevo precio de {n_edit}: "))
#     frutas[n_edit]=p_edit
#     print(f"Se edito exitosamente el precio de {n_edit} a ${p_edit}")
#     print("Volviendo al menu...")
#     time.sleep(1)

# def borrar():
#     n_delete=input("Ingrese el nombre de la fruta a borrar: ")
#     del frutas[n_delete]
#     print(f"Se borro {n_delete} de las frutas")
#     print(f"La lista se a actualizado: {frutas}")
#     print("Volviendo al menu...")
#     time.sleep(1)
#     menu()

# def mostrar():
#     for key, value, i in frutas.items:
#         print(f"{i}. {key}, ${value}")
#     print("Volviendo al menu...")
#     time.sleep(1)
#     menu()

# def comprar():
#     global frutas, total
#     print("Bienvenido al menu de compras")
#     n_compra=input("Ingrese el nombre de la fruta que desea comprar: ")
#     precio= frutas.get(n_compra)
#     total += precio
#     carrito.append(n_compra)
#     print(f"Su carrito lleva: {carrito}")
#     print(f"Su total actual es de: {total}")
#     print("Volviendo al menu...")
#     time.sleep(1)
#     menu()







# def menu():
#     print('''Tienda de frutas:
#         1. Ingresar fruta y precio
#         2. Actualizar precio
#         3. Borrar fruta y precio
#         4. Mostrar todas las frutas y precios
#         5. Comprar
#         6. Salir''')
#     op1 = int(input("Ingrese su opción: "))
#     match op1:
#         case 1:
#             print("Cargando...")
#             time.sleep(1)
#             ingresar()

#         case 2:
#             print("Cargando...")
#             time.sleep(1)
#             actualizar_p()

#         case 3:
#             print("Cargando...")
#             time.sleep(1)
#             borrar()

#         case 4:
#             print("Cargando...")
#             time.sleep(1)
#             mostrar()

#         case 5:
#             print("Cargando...")
#             time.sleep(1)
#             comprar()

#         case 6:
#             print("Cargando...")
#             time.sleep(1)



# menu()

#----------------------------------------------------------------------------

# import time

# op1 = 0
# op2 = 0
# i = 0
# p_1 = 0

# dicc = {
#     "nombre":"Lapiz", "precio":100,
#     "nombre":"Goma", "precio":300
# }

# print(dicc)

# def agregar():
#     global i, op1, op2, p_1
#     print("Lista de objetos actual")
#     for nombre, precio in dicc.items():
#         if dicc["nombre"] == p_1:
#             break
#         i+= 1
#         print(f"{i}. {dicc["nombre"]}, ${dicc["precio"]}")
#         p_1=dicc["nombre"]
#     p_add = str(input("Ingrese el nombre del producto a agregar: "))
#     p_add_price = int(input("Ingrese el precio del producto a agregar: "))





# op1=(int(input('''
# Seleccione una opción:
# 1. Agregar articulo
# 2. Borrar Articulo
# 3. Actualizar Articulo
# 4. Mostrar listado de articulos
# 5. Salir''')))

# match op1:
#     case 1:
#         print("Cargando...")
#         agregar()

#     case 2:
#         print("Cargando...")

#     case 3:
#         print("Cargando...")

#     case 4:
#         print("Cargando...")

#     case 5:
#         print("Cargando...")


#----------------------------------------------------------------------------

import random, time
p_valida = None
code_last = 15

todo = {
    'obj1':{
        "nombre": "kuek",
        "precio":58000,
        "code":15
    },
    'obj2':{
        "nombre": "lel",
        "precio": 1000,
        "code": 12
    },
    'obj3':{
        'nombre':"alo",
        "precio":500,
        "code":19
    }
}

# valor1 = todo['obj1']['nombre']
# precio1 = todo['obj1']['precio']
# valor2 = todo['obj2']['nombre']
# print(valor1)

# for i in range (len(todo)):
#     valor_n = todo[f'obj{i+1}']['nombre']
#     valor_p = todo[f'obj{i+1}']['precio']
#     valor_c = todo[f'obj{i+1}']['code']
#     print(f"{i+1}.{valor_n}: ${valor_p}, {valor_c}")
def ver_objs():
    print("Objetos en el diccionario:")
    for i in range (len(todo)):
        value_n = todo[f'obj{i+1}']['nombre']
        value_p = todo[f'obj{i+1}']['precio']
        value_c = todo[f'obj{i+1}']['code']
        print(f"{i+1}.{value_n}: ${value_p}, {value_c}")
    print("Volviendo al menu...")
    time.sleep(1)
    menu()

def add_objs():
    print("Añadir objetos")
    print("Objetos actuales:")
    for i in range (len(todo)):
        value_n = todo[f'obj{i+1}']['nombre']
        value_p = todo[f'obj{i+1}']['precio']
        value_c = todo[f'obj{i+1}']['code']
        print(f"{i+1}.{value_n}: ${value_p}, {value_c}")
    add_n = str(input("Ingrese el nombre del objeto a añadir: "))
    add_p = int(input("Ingrese el precio del objeto a añadir: "))
    add_code = code_last+1
    code_last += 1
    

    



def menu():
    print('''Menu
          1. Ver Objetos en el diccionario
          2. Añadir objetos
          3. Eliminar objetos
          4. Editar objetos
          5. Salir''')
    op1 = int(input("Ingrese una opcion: "))
    match op1:
        case 1:
            print("Cargando...")
            ver_objs()

        case 2:
            print("Cargando...")

        case 3:
            print("Cargando...")

        case 4:
            print("Cargando...")

        case 5:
            print("Saliendo...")
            time.sleep(2)


def login():
    global user, passw
    Mayuscula = None
    Minuscula = None
    Numero = None
    user = input("Ingrese usuario a crear: ")
    passw = input("Ingrese contraseña a crear: ")
    for palabra in passw:
        if palabra.isupper():
            Mayuscula = True
        if palabra.islower():
            Minuscula = True
        if palabra.isdigit():
            Numero = True

    if Numero == True and Mayuscula == True and Numero == True:
        p_valida == True
        print("Su contraseña es valida para ingreso")
        print("Cargando...")
    else:
        print("Su contraseña no es valida para el ingreso, intente nuevamente.")

login()