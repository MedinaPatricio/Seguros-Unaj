import sqlite3
import time
import os
import conexiones
import baja_seguro
import opciones_envio_mail
import cobrar_cuota
import menu_principal
from datetime import datetime
from datetime import date, timedelta

listaitem =["POLIZA","FECHA","EMPLEADO","NOMBRE", "APELLIDO", "DNI", "MAIL", "MARCA", "MODELO", "TIPO", "PATENTE", "AÑO", "CHASIS", "MOTOR", "VALUACION","CUOTA"]

def mostrar_datos(usuario,asegurado): #Cambia el mail del asegurado
		contador = 0
		if len(asegurado) == 1:
			for dato in asegurado[0]:
				print(listaitem[contador]+" :"+ str(dato))
				contador = contador + 1
		opcion = input ("'S' PARA MODIFICAR MAIL O CUALQUIER TECLA PARA VOLVER: ")
		opcion = opcion.upper()
		
		if opcion != "S":
			os.system("cls")
			opciones_menu(usuario,asegurado)
		else:
			nuevo_mail = input("INGRESE EL NUEVO MAIL: ")
			while len(nuevo_mail) == 0:
				nuevo_mail = input("INGRESE EL NUEVO MAIL: ")
			
			conexiones.acciones_asegurados('''UPDATE ASEGURADOS1 SET MAIL =('%s') WHERE POLIZA =('%s')''' %(nuevo_mail, asegurado[0][0]))
			print("MAIL ACTUALIZADO")
			print("VOLVIENDO AL MENU PRINCIPAL")
			time.sleep(2)
			os.system("cls")
			import menu_principal
			menu_principal.menu(usuario)


def opcion_seleccionada(usuario,asegurado,opcion):
	if opcion == "0":
		os.system("cls")
		import menu_principal
		menu_principal.menu(usuario)
	elif opcion == "1":
		mostrar_datos(usuario,asegurado)
	elif opcion == "2":
		
		baja_seguro.baja(usuario, asegurado)
	elif opcion == "3":
		
		opciones_envio_mail.opciones_mail(usuario,asegurado)
	elif opcion == "4":
		
		cobrar_cuota.cobranzas(usuario,asegurado)

#Menu del asegurado
def opciones_menu(usuario, asegurado):
		
	print("Usuario: " + usuario.upper() + ", Bienvenido..... ASEGURADO: "+asegurado[0][4]+" "+ asegurado[0][3] + " POLIZA: " + asegurado[0][0])
	print("**********************************************")
	print(" seleccione una opcion")
	print("")
	print("1. VER/MODIFICAR MAIL".rjust(28) + "2. BAJA DE SEGURO".rjust(31))
	print("")
	print("3. ENVIAR MAIL".rjust(21) + "4. COBRAR/PAGOS REALIZADOS".rjust(47))
	print("")
	print("")
	opcion = input("SELECCIONE UNA OPCION O 0 PARA VOLVER: ")
	while opcion not in "012345" or opcion == "":
		os.system("cls")
		print("OPCION INCORRECTA, POR FAVOR INGRESE SOLO EL NUMERO DE LA OPCION DESEADA O 0 PARA CERRAR")
		print("")
		opciones_menu(usuario,asegurado)
		opcion = input("SELECCIONE UNA OPCION O 0 PARA CERRAR: ")
	opcion_seleccionada(usuario,asegurado,opcion)

def menu_asegurado(usuario):
	import conexiones
	lista_asegurado = conexiones.conexion_asegurados()
	buscar_asegurado = input("INGRESE EL DNI DEL ASEGURADO O 0 PARA VOLVER: ")
	while buscar_asegurado == "":
		print("POR FAVOR INGRESE EL DNI DEL ASEGURADO")
		buscar_asegurado = input("INGRESE EL DNI DEL ASEGURADO O 0 PARA VOLVER: ")
	
	if buscar_asegurado == "0":
		os.system("cls")
		import menu_principal
		menu_principal.menu(usuario)
		
	asegurado_list = []
	for asegurado in lista_asegurado:
		if buscar_asegurado == asegurado[5]:
			asegurado_list.append(asegurado)
			
	if asegurado_list == []:
		os.system("cls")
		print("No se ha encontrado al asegurado, vuelva a intentar")
		menu_asegurado(usuario)	
		
	elif len(asegurado_list) > 1:
		print("POSEE MAS DE UN VEHICULO")
		
		lista_asegurado = []
		for autos in asegurado_list:
			print("POLIZA: "+autos[0]+" MARCA: "+autos[7]+ " MODELO: "+autos[8]+" PATENTE: "+autos[10])
		seleccion=input("ESCRIBA EL NUMERO DE POLIZA QUE DESEA VERIFICAR: ")
		error=0
		
		for vehiculo in asegurado_list:
			if seleccion == vehiculo[0]:
				lista_asegurado.append((vehiculo))
				error = error+1
				
		if error == 0:
			os.system("cls")
			print("LA POLIZA SELECCIONADA NO EXISTE, VUELVA A INTENTARLO Y LEA ATENTAMENTE!")
			import menu_principal
			menu_principal.menu(usuario)
		os.system("cls")
		opciones_menu(usuario,lista_asegurado)
		
	else:
		os.system("cls")
		opciones_menu(usuario, asegurado_list)	
