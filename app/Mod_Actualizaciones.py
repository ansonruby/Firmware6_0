#---------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------
"""

Autor:  Luding Castaneda,
        Anderson Amaya Pulido

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
T_Antes_send_autorizations=time.time()

Config_Mod  = Get_Mod_Actualizaciones()
Tiempo_stop = float(Config_Mod['Time_Sleep_Mod'])

Bandera_Periodo_Usuario = 0
Timepo_periodo=10
if Config_Mod['Usuarios_Periodo'] != "False":
    Bandera_Periodo_Usuario = 1
    Timepo_periodo=int(Config_Mod['Usuarios_Periodo'])

Bandera_Hora_Usuario = 0
if Config_Mod['Usuarios_Time'] != "False":
    Bandera_Hora_Usuario = 1
    Hora_Usuario= Config_Mod['Usuarios_Time']

Bandera_Inicio_Usuario = 0
if Config_Mod['Usuarios_Inicio'] != "False":
    Bandera_Inicio_Usuario = 1    

            


def Sort_data(Data_json):
    for Location in Data_json.keys():
        #print Location
        Ruta_Location = os.path.join(FIRM,'db',Location,NEW_DATA[:-1]+'_New')
        Ruta_Location_BK = os.path.join(FIRM,'db',Location,NEW_DATA[:-1]+'_BK')
        Ruta_Location_ACT = os.path.join(FIRM,'db',Location,NEW_DATA[:-1])
        Delete_directory(Ruta_Location)
        Delete_directory(Ruta_Location_BK)
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
            os.rename(Ruta_Location_ACT, Ruta_Location_BK)            
            os.rename(Ruta_Location, Ruta_Location_ACT)            
            Delete_directory(Ruta_Location_BK)
            #return 1
        except Exception as e:
            print 'Error en el buffer'#posiblemente por que no exite la lacacion
#---------------------------------------------------------
def Hora_Actual():
	tiempo_segundos = time.time()
	#print(tiempo_segundos)
	#tiempo_cadena = time.ctime(tiempo_segundos) # 1488651001.7188754 seg
	tiempo_cadena = time.strftime("%I:%M %p")
	#print(tiempo_cadena)
	return tiempo_cadena
#---------------------------------------------------------
def Actualizacion_Usuarios():
    Data_sen = send_petition("get_users")
    if Data_sen != False and Data_sen.ok:
        Sort_data(Data_sen.json())
#---------------------------------------------------------
def Hora_Actualizacion_Usuarios(Hora_Actualizacion):
    global Data_simulada
    if Hora_Actualizacion == Hora_Actual():
        while 1:
            time.sleep(2)
            if Hora_Actual() != Hora_Actualizacion : break        
        Actualizacion_Usuarios()       
#---------------------------------------------------------
def Periodo_Actualizacion_Usuarios(Periodo):
    global T_Antes
    global Data_simulada
    T_Actual = time.time()
    T_transcurido = int(T_Actual-T_Antes)
    #print 'T_Diferencia: ' + str(T_transcurido)
    if T_transcurido >= Periodo :
        print 'Actualizando Usuarios por periodo'
        T_Antes = T_Antes = time.time()
        Actualizacion_Usuarios()
#---------------------------------------------------------
def send_autorizations():
    Status_Autorisados=0
    Data_Autorizados ={}
    Data_Location={}
    for Location in range(3):
        Ruta = os.path.join(FIRM,'db','S'+str(Location))
        if os.path.exists(Ruta) == True:
            Data_Autorizados ={}
            for Tipo in range(1,7):
                Archivo = 'Tipo_'+str(Tipo)
                Ruta = os.path.join(FIRM,'db','S'+str(Location),DATA,'Autorizaciones',Archivo +'.txt')
                if os.path.exists(Ruta) == True:
                    Ev = Get_File(Ruta)
                    if len(Ev) >=2:
                        Ev =Ev.split('\n')[:-1]
                        Status_Autorisados=1
                    else:           Ev = []
                else:   Ev = []
                Data_Autorizados[Archivo]=Ev
            Data_Location['S'+str(Location)] = Data_Autorizados
            #print Data_Autorizados
    if Status_Autorisados == 1:
        #print Data_Location
        repuesta= send_petition("send_autorizations", method="POST", json_data= Data_Location)
        if repuesta.ok :
            print 'se resivieron los datos eliminado'
            for Location in range(3):
                Ruta = os.path.join(FIRM,'db','S'+str(Location))
                if os.path.exists(Ruta) == True:
                    for Tipo in range(1,7):
                        Archivo = 'Tipo_'+str(Tipo)
                        Ruta = os.path.join(FIRM,'db','S'+str(Location),DATA,'Autorizaciones',Archivo +'.txt')
                        if os.path.exists(Ruta) == True: Clear_File(Ruta)
        else:
            print 'nuevo intento'

    else:                       print 'NO hay datos'
#---------------------------------------------------------
def Periodo_send_autorizations(Periodo):
    global T_Antes_send_autorizations
    global Data_simulada
    T_Actual = time.time()
    T_transcurido = int(T_Actual-T_Antes_send_autorizations)
    #print 'T_Diferencia: ' + str(T_transcurido)
    if T_transcurido >= Periodo :
        print 'Periodo_send_autorizations'
        T_Antes_send_autorizations = time.time()
        Data_sen = send_petition("get_users")
        send_autorizations()
#---------------------------------------------------------
def Actualizar_Inicio_Usuarios():
    Actualizacion_Usuarios()


print Hora_Actual()

if Bandera_Inicio_Usuario: Actualizar_Inicio_Usuarios()

while 1:
    #---------------------------------------------------------
    #  Proceso 1: Tiempo de espera para disminuir proceso
    #---------------------------------------------------------
    time.sleep(Tiempo_stop) #minimo 1
    #---------------------------------------------------------
    # Proceso 2: Actualizar base de datos en una hora determinada ("12:10 AM") # 12:00 AM     03:59 PM # hora chile  10:00 PM 12:10 AM
    #---------------------------------------------------------
    if Bandera_Hora_Usuario: Hora_Actualizacion_Usuarios(Hora_Usuario)
    #---------------------------------------------------------
    # Proceso 3: Actualizar base de datos por periodos de tiempos minimo 1 segundo,  60*1 ->1 minuto
    #---------------------------------------------------------
    if Bandera_Periodo_Usuario: Periodo_Actualizacion_Usuarios(Timepo_periodo)
    #---------------------------------------------------------
    #  Proceso 4:Enviar usuarios a servidor periodicamente si hay
    #---------------------------------------------------------
    #Periodo_send_autorizations(6)


#-------------------------------------
# pruebas de uso
#-------------------------------------
#actualizacion de usuario se realisa todo al mismo timepo , 
# posiblemente hay que separa para cada configuracion de locacion
# falta realisa hilos por cada accion par que cada una sea separada
#Actualizacion_Usuarios()
#send_autorizations()