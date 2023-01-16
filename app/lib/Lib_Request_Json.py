from Lib_File import *            # importar con los mismos nombres
from Lib_Rout import *
import requests

petition_time_out = 60 * 60

fixed_urls = {
    "get_users": "/api/access/get_granted_users_pi",
    "grant": "/api/access/grant",
    "1": "/api/access/keyboard_access",
    "2": "/api/access/set_in_out_activity",
    "3": "/api/access/verify_conection",
    "4": "/api/firmware/review_update",
    "5": "/api/firmware/confirm_update"
}

# method can be GET, OPTIONS, HEAD, POST, PUT, PATCH, or DELETE


def send_petition(url, method="GET", params=None, data=None, json_data=None, headers=None, timeout=petition_time_out):
    response = None
    petition_url = url
    if url in fixed_urls:
        petition_url = Get_Rout_server() + fixed_urls[url]
    elif not "http" in url:
        petition_url = Get_Rout_server() + url

    try:
        response = requests.request(method, petition_url, params=params, data=data,
                                    json=json_data, headers=headers, timeout=timeout)
        return response.json()
    except (TypeError, ValueError):
        if response:
            return response.text
        else:
            return False
    except:
        return False


def Get_Rout_server():
    mejor_opcion = Get_File(S0+CONF_M_CONEX_SERVER)
    IP_Ser = Get_File(S0+CONF_IP_SERVER)
    Domi_Ser = Get_File(S0+CONF_DOMI_SERVER)

    opciones = {'0': 'http://' + IP_Ser,
                '1': 'http://' + Domi_Ser,
                '10': 'http://' + IP_Ser,
                '11': 'http://' + IP_Ser,
                '100': 'https://' + IP_Ser,
                '101': 'https://' + IP_Ser,
                '110': 'https://' + IP_Ser,
                '111': 'https://' + IP_Ser,
                '1000': 'https://' + Domi_Ser,
                '1001': 'https://' + Domi_Ser,
                '1010': 'http://' + IP_Ser,
                '1011': 'http://' + IP_Ser,
                '1100': 'https://' + IP_Ser,
                '1101': 'https://' + IP_Ser,
                '1110': 'https://' + IP_Ser,
                '1111': 'https://' + IP_Ser}

    # return 'https://solutions.fusepong.com'
    return 'http://192.168.0.103:3000'
    # return opciones[mejor_opcion]


# print send_petition("get_users")
# print send_petition("/api/access/get_granted_users_pi")
# print send_petition("http://localhost:3000/api/access/get_granted_users_pi")
# print send_petition("grant", method="POST", data={"data": "a1b2"})
