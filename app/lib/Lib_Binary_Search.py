# ---------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------
"""

Autor: Luding Andres Castaneda Garcia(Por Ahora)

Libreria personal busqueda binaria.











"""
# ---------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------

# ---------------------------------------------------------------------------------------
#                                   importar complementos
# ---------------------------------------------------------------------------------------
from Lib_File import *
# ---------------------------------------------------------------------------------------
#                                   Funciones para el manejo de archivos
# ---------------------------------------------------------------------------------------

# ---------------------------------------------------------------------------------------
#                   Manejo de archivos Total
# ---------------------------------------------------------------------------------------


def Binary_Search(db_list, value):
    find = False
    high = len(db_list)-1
    low = 0
    mid = 0
    # rep=0
    while low <= high:
        # rep=rep+1
        mid_data = 0
        mid = (high + low) // 2
        try:
            mid_data = int(db_list[mid])
        except:
            mid_data = None
        if mid_data == value:
            find = True
            break
        elif high <= low:
            break
        elif mid_data < value:
            low = mid + 1

        elif mid_data > value:
            high = mid - 1
    # print rep
    return find, mid
# -------------------------------------------------------


# def Write_DB(code_type, user_ids):
#     user_ids = user_ids.strip()
#     folder_path = NEW_QR_TYPE_DATA_FOLDER+"Tipo_"+str(code_type)+"/"

#     if not os.path.exists(folder_path):
#         os.makedirs(folder_path)

#     file_name = folder_path+"Tabla_Usuarios.txt"
#     with open(file_name, 'w') as file:
#         file.write(user_ids)
# -------------------------------------------------------


def Binary_Search_Id(file_name, user_id):
    user_id = int(user_id)
    db = Get_File(file_name).split("\n")
    line = False
    find, position = Binary_Search(db, user_id)
    if find:
        line = position+1
    return line
# -------------------------------------------------------


def Binary_Add_Id(file_name, user_id):
    user_id = int(user_id)
    db = Get_File(file_name).split("\n")
    find, position = Binary_Search(db, user_id)
    line = False
    if not find:
        line = position+1
        try:
            if user_id > int(Get_Line(file_name, line)):
                line += 1
        except:
            pass
        data = str(user_id)
        if line <= len(db):
            data += "\n"
            Add_Line_Pos(file_name, line, str(user_id)+"\n")
        else:
            Add_Line_End(file_name,  "\n"+str(user_id))

    return line
# -------------------------------------------------------


def Binary_Remove_Id(file_name, user_id):
    user_id = int(user_id)
    db = Get_File(file_name).split("\n")
    find, position = Binary_Search(db, user_id)
    line = False
    if find:
        line = position+1
        Clear_Line(file_name, line)
        if line == len(db):
            Update_Line(file_name, line-1, Get_Line(file_name, line-1).strip())
    return line
# -------------------------------------------------------


# ---------------------------------------------------------------------------------------
# -----------------------------------------------------------
#                       Test unitarios
# -----------------------------------------------------------
# ---------------------------------------------------------------------------------------

# # Tests Write_DB
# randomlist = random.sample(range(0, 1000000), 50000)
# arr = (list(set(randomlist)))
# arr.sort()
# Write_DB("1", "\n".join(list(map(lambda x:str(x),arr))))

# # Tests Search_Id just one id
# start_time = time.time()
# print Search_Id("1", "999987")
# end_time = time.time()
# print((end_time-start_time)*1000)

# # Tests Search_Id all db ids
# code_type=1
# file_name = NEW_QR_TYPE_DATA_FOLDER+"Tipo_"+str(code_type)+"/Tabla_Usuarios.txt"
# db = Get_File(file_name).split("\n")
# all_find=True
# start_time = time.time()
# for user_id in db:
#     all_find= all_find and Search_Id(code_type, user_id)!=False
# print all_find
# end_time = time.time()
# print((end_time-start_time)*1000)

# # Tests Add_Id just one id
# start_time = time.time()
# print Add_Id("1", "999987")
# end_time = time.time()
# print((end_time-start_time)*1000)

# # Tests Remove_Id just one id
# start_time = time.time()
# print Remove_Id("1", "999987")
# end_time = time.time()
# print((end_time-start_time)*1000)
