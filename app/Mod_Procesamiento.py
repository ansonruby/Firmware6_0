from lib.Lib_File import Clear_File, Get_File
from lib.Lib_Rout import *  
from lib.Lib_Threads import Create_Thread_Daemon 


def Filtro_Tipos_Acceso_Antiguos(qr_code, medio_acceso=1,lectora=0):
    print qr_code
    print medio_acceso
    print lectora
    try:
        data = qr_code.split(".")

        #Tipo 6:Dispositivos adicionales
        if data[0] == "6":  
            pass
        
        #Tipo 1 0 2 o 5: LLave de acceso o Reserva general con QR o Llave empleado
        elif len(data) == 2:  
            pass

        #Tipo 3: Invitacion de unico uso
        elif len(data) == 5 and data[0] == "3":
            pass

        #Tipo 4: Invitacion de multipes uso
        elif len(data) == 5:
            pass

    except Exception as e:
        pass


def Recibir_Datos_Accesso():
    #Medio de acceso 1:QR
    if Get_File(STATUS_QR) == '1':
        Create_Thread_Daemon(Filtro_Tipos_Acceso_Antiguos, Get_File(COM_QR),0,0)
        Clear_File(STATUS_QR)
        
    if Get_File(STATUS_QR_S1) == '1':
        Create_Thread_Daemon(Filtro_Tipos_Acceso_Antiguos, Get_File(COM_QR_S1),0,1)
        Clear_File(STATUS_QR_S1)

    if Get_File(STATUS_QR_S2) == '1':
        Create_Thread_Daemon(Filtro_Tipos_Acceso_Antiguos, Get_File(COM_QR_S2),0,2)
        Clear_File(STATUS_QR_S2)

    #Medio de acceso 2:PIN
    if Get_File(STATUS_TECLADO) == '1':
        Create_Thread_Daemon(Filtro_Tipos_Acceso_Antiguos, Get_File(COM_TECLADO),0,0)
        Clear_File(STATUS_TECLADO)
        
    if Get_File(STATUS_TECLADO_S1) == '1':
        Create_Thread_Daemon(Filtro_Tipos_Acceso_Antiguos, Get_File(COM_TECLADO_S1),0,1)
        Clear_File(STATUS_TECLADO_S1)

    if Get_File(STATUS_TECLADO_S2) == '1':
        Create_Thread_Daemon(Filtro_Tipos_Acceso_Antiguos, Get_File(COM_TECLADO_S2),0,2)
        Clear_File(STATUS_TECLADO_S2)

    #Medio de acceso 5-11:PIN
    if Get_File(STATUS_NFC) == '1':
        Create_Thread_Daemon(Filtro_Tipos_Acceso_Antiguos, Get_File(COM_NFC),0,0)
        Clear_File(STATUS_NFC)
        
    if Get_File(STATUS_NFC_S1) == '1':
        Create_Thread_Daemon(Filtro_Tipos_Acceso_Antiguos, Get_File(COM_NFC_S1),0,1)
        Clear_File(STATUS_NFC_S1)

    if Get_File(STATUS_NFC_S2) == '1':
        Create_Thread_Daemon(Filtro_Tipos_Acceso_Antiguos, Get_File(COM_NFC_S2),0,2)
        Clear_File(STATUS_NFC_S2)
