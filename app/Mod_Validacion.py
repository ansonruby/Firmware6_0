from lib.Lib_Rout import *
from lib.Lib_File import Get_File, Set_File, Add_Line_End, Get_Line
from lib.Fun_Tipo_NFC import MD5
from lib.Lib_Binary_Search import Binary_Search_Id, Binary_Remove_Id
from lib.Lib_Request_Json import send_petition
from lib.Lib_settings import Get_Mod_Validacion, Get_Lectoras
from Mod_Actualizaciones import send_autorizations, Actualizacion_Usuarios_Periodica
import json
import re
import time
import datetime
import os

Configs = Get_Mod_Validacion()
Lectoras = Get_Lectoras()

config_access = "Acceso fisico"  # "Accesos" o "Acceso dinamico" o "Acceso fisico"

if "Configuracion_Acceso" in Configs:
    config_access = Configs["Configuracion_Acceso"]


def Validar_Acceso(access_code, tipo_acceso, medio_acceso, lectora):
    valid_access = False
    if medio_acceso == 1:
        valid_access = Validar_QR(access_code, tipo_acceso, lectora)
    elif medio_acceso == 2:
        valid_access = Validar_PIN(access_code, tipo_acceso, lectora)
    elif medio_acceso == 11:
        valid_access = Validar_NFC(access_code, tipo_acceso, lectora)

    if valid_access:
        user_index, direction_ref, access_limit_quantity = valid_access
        Enviar_Respuesta(user_index, tipo_acceso,
                         medio_acceso, lectora, direction_ref, access_limit_quantity)
    else:
        Respaldo_Online({
            "access_type": tipo_acceso,
            "access_medium": medio_acceso,
            "access_code": access_code,
            "reader": lectora
        }, lectora)


def Validar_QR_Antiguo(access_data, tipo_acceso, medio_acceso, lectora):
    Respaldo_Online({
        "access_type": tipo_acceso,
        "access_medium": medio_acceso,
        "data": "<" + ".".join(access_data) + ">",
        "old_qr_code": True
    }, lectora)


def Validar_QR(access_code, tipo_acceso, lectora):
    separator = re.findall("F[A-F]", access_code)

    # Separador no encontrado
    if len(separator) == 0:
        return False
    else:
        separator = separator[0]

    user_index, final_data = access_code.split(separator)
    read_time = int(time.time()*1000)
    time_len = len(str(read_time))
    qr_time_str = final_data[:time_len]
    qr_time = int(qr_time_str) if len(qr_time_str) > 0 else 0
    extra_data = final_data[time_len:]

    direction_ref = False
    access_limit_quantity = 0
    invitation_index = False

    if tipo_acceso in [4]:
        direction_ref = user_index
        user_index, invitation_index = user_index.split("E")

    # validaciones de tiempo para qrs dinamicos
    if tipo_acceso in [1, 2, 4, 5]:

        # Tiempo de lectura excedido (milisegundos)
        time_diff = read_time-qr_time
        if time_diff <= 0 or time_diff > 1000 * 8:
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
    location = get_location_of_reader(lectora)
    file_db = location+tabs_users[tipo_acceso-1]
    access_index = False
    access_index = Binary_Search_Id(file_db, user_index)

    if not access_index:
        return False

    db_data = Get_Line(file_db, access_index).strip().split(".")

    if tipo_acceso in [1, 2, 5]:
        direction_ref = db_data[-1]

    if tipo_acceso in [1]:
        access_limit_quantity = int(db_data[2])

    user_in_data = Buscar_usuario_adentro(
        direction_ref, lectora)

    if user_in_data:
        user_in_index, user_access_quantity = user_in_data
        if access_limit_quantity != 0 and access_limit_quantity <= user_access_quantity:
            return False
        elif user_access_quantity % 1 != 0:
            if tipo_acceso in [2, 4]:
                return (user_in_index, direction_ref, access_limit_quantity)
            else:
                return (user_index, direction_ref, access_limit_quantity)

    if tipo_acceso in [1, 5]:
        week_schedules = json.loads(db_data[1])
        if not separator in week_schedules:
            return False

        day_schedules = week_schedules[separator]

        valid_access_time = False
        for schedule in day_schedules:
            start_time_day = schedule[0].split(":")
            start_time = datetime.time(
                int(start_time_day[0]), int(start_time_day[1]))

            end_time_day = schedule[1].split(":")
            end_time = datetime.time(
                int(end_time_day[0]), int(end_time_day[1]))

            if start_time < datetime.datetime.now().time() and end_time > datetime.datetime.now().time():
                valid_access_time = True
                break

        if not valid_access_time:
            return False

    elif tipo_acceso == 2:
        bookings = json.loads(db_data[1])

        active_booking = False
        for booking_id, (start_time, end_time) in bookings.items():
            if start_time <= read_time and end_time >= read_time:
                active_booking = True
                user_index = booking_id
                break

        if not active_booking:
            return False

    elif tipo_acceso == 3:

        # Fuera del tiempo de uso (milisegundos)
        if not (read_time > int(db_data[1]) and read_time < int(db_data[2])):
            return False

        Binary_Remove_Id(file_db, user_index)

    elif tipo_acceso == 4:
        invitations = json.loads(db_data[1])

        if not invitation_index in invitations:
            return False

        start_time = int(invitations[invitation_index][0])
        end_time = int(invitations[invitation_index][1])

        if start_time <= read_time and end_time >= read_time:
            user_index = invitation_index
        else:
            return False

    return (str(user_index), direction_ref, access_limit_quantity)


