import os
import sqlite3
import time



def opcion_seleccionada(opcion,usuario):
	if opcion == "0":
		os.system("cls")
		print("HASTA LUEGO " + usuario.upper() +  ", GRACIAS POR UTILIZAR NUESTROS SERVICIOS ;) TE ESPERAMOS PRONTO")
		exit()
	elif opcion == "1":
		os.system("cls")
		import nuevo_seguro
		nuevo_seguro.aviso(usuario)
	elif opcion == "2":
		import menu_asegurados
		menu_asegurados.menu_asegurado(usuario)
	elif opcion == "3":
		import crear_usuario
		crear_usuario.crear_usuario(usuario)
	elif opcion == "4":
		os.system("cls")
		import conexiones
		usuarios = conexiones.conexion_usuario()
		import ingreso
		ingreso.sistema_acceso(usuarios)
	elif opcion == "5":
		import cierre_caja_dia
		cierre_caja_dia.cierre(usuario)
	elif opcion == "6":
		modificar_mail(usuario)
	elif opcion == "7":
		eliminar_usuario(usuario)	
	elif opcion == "8":
		os.system("cls")
		print("HASTA LUEGO " + usuario.upper() +  ", GRACIAS POR UTILIZAR NUESTROS SERVICIOS ;) TE ESPERAMOS PRONTO")
		exit()

def eliminar_usuario(usuario):
	print("**********************************************************************************************")
	print("")
	opcion = input("REALMENTE DESEA ELIMINAR ESTE USUARIO? 'S' PARA SI O CUALQUIER TECLA PARA VOLVER: ")
	opcion = opcion.upper()
	if opcion != "S":
		os.system("cls")
		menu(usuario)
	else:
		import conexiones
		conexiones.acciones_usuarios('''DELETE FROM USUARIOS1 WHERE USUARIOS =('%s')''' %(usuario))
		print("USUARIO ELIMINADO")
		print("VOLVIENDO AL MENU PRINCIPAL")
		time.sleep(2)
		os.system("cls")
		import ingreso



def modificar_mail(usuario):
	print("")
	nuevo_mail = input("INGRESE SU NUEVO MAIL O 0 PARA VOLVER: ")
	if nuevo_mail == "0":
		os.system("cls")
		menu(usuario)
	else:
		import conexiones
		conexiones.acciones_usuarios('''UPDATE USUARIOS1 SET MAIL =('%s') WHERE USUARIOS =('%s')''' %(nuevo_mail, usuario))
		print("MAIL ACTUALIZADO")
		print("INICIE SESION NUEVAMENTE")
		time.sleep(2)
		os.system("cls")
		import ingreso



def opciones_menu(usuario):
	print("Usuario: " + usuario.upper() + ", Bienvenido")
	print("**********************************************")
	print(" seleccione una opcion")
	print("")
	print("1. NUEVO SEGURO".rjust(26) + "2. ASEGURADOS".rjust(37))
	print("")
	print("3. CREAR USUARIO".rjust(27) + "4. CERRAR SESION".rjust(39))
	print("")
	print("5. CALCULAR CAJA DEL DIA".rjust(35) + "6. MODIFICAR MAIL DE USUARIO".rjust(43))
	print("")
	print("7. ELIMINAR USUARIO".rjust(30) + "8. SALIR".rjust(28))

def menu(usuario):
	opciones_menu(usuario)
	print("")
	opcion = input("SELECCIONE UNA OPCION O 0 PARA CERRAR: ")
	while opcion not in "012345678" or opcion == "":
		os.system("cls")
		print("OPCION INCORRECTA, POR FAVOR INGRESE SOLO EL NUMERO DE LA OPCION DESEADA O 0 PARA CERRAR")
		print("")
		opciones_menu(usuario)
		opcion = input("SELECCIONE UNA OPCION O 0 PARA CERRAR: ")
	opcion_seleccionada(opcion,usuario)
	
