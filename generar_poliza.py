import time


from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
w, h = A4



def generar_poliza_seguro(nombre,apellido,dni,marca,modelo,patente,poliza,cuota,fecha,numero_cuota):
	hoy = time.strftime('%Y-%m-%d %H-%M-%S', time.localtime())
	nombre_poliza="POLIZA, "+ nombre+" "+apellido +" "+str(hoy)+".pdf"
	c = canvas.Canvas(nombre_poliza, pagesize=A4)
	c.setFont("Times-Roman", 45)
	c.drawString(150, h - 40, "SEGUROS UNAJ")
	c.setFont("Times-Roman", 16)
	c.drawString(60, h - 70, "POLIZA: " + poliza)
	c.setFont("Times-Roman", 12)
	c.drawString(60, h - 110, "MARCA: " + marca)
	c.drawString(60, h - 130, "MODELO: " + modelo)
	c.drawString(60, h - 150, "PATENTE: " + patente)
	c.drawString(60, h - 170,"TITULAR: "+ apellido + " " + nombre + " DNI: " + dni)
	text = c.beginText(30, h - 200)
	text.setFont("Times-Roman", 12)

	text.textLines("ADVERTENCIA: El vehiculo debera contar con el respectivo grabado indeleble del dominio en"
			"\ndeterminadas partes de la carroceria conforme lo disponga la normativa de aquellas jurisdicciones"
			"\n en las que el mismo es obligatorio."
			"\nLa cobertura de casco (Daños, Incendio, Robo o Hurto) del vehículo no se hará efectiva si"
			"\nel vehículo no se encuentra registrado a nombre del asegurado, hasta tanto se acredite la"
			"\ntransferencia registral a su favor o se obtenga expresa conformidad del titular del"
			"\ndominio del vehículo asegurado, manifestada ante escribano público, para que perciba la"
			"\nndemnización el asegurado."
			"\nCuando se tratare de pólizas contratadas con tarifa diferencial, en razón del domicilio"
			"\ndel asegurado, o la guarda normal del vehículo, éste deberá acreditarlo con documentación"
			"\nfehaciente en el momento de la contratación, o cuando el Asegurador lo requiera, el cual"
			"\ndebe figurar en el Frente de Póliza. La falsa declaración o reticencia en dicha"
			"\ndeclaración produce la nulidad del contrato de acuerdo con lo establecido en el Art. 5"
			"\nde la Ley de Seguros. Si durante la vigencia del seguro, el Asegurado cambiare de"
			"\ndomicilio y/o lugar de la guarda normal habitual trasladándolo a una zona de mayor riesgo"
			"\n(según se detalla a continuación) deberá comunicarlo al Asegurador en forma fehaciente"
			"\nantes de producido el cambio, a los fines de que éste proceda a reajustar el premio. La"
			"\nomisión de esta comunicación, producirá en forma automática la suspensión de la cobertura"
			"\ndeterminadas partes de la carroceria conforme lo disponga la normativa de aquellas jurisdicciones"
			"\n en las que el mismo es obligatorio."
			"\nLa cobertura de casco (Daños, Incendio, Robo o Hurto) del vehículo no se hará efectiva si"
			"\nel vehículo no se encuentra registrado a nombre del asegurado, hasta tanto se acredite la"
			"\ntransferencia registral a su favor o se obtenga expresa conformidad del titular del"
			"\ndominio del vehículo asegurado, manifestada ante escribano público, para que perciba la"
			"\nndemnización el asegurado."
			"\nCuando se tratare de pólizas contratadas con tarifa diferencial, en razón del domicilio"
			"\ndel asegurado, o la guarda normal del vehículo, éste deberá acreditarlo con documentación"
			"\nfehaciente en el momento de la contratación, o cuando el Asegurador lo requiera, el cual"
			"\ndebe figurar en el Frente de Póliza. La falsa declaración o reticencia en dicha"
			"\ndeclaración produce la nulidad del contrato de acuerdo con lo establecido en el Art. 5"
			"\nde la Ley de Seguros. Si durante la vigencia del seguro, el Asegurado cambiare de"
			"\ndomicilio y/o lugar de la guarda normal habitual trasladándolo a una zona de mayor riesgo"
			"\n(según se detalla a continuación) deberá comunicarlo al Asegurador en forma fehaciente"
			"\nantes de producido el cambio, a los fines de que éste proceda a reajustar el premio. La"
			"\nomisión de esta comunicación, producirá en forma automática la suspensión de la cobertura"
			"\ndeterminadas partes de la carroceria conforme lo disponga la normativa de aquellas jurisdicciones"
			"\n en las que el mismo es obligatorio."
			"\ndel casco del vehículo asegurado, hasta que se diere cumplimiento a esta exigencia.")
	c.drawText(text)
	
	c.showPage()
	c.save()
	print("POLIZA GENERADA CON EXITO")
	time.sleep(1.5)
	return nombre_poliza
