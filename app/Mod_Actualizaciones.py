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
from lib.Lib_settings import Get_Mod_Actualizaciones
from lib.Lib_Binary_Search import Get_List_Indexes, Binary_Update_Id, Binary_Remove_Id

#-----------------------------------------------------------
#                       CONTANTES
#-----------------------------------------------------------

MA_Mensajes = 0     # 0: NO print  1: Print

#BKDB                = FIRM +'db/HUB/BKdb/'
T_Antes =time.time()
T_Antes_send_autorizations=time.time()

Config_Mod  = Get_Mod_Actualizaciones()
Tiempo_stop = float(Config_Mod['Time_Sleep_Mod'])

Bandera_Periodo_Usuario = 0
Tiempo_periodo_Usuarios=10
if Config_Mod['Usuarios_Periodo'] != "False":
    Bandera_Periodo_Usuario = 1
    Tiempo_periodo_Usuarios=int(Config_Mod['Usuarios_Periodo'])

Bandera_Hora_Usuario = 0
if Config_Mod['Usuarios_Time'] != "False":
    Bandera_Hora_Usuario = 1
    Hora_Usuario= Config_Mod['Usuarios_Time']

Bandera_Hora_Salida_Automatica = 0
if Config_Mod['Salida_Automantica'] != "False":
    Bandera_Hora_Salida_Automatica = 1
    Hora_Salida_Automatica= Config_Mod['Salida_Automantica']

Bandera_Inicio_Usuario = 0
if Config_Mod['Usuarios_Inicio'] != "False":
    Bandera_Inicio_Usuario = 1

Bandera_Periodo_Autorizacion = 0
Tiempo_periodo_Autorizacion=10
if Config_Mod['Actualizaciones_Periodo'] != "False":
    Bandera_Periodo_Autorizacion = 1
    Tiempo_periodo_Autorizacion=int(Config_Mod['Actualizaciones_Periodo'])




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
            Data_Tipo = "\n".join(Data_Tipo) 
            #print Data_Tipo
            Create_Set_File(Ruta_Dato, Data_Tipo) # Crear Archivo y llenado
        # intercambair buffer
        try:
            os.rename(Ruta_Location_ACT, Ruta_Location_BK)
            os.rename(Ruta_Location, Ruta_Location_ACT)
            Delete_directory(Ruta_Location_BK)
            #return 1
        except Exception as e:
            if MA_Mensajes: print 'Error en el buffer'#posiblemente por que no exite la lacacion
#---------------------------------------------------------
def Sort_updated_data(Data_json):
    update_data = Data_json["created_index_data"]
    delete_data = Data_json["deleted_index_data"]
    for location in update_data.keys():
        for tipo in update_data[location].keys():
            tipo_path = os.path.join(
                FIRM, 'db', location, NEW_DATA[:-1], tipo+'.txt')

            #Delete indexes
            if location in delete_data and tipo in delete_data[location]:
                for index_data in delete_data[location][tipo]:
                    if index_data=="":
                        continue
                    Binary_Remove_Id(tipo_path,index_data)           
                    
            #Create and update indexes
            for index_data in update_data[location][tipo]:
                if index_data=="":
                    continue
                Binary_Update_Id(tipo_path,index_data)


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
def Salida_Automatica():
    db_path = os.path.join(FIRM, 'db')
    locations = [location for location in os.listdir(
        db_path) if location.startswith("S")]
    for location in locations:
        users_in_path = os.path.join(db_path, location, TAB_USER_IN)
        if os.path.exists(users_in_path):
            users_in = ""
            users_in_json = {}
            with open(users_in_path, 'r') as df:
                users_in = df.read().strip()
                df.close()
            try:
                users_in_json = json.loads(users_in)
            except Exception as e:
                users_in_json = {}

            read_time = int(time.time()*1000)

            for user in users_in_json.keys():
                if users_in_json[user][1] % 1:
                    athorization_code = user + "." + str(read_time) + ".13.1.1"
                    Add_Line_End(
                        os.path.join(db_path, location, NEW_AUTO_USER_TIPO_6),
                        athorization_code+"\n"
                    )

            with open(users_in_path, 'w') as dfw:
                dfw.write(json.dumps({}))
                dfw.close()
#---------------------------------------------------------
def Actualizacion_Usuarios_Periodica():
    indexes_to_review = {}
    db_path=os.path.join(FIRM,'db')
    locations = [location for location in os.listdir(db_path) if location.startswith("S")]
    for location in locations:
        indexes_to_review[location]={}
        tipos_path=os.path.join(db_path, location, NEW_DATA[:-1])
        tipos = os.listdir(tipos_path)
        for tipo in tipos:
            indexes_path=os.path.join(tipos_path,tipo)
            indexes_to_review[location][tipo.split(".")[0]]=Get_List_Indexes(indexes_path)
    Data_sen = send_petition("get_users_periodic",method="POST", json_data=indexes_to_review)
    if Data_sen != False and Data_sen.ok:
        Sort_updated_data(Data_sen.json())
#---------------------------------------------------------
def Hora_Actualizacion_Usuarios(Hora_Actualizacion):
    global MA_Mensajes
    if Hora_Actualizacion == Hora_Actual():
        while 1:
            time.sleep(2)
            if Hora_Actual() != Hora_Actualizacion : break
        if MA_Mensajes: print 'Hora_Actualizacion_Usuarios'
        Actualizacion_Usuarios()
