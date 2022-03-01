import sqlite3
import time
import os
from datetime import date, timedelta
from datetime import datetime


def cobranzas(usuario, asegurado):
	import conexiones
	lista_cobros = conexiones.conexion_pagos()
	cont = 1
	cuota = ""
	print("***************************************************")
	print("HISTORICO DE PAGOS")
	print("***************************************************")
	print("")
	
	#Conteo y muestra de los pagos realizados
	for pagos in lista_cobros:
		if asegurado[0][10]==pagos[5]:
			print("CUOTA "+str(cont)+ " PAGO REALIZADO EL DIA: "+str(pagos[0])+ " pago $" + str(pagos[6]) )
			print("")
			cont = cont+1
			cuota = str(pagos[6])
	opcion = input("REALIZAR PAGO CUOTA "+str(cont)+ " POR : $" + cuota +" INGRESE 'S' PARA REALIZAR EL PAGO O ENTER PARA VOLVER: ")
	opcion = opcion.upper()
	
	#Carga de pago en base de datos
	if opcion == "S":
		today = date.today()
		td = timedelta()
		import conexiones
		conexiones.acciones_pagos('''INSERT INTO PAGOS1 (FECHA, EMPLEADO, NOMBRES, APELLIDOS, DNI, PATENTE, CUOTA)VALUES('%s','%s','%s','%s','%s','%s','%s')''' %(str(today+td), usuario.upper(),asegurado[0][3].upper(),asegurado[0][4].upper(),asegurado[0][5].upper(),asegurado[0][10].upper(),cuota))
		
		
		#Intentamos calcular el vuelto, es solo una ayuda para el empleado
		cuota = int(pagos[6])
		try:
			pago = int(input("INGRESE LA CANTIDAD DE DINERO QUE RECIBE: $"))
		except:
			print("DEBE INGRESAR EL MONTO QUE RECIBIO PARA EL PAGO, CALCULE USTED EL VUELTO POR FAVOR")
		try:
			print("DEVUELVA: $", (pago-cuota))
		except:
			print("NO SE PUDO CALCULAR EL VUELTO,")	
		time.sleep(5)
		print("PAGO CARGADO CON EXITO, VOLVIENDO AL MENU")
		
		#Preparamos el comprobante de pago y los datos necesarios para el envio del mail
		import comprobante_pagos
		adjunto = comprobante_pagos.generar_comprobante(asegurado[0][3],asegurado[0][4],asegurado[0][5],asegurado[0][7],asegurado[0][8],asegurado[0][10],asegurado[0][0],asegurado[0][15],str(today),str(cont))
		time.sleep(2)
		
		
		#Creamos la proxima fecha de pago dependiendo de la cantidad de cuotas pagas
		import enviar_mail
		today = date.today()
		td = timedelta()
		mail = str(asegurado[0][6])
		nombre = asegurado[0][3]
		fecha_inicio = asegurado[0][1]
		proxima_fecha = datetime.strptime(fecha_inicio, '%Y-%m-%d')
		cont_suma = 30*cont
		proxima_fecha_pago = proxima_fecha+timedelta(cont_suma)
		time.sleep(5)
		msj = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())+"...........HOLA "+nombre + ",SU PAGO POR $"+str(asegurado[0][15])+" CORRESPONDIENTE A LA CUOTA "+str(cont)+" FUE REGISTRADO CON EXITO \nPROXIMA FECHA DE PAGO "+str(proxima_fecha_pago)+" \nGRACIAS POR CONFIAR EN SEGUROS UNAJ \nSALUDOS ATTE." 
		
		#Envio mail
		enviar_mail.envio_mail_adjunto(mail,msj,"PAGO REGISTRADO", adjunto,"COMPROBANTE DE PAGO")
		time.sleep(2)
		os.system("cls")
		
		#Vuelve al menu
		import menu_asegurados
		menu_asegurados.opciones_menu(usuario,asegurado)
	else:
		#Vuelve al menu
		os.system("cls")
		import menu_asegurados
		menu_asegurados.opciones_menu(usuario,asegurado)
