#---------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------
"""

Autor: Anderson Amaya Pulido

Libreria personal para procesar un qr.




# ideas a implementar





"""
#---------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------
# Librerias creadas para multi procesos o hilos -------------
import datetime
import time
import commands
import sys
import socket
import os


#---------------------------------
#           Librerias personales
#---------------------------------

from lib.Lib_File import *            # importar con los mismos nombres
from lib.Lib_Rout import *            # importar con los mismos nombres
from lib.Lib_Requests_Server import *   #
from lib.Lib_Networks import *   #
from lib.Fun_Dispositivo import *   #
from lib.Fun_Server import *   #
from lib.Fun_Tipo_QR import *   #

#from lib.Verificar_Usuarios import *  # importar con los mismos nombres

#-------------------------------------------------------
# inicio de variable	--------------------------------------
PSP_Mensajes = 1     # 0: NO print  1: Print
#-------------------------------------------------------

#-------------------------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------------------------
#                   funciones para la peticion de usuarios
#-------------------------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------
def Hora_Actual():
	tiempo_segundos = time.time()
	#print(tiempo_segundos)
	#tiempo_cadena = time.ctime(tiempo_segundos) # 1488651001.7188754 seg
	tiempo_cadena = time.strftime("%I:%M %p")
	#print(tiempo_cadena)
	return tiempo_cadena


Tiempo_Actual = str(int(time.time()*1000.0))  # Tiempo()
Ruta            = Get_Rout_server()
ID_Dispositivo  = Get_ID_Dispositivo()
print ID_Dispositivo

if PSP_Mensajes: print 'Ruta:' + str(Ruta.strip()) + ', UUID:' + ID_Dispositivo

Respuesta = Pedir_Usuarios_Activos(Ruta.strip(),Tiempo_Actual,ID_Dispositivo)

print Respuesta

'
{
"invitations":["4.g26t3.tiempo.tiempo.4123"],
"data":[
"g26t3.0e26423509caa8da168651df506a3a6c",
"g27dq.43edb9f77d3f86dfea6a6152cad1af0d",
"g27ds.82ab4f18ef92c41f8b03221a24aeef26",
"gq6t1.3343b732bb1de413a507c6b125159838",
"gq6ds.a8f396ab149244c64f5908fe851b7f00",
"gq6tc.bb6148027c89459d7f78ca3a3cc88d63",
"6.h2.eea9648ac4adf4b1327af110632dc6cd",
"6.h2.9bc0a6b8b29687a400fbbd97da3e8826",
"6.h2.9da509f613bb819a8d6bae0cfb65dbe2"]}'