#---------------------------------------------------------
def Hora_Salida_Automatica_Usuarios(Hora_Salida_Automatica):
    global MA_Mensajes
    if Hora_Salida_Automatica == Hora_Actual():
        while 1:
            time.sleep(2)
            if Hora_Actual() != Hora_Salida_Automatica : break
        if MA_Mensajes: print 'Hora_Actualizacion_Usuarios'
        Salida_Automatica()
#---------------------------------------------------------
def Periodo_Actualizacion_Usuarios(Periodo):
    global T_Antes
    
    T_Actual = time.time()
    T_transcurido = int(T_Actual-T_Antes)
    #print 'T_Diferencia: ' + str(T_transcurido)
    if T_transcurido >= Periodo :
        if MA_Mensajes: print 'Periodo_Actualizacion_Usuarios'
        T_Antes = T_Antes = time.time()
        Actualizacion_Usuarios_Periodica()
#---------------------------------------------------------
def send_autorizations():
    global MA_Mensajes
    Status_Autorisados=0
    Data_Autorizados ={}
    Data_Location={}
    for Location in range(3):
        Ruta = os.path.join(FIRM,'db','S'+str(Location))
        #print Ruta
        if os.path.exists(Ruta) == True:
            Data_Autorizados ={}
            for Tipo in range(1,8):
                Archivo = 'Tipo_'+str(Tipo)
                Ruta = os.path.join(FIRM,'db','S'+str(Location),DATA,'Autorizaciones',Archivo +'.txt')
                #print Ruta
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
        # print Data_Location
        repuesta= send_petition("send_autorizations", method="POST", json_data= Data_Location)
        if repuesta.ok :
            #print 'se resivieron los datos eliminando'
            for Location in range(3):
                Ruta = os.path.join(FIRM,'db','S'+str(Location))
                if os.path.exists(Ruta) == True:
                    for Tipo in range(1,8):
                        Archivo = 'Tipo_'+str(Tipo)
                        Ruta = os.path.join(FIRM,'db','S'+str(Location),DATA,'Autorizaciones',Archivo +'.txt')
                        #print Ruta
                        if os.path.exists(Ruta) == True: Clear_File(Ruta)
        else:
            if MA_Mensajes: print 'nuevo intento'
    else:
        if MA_Mensajes: print 'NO hay datos'
#---------------------------------------------------------
def Periodo_send_autorizations(Periodo):
    global T_Antes_send_autorizations
    
    T_Actual = time.time()
    T_transcurido = int(T_Actual-T_Antes_send_autorizations)
    #print 'T_Diferencia: ' + str(T_transcurido)
    if T_transcurido >= Periodo :
        if MA_Mensajes: print 'Periodo_send_autorizations'
        T_Antes_send_autorizations = time.time()
        #Data_sen = send_petition("get_users")
        send_autorizations()
#---------------------------------------------------------
def Actualizar_Inicio_Usuarios():
    global MA_Mensajes
    if MA_Mensajes: print 'Actualizar_Inicio_Usuarios'
    Actualizacion_Usuarios()

if __name__ == '__main__':
    if MA_Mensajes: print Hora_Actual()

    if Bandera_Inicio_Usuario: Actualizar_Inicio_Usuarios()

    while 1:
        #---------------------------------------------------------
        # Proceso 1: Tiempo de espera para disminuir proceso
        #---------------------------------------------------------
        time.sleep(Tiempo_stop) #minimo 1
        #---------------------------------------------------------
        # Proceso 2: Actualizar base de datos en una hora determinada ("12:10 AM") # 12:00 AM     03:59 PM # hora chile  10:00 PM 12:10 AM
        #---------------------------------------------------------
        if Bandera_Hora_Usuario: Hora_Actualizacion_Usuarios(Hora_Usuario)
        #---------------------------------------------------------
        # Proceso 3: Actualizar base de datos por periodos de tiempos minimo 1 segundo,  60*1 ->1 minuto
        #---------------------------------------------------------
        if Bandera_Periodo_Usuario: Periodo_Actualizacion_Usuarios(Tiempo_periodo_Usuarios)
        #---------------------------------------------------------
        # Proceso 4:Enviar usuarios a servidor periodicamente si hay
        #---------------------------------------------------------
        if Bandera_Periodo_Autorizacion: Periodo_send_autorizations(Tiempo_periodo_Autorizacion)
        #---------------------------------------------------------
        # Proceso 5: Salida de usuarios que sigan en la locaion ("01:00 AM") # 01:00 AM
        #---------------------------------------------------------
        if Bandera_Hora_Salida_Automatica: Hora_Salida_Automatica_Usuarios(Hora_Salida_Automatica)


        #-------------------------------------
        # pruebas de uso
        #-------------------------------------
        #actualizacion de usuario se realisa todo al mismo timepo ,
        # posiblemente hay que separa para cada configuracion de locacion
        # falta realisa hilos por cada accion par que cada una sea separada
        #Actualizacion_Usuarios()
        #send_autorizations()
        """
        while 1:
            Periodo_send_autorizations(6)
        """
        #print S0+STATUS_QR_S1
