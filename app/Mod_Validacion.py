from lib.Lib_File import Get_File
from lib.Lib_Rout import *


def Validar_Acceso_Antiguos(*args):
    medio_acceso = args[2]
    ans = False
    if medio_acceso == 1:
        ans = Validar_QR_Antiguo(*args)
    print ans


def Validar_QR_Antiguo(access_data, tipo_acceso, medio_acceso, lectora):
    ans = False
    if tipo_acceso == 1:
        db = Get_File(S0+TAB_USER_TIPO_1).strip()
        ans = db
    elif tipo_acceso == 4:
        db = Get_File(S0+TAB_USER_TIPO_1).strip().split("\n")
        ans = db
    return ans

# def auth_petition(access_data, ws, direction="0"):
#     try:
#         qr_list = []
#         data = qr.split(".")
#         ans = False
#         access_identifier = "1"
#         with open(QR_LIST_PATH, 'r', encoding='utf-8', errors='replace') as df:
#             qr_list_text = df.read().strip()
#             df.close()
#             qr_list = qr_list_text.split("\n")
#         for compare_qr in qr_list:
#             if compare_qr == "":
#                 continue

#     except Exception as e:
#         pass

# def save_authorization():
#     with open(AUTH_LIST_PATH, 'a', encoding='utf-8', errors='replace') as dfw:
#         dfw.write(qr+"."+str(int(time.time()*1000.0)) +
#                   "."+access_identifier+"."+direction+".1."+str(ws.server_id)+"\n")
#         dfw.close()
