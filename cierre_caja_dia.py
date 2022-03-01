
import sqlite3
import time
import os
import crear_usuario
from datetime import datetime
from datetime import date, timedelta


def cierre(usuario): #Obtiene todos los pagos realizados en dia de hoy y los suma.
	today = date.today()
	import conexiones
	lista_cobros = conexiones.conexion_pagos()
	caja = 0
	for pagos in lista_cobros:
		if str(today) == pagos[0]:
			caja = caja + pagos[6]
	print("****************************************************************************")
	print("")
	os.system("cls")
	print(usuario.upper()+", EL MONTO FACTURADO EL DIA DE HOY " + str(today) + " ES DE ***$" + str(caja)+"***")
	print("")
	import menu_principal
	menu_principal.menu(usuario)
