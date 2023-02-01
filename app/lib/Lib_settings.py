#---------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------
"""

Autor:  Luding Castaneda,
        Anderson Amaya Pulido

Libreria personal para manejo de archivos de texto.
1)  manejo y busqueda de linea como base de Datos










"""
#---------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------


#---------------------------------------------------------------------------------------
#                                   importar complementos
#---------------------------------------------------------------------------------------

import os
import json


from Lib_File import *  # importar con los mismos nombres
from Lib_Rout import *  # importar con los mismos nombres
#---------------------------------------------------------------------------------------
#                                   Funciones para el manejo de archivos
#---------------------------------------------------------------------------------------

#---------------------------------------------------------------------------------------
#                   Manejo del archivo de configuraciones
#---------------------------------------------------------------------------------------
def Get_Mod_Actualizaciones():
	data = Get_File_Json(CONF_HUB)
	return data["Mod_Actualizaciones"]
#---------------------------------------------------------------------------------------
def Get_Mod_Respuesta():
	data = Get_File_Json(CONF_HUB)
	return data["Mod_Respuesta"]
#---------------------------------------------------------------------------------------	
def Get_Lectoras():
	data = Get_File_Json(CONF_HUB)
	return data["Lectoras"]
#---------------------------------------------------------------------------------------
def Get_Salidas():
	data = Get_File_Json(CONF_HUB)
	return data["Reles"]
#---------------------------------------------------------------------------------------
def Get_Pat_Server():
	data = Get_File_Json(CONF_HUB)
	return data["HUB"]["Ser_Dominio"], data["HUB"]["Ser_Ip"], data["HUB"]["Mejor_Coneccion"]






#---------------------------------------------------------------------------------------
#-----------------------------------------------------------
#                       RESUMEN y descripciones
#-----------------------------------------------------------
#---------------------------------------------------------------------------------------

#---------------------------------------------------------------------------------------
#                   Manejo del archivo Generales
#---------------------------------------------------------------------------------------


#---------------------------------------------------------------------------------------
#                   Manejo del archivo por lineas
#---------------------------------------------------------------------------------------
