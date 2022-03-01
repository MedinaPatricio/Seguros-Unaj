import os
import sqlite3
import menu_principal


def solicitar_datos_acceso(): #solicita usuario y contraseña, devuelve una lista con lso datos.
	entrar= []
	#Menu de ingreso
	print("")
	print("SISTEMA DE ACCESO".rjust(48))
	print("")
	print("*******************************************************".rjust(68))
	print("")
	print("SI OLVIDO SU USUARIO Y/O CONTRASEÑA INGRESE 999 EN LA SECCION 'USUARIO'".rjust(76))
	print("")
	print("*******************************************************".rjust(68))
	print("Ingrese su usuario y contraseña o 0 para cerrar".rjust(62))
	print("")
	usuario = input("USUARIO: ".rjust(45))
	
	#Opcion de recuperacion de usuario y/o contraseña
	if usuario == "999":
		print("")
		mail = input("Ingrese el mail con el cual se registro o 0 para volver  : ".rjust(45))
		if mail == "0":
			os.system("cls")
			solicitar_datos_acceso()
		while len(mail)== 0:
			mail = input("Ingrese el mail con el cual se registro o 0 para volver    : ".rjust(45))
		import recuperar_usuario_contraseña
		recuperar_usuario_contraseña.buscar_usuario(mail)
		
	if usuario == "0":
		os.system("cls")
		print("GRACIAS POR UTILIZAR NUESTROS SERVICIOS, VUELVE PRONTO")
		exit()
	contraseña = input("CONTRASEÑA: ".rjust(45))
	
	if contraseña == "0":
		os.system("cls")
		print("GRACIAS POR UTILIZAR NUESTROS SERVICIOS, VUELVE PRONTO")
		exit()
	entrar.append([usuario,contraseña])
	return entrar	

def sistema_acceso(lista_usuarios): #compara los datos ingresados de con la lista de usuarios registrados
	print ("SEGUROS UNAJ".rjust(45))
	usuario_ingresado = solicitar_datos_acceso()
	cont = 0
	for i in lista_usuarios:	
		if i [0].upper() == usuario_ingresado[0][0].upper() and i [1] == usuario_ingresado[0][1]:
			os.system("cls")
			print ("SEGUROS UNAJ".rjust(45))
			print("")
			usuario_activo = i[0]
			import menu_principal
			menu_principal.menu(usuario_activo)
		else:
			cont = cont + 1	
			
	if len(lista_usuarios) == cont:
		usuario_ingresado.clear()
		os.system("cls")
		print("El usuario y/o la contraseña son incorrectas")
		print("")
		print("Intente nuevamente")
		print("")
		sistema_acceso(usuarios)

conexion = sqlite3.connect("usuarios1")
cursor = conexion.cursor()
usuarios = cursor.execute("SELECT * FROM USUARIOS1")
conexion.commit()
usuarios = usuarios.fetchall()
conexion.close()
sistema_acceso(usuarios)


# Se intento importar la conexion a la base desde el archivo conexciones pero genera errores
# ~ import conexiones
# ~ usuarios = conexiones.conexion_usuario()

