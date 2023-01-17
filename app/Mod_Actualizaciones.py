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
import json
import shutil
import datetime
import time
import commands
import sys
import socket
import os

#---------------------------------
#           Librerias personales
#---------------------------------
from lib.Lib_Request_Json import *            # importar con los mismos nombres
from lib.Fun_Dispositivo import *   #

#BKDB                = FIRM +'db/HUB/BKdb/'
T_Antes =time.time()

def Create_Set_File(arch, Text):
    archivo = open(arch, "w")
    archivo.write(Text)
    archivo.close()

def Delete_directory(Ruta):
	try:
		shutil.rmtree(Ruta) # eliminar directorios
		return 1
	except Exception as e:
		#print 'No Existe el directorio'
		return -1

def Create_Directory_new(Ruta):
	Delete_directory(Ruta)
	os.makedirs(Ruta)

def Sort_data(Data_json):
	for Location in Data_json.keys():
		#print Location
		Ruta_Location = os.path.join(FIRM,'db',Location,NEW_DATA[:-1]+'_New')
		#print Ruta_Location
		Create_Directory_new(Ruta_Location)
		Data_Location= Data_json[Location]
		for Tipo in Data_Location.keys():
			#print Tipo
			Ruta_Dato = os.path.join(Ruta_Location, Tipo+'.txt' )
			#print Ruta_Dato
			Data_Tipo= Data_Location[Tipo]#lista ordenada
			Data_Tipo = "\n".join(Data_Tipo) + "\n"
			#print Data_Tipo
			Create_Set_File(Ruta_Dato, Data_Tipo) # Crear Archivo y llenado
		# intercambair buffer
		try:
			Ruta_Location_BK = os.path.join(FIRM,'db',Location,NEW_DATA[:-1]+'_BK')
			Ruta_Location_ACT = os.path.join(FIRM,'db',Location,NEW_DATA[:-1])
			os.rename(Ruta_Location_ACT, Ruta_Location_BK)
			os.rename(Ruta_Location, Ruta_Location_ACT)
			Delete_directory(Ruta_Location_BK)
			#return 1
		except Exception as e:
			print 'Error en el buffer'#posiblenete por que no exite la lacacion
			#return -1

def Hora_Actual():
	tiempo_segundos = time.time()
	#print(tiempo_segundos)
	#tiempo_cadena = time.ctime(tiempo_segundos) # 1488651001.7188754 seg
	tiempo_cadena = time.strftime("%I:%M %p")
	#print(tiempo_cadena)
	return tiempo_cadena

def Hora_Actualizacion_Usuarios(Hora_Actualizacion):
    global Data_simulada
    if Hora_Actualizacion == Hora_Actual():
        while 1:
            time.sleep(2)
            if Hora_Actual() != Hora_Actualizacion : break
            #if PSP_Mensajes:
        print 'Actualizando Usuarios'
        Data_sen = send_petition("get_users")
        print Data_sen
        #Data_sen = Data_simulada
        x_json = json.loads(Data_sen)
        Sort_data(x_json)

def Periodo_Actualizacion_Usuarios(Periodo):
    global T_Antes
    global Data_simulada
    T_Actual = time.time()
    T_transcurido = int(T_Actual-T_Antes)
    #print 'T_Diferencia: ' + str(T_transcurido)
    if T_transcurido >= Periodo :
        print 'Actualizando Usuarios por periodo'
        T_Antes = T_Antes = time.time()
        #Data_sen = send_petition("get_users")
        Data_sen = Data_simulada
        x_json = json.loads(Data_sen)
        Sort_data(x_json)


