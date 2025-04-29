# voto = int(0)
# op1 = int(0)
# p1 = str("Piñera")
# op2 = int(0)
# p2 = str("Bachelet")
# op3 = int(0)
# p3 = str("Nulo")
# win = int(1)
# winner = str("Nadie")
# votantes = int(input("Ingrese numero de votantes: "))

# for i in range (0, votantes):
#     voto = int(input("1. Piñera, 2. Bachelet, Cualquier otra opcion cuenta como nulo: "))
#     if voto == 1:
#         op1 +=1
#     elif voto == 2:
#         op2 +=1
#     else:
#         op3 +=1

# if op1>op2:
#     winner = p1
# elif op1<op2:
#     winner = p2
# elif op1==op2:
#     win = 0

# print("Fin de las elecciones")
# print("La cantidad de votos totales es:", votantes)
# if win==0:
#     print("Las elecciones terminaron en empate")
# else:
#     print("El ganador de las elecciones fue:", winner)

# print("La cantidad de votos nulos fue:", op3)

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




