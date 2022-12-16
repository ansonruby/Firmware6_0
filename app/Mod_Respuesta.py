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
from lib.Lib_File import *  # importar con los mismos nombres
from lib.Lib_Rout import *  # importar con los mismos nombres


#---------------------------------------
#           Configuraciones de lectoras
#---------------------------------------




def avilitaciones():
    #Set_File(S0 + COM_RES)
    Set_File(S0+COM_RELE,'Access granted-E')

avilitaciones()


"""



#print S0 + COM_RES
print  Get_File(S0 + COM_RES)

while (True):
try :
time.sleep(0.5)                # 0.05
Comando = Get_File(S0 + COM_RES)
if Comando != '':
#Direcion_Rele(Puerta, Comando)
Clear_File(S0 + COM_RES)
except SerialException:
print 'error'
"""
