
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

sub_prom = float(0)
prom = float(0)
prom_seccion = float(0)
n_actual = 0
a_actual = 0
a_aprueban = int(0)
a_reprueban = int(0)
print("Bienvenido al sistema de notas")
n_alumnos = int(input("Ingrese la cantidad de alumnos de la sección: "))
while a_actual < n_alumnos:
    for h in  range (0, n_alumnos):
        n_notas = int(input(f"Ingrese la cantidad de notas del alumno {h+1}: "))
        for i in range (0, n_notas):
            sub_prom += float(input(f"Ingrese la nota {i+1} del alumno {h+1}: "))
            prom = sub_prom/(i+1)

        prom_seccion += prom
        print(f"El promedio del alumno {h+1} es de: {prom}")
        if prom < 4:
            print(f"El alumno {h+1} reprobo con un: {prom}")
            a_reprueban += 1

        else:
            print(f"El alumno {h+1} aprobo con un: {prom}")
            a_aprueban += 1
        prom = 0

print(f"El promedio de la seccion fue de: {prom_seccion}")
print(f"La cantidad de alumnos que aprobaron fue de: {a_aprueban} ")
print(f"La cantidad de alumnos que reprobo fue de: {a_reprueban}")