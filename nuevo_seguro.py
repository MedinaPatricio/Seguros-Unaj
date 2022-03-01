import os
import sqlite3
import time
from datetime import datetime
from datetime import date, timedelta

def error_carga(lista, lista1, usuario):
	for i in lista:
		print("NOTA: EN CASO DE NO POSEER EL SIGUIENTE ITEM, INGRESE CUALQUIER DATO PARA CONTINUAR CON LA CARGA Y NO GUARDARLA AL FINAL DEL PROCESO")
		error1 = input("Corrija el item"+ str(i) + ": ")
		i = int(i)
		lista1[0][i-1] = error1.upper()	
	lista_corregida = lista1
	verificar(lista_corregida, usuario)	

def verificar(lista,usuario): #crea lista con errores(campos en blanco) en caso de encontrar, solicita el nuevo ingreso de ese dato para poder completar la lista final.
	listaitem =["[1]NOMBRE", "[2]APELLIDO", "[3]DNI", "[4]MAIL", "[5]MARCA", "[6]MODELO", "[7]TIPO", "[8]PATENTE", "[9]AÑO", "[10]CHASIS", "[11]MOTOR", "[12]VALUACION"]
	print("USUARIO: " + usuario.upper())
	for asegurado in lista:
		os.system("cls")
		cont = 0
		lista_errores = []
		print("")
		print("--------------------------------")
		print("POR FAVOR, VERIFIQUE LOS DATOS")
		error = 0
		for i in asegurado:
			cont = cont + 1
			if i == "":
				error = error + 1
				lista_errores.append(cont)
				print("Error en ITEM : " + listaitem[cont-1])
			else:
				print (listaitem[cont-1] +" = "+ str(i))

	if error == 0:
		cuota = lista[0][11]*0.1/13
		cuota = int(cuota)
		print("*****************************************************************************")
		print("")
		print("*****************************************************************************")
		print("CONTRATO ANUAL, LA CUOTA MENSUAL PARA " + lista[0][0].upper() +" "+ lista[0][1].upper() + " ES DE:****** $" +str(cuota)+"****** MENSUALES")
		today = date.today()
		td = timedelta(30)
		pago = today+td
		print("PROXIMA FECHA DE PAGO: " + str(pago))
		print("VENCIMIENTO: " + str(pago+timedelta(10)))
		print('"ATENCION", CONFIRME LOS DATOS DESPUES DE RECIBIR EL PAGO DE LA PRIMERA CUOTA')
		print("NOTA: SI TUVO ALGUN DATO FALTANTE, LE ROGAMOS QUE NO CONFIRME LOS DATOS PARA EVITAR FUTUROS PROBLEMAS CON EL ASEGURADO")
		confirmar = input("CONFIRMAR DATOS? S/SI -- N/NO : ")
		confirmar = confirmar.upper()
		while confirmar not in "SN":
			print("OPCION INCORRECTA, INGRESE 'S' PARA SI O 'N' PARA NO")
			confirmar = input("CONFIRMAR DATOS? S/SI -- N/NO : ")
			confirmar = confirmar.upper()
		if confirmar == "S": #Procedemos con la carga del seguro
			import conexiones
			poliza_asegurado = conexiones.conexion_asegurados()
			poliza = poliza_asegurado[-1][0]
			poliza = int(poliza)
			nueva_poliza = poliza + 1 #toma el ultimo numero de poliza cargado y le suma 1 para que no se repita
			today = date.today()
			td = timedelta()
			import conexiones
			conexiones.acciones_asegurados('''INSERT INTO ASEGURADOS1 (POLIZA, FECHA, EMPLEADO, NOMBRES, APELLIDOS, DNI, MAIL, MARCA, MODELO,TIPO, PATENTE, AÑO, CHASIS, MOTOR, VALUACION, CUOTA)VALUES('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')''' %(str(nueva_poliza),today+td, usuario.upper(),lista[0][0],lista[0][1],lista[0][2].upper(),lista[0][3],lista[0][4],lista[0][5],lista[0][6],lista[0][7].upper(),lista[0][8],lista[0][9],lista[0][10],lista[0][11],cuota))
			import conexiones
			conexiones.acciones_pagos('''INSERT INTO PAGOS1 (FECHA, EMPLEADO, NOMBRES, APELLIDOS, DNI, PATENTE, CUOTA)VALUES('%s','%s','%s','%s','%s','%s','%s')''' %(str(today+td), usuario.upper(),lista[0][0].upper(),lista[0][1].upper(),lista[0][2].upper(),lista[0][7].upper(),cuota))
			mensaje_poliza = "BIENVENIDX " + str(lista[0][0]) + " A SEGUROS UNAJ, \nSU NUMERO DE POLIZA ES: " + str(nueva_poliza) +  "\nLA CUOTA PARA EL VEHICULO " + str(lista[0][4]) +" "+ str(lista [0][5]) +" ES DE $" + str(cuota)+" MENSUALES "+" \nAGENDE SUS PROXIMAS FECHAS DE PAGO Y RECUERDE QUE EL SEGUNDO VENCIMIENTOS DE CADA CUOTA ES A LOS 10 DIAS CORRIDOS POSTERIORES:   \n" + str(pago) + " CUOTA: $" +str(cuota) +  "\n" + str(pago+timedelta(30)) + " CUOTA: $" +str(cuota) +  "\n" + str(pago+timedelta(90)) + " CUOTA: $" +str(cuota)+  "\n" + str(pago+timedelta(120)) + " CUOTA: $"+ str(cuota) +  "\n" + str(pago+timedelta(150)) + " CUOTA: $" +str(cuota) +  "\n" + str(pago+timedelta(180)) + " CUOTA: $" +str(cuota) +  "\n" + str(pago+timedelta(210)) + " CUOTA: $" +str(cuota) +  "\n" + str(pago+timedelta(240)) + " CUOTA: $"+ str(cuota) +  "\n" + str(pago+timedelta(270)) + " CUOTA: $" +str(cuota) +  "\n" + str(pago+timedelta(300)) + " CUOTA: $" +str(cuota) +  "\n" + str(pago+timedelta(330)) + " CUOTA: $" +str(cuota)
			mensaje_pago = str(lista[0][0])+ "!, TE DEJAMOS POR AQUI TU COMPROBANTE DE PAGO \nSALUDOS ATTE." 
			destinatario = str(lista[0][3])
			import comprobante_pagos
			comprobante = comprobante_pagos.generar_comprobante(str(lista[0][1]),str(lista[0][0]),str(lista[0][2]),str(lista[0][4]),str(lista[0][5]),str(lista[0][7]),str(poliza),str(cuota),str(today+td),"1")
			import generar_poliza
			poliza_asegurado = generar_poliza.generar_poliza_seguro(str(lista[0][1]),str(lista[0][0]),str(lista[0][2]),str(lista[0][4]),str(lista[0][5]),str(lista[0][7]),str(poliza),str(cuota),str(today+td),"1")
			import enviar_mail
			enviar_mail.envio_mail_adjunto(destinatario,mensaje_poliza,"BIENVENIDO A SEGUROS UNAJ", poliza_asegurado, "POLIZA")
			enviar_mail.envio_mail_adjunto(destinatario,mensaje_pago,"COMPROBANTE DE PAGO", comprobante,"COMPROBANTE DE PAGO")
			print("NUEVO ASEGURADO GUARDADO CON EXITO")
			print("VOLVIENDO AL MENU")
			time.sleep(4)
			os.system("cls")
			import menu_principal
			menu_principal.menu(usuario)
		else:
			os.system("cls")
			import menu_principal
			menu_principal.menu(usuario)
	else:
		
		print("*****************************************************************************")
		print("POR FAVOR CORRIJA EL/LOS SUGUIENTE/S DATO/S, DE LO CONTRARIO NO PODREMOS CONTINUAR CON LA CARGA")
		print("*****************************************************************************")
		error_carga(lista_errores,lista, usuario)


