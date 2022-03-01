import sqlite3
import time
import os
from datetime import date, timedelta
from datetime import datetime



def enviar_pagos(usuario,asegurado):
	import enviar_mail
	today = date.today()
	td = timedelta()
	fecha_inicio = asegurado[0][1]
	formato_fecha = datetime.strptime(fecha_inicio, '%Y-%m-%d')
	import conexiones
	lista_cobros = conexiones.conexion_pagos()
	# ~ conexion = sqlite3.connect("pagos1")
	# ~ cursor = conexion.cursor()
	# ~ lista_cobros = cursor.execute("SELECT * FROM PAGOS1")
	# ~ conexion.commit()
	# ~ lista_cobros = lista_cobros.fetchall()
	# ~ conexion.close()
	cuota = ""
	lista_pagos = []
	for pagos in lista_cobros:
		if asegurado[0][10]==pagos[5]:
			lista_pagos.append(pagos)
	contador = len(lista_pagos)
	contador = int(contador)
	contador2 = contador*30
	proximo_vencimiento = formato_fecha+timedelta(contador2)
	pago = formato_fecha
	lista = asegurado
	mensaje = "BIENVENIDE " + str(lista[0][4]) + " A SEGUROS UNAJ, \nSU NUMERO DE POLIZA ES: " + str(lista[0][0]) +  "\nLA CUOTA PARA EL VEHICULO " + str(lista[0][7]) +" "+ str(lista [0][8]) +" ES DE $" + str(lista [0][15])+" MENSUALES "+" \nCUOTAS PAGAS A LA FECHA "+ str(contador)+" \nVENCIMIENTOS TOTAL DEL CONTRATO ANUAL: \n" + str(pago+timedelta(30))+  "\n" + str(pago+timedelta(90)) + "\n" + str(pago+timedelta(120)) + "\n" + str(pago+timedelta(150)) + "\n" + str(pago+timedelta(180))  +  "\n" + str(pago+timedelta(210))  +  "\n" + str(pago+timedelta(240)) +  "\n" + str(pago+timedelta(270))  +  "\n" + str(pago+timedelta(300)) +  "\n" + str(pago+timedelta(330))+ "\n" + str(pago+timedelta(360)) + "\n SU PROXIMA FECHA DE PAGO ES *******" + str(proximo_vencimiento)+"*********" 
	print("********************************************************************")
	print("CUOTAS PAGAS A LA FECHA "+ str(contador)+" \nVENCIMIENTOS TOTAL DEL CONTRATO ANUAL: \n" + str(pago+timedelta(30))+  "\n" + str(pago+timedelta(90)) + "\n" + str(pago+timedelta(120)) + "\n" + str(pago+timedelta(150)) + "\n" + str(pago+timedelta(180))  +  "\n" + str(pago+timedelta(210))  +  "\n" + str(pago+timedelta(240)) +  "\n" + str(pago+timedelta(270))  +  "\n" + str(pago+timedelta(300)) +  "\n" + str(pago+timedelta(330))+"\n" + str(pago+timedelta(360))+ "\n SU PROXIMA FECHA DE PAGO ES *******" + str(proximo_vencimiento)+"*********")
	
	opcion_enviar = input("ENVIAR INFORMACION POR MAIL? 'S' PARA SI O CUALQUEIR TECLA PARA VOLVER: ")
	opcion_enviar = opcion_enviar.upper()
	if opcion_enviar == "S":
		enviar_mail.envio_mail(str(lista[0][6]),mensaje,"INFORMACION")
		time.sleep(4)
		os.system("cls")
		import menu_asegurados
		menu_asegurados.opciones_menu(usuario,asegurado)
	else:
		os.system("cls")
		import menu_asegurados
		menu_asegurados.opciones_menu(usuario,asegurado)


def enviar_personalizado(usuario,asegurado):
	print("******************************************")
	print("ENVIAR MENSAJE A " + asegurado [0][6])
	asunto = input("INGRESE EL ASUNTO O 0 PARA VOLVER: ")
	
	while len(asunto) == 0:
		print("DEBE INGRESAR UN ASUNTO")
		asunto = input("INGRESE EL ASUNTO O 0 PARA VOLVER: ")
	if asunto == "0":
		os.system("cls")
		import menu_asegurados
		menu_asegurados.opciones_menu(usuario,asegurado)	
	mensaje = input("INGRESE EL MENSAJE O 0 PARA VOLVER: ")
	
	while len(mensaje) == 0:
		print("DEBE INGRESAR UN MENSAJE")
		mensaje = input("INGRESE EL MENSAJE O 0 PARA VOLVER: ")
	if mensaje == "0":
		os.system("cls")
		import menu_asegurados
		menu_asegurados.opciones_menu(usuario,asegurado)	
	asunto = asunto.upper()
	mensaje = mensaje.upper()
	import enviar_mail
	enviar_mail.envio_mail(str(asegurado[0][6]),mensaje,asunto)
	time.sleep(4)
	os.system("cls")
	import menu_asegurados
	menu_asegurados.opciones_menu(usuario,asegurado)
	






def opciones_mail(usuario,asegurado):
	print("********************************************************************************************")
	print("")
	print("1. ENVIAR PAGOS REALIZADOS Y FECHAS DE VENCIMIENTOS" + "        2. MENSAJE PERSONALIZADO")
	print("")
	opcion = input("INGRESE UNA OPCION o 0 PARA VOLVER: ")
	while opcion not in ("12") or opcion == "":
		print("OPCION INCORRECTA")
		if opcion == "0":
			os.system("cls")
			import menu_asegurados
			menu_asegurados.opciones_menu(usuario,asegurado)
		opcion = input("INGRESE UNA OPCION o 0 PARA VOLVER: ")
	if opcion == "1":
		enviar_pagos(usuario, asegurado)
	elif opcion == "2":
		enviar_personalizado(usuario,asegurado)
