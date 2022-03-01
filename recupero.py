import os
import sqlite3
conexion = sqlite3.connect("usuarios1")
cursor = conexion.cursor()
usuarios = cursor.execute("SELECT * FROM USUARIOS1")
conexion.commit()
usuarios = usuarios.fetchall()
conexion.close()




def modificar_contraseña(lista,codigo):
	print("")
	print("SE ENVIO UN CODIGO DE SEGURIDAD AL SU CORREO ELECTRONICO")
	print("")
	ingresar_codigo = input("INGRESE EL CODIGO DE SEGURIDAD: ")
	if ingresar_codigo == codigo:
			modificar_contraseña(lista)
	nueva_contraseña = input("INGRESE SU NUEVA CONTRASEÑA: ")
	while len(nuevo_mail) == 0:
		nueva_contraseña = input("INGRESE SU NUEVA CONTRASEÑA: ")
	conexion = sqlite3.connect("usuarios1")
	cursor = conexion.cursor()
	cursor.execute('''UPDATE USUARIOS1 SET MAIL =('%s') WHERE USUARIO =('%s')''' %(nuevo_mail, lista[0]))
	conexion.commit()
	conexion.close()
	os.system("cls")
	print("MAIL ACTUALIZADO")
	import ingreso
	ingreso.solicitar_datos_acceso()

def enviar_mail_verificar(lista):
	import enviar_mail
	enviar_mail.envio_mail("PATRICIOMEDINAJ@GMAIL.COM","hola","hola")


def cambiar_contraseña(mail):
	usuario_encontrado = []
	for usuario_registrado in usuarios:
		if mail == usuario_registrado[2]:
			usuario_encontrado = usuario_registrado
	if len(usuario_encontrado) == 0:
		os.system("cls")
		print("USUARIO NO ENCONTRADO")
		import ingreso
		ingreso.solicitar_datos_acceso()
	else:
		enviar_mail_verificar(usuario_encontrado)
