#---------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------
"""

Autor: Anderson Amaya Pulido

Libreria personal para procesar un qr.




# ideas a implementar




# dmesg | grep tty
"""
#---------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------
import time


#---------------------------------
#           Librerias personales
#---------------------------------
from lib.Lib_File import *  # importar con los mismos nombres
from lib.Lib_Rout import *  # importar con los mismos nombres


#---------------------------------------
#           Configuraciones de lectoras
#---------------------------------------

#---------------------------------------------
#      funciones para la rspuesta al usaurio con indicadores
#---------------------------------------------

def Access_Entry_Users():
    Set_File(S0+COM_RELE,'Access granted-E')
    Set_File(S0+COM_LED,'Access granted-E')
    Set_File(S0 + COM_BUZZER, '1')           # activar sonido por 500*1

def Access_Out_Users():
    Set_File(S0+COM_RELE,'Access granted-S')
    Set_File(S0+COM_LED,'Access granted-S')
    Set_File(S0 + COM_BUZZER, '1')           # activar sonido por 500*1

def Access_Denied_Users():
    Set_File(S0+COM_RELE,'Error')
    Set_File(S0+COM_LED,'Error')
    Set_File(S0 + COM_BUZZER, '1')           # activar sonido por 500*1

def Acciones_Dispositivo(Comando):
    #--------- para usuarios
    if    'Access granted-E' in Comando :  Access_Entry_Users()
    elif  'Access granted-S' in Comando :  Access_Out_Users()
    elif  'Denied'           in Comando :  Access_Denied_Users()
    else: Access_Denied_Users()




print 'Hola'
# avilitaciones()
# print S0 + COM_RES
# print  Get_File(S0 + COM_RES)
#--- pensados solo para CAT
Set_File(S0+COM_LED,'0')
while (True):
    try :
        time.sleep(0.5)                # 0.05
        Comando = Get_File(S0 + COM_RES)
        if Comando != '':
            Acciones_Dispositivo(Comando)
            Clear_File(S0 + COM_RES)
    except SerialException:
        print 'error'