def ingreso_seguro(usuario):
	print(usuario.upper())
	lista_asegurados = []
	print("NUEVO SEGURO".rjust(48))
	print("")
	nombre = input("[1]NOMBRE: ")
	apellido = input("[2]APELLIDO: ")
	dni = input("[3]DNI (sin puntos): ")
	mail = input("[4]MAIL : ")
	marca = input("[5]MARCA: ")
	modelo = input("[6]MODELO: ")
	tipo = input("[7]TIPO (AUTO-CAMIONETA): ")
	patente = input("[8]PATENTE (SIN GUION): ")
	patente = patente.upper()
	import conexiones
	usuarios = conexiones.conexion_asegurados()
	for asegurado in usuarios: #verifica que la pantete no exista en la base de datos, la pantente se utiliza para calular los pagos y cobros.
		while patente == asegurado[10]: 
			print("LA PATENTE INGRESADA CORRESPONDE A OTRO VEHICULO")
			patente = input("[8]PATENTE (SIN GUION): ")
			patente = patente.upper()
	anio = input("[9]AÑO: ")
	chasis = input("[10CHASIS: ")
	motor = input("[11]MOTOR: ")
	try: # se le da 3 oportunidades para que ingrese solo numeros y por seguridad vuelve.
		valuacion = int(input("[12]VALUACION (SOLO NUMEROS SIN PUNTOS):$ "))
	except ValueError:
		print("POR FAVOR! INGRESE SOLO NUMEROS")
		
		try:
			valuacion = int(input("[12]VALUACION (SOLO NUMEROS SIN PUNTOS):$ "))
		except ValueError:
			print("POR FAVOR! INGRESE SOLO NUMEROS !!!!!!!!ULTIMO INTENTO¡¡¡¡¡¡¡¡")
			
			try:
				valuacion = int(input("[11]VALUACION (SOLO NUMEROS SIN PUNTOS):$ "))
			except ValueError:
				os.system("cls")
				print("*************************************************************************************************************")
				print("EXCEDIO EL NUMERO DE INTENTOS, LA VALUACION DEBE SER SOLO NUMERICA, POR SU SEGURIDAD VUELVA A INTENTARLO.")
				print("*************************************************************************************************************")
				print("LOS DATOS INGRESADOS ANTERIORMENTE NO HAN SIDO GUARDADOS")
				print("*************************************************************************************************************")
				import menu_principal
				menu_principal.menu(usuario)
	lista_asegurados.append([nombre.upper(),apellido.upper(),dni,mail,marca.upper(),modelo.upper(),tipo.upper(),patente.upper(),anio,chasis.upper(),motor.upper(),valuacion])
	verificar(lista_asegurados, usuario)


