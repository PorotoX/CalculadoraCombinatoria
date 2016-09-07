# -*- coding: UTF-8 -*-

#CALCULADORA DE ARREGLOS, PERMUTACIONES Y COMBINACIONES
#Obligatorio - Probabilidad y Estadística - Prof.: Álvaro Núñez - Ce.R.P. - 2016
#Integrantes: Alicia Ronzoni - Gianna Giupponi - Jorge (Poroto) Ferreira
#Desarrollado en Python 3.4.3

import os, sys
from itertools import *
opcion = -1
autores = "\nAutores: Alicia Ronzoni, Gianna Giupponi y Jorge Ferreira\n\n"
os.system("title Calculadora de Arreglos, Permutaciones y Combinaciones") #Título de la ventana

def limpiar():
	sistema = os.name

	#Limpia pantalla tanto en Linux como Windows
	if sistema == "nt":
		return os.system("cls")
	else:
		return os.system("clear")

def volver():
	return input("\nPresione Enter para volver al Menú Principal")

def factorial(x, n): #Cálculo de factorial recursivo
	if(n>0):
		x = factorial(x, n-1)
		x = x * n
	else:
		x = 1
	return x

def cargar_elementos(items):
	for i in range(len(items)):
		items[i] = input("Ingrese elemento " + str(i+1) + ": ")

def mostrar_arreglos():
	i = 1
	m = int(input("Indique cantidad de datos a ingresar: M="))
	print("") #Salto de línea luego de ingresada cantidad

	elementos = [0 for i in range(m)]
	cargar_elementos(elementos)

	n = int(input("\nIndique cantidad de elementos a seleccionar (N < M): N="))
	while(n >= m): #No permite seguir el programa hasta que no se ingrese un N menor a M
		n = int(input("¡N DEBE SER MENOR A M! \nReingrese cantidad de elementos a seleccionar (N < M): N="))

	print("\nCantidad de Arreglos (Am/n):", int(factorial(1, m) / factorial(1, m - n)), "\n") #Am/n = m! / (m - n)! - Arreglo de M elementos, tomados de a N - importa el orden

	for elementos in permutations(elementos, n):
		print(str(i) + ")", elementos)
		i += 1

def mostrar_combinaciones():
	i = 1
	m = int(input("Indique cantidad de datos a ingresar: M="))
	print("") #Salto de línea luego de ingresada cantidad

	elementos = [0 for i in range(m)]
	cargar_elementos(elementos)

	n = int(input("\nIndique cantidad de elementos a seleccionar (N < M): N="))
	while(n >= m): #No permite seguir el programa hasta que no se ingrese un N menor a M
		n = int(input("¡N DEBE SER MENOR A M! \nReingrese cantidad de elementos a seleccionar (N < M): N="))

	print("\nCantidad de Combinaciones (Cm/n):", int(factorial(1, m) / (factorial(1, n) * factorial(1, m - n))), "\n") #Cm/n = m! / (n!*(m - n)!) - Combbinación de M elementos, tomados de a N - no importa el orden

	for elementos in combinations(elementos, n):
		print(str(i) + ")", elementos)
		i += 1

def permutaciones(n, i):
    if i == len(n) - 1:
        print(n)
    else:
        for j in range(i, len(n)):
            n[i], n[j] = n[j], n[i]
            permutaciones(n, i + 1)
            n[i], n[j] = n[j], n[i] #Intercambiar denuevo para la próxima iteración

def mostrar_permutaciones():
	i = 1
	p = int(input("Indique cantidad de datos a ingresar: n="))
	print("") #Salto de línea luego de ingresada cantidad

	elementos = [0 for i in range(p)]
	cargar_elementos(elementos)

	print("\nCantidad de Permutaciones (Pn):", factorial(1, p), "\n") #P! - Prmutación: Arreglo de todos los elementos, tomados de a todos - importa el orden
	permutaciones(elementos, 0)

while opcion != 0:
	limpiar()
	print("Bienvenido a Programa Combinatorio!", autores)
	print("Digite su opción y presione Enter: \n\n 1. Arreglos \n 2. Combinaciones \n 3. Permutaciones \n 0. Salir")

	try:
		opcion = int(input())

		if opcion == 1:
			limpiar()
			print("Cálculo de Arreglos", autores)
			mostrar_arreglos()
			volver()
		elif opcion == 2:
			limpiar()
			print("Cálculo de Combinaciones", autores)
			mostrar_combinaciones()
			volver()
		elif opcion == 3:
			limpiar()
			print("Cálculo de Permutaciones", autores)
			mostrar_permutaciones()
			volver()

	except:
		print("Ingreso de dato inválido")
		volver()
