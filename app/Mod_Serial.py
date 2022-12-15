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



#---------------------------------
#           Librerias personales
#---------------------------------
from lib.Fun_Mod_Serial import *  # importar con los mismos nombres

#---------------------------------
#           Configuraciones de lectoras
#---------------------------------
#print HUB + CONF_LECTORAS
VECTOR_LECTORAS = []
Lectoras = Get_File(HUB + CONF_LECTORAS)
for Lectora in Lectoras.split('\n'):
    if len(Lectora) > 0:
        Conf_Lector = Lectora.split(".")
        VECTOR_LECTORAS.append(LECTORAS (Conf_Lector[0], Conf_Lector[1]))

for Lectora in VECTOR_LECTORAS:
    Lectora.Inicio_Lectora()

#---------------------------------
#           pruebas
#---------------------------------
#LECTORA_1 = LECTORAS ('0', 'QR600-VHK-E')
#LECTORA_2 = LECTORAS ('1', 'QR600-VHK-E')
#LECTORA_1.Inicio_Lectora()
#LECTORA_2.Inicio_Lectora()
