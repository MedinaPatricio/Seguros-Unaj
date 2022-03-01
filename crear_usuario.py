import sqlite3
import os
import time

conexion = sqlite3.connect("usuarios1")
cursor = conexion.cursor()
usuarios = cursor.execute("SELECT * FROM USUARIOS1")
conexion.commit()
usuarios = usuarios.fetchall()
conexion.close()


def agregar_usuarios(usuario):
	
	print("NUEVO USUARIO")
	nuevo_usuario = input('Ingrese un nuevo usuario o 0 para volver : ')
	nuevo_usuario = nuevo_usuario.upper()
	
	if nuevo_usuario == "0" or nuevo_usuario == "":
		os.system("cls")
		import menu_principal
		menu_principal.menu(usuario)
		
	for usuario1 in usuarios:
		while nuevo_usuario == usuario1[0].upper(): #verifica que el usuario no exista en la base de datos
			print("EL USUARIO YA EXISTE")
			nuevo_usuario = input('Ingrese un nuevo usuario o 0 para volver : ')
			nuevo_usuario = nuevo_usuario.upper()
	contraseña = input("Ingrese la contraseña o para volver : ")
	
	if contraseña == "0" or contraseña == "":
		os.system("cls")
		import menu_principal
		menu_principal.menu(usuario)
		
	if contraseña != "0" and usuario != "0":
		mail = input("Ingrese su mail correctamente ya que se utiliza para el recupero de usuario y contraseña: ")
		while len(mail) == 0:
			mail = input("Ingrese su mail correctamente ya que se utiliza para el recupero de usuario y contraseña: ")
		
		#Agrega el usuario a la base de datos
		import conexiones
		conexiones.acciones_usuarios('''INSERT INTO USUARIOS1 (USUARIOS, CONTRASEÑA,MAIL)VALUES('%s','%s','%s')''' %(nuevo_usuario, contraseña,str(mail)))
		print("FELICITACION, USUARIO CREADO CON EXITO")
		print("VOLVIENDO AL MENU EN...")
		
		#Visualizacion de cuenta regresiva antes del volver al menu
		cont = 4
		while cont != 0:
			time.sleep(1)
			cont = cont-1
			print(cont)
		os.system("cls")
		import menu_principal
		menu_principal.menu(usuario)

#Es necesario la contraseña del administrador para poder crear un usuario, esta funcion la solicita.
def crear_usuario(usuario):
	contraseña = input(usuario.upper() + ", INGRESE LA CONTRASEÑA DEL ADMINISTRADOR O PRESIONE ENTER PARA VOLVER AL MENU: ")
	if contraseña == "0":
		import menu_principal
		menu_principal.menu(usuario)
	elif contraseña == administrador:
		os.system("cls")
		agregar_usuarios(usuario)
	else:
		os.system("cls")
		print("")
		print("LO SENTIMOS SR ADMINISTRADOR, LA CONTRASEÑA INGRESADA NO ES CORRECTA. VUELVA A INTENTARLO O CONTACTESE CON EL AREA DE SISTEMAS")
		import menu_principal
		menu_principal.menu(usuario)

administrador = "Unaj"