def Validar_PIN(access_code, tipo_acceso, lectora):
    location = get_location_of_reader(lectora)
    file_db = location+NEW_TAB_USER_TIPO_7

    access_index = Binary_Search_Id(file_db, access_code)

    if not access_index:
        return False

    db_data = Get_Line(file_db, access_index).strip().split(".")


    direction_ref = db_data[-1]

    access_limit_quantity = int(db_data[2])

    user_in_data = Buscar_usuario_adentro(
        direction_ref, lectora)

    if user_in_data:
        user_in_index, user_access_quantity = user_in_data
        if access_limit_quantity != 0 and access_limit_quantity <= user_access_quantity:
            return False
        elif user_access_quantity % 1 != 0:
            return (user_in_index, direction_ref, access_limit_quantity)

    if tipo_acceso == 7:

        weekdays = ["F0", "FA", "FB", "FC", "FD", "FE", "FF"]

        today = weekdays[datetime.datetime.today().weekday()]
        week_schedules = json.loads(db_data[1])
        if not today in week_schedules:
            return False

        day_schedules = week_schedules[today]

        valid_access_time = False
        for schedule in day_schedules:
            start_time_day = schedule[0].split(":")
            start_time = datetime.time(
                int(start_time_day[0]), int(start_time_day[1]))

            end_time_day = schedule[1].split(":")
            end_time = datetime.time(
                int(end_time_day[0]), int(end_time_day[1]))

            if start_time < datetime.datetime.now().time() and end_time > datetime.datetime.now().time():
                valid_access_time = True
                break

        if not valid_access_time:
            return False

    return (str(access_code), direction_ref,access_limit_quantity)


def Validar_NFC(access_code, tipo_acceso, lectora):
    valid_access = False
    access_key = False
    location = get_location_of_reader(lectora)
    if tipo_acceso == 6:
        access_key = MD5(access_code)
        db = Get_File(location+TAB_USER_TIPO_6).strip().split("\n")
        for access_db in db:
            if access_db == "":
                continue
            db_data = access_db.split(".")
            nfc_code = db_data[0]

            if access_key == nfc_code:

                weekdays = ["F0", "FA", "FB", "FC", "FD", "FE", "FF"]

                today = weekdays[datetime.datetime.today().weekday()]
                week_schedules = json.loads(db_data[1])
                if not today in week_schedules:
                    return False

                day_schedules = week_schedules[today]

                valid_access_time = False
                for schedule in day_schedules:
                    start_time_day = schedule[0].split(":")
                    start_time = datetime.time(
                        int(start_time_day[0]), int(start_time_day[1]))

                    end_time_day = schedule[1].split(":")
                    end_time = datetime.time(
                        int(end_time_day[0]), int(end_time_day[1]))

                    if start_time < datetime.datetime.now().time() and end_time > datetime.datetime.now().time():
                        valid_access_time = True
                        break

                if valid_access_time:
                    direction_ref = db_data[-1]
                    valid_access = True
                break

    if valid_access:
        return (direction_ref, direction_ref)


def Buscar_usuario_adentro(access_key,  lectora):
    global config_access
    location = get_location_of_reader(lectora)
    if (config_access == "Acceso fisico" and get_direction_of_reader(lectora) == 1) or config_access == "Acceso dinamico":
        if access_key and access_key != "":
            users_in = ""
            with open(location+TAB_USER_IN, 'r') as df:
                users_in = df.read().strip()
                df.close()
            try:
                users_in_json = json.loads(users_in)
            except Exception as e:
                users_in_json = {}

            if not str(access_key) in users_in_json:
                return False

            return users_in_json[str(access_key)][0:2]


