import os
import smtplib, ssl
import getpass
import time
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders


def envio_mail(mail, mensaje_enviar, asunto):
	message = mensaje_enviar
	subject = asunto

	message = "subject: {}\n\n{}".format(subject, message)

	server = smtplib.SMTP("smtp.gmail.com", 587)# Creamos la conexión con el servidor
	server.starttls()
	envio = ""
	server.login ("segurosunaj@gmail.com","patriciomedina")#Iniciamos sesion
	try:
		server.sendmail("segurosunaj@gmail.com",mail,message)
		print("MENSAJE ENVIADO CON EXITO A : " + mail.lower())
		time.sleep(1.5)
		return "true" #Truco para no tener errores en recuperar usuario y/o contraseña
	except:
		print("LO SENTIMOS, NO SE PUDO ENVIAR EL MAIL")
		time.sleep(1.5)
		return "false"#Truco para no tener errores en recuperar usuario y/o contraseña
	server.quit()

def envio_mail_adjunto(mail,mensaje_enviar,asunto,adjunto,motivo):

	# Iniciamos los parámetros del script
	remitente = 'segurosunaj@gmail.com'
	destinatarios = mail
	asunto = asunto
	cuerpo = mensaje_enviar
	ruta_adjunto = adjunto
	nombre_adjunto = adjunto
	
	mensaje = MIMEMultipart()# Creamos el objeto mensaje
	 
	# Establecemos los atributos del mensaje
	mensaje['From'] = remitente
	mensaje['To'] = ", ".join(destinatarios)
	mensaje['Subject'] = asunto
	 
	mensaje.attach(MIMEText(cuerpo, 'plain'))# Agregamos el cuerpo del mensaje como objeto MIME de tipo texto
	 
	archivo_adjunto = open(ruta_adjunto, 'rb')# Abrimos el archivo que vamos a adjuntar
	 
	adjunto_MIME = MIMEBase('application', 'octet-stream')# Creamos un objeto MIME base
	
	adjunto_MIME.set_payload((archivo_adjunto).read())# Y le cargamos el archivo adjunto
	
	encoders.encode_base64(adjunto_MIME)# Codificamos el objeto en BASE64
	
	adjunto_MIME.add_header('Content-Disposition', "attachment; filename= %s" % nombre_adjunto)# Agregamos una cabecera al objeto
	
	mensaje.attach(adjunto_MIME)# Y finalmente lo agregamos al mensaje
	 
	sesion_smtp = smtplib.SMTP('smtp.gmail.com', 587)# Creamos la conexión con el servidor
	 
	sesion_smtp.starttls()# Ciframos la conexión

	sesion_smtp.login('segurosunaj@gmail.com','patriciomedina')# Iniciamos sesión en el servidor

	texto = mensaje.as_string()# Convertimos el objeto mensaje a texto

	try:
		sesion_smtp.sendmail(remitente, destinatarios, texto)# Enviamos el mensaje
		print(motivo + " ENVIADO CON EXITO")
		time.sleep(1.5)
	except:
		print("NO SE PUDO ENVIAR "+motivo+ ", POR FAVOR MODIFIQUE LOS DATOS EN LA SECCION ASEGURADOS, VER/MODIFICAR MAIL")
		time.sleep(1.5)
		
	
	sesion_smtp.quit()# Cerramos la conexión
