import json

from lib.Lib_File import *  # importar con los mismos nombres
from lib.Lib_Rout import *  # importar con los mismos nombres

Ev = Get_File('../db/HUB/Config/Config_Hub.json')
#print Ev
data = json.loads(Ev)
#print len (x_json["S0"]["Lectoras"])
print data["S0"]["Lectoras"][0]["Nombre"]
print data["S0"]["Lectoras"][0]["Rele"]

print data.keys(), len(data.keys())

#----------------------------------------------
#   Generador de locacion y eliminacion
#----------------------------------------------
if len(data.keys())>= 2:
    for Key_Location in data.keys():#numero de locaciones a generar
        print Key_Location



"""
with open('../db/HUB/Config/Config_Hub.json') as file:
    data = json.load(file)

    for Key_Location in data.keys():#numero de locaciones a generar
        print Key_Location
        for config in data[Key_Location].keys():
            print config, len(config)
            for parametro in data[Key_Location][config].keys():
                #print data[Key_Location][config]
                print parametro, len(parametro)

"""

"""
for Locacion in data[Key_Location]:
print 'Conf_Lectora:', Locacion['Lectora']
print 'Conf_Lectora:', Locacion['Salida']
"""