def Definir_Direccion(access_key, user_index, access_limit_quantity, lectora):
    global config_access

    direction = "0"
    location = get_location_of_reader(lectora)

    if config_access == "Accesos":
        return direction
    elif config_access == "Acceso fisico":
        if access_key and access_key != "":
            users_in = ""
            with open(location+TAB_USER_IN, 'r') as df:
                users_in = df.read().strip()
                df.close()
            try:
                users_in_json = json.loads(users_in)
            except Exception as e:
                users_in_json = {}

            if get_direction_of_reader(lectora) and str(access_key) in users_in_json:
                users_in_json.pop(str(access_key))
            else:
                users_in_json[str(access_key)] = [user_index, "1"]

            users_in = json.dumps(users_in_json, indent=4)
            with open(location+TAB_USER_IN, 'w') as dfw:
                dfw.write(users_in)
                dfw.close()

        return str(int(get_direction_of_reader(lectora)))
    elif config_access == "Acceso dinamico":
        if access_key and access_key != "":
            users_in = ""
            with open(location+TAB_USER_IN, 'r') as df:
                users_in = df.read().strip()
                df.close()
            try:
                users_in_json = json.loads(users_in)
            except Exception as e:
                users_in_json = {}

            if str(access_key) in users_in_json:
                if int(access_limit_quantity) != 0:
                    access_cycle = users_in_json[str(access_key)][1]
                    if (access_cycle % 1) != 0:
                        direction = "1"
                    users_in_json[str(access_key)] = [
                        user_index, access_cycle + 0.5]
                else:
                    direction = "1"
                    users_in_json.pop(str(access_key))
            else:
                users_in_json[str(access_key)] = [user_index, 0.5]
            users_in = json.dumps(users_in_json, indent=4)

            with open(location+TAB_USER_IN, 'w') as dfw:
                dfw.write(users_in)
                dfw.close()

        return direction


def Enviar_Respuesta(user_index, tipo_acceso, medio_acceso, lectora, direction_ref, access_limit_quantity):
    respuesta_acceso = "Access denied"
    if user_index:
        direction = "0"

        if tipo_acceso != 3:
            # Cambiar el id en la tabla autorizados para invitaciones multiples usos
            direction = Definir_Direccion(
                str(direction_ref), user_index, access_limit_quantity, lectora)

        respuesta_acceso = "Access granted-E" if direction == "0" else "Access granted-S"
        read_time = int(time.time()*1000)
        athorization_code = str(user_index) + "."+str(read_time) + \
            "."+str(medio_acceso) + "."+direction+"."+"1"
        tabs_autorizaciones = [
            NEW_AUTO_USER_TIPO_1,
            NEW_AUTO_USER_TIPO_2,
            NEW_AUTO_USER_TIPO_3,
            NEW_AUTO_USER_TIPO_4,
            NEW_AUTO_USER_TIPO_5,
            NEW_AUTO_USER_TIPO_6,
            NEW_AUTO_USER_TIPO_7
        ]
        location = get_location_of_reader(lectora)
        Add_Line_End(
            location+tabs_autorizaciones[tipo_acceso-1],
            athorization_code+"\n"
        )

    comand_res = [
        COM_RES,
        COM_RES_S1,
        COM_RES_S2
    ]

    # Envio modulo respuesta
    Set_File(os.path.join(FIRM, HUB, comand_res[lectora]), respuesta_acceso)


def Respaldo_Online(data, lectora):
    respuesta_acceso = "Access denied"
    try:
        respuesta_server = False
        if "old_qr_code" in data:
            respuesta_server = send_petition(
                "grant", method="POST", json_data=data, timeout=10)
            if respuesta_server and respuesta_server.ok:
                respuesta_acceso = respuesta_server.text
                respuesta_acceso = respuesta_acceso if "Access granted" in respuesta_acceso else "Access denied"
        else:
            send_autorizations()
            respuesta_server = send_petition(
                "online_backup", method="POST", json_data=data)
            if respuesta_server and respuesta_server.ok:
                respuesta_server = respuesta_server.json()
                respuesta_acceso = respuesta_server["access_answer"]
                if "Access granted" in respuesta_server["access_answer"]:
                    Definir_Direccion(
                        respuesta_server["user_id"], respuesta_server["user_index"], respuesta_server["access_limit_quantity"], lectora)
    except:
        pass

    comand_res = [
        COM_RES,
        COM_RES_S1,
        COM_RES_S2
    ]

    # Envio modulo respuesta
    Set_File(os.path.join(FIRM, HUB, comand_res[lectora]), respuesta_acceso)
    Actualizacion_Usuarios_Periodica()


def get_location_of_reader(lectora):
    global Lectoras

    locations = {
        "S0": S0,
        "S1": S1,
        "S2": S2
    }

    for reader in Lectoras:
        if "Puerto" in reader and "Locacion" in reader and int(reader["Puerto"]) == int(lectora):
            return locations[reader["Locacion"]]

    return S0


def get_direction_of_reader(lectora):
    global Lectoras

    for reader in Lectoras:
        if "Puerto" in reader and "Direccion" in reader and int(reader["Puerto"]) == int(lectora):
            return reader["Direccion"] == "EXIT"

    # 0 for entrys
    # 1 for exits

    return int(int(lectora) % 2)