def aviso(usuario): #1 AVISO solo se puede generar una seguro nuevo solo si poseen todos los datos que se muestran
	print(usuario.upper() + " BIENVENIDO A LA SECCION NUEVO SEGURO")
	print("")
	print("AVISO IMPORTANTE!! ANTES DE CONTINUAR VERIFIQUE QUE POSEE TODOS LOS DATOS REQUERIDOS PARA EL NUEVO SEGURO")
	print("")
	print("***********************************************************************************************************")
	print("")
	print("[1]NOMBRE")
	print("[2]APELLIDO")
	print("[3]DNI")
	print("[4]MAIL")
	print("[5]MARCA")
	print("[6]MODELO")
	print("[7]TIPO (AUTO-CAMIONETA)")
	print("[8]PATENTE")
	print("[9]AÑO")
	print("[10]CHASIS")
	print("[11]MOTOR")
	print("[12]VALUACION")
	print("")
	opcion = input(usuario.upper() + " DESEA CONTINUAR? PARA SI INGRESE 'S', PARA VOLVER INGRESE 'N' : ")
	opcion = opcion.upper()
	while opcion not in "SN" or opcion == "":
		print("OPCION INCORRECTA")
		opcion = input(usuario.upper() + " DESEA CONTINUAR? PARA SI INGRESE 'S', PARA VOLVER INGRESE 'N' : ")
		opcion = opcion.upper()
	if opcion == "S":
		os.system("cls")
		ingreso_seguro(usuario)
	else:
		os.system("cls")
		import menu_principal
		menu_principal.menu(usuario)	


