import sqlite3
import baja_seguro
import cierre_caja_dia
import cobrar_cuota
import crear_usuario
import menu_asegurados
#Conexion con las 3 base de datos para obtener un lista con todos los campos

def conexion_usuario():
	conexion = sqlite3.connect("usuarios1")
	cursor = conexion.cursor()
	usuarios = cursor.execute("SELECT * FROM USUARIOS1")
	conexion.commit()
	usuarios = usuarios.fetchall()
	conexion.close()
	return usuarios
	
def conexion_asegurados():
	conexion = sqlite3.connect("asegurados1")
	cursor = conexion.cursor()
	lista_asegurado = cursor.execute("SELECT * FROM ASEGURADOS1")
	conexion.commit()
	lista_asegurado = lista_asegurado.fetchall()
	conexion.close()
	return lista_asegurado
	
def conexion_pagos():
	conexion = sqlite3.connect("pagos1")
	cursor = conexion.cursor()
	lista_cobros = cursor.execute("SELECT * FROM PAGOS1")
	conexion.commit()
	lista_cobros = lista_cobros.fetchall()
	conexion.close()
	return lista_cobros	

#Conexion con las 3 bases para realizar alguna accion, "CRUD"

def acciones_asegurados(accion):
	conexion = sqlite3.connect("asegurados1")
	cursor = conexion.cursor()
	cursor.execute(accion)
	conexion.commit()
	conexion.close()

def acciones_pagos(accion):
	conexion = sqlite3.connect("pagos1")
	cursor = conexion.cursor()
	cursor.execute(accion)
	conexion.commit()
	conexion.close()
	
def acciones_usuarios(accion):
	conexion = sqlite3.connect("usuarios1")
	cursor = conexion.cursor()
	cursor.execute(accion)
	conexion.commit()
	conexion.close()