"""

{
        "S0": {
            "Tipo_1": ['1', '2', '3'],
            "Tipo_2": ['1.123132.1231234', '2.123132.1231234', '3.123132.1231234'],
            "Tipo_3": [],
            "Tipo_4": []
        },

        "S1": {
            "Tipo_1": ['1', '2', '3'],
            "Tipo_2": ['1.123132.1231234', '2.123132.1231234', '3.123132.1231234'],
            "Tipo_3": [],
            "Tipo_4": []
        }
    }
        
#Data_simulada ='{"S0":{"Tipo_1":"1,2,3","Tipo_2":"1.123132.1231234,2.123132.1231234,3.123132.1231234"}}'
Data_simulada ='{"S0":{"Tipo_1":"1,2,3","Tipo_2":"1.123132.1231234,2.123132.1231234,3.123132.1231234","Tipo_3":"","Tipo_4":""},"S1":{"Tipo_1":"1,2,3","Tipo_2":"1.123132.1231234,2.123132.1231234,3.123132.1231234","Tipo_3":"","Tipo_4":""}}'

print Hora_Actual()



while 1:
	#---------------------------------------------------------
	#  Proceso 1: Tiempo de espera para disminuir proceso
	#---------------------------------------------------------
	time.sleep(2) #minimo 1
	#---------------------------------------------------------
	# Proceso 2: Actualizar base de datos en una hora determinada ("12:10 AM") # 12:00 AM     03:59 PM # hora chile  10:00 PM 12:10 AM
	#---------------------------------------------------------
	Hora_Actualizacion_Usuarios("01:10 PM")
    #---------------------------------------------------------
	# Proceso 3: Actualizar base de datos por periodos de tiempos minimo 1 segundo,  60*1 ->1 minuto
	#---------------------------------------------------------
	#Periodo_Actualizacion_Usuarios(60*2)
	#---------------------------------------------------------
	#  Proceso 4:Enviar usuarios a servidor si hay y si esta en la funcion
	#---------------------------------------------------------


"""




#-------------------------------------
# pruebas de uso
#-------------------------------------

#Data_sen = send_petition("get_users")
#print Data_sen
#x_json = json.loads(Data_sen)
#Sort_data(Data_sen)

#x_json = json.loads(Data_simulada)
#Sort_data(x_json)




























"""
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
{u'S0': {u'T2': u'1.123132.1231234\n2.123132.1231234\n3.123132.1231234', u'T1': u'1\n2\n3'}}
{"S0":{"T1":"1,2,3","T2":"1.123132.1231234,2.123132.1231234,3.123132.1231234"}}
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

# Medio de acceso 2:PIN
Mod_Procesamiento
from lib.Lib_Threads import Create_Thread_Daemon

if Get_File(S0+STATUS_TECLADO) == '1':
	Create_Thread_Daemon(Filtro_Tipos_Acceso,
						 Get_File(S0+COM_TECLADO), 2, 0)
	Clear_File(S0+STATUS_TECLADO)

"""
#print send_petition("http://192.168.0.46:3000/get_users")
#print send_petition("http://localhost:3000/get_users")

#users_in_json = json.loads(users_in)

#b_json = '{"S0":{"T1":"1\n2\n3","T2":"1.123132.1231234\n2.123132.1231234\n3.123132.1231234"}}'
#b_json ='{"T1":"1\n2\n3","T2":"1.123132.1231234\n2.123132.1231234\n3.123132.1231234"}'
#users_in_json = json.loads(b_json)
#print users_in_json["T1"]

#x = '{"S0":"{"T1":"1.2.3", "T2":"1.123132.1231234,2.123132.1231234,3.123132.1231234"}"}'
"""
try:
	users_in_json = json.loads(users_in)
except Exception as e:
	users_in_json = {}
"""
"""
#-----------------------------------------------
#-----------------------------------------------
x_json = json.loads(x)
#print 'anson'
#print x_json["S0"]["T1"]
#print x_json["S0"]["T1"]
#T1 = x_json["S0"]["T1"]
#s = T1.replace(',',"\n")
#print s




"""
"""
try:
	users_T1_json = x_json["S0"]["T3"]
except Exception as e:
	users_T1_json = {}

print users_T1_json



def Pedir_Usuarios():

	ID_Dispositivo  = Get_ID_Dispositivo()
	send_petition("http://192.168.0.46:3000/get_users")




def Actualizar_Usuarios_Desde_server():
	global PSP_Mensajes
	Tiempo_Actual = str(int(time.time()*1000.0))  # Tiempo()
	#Ruta            = Get_Rout_server()
	#ID_Dispositivo  = Get_ID_Dispositivo()

	if PSP_Mensajes: print 'Ruta:' + str(Ruta.strip()) + ', UUID:' + ID_Dispositivo

	Respuesta = Pedir_Usuarios_Activos(Ruta.strip(),Tiempo_Actual,ID_Dispositivo)
"""
