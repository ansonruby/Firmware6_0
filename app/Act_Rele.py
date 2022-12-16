# -*- coding: utf-8 -*-
#-------------------------------------------------------
#----      importar complementos                    ----
#-------------------------------------------------------
import time
import threading

import RPi.GPIO as GPIO #Libreria Python GPIO

from lib.Lib_File import *  # importar con los mismos nombres
from lib.Lib_Rout import *  # importar con los mismos nombres


#-----------------------------------------------------------
#                       CONTANTES
#-----------------------------------------------------------

PN_Mensajes_AR = 0     # 0: NO print  1: Print
#            Entrada, Salida de los relevos
# puerta 0 : [37,38]
# puerta 1 : [35,36]
# puerta 2 : [31,33]

# Rele =   [37,38]        #16, 19 #[21,23]

Reles =[[37,38],[35,36],[31,33]]


#-----------------------------------------------------------
#                       DEFINICIONES
#-----------------------------------------------------------

#-----------------------------------------------------------
#                       VARIABLES
#-----------------------------------------------------------


#-----------------------------------------------------------
#----      Funciones para el manejo de los relevos     ----
#-----------------------------------------------------------


def Configurar_Relevos(Puerta):
    global Reles

    Tipo_Comunicacion = Get_File(Puerta+CONF_COMU_RELE)
    Selec_Puerta  = int (Puerta[22])


    if Tipo_Comunicacion == 'R':     #Para dispositivos con relevos
        GPIO.setmode (GPIO.BOARD)
        for k in range(2):
            GPIO.setup(Reles[Selec_Puerta][k], GPIO.OUT)
        Rele_close(Puerta)

    if Tipo_Comunicacion == 'T':     #Para dispositivos con comunicacion rs485
        Comando_Rele(Puerta, 2)
#-----------------------------------------------------------
def Rele_close(Puerta):
    global Reles
    Selec_Puerta  =int (Puerta[22])
    GPIO.output(Reles[Selec_Puerta][0], GPIO.HIGH)# Entrada
    GPIO.output(Reles[Selec_Puerta][1], GPIO.HIGH)# Salida
#-----------------------------------------------------------
def Actividad_Rele(Puerta, Direccion):
    global Reles
    Tiempo_Rele =int(Get_File(Puerta+CONF_TIEM_RELE))
    Selec_Puerta =int (Puerta[22])

    GPIO.output(Reles[Selec_Puerta][Direccion], GPIO.LOW)
    time.sleep(Tiempo_Rele)
    GPIO.output(Reles[Selec_Puerta][Direccion], GPIO.HIGH)
#-----------------------------------------------------------
def Comando_Rele(Puerta, Direccion): #modificar a COM_TX_RELE revizar funcionamiento

    Tiempo_Rele =int(Get_File(Puerta+CONF_TIEM_RELE))
    Clear_File(Puerta+COM_TX_RELE)

    if Direccion == 0:      Set_File(Puerta+COM_TX_RELE,"¿00000004000" + str(Tiempo_Rele) + "?") #Entrar
    elif Direccion == 1:    Set_File(Puerta+COM_TX_RELE,"¿00000004010" + str(Tiempo_Rele) + "?") #Salir
    elif Direccion == 2:    Set_File(Puerta+COM_TX_RELE,"¿000000040300?")                        #Cerrar
#-----------------------------------------------------------
def Entrar(Puerta):
    Tipo_Comunicacion = Get_File(Puerta+CONF_COMU_RELE)
    if Tipo_Comunicacion == 'T':     Comando_Rele(Puerta, 0)       #Para dispositivos CCCB
    if Tipo_Comunicacion == 'R':     Actividad_Rele(Puerta, 0)     #Para dispositivos con relevos
#-----------------------------------------------------------
def Salir(Puerta):
    Tipo_Comunicacion = Get_File(Puerta+CONF_COMU_RELE)
    if Tipo_Comunicacion == 'T':    Comando_Rele(Puerta, 1)       #Para dispositivos CCCB
    if Tipo_Comunicacion == 'R':    Actividad_Rele(Puerta, 1)     #Para dispositivos con relevos
