import sqlite3
import os
import time


def baja(usuario,asegurado):
	print("**********************************************************************************************")
	print("")
	opcion = input("REALMENTE DESEA DAR DE BAJA ESTE SEGURO? 'S' PARA SI O CUALQUIER TECLA PARA VOLVER: ")
	opcion = opcion.upper()
	if opcion != "S":
		os.system("cls")
		import menu_asegurados
		menu_asegurados.opciones_menu(usuario,asegurado)
	else:
		
		#Elimina al asegurado seleccionado
		import conexiones
		conexiones.acciones_asegurados('''DELETE FROM ASEGURADOS1 WHERE POLIZA =('%s')''' %(asegurado[0][0]))
		print("BAJA DE SEGURO REALIZADA CON EXITO")
		print("VOLVIENDO AL MENU PRINCIPAL")
		time.sleep(2)
		os.system("cls")
		import menu_principal
		menu_principal.menu(usuario)
