#
def auth_petition(access_data, ws, direction="0"):
    try:
        qr_list = []
        data = qr.split(".")
        ans = False
        access_identifier = "1"
        with open(QR_LIST_PATH, 'r', encoding='utf-8', errors='replace') as df:
            qr_list_text = df.read().strip()
            df.close()
            qr_list = qr_list_text.split("\n")
        for compare_qr in qr_list:
            if compare_qr == "":
                continue

    except Exception as e:
        pass


def save_authorization():
    with open(AUTH_LIST_PATH, 'a', encoding='utf-8', errors='replace') as dfw:
        dfw.write(qr+"."+str(int(time.time()*1000.0)) +
                  "."+access_identifier+"."+direction+".1."+str(ws.server_id)+"\n")
        dfw.close()
