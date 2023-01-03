from lib.Lib_Rout import *
from lib.Lib_File import Get_File
from lib.Fun_Tipo_NFC import MD5
import json



def Validar_Acceso(access_data, tipo_acceso, medio_acceso, lectora):
    ans = False
    if medio_acceso == 1:
        ans = Validar_QR_Antiguo(access_data, tipo_acceso)
    elif medio_acceso == 2:
        ans = Validar_PIN(access_data, tipo_acceso)
    elif medio_acceso == 11:
        ans = Validar_NFC(access_data, tipo_acceso)
    print ans


def Validar_QR_Antiguo(access_data, tipo_acceso, medio_acceso, lectora):
    access_valido = False
    access_key = False
    if tipo_acceso == 1:
        access_key = access_data[1]
        db = Get_File(S0+TAB_USER_TIPO_1).strip().split("\n")
        for access_db in db:
            if access_data == "":
                continue

            key_db = access_db.split(".")[0]
            if access_key == key_db:
                access_valido = True
                break
    elif tipo_acceso == 3:
        access_key = ".".join(access_data[0:3])
        db = Get_File(S0+TAB_USER_TIPO_3).strip().split("\n")
        for access_db in db:
            if access_data == "":
                continue
            key_db = ".".join(access_db.split(".")[0:3])
            if access_key == key_db:
                access_key = False
                access_valido = True
                break
    elif tipo_acceso == 4:
        access_key = ".".join(access_data[1:5])
        db = Get_File(S0+TAB_USER_TIPO_4).strip().split("\n")
        for access_db in db:
            if access_data == "":
                continue
            key_db = ".".join(access_db.split(".")[1:5])
            if access_key == key_db:
                access_valido = True
                break

    respuesta_acceso = "Access denied"
    if access_valido:
        direction = Definir_Direccion(access_key)
        respuesta_acceso = "Access granted-E" if direction == "0" else "Access granted-S"

    print respuesta_acceso



def Validar_PIN(access_data, tipo_acceso):
    access_valido = False
    access_key = False
    if tipo_acceso == 1:
        access_key = MD5(access_data)
        db = Get_File(S0+TAB_USER_TIPO_1).strip().split("\n")
        for access_db in db:
            if access_db == "":
                continue
            key_db, encrypted_pin = access_db.split(".")
            if access_key == encrypted_pin:
                access_valido = True
                break
    respuesta_acceso = "Access denied"
    if access_valido:
        direction = Definir_Direccion(key_db)
        respuesta_acceso = "Access granted-E" if direction == "0" else "Access granted-S"

    return respuesta_acceso


def Validar_NFC(access_data, tipo_acceso):
    access_valido = False
    access_key = False
    if tipo_acceso == 6:
        access_key = MD5(access_data)
        db = Get_File(S0+TAB_USER_TIPO_6).strip().split("\n")
        for access_db in db:
            if access_db == "":
                continue
            key_db, encrypted_pin = access_db.split(".")
            if access_key == encrypted_pin:
                access_valido = True
                break
    respuesta_acceso = "Access denied"
    if access_valido:
        direction = Definir_Direccion(key_db)
        respuesta_acceso = "Access granted-E" if direction == "0" else "Access granted-S"

    return respuesta_acceso


def Definir_Direccion(access_key):
    direction = "0"

    if access_key and access_key != "":
        users_in = ""
        with open(S0+TAB_USER_IN, 'r') as df:
            users_in = df.read().strip()
            df.close()
        try:
            users_in_json = json.loads(users_in)
        except Exception as e:
            users_in_json = {}

        if access_key in users_in_json:
            direction = "1"
            users_in_json.pop(access_key)
        else:
            users_in_json[access_key] = "1"
        users_in = json.dumps(users_in_json, indent=2)

        with open(S0+TAB_USER_IN, 'w') as dfw:
            dfw.write(users_in)
            dfw.close()

    return direction
