import time


from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
w, h = A4


#Crea un pdf con los datos del pago, lo guarda en la carpeta actual del sistema.
def generar_comprobante(nombre,apellido,dni,marca,modelo,patente,poliza,cuota,fecha,numero_cuota):
	hoy = time.strftime('%Y-%m-%d %H-%M-%S', time.localtime())
	nombre_comprobante = "PAGO, "+nombre+" "+apellido +" "+str(hoy)+".pdf"
	c = canvas.Canvas(nombre_comprobante, pagesize=A4)
	c.setFont("Times-Roman", 45)
	c.drawString(150, h - 40, "SEGUROS UNAJ")
	c.setFont("Times-Roman", 16)
	c.drawString(60, h - 70, "COMPROBANTE DE PAGO ")
	c.setFont("Times-Roman", 12)
	c.drawString(60, h - 90, "CUOTA N°"+numero_cuota+ " SEGURO N° DE POLIZA: "+str(poliza))
	c.drawString(60, h - 110, "MARCA: " + marca)
	c.drawString(60, h - 130, "MODELO: " + modelo)
	c.drawString(60, h - 150, "PATENTE: " + patente)
	c.drawString(60, h - 170,"TITULAR: "+ apellido + " " + nombre + " DNI: " + dni)
	c.drawString(60, h - 500, "PAGO................................$" + str(cuota) + "  FECHA Y HORA.... " + str(hoy))
	c.showPage()
	c.save()
	print("COMPROBANTE DE PAGO GENERADO CON EXITO")
	time.sleep(1.5)
	return nombre_comprobante
	