#-----------------------------------------------------------
def Cerrado(Puerta):

    Tipo_Comunicacion = Get_File(Puerta+CONF_COMU_RELE)
    if Tipo_Comunicacion == 'T':    Comando_Rele(Puerta, 2)     #Para dispositivos CCCB
    if Tipo_Comunicacion == 'R':    Rele_close(Puerta)          #Para cerrar pines
#-----------------------------------------------------------
def Activar_salida(Puerta):
    Selec_Puerta =int (Puerta[22])
    if VECTOR_Salidas[Selec_Puerta].isAlive() is False:
        VECTOR_Salidas[Selec_Puerta]  = threading.Thread(target=Salir   , args =(Puerta,) )
        VECTOR_Salidas[Selec_Puerta].start()
#-----------------------------------------------------------
def Activar_Entrada(Puerta):
    Selec_Puerta =int (Puerta[22])
    if VECTOR_Entradas[Selec_Puerta].isAlive() is False:
        VECTOR_Entradas[Selec_Puerta]  = threading.Thread(target=Entrar   , args =(Puerta,) )
        VECTOR_Entradas[Selec_Puerta].start()
#-----------------------------------------------------------
def Direcion_Rele(Puerta, Res):

    Direc = Get_File(Puerta+CONF_DIREC_RELE) #Leer_Archivo(13)  # Direccion_Torniquete
    if      Res == 'Access granted-E':
        if Direc == 'D':    Activar_salida(Puerta)  #Salir()
        else :              Activar_Entrada(Puerta) #Entrar()
    elif    Res == 'Access granted-S':
        if Direc == 'D':    Activar_Entrada(Puerta) #Entrar()
        else :              Activar_salida(Puerta)  #Salir()

#-----------------------------------------------------------
def Ciclo_Rele(Puerta):
    Configurar_Relevos(Puerta)
    while (True):
        time.sleep(0.5)                # 0.05
        Comando = Get_File(Puerta+COM_RELE)
        if Comando != '':
            Direcion_Rele(Puerta, Comando)
            Clear_File(Puerta+COM_RELE)

#-----------------------------------------------------------
#                   Configuracion local
#-----------------------------------------------------------

VECTOR_RELES    = []
VECTOR_Salidas  = []
VECTOR_Entradas = []

Salidas_reles = Get_File(HUB + CONF_SALIDAS)
#print Salidas_reles
#-----------------------------------------------------------
for Rele in Salidas_reles.split('\n'):
    if len(Rele) > 0:
        Conf_Rele = Rele.split(".")
        #print Conf_Rele[0]
        #print Conf_Rele[1]
        #VECTOR_LECTORAS.append(LECTORAS (Conf_Lector[0], Conf_Lector[1], Conf_Lector[2]))
        if Conf_Rele[0] == 'S0':
            #print 'dentro s0'
            VECTOR_RELES.append( threading.Thread(target = Ciclo_Rele, args =(S0,)) )
            VECTOR_Salidas.append( threading.Thread(target=Salir   , args =(S0,) ) )
            VECTOR_Entradas.append( threading.Thread(target=Entrar  , args =(S0,) ) )
        if Conf_Rele[0] == 'S1':
            VECTOR_RELES.append( threading.Thread(target = Ciclo_Rele, args =(S1,)) )
            ECTOR_Salidas.append( threading.Thread(target=Salir   , args =(S1,) ) )
            VECTOR_Entradas.append( threading.Thread(target=Entrar  , args =(S1,) ) )
        if Conf_Rele[0] == 'S2':
            VECTOR_RELES.append( threading.Thread(target = Ciclo_Rele, args =(S2,)) )
            ECTOR_Salidas.append( threading.Thread(target=Salir   , args =(S2,) ) )
            VECTOR_Entradas.append( threading.Thread(target=Entrar  , args =(S2,) ) )
#-----------------------------------------------------------
for Rele in VECTOR_RELES:
    Rele.start()
#-----------------------------------------------------------

#-----------------------------------------------------------
#-----------------------------------------------------------
#                   Ciclo principal
#-----------------------------------------------------------
#-----------------------------------------------------------



# activar cuando este configurado una puerta
print 'Hilos start'

#-----------------------------------------------------------
#-----------------------------------------------------------
#                       RESUMEN y descripciones
#-----------------------------------------------------------
#-----------------------------------------------------------

#-----------------------------------------------------------
#               Pruebas de funcioanmiento
#-----------------------------------------------------------
