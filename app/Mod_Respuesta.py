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




#---------------------------------------------------------
#---------------------------------------------------------
#----       Clase respuestas para lso diferentes dispsotyivos cae cat hub
#---------------------------------------------------------
#---------------------------------------------------------

class SALIDAS_ACCIONES(object):

    #---------------------------------------------------------
    def __init__(self, Port_Config, Locacion):

        self.Canal  = Port_Config
        self.Sede   = Locacion
        #---------------------------------------
        self.Salida_COM_RES     = ''

        self.Salida_COM_RELE    = ''
        self.Salida_COM_LED     = ''
        self.Salida_COM_BUZZER  = ''

        #---------------------------------------
        self.Enrutar_Archivos_Salidas()
        #print self.Salida_COM_RES


    def Ciclo_revicion(self):
        while (True):
            time.sleep(0.5)                # 0.05
            Comando = Get_File(self.Salida_COM_RES)
            if Comando != '':
                self.Acciones_Dispositivo(Comando)
                Clear_File(self.Salida_COM_RES)



    def Enrutar_Archivos_Salidas(self):

        if self.Sede == '0':

            if  self.Canal == 'S3':
                self.Salida_COM_RES     = S0 + COM_RES
                self.Salida_COM_RELE    = S0 + COM_RELE
                self.Salida_COM_LED     = S0 + COM_LED
                self.Salida_COM_BUZZER  = S0 + COM_BUZZER
            elif  self.Canal == 'S0':    self.Salida_COM_RES     = S0 + COM_RES
            elif  self.Canal == 'S1':    self.Salida_COM_RES     = S1 + COM_RES_S1
            elif  self.Canal == 'S2':    self.Salida_COM_RES     = S2 + COM_RES_S2

        elif self.Sede == '1':

            if  self.Canal == 'S0':    self.Salida_COM_RES       = S0 + COM_RES
            elif  self.Canal == 'S1':    self.Salida_COM_RES     = S1 + COM_RES_S1
            elif  self.Canal == 'S2':    self.Salida_COM_RES     = S2 + COM_RES_S2

        elif self.Sede == '2':

            if  self.Canal == 'S0'  :    self.Salida_COM_RES     = S0 + COM_RES
            elif  self.Canal == 'S1':    self.Salida_COM_RES     = S1 + COM_RES_S1
            elif  self.Canal == 'S2':     self.Salida_COM_RES    = S2 + COM_RES_S2

    def Access_Entry_Users(self):

        Set_File(self.Salida_COM_RELE,'Access granted-E')
        if  self.Canal == 'S3':
            Set_File(self.Salida_COM_LED,'Access granted-E')
            Set_File(self.Salida_COM_BUZZER , '1')           # activar sonido por 500*1

    def Access_Out_Users(self):

        Set_File(self.Salida_COM_RELE,'Access granted-S')
        if  self.Canal == 'S3':
            Set_File(self.Salida_COM_LED,'Access granted-S')
            Set_File(self.Salida_COM_BUZZER , '1')           # activar sonido por 500*1

    def Access_Denied_Users(self):
        Set_File(self.Salida_COM_RELE,'Error')
        if  self.Canal == 'S3':
            Set_File(self.Salida_COM_LED,'Error')
            Set_File(self.Salida_COM_BUZZER, '1')           # activar sonido por 500*1

    def Acciones_Dispositivo(self, Comando):
        #--------- para usuarios
        if    'Access granted-E' in Comando :  self.Access_Entry_Users()
        elif  'Access granted-S' in Comando :  self.Access_Out_Users()
        elif  'Denied'           in Comando :  self.Access_Denied_Users()
        else:                                  self.Access_Denied_Users()




#---------------------------------
#           Configuraciones de Salidas
#---------------------------------

VECTOR_SALIDAS = []

Salidas_reles = Get_File(HUB + CONF_SALIDAS)
print Salidas_reles

for Salida_Rele in Salidas_reles.split('\n'):
    if len(Salida_Rele) > 0:
        Conf_Salida = Salida_Rele.split(".")
        #print Conf_Salida[0]
        VECTOR_SALIDAS.append(SALIDAS_ACCIONES (Conf_Salida[0], Conf_Salida[1] ))

for Salida_Rele in VECTOR_SALIDAS:
    Salida_Rele.Ciclo_revicion()
