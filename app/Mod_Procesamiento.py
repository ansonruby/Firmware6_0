from lib.Lib_File import Clear_File, Get_File
from lib.Lib_Rout import *  
from lib.Lib_Threads import Create_Thread_Daemon 
import re


def Filtro_Tipos_Acceso_Antiguos(access_code, medio_acceso=1,lectora=0):
    try:
        access_data = re.sub("[<>]","",access_code).split(".")
        #Tipo 6:Dispositivos adicionales
        if medio_acceso==11:  
            print 6
        
        #Tipo 1 0 2 o 5: LLave de acceso o Reserva general con QR o Llave empleado
        elif len(access_data) == 2 or medio_acceso==2:  
            print 1

        #Tipo 3: Invitacion de unico uso
        elif len(access_data) == 5 and access_data[0] == "3":
            print 3

        #Tipo 4: Invitacion de multipes uso
        elif len(access_data) == 5:
            print 4

    except Exception as e:
        print e


def Recibir_Codigo_Accesso():
    #Medio de acceso 1:QR
    if Get_File(S0+STATUS_QR) == '1':
        Create_Thread_Daemon(Filtro_Tipos_Acceso_Antiguos, Get_File(S0+COM_QR),1,0)
        Clear_File(S0+STATUS_QR)
        
    if Get_File(S0+STATUS_QR_S1) == '1':
        Create_Thread_Daemon(Filtro_Tipos_Acceso_Antiguos, Get_File(S0+COM_QR_S1),1,1)
        Clear_File(S0+STATUS_QR_S1)

    if Get_File(S0+STATUS_QR_S2) == '1':
        Create_Thread_Daemon(Filtro_Tipos_Acceso_Antiguos, Get_File(S0+COM_QR_S2),1,2)
        Clear_File(S0+STATUS_QR_S2)

    #Medio de acceso 2:PIN
    if Get_File(S0+STATUS_TECLADO) == '1':
        Create_Thread_Daemon(Filtro_Tipos_Acceso_Antiguos, Get_File(S0+COM_TECLADO),2,0)
        Clear_File(S0+STATUS_TECLADO)
        
    if Get_File(S0+STATUS_TECLADO_S1) == '1':
        Create_Thread_Daemon(Filtro_Tipos_Acceso_Antiguos, Get_File(S0+COM_TECLADO_S1),2,1)
        Clear_File(S0+STATUS_TECLADO_S1)

    if Get_File(S0+STATUS_TECLADO_S2) == '1':
        Create_Thread_Daemon(Filtro_Tipos_Acceso_Antiguos, Get_File(S0+COM_TECLADO_S2),2,2)
        Clear_File(S0+STATUS_TECLADO_S2)

    #Medio de acceso 5-11:PIN
    if Get_File(S0+STATUS_NFC) == '1':
        Create_Thread_Daemon(Filtro_Tipos_Acceso_Antiguos, Get_File(S0+COM_NFC),11,0)
        Clear_File(S0+STATUS_NFC)
        
    if Get_File(S0+STATUS_NFC_S1) == '1':
        Create_Thread_Daemon(Filtro_Tipos_Acceso_Antiguos, Get_File(S0+COM_NFC_S1),11,1)
        Clear_File(S0+STATUS_NFC_S1)

    if Get_File(S0+STATUS_NFC_S2) == '1':
        Create_Thread_Daemon(Filtro_Tipos_Acceso_Antiguos, Get_File(S0+COM_NFC_S2),11,2)
        Clear_File(S0+STATUS_NFC_S2)

Recibir_Codigo_Accesso()
# print Get_File(S0+STATUS_QR)