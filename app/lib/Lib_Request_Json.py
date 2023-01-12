import requests
import json

petition_time_out = 60 * 60


# method can be GET, OPTIONS, HEAD, POST, PUT, PATCH, or DELETE
def send_petition(url, method="GET", params=None, data=None, json_data=None, headers=None, timeout=petition_time_out):
    response = None
    try:
        response = requests.request(method, url, params=params, data=data,
                                    json=json_data, headers=headers, timeout=timeout)
        return response.json()
    except (TypeError, ValueError):
        return response.text
    except: 
        return False


# print send_petition("http://localhost:3000/get_users")
# print send_petition("http://localhost:3000/grant",method="POST",data={"datas":"a1b2"})
