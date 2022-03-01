import time
import sqlite3
import random
import os


def ver_usuario_contraseña(lista,codigo,usuarios):
	print('"ATENCION"')
	print("")
	print("SI USTED NO TIENE ACCESO A SU CORREO ELECTRONICO, COMUNIQUESE CON EL AREA DE SISTEMAS")
	print("")
	print("")
	ingresar_codigo = input("INGRESE EL CODIGO DE SEGURIDAD QUE ENVIAMOS A SU CORREO: ")
	if ingresar_codigo == codigo:
		print("TOME NOTA DE SUS DATOS DE ACCESO POR FAVOR, TENDRA 10 SEGUNDOS")
		time.sleep(2)
		print("USUARIO: " + lista[0] + "          CONTRASEÑA: " + lista[1])
		time.sleep(10)
		os.system("cls")		
	else:
		print("CODIGO INCORRECTO, INTENTE NUEVAMENTE SOLICITANDO UN NUEVO CODIGO DE SEGURIDAD")
	time.sleep(4)
	os.system("cls")
	import ingreso
	ingreso.sistema_acceso(usuarios)

def enviar_mail_verificar(lista,usuarios):
	codigo = random.randint(100000,999999)
	codigo = str(codigo)
	mensaje = "SU CODIGO DE SEGURIDAD ES:  " + str(codigo) + "  SIGA LAS INSTRUCCIONES EN EL SISTEMA POR FAVOR"
	import enviar_mail
	envio = enviar_mail.envio_mail(lista[2].upper(),mensaje,"CODIGO DE SEGURIDAD")
	if envio == "false":
		print("ANTE CUALQUIER DUDA COMUNICATE CON EL AREA DE SISTEMAS")
		time.sleep(4)
		os.system("cls")
		import ingreso
	else:
		ver_usuario_contraseña(lista,codigo,usuarios)


def buscar_usuario(mail):
	import conexiones
	mail = mail.lower()
	usuarios = conexiones.conexion_usuario()
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
		enviar_mail_verificar(usuario_encontrado,usuarios)


