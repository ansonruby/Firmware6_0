from lib.Lib_Rout import *
from lib.Lib_File import Get_File, Clear_Line, Set_File, Add_Line_End
from lib.Fun_Tipo_NFC import MD5
from lib.Lib_Binary_Search import Binary_Search_Id, Binary_Remove_Id
from lib.Lib_Request_Json import send_petition
import json
import re
import time
import datetime


def Validar_Acceso(access_code, tipo_acceso, medio_acceso, lectora):
    user_id = False

    if medio_acceso == 1:
        user_id = Validar_QR(access_code, tipo_acceso)
    elif medio_acceso == 2:
        user_id = Validar_PIN(access_code, tipo_acceso)
    elif medio_acceso == 11:
        user_id = Validar_NFC(access_code, tipo_acceso)
    if user_id:
        Enviar_Respuesta(user_id, tipo_acceso, medio_acceso, lectora)
    else:
        Respaldo_Online(access_code, lectora)


def Validar_QR_Antiguo(access_data, tipo_acceso, medio_acceso, lectora):
    valid_access = False
    access_key = False

    if tipo_acceso == 1:
        access_key = access_data[1]
        db = Get_File(S0+TAB_USER_TIPO_1).strip().split("\n")
        for access_db in db:
            if access_db == "":
                continue

            key_db = access_db.split(".")[0]
            if access_key == key_db:
                valid_access = True
                break
    elif tipo_acceso == 3:
        access_key = ".".join(access_data[0:3])
        db = Get_File(S0+TAB_USER_TIPO_3).split("\n")

        for i, access_db in enumerate(db):
            if access_db == "":
                continue
            key_db = ".".join(access_db.split(".")[0:3])
            if access_key == key_db:
                Clear_Line(S0+TAB_USER_TIPO_3, i+1)
                access_key = False
                valid_access = True
                break
    elif tipo_acceso == 4:
        access_key = ".".join(access_data[1:5])
        db = Get_File(S0+TAB_USER_TIPO_4).strip().split("\n")
        for access_db in db:
            if access_db == "":
                continue
            key_db = ".".join(access_db.split(".")[1:5])
            if access_key == key_db:
                valid_access = True
                break

    respuesta_acceso = "Access denied"
    if valid_access:
        direction = "0"

        if tipo_acceso != 3:
            direction = Definir_Direccion(key_db)

        respuesta_acceso = "Access granted-E" if direction == "0" else "Access granted-S"
        read_time = int(time.time()*1000)
        athorization_code = ".".join(access_data) + "."+str(read_time) + \
            "."+str(medio_acceso) + "."+direction+"."+"1"
        Add_Line_End(S0+TAB_ENV_SERVER, athorization_code+"\n")
        comand_res = [
            COM_RES,
            COM_RES_S1,
            COM_RES_S2
        ]

        # Envio modulo respuesta
        Set_File(S0+comand_res[lectora], respuesta_acceso)
    else:
        Respaldo_Online("<" + ".".join(access_data) + ">", lectora)


def Validar_QR(access_code, tipo_acceso):
    separator = re.findall("F[A-F]", access_code)

    # Separador no encontrado
    if len(separator) == 0:
        return False
    else:
        separator = separator[0]

    user_id, final_data = access_code.split(separator)
    user_id = int(user_id)
    read_time = int(time.time()*1000)
    time_len = len(str(read_time))
    qr_time = int(final_data[:time_len])
    extra_data = final_data[time_len:]

    # validaciones de tiempo para qrs dinamicos
    if tipo_acceso in [1, 2, 4, 5]:

        # Tiempo de lectura excedido
        time_diff = read_time-qr_time
        if time_diff <= 0 or time_diff > 8000:
            return False

        # Dia de la semana incorrecto => F0 - FF (Lunes a domingo)
        weekdays = ["F0", "FA", "FB", "FC", "FD", "FE", "FF"]
        if weekdays[datetime.datetime.today().weekday()] != separator:
            return False

    tabs_users = [
        NEW_TAB_USER_TIPO_1,
        NEW_TAB_USER_TIPO_2,
        NEW_TAB_USER_TIPO_3,
        NEW_TAB_USER_TIPO_4,
        NEW_TAB_USER_TIPO_5
    ]

    file_db = S0+tabs_users[tipo_acceso-1]
    access_index = False
    if tipo_acceso == 3:
        access_index = Binary_Remove_Id(file_db, user_id)
    else:
        access_index = Binary_Search_Id(file_db, user_id)

    if access_index:
        return str(user_id)


def Validar_PIN(access_code, tipo_acceso):
    valid_access = False
    access_key = False
    if tipo_acceso == 1:
        access_key = MD5(access_code)
        db = Get_File(S0+TAB_USER_TIPO_1).strip().split("\n")
        for access_db in db:
            if access_db == "":
                continue
            key_db, encrypted_pin = access_db.split(".")
            if access_key == encrypted_pin:
                valid_access = True
                break

    if valid_access:
        return key_db


def Validar_NFC(access_code, tipo_acceso):
    valid_access = False
    access_key = False
    if tipo_acceso == 6:
        access_key = MD5(access_code)
        db = Get_File(S0+TAB_USER_TIPO_6).strip().split("\n")
        for access_db in db:
            if access_db == "":
                continue
            key_db, encrypted_pin = access_db.split(".")
            if access_key == encrypted_pin:
                valid_access = True
                break

    if valid_access:
        return key_db


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

        if str(access_key) in users_in_json:
            direction = "1"
            users_in_json.pop(str(access_key))
        else:
            users_in_json[str(access_key)] = "1"
        users_in = json.dumps(users_in_json, indent=2)

        with open(S0+TAB_USER_IN, 'w') as dfw:
            dfw.write(users_in)
            dfw.close()

    return direction


def Enviar_Respuesta(user_id, tipo_acceso, medio_acceso, lectora):
    respuesta_acceso = "Access denied"
    if user_id:
        direction = "0"

        if tipo_acceso != 3:
            # Cambiar el id en la tabla autorizados para invitaciones multiples usos
            if tipo_acceso == 4:
                direction = Definir_Direccion(
                    str(tipo_acceso)+"."+str(user_id))
            else:
                direction = Definir_Direccion(str(user_id))

        respuesta_acceso = "Access granted-E" if direction == "0" else "Access granted-S"
        read_time = int(time.time()*1000)
        athorization_code = str(user_id) + "."+str(read_time) + \
            "."+str(medio_acceso) + "."+direction+"."+"1"
        Add_Line_End(S0+TAB_ENV_SERVER, athorization_code+"\n")

    comand_res = [
        COM_RES,
        COM_RES_S1,
        COM_RES_S2
    ]

    # Envio modulo respuesta
    Set_File(S0+comand_res[lectora], respuesta_acceso)


def Respaldo_Online(access_code, lectora):
    respuesta_acceso = "Access denied"

    respuesta_server = send_petition(
        "grant", data={"data": access_code})

    if respuesta_server:
        respuesta_acceso = respuesta_server

    comand_res = [
        COM_RES,
        COM_RES_S1,
        COM_RES_S2
    ]

    # Envio modulo respuesta
    Set_File(S0+comand_res[lectora], respuesta_acceso)
