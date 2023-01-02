# ---------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------
"""

Autor: Anderson Amaya Pulido

Libreria personal para el manejo de rutas del aplicativo.











"""
# ---------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------


# ---------------------------------------------------------------------------------------
#                                   Rutas Generales
# ---------------------------------------------------------------------------------------

import os
# Ruta      FirmwareBK o anterior
FIRMBK = '/home/pi/FirmwareBK/'
# Ruta      Firmware
FIRM = '/home/pi/Firmware/'
# Ruta      Firmware
FIRM = os.path.dirname(os.path.realpath(__file__))+"/../../"
# Ruta      Imagenes del firmware
IMG = 'img/'
# Ruta      Informacion Dispositivo
DISP = '/home/pi/.ID/'
# Ruta      WEB
DWEB = '/var/www/html/'
# Ruta      Actualizador
ACTUALI = '/home/pi/Actualizador/'
# --------- data del firmware y de las sedes
# Ruta      Comandos
COMMA = 'Command/'
# Ruta      Configuraciones
CONF = 'Config/'
# Ruta      Estados
STATUS = 'Status/'
# Ruta      Base de datos
DATA = 'Data/'

# Ruta      Actualizador
S0 = FIRM + 'db/S0/'
# Ruta      Actualizador
S1 = FIRM + 'db/S1/'
# Ruta      Actualizador
S2 = FIRM + 'db/S2/'
# Ruta      Actualizador
HUB = FIRM + 'db/HUB/'

# ---------------------------------------------------------------------------------------
#                                  Datos del dispositivo
# ---------------------------------------------------------------------------------------

# Datos y contenido del repositorio git
INF_FIRMWARE = FIRM + 'README.md'
# Datos de la vercion del Firmware
INF_VERCION = CONF + 'Vercion/Vercion_Firmware.txt'
# Datos propios del dispositivo pieza 1 UUID
INF_DISPO = DISP + 'Datos_Creacion.txt'
# Datos propios del dispositivo
KEY_DISPO = DISP + 'Key.txt'

# ---------------------------------------------------------------------------------------
#                                  Firmware
# ---------------------------------------------------------------------------------------

# Configuraciones personalizadas del Firmware
COM_FIRMWARE = COMMA + 'Firmware/Com_Firmware.txt'

# ---------------------------------------------------------------------------------------
#                                  Base de datos separacion por tipos de qr
# ---------------------------------------------------------------------------------------

# -------------- Tipos de qr

# Usuarios del servidor o counter
TAB_USER_TIPO_1_1 = DATA + 'Tipo_1_1/Tabla_Usuarios.txt'
# Registro de usuarios autorizados entrada y salida
TAB_AUTO_TIPO_1_1 = DATA + 'Tipo_1_1/Tabla_Autorizados.txt'
# Usuarios del servidor o counter
TAB_USER_TIPO_1 = DATA + 'Tipo_1/Tabla_Usuarios.txt'
# Registro de usuarios autorizados entrada y salida
TAB_AUTO_TIPO_1 = DATA + 'Tipo_1/Tabla_Autorizados.txt'
# pines de usuarios generados
TAB_PINES_TIPO_1 = DATA + 'Tipo_1/Tabla_Pines.txt'
# Usuarios del servidor o counter
TAB_USER_TIPO_2 = DATA + 'Tipo_2/Tabla_Usuarios.txt'
# Registro de usuarios autorizados entrada y salida
TAB_AUTO_TIPO_2 = DATA + 'Tipo_2/Tabla_Autorizados.txt'
# Usuarios del servidor o counter
TAB_USER_TIPO_2_1 = DATA + 'Tipo_2_1/Tabla_Usuarios.txt'
# Registro de usuarios autorizados entrada y salida
TAB_AUTO_TIPO_2_1 = DATA + 'Tipo_2_1/Tabla_Autorizados.txt'
# Usuarios del servidor o counter
TAB_USER_TIPO_3 = DATA + 'Tipo_3/Tabla_Usuarios.txt'
# Registro de usuarios autorizados entrada y salida
TAB_AUTO_TIPO_3 = DATA + 'Tipo_3/Tabla_Autorizados.txt'
# Usuarios del servidor o counter
TAB_USER_TIPO_4 = DATA + 'Tipo_4/Tabla_Usuarios.txt'
# Registro de usuarios autorizados entrada y salida
TAB_AUTO_TIPO_4 = DATA + 'Tipo_4/Tabla_Autorizados.txt'

# -------------- Tipos de tag o targetas

# Usuarios del servidor o counter
TAB_USER_TIPO_6 = DATA + 'Tipo_6/Tabla_Usuarios.txt'
# Registro de usuarios autorizados entrada y salida
TAB_AUTO_TIPO_6 = DATA + 'Tipo_6/Tabla_Autorizados.txt'

# -------------- Control de autorizaciones Autorizaciones

# Registro de usuarios autorizados por el dispositivo
TAB_ENV_SERVER = DATA + 'Autorizaciones/Tabla_Envio_server.txt'
# Registro de usuarios autorizados por el dispositivo
TAB_USER_AUTO = DATA + 'Autorizaciones/Tabla_Usuarios_Autorisados.txt'
# Registro de usuarios autorizados por el dispositivo
TAB_USER_IN = DATA + 'Autorizaciones/Tabla_Usuarios_Autorisados.json'

# ---------------------------------------------------------------------------------------
#                                  Led RGB -> WS2812B
# ---------------------------------------------------------------------------------------

# Comandos para el control de los led
COM_LED = COMMA + 'Led_RGB/Com_Led.txt'

# ---------------------------------------------------------------------------------------
#                                  Rele dual
# ---------------------------------------------------------------------------------------

# Configuracion rele
CONF_TIEM_RELE = CONF + 'Rele/Tiempo_Rele.txt'
# Configuracion Direccion rele
CONF_DIREC_RELE = CONF + 'Rele/Direccion_Rele.txt'
# Configuracion de tipo de relevos
CONF_COMU_RELE = CONF + 'Rele/Tipo_Rele.txt'
# Comando de comunicaiones relevos serial
COM_TX_RELE = COMMA + 'Rele/Com_Tx_Rele.txt'
COM_RELE = COMMA + 'Rele/Com_Rele.txt'                             # Comando relevos

# ---------------------------------------------------------------------------------------
#                                  Buzzer 5V
# ---------------------------------------------------------------------------------------

# Archivo de comandos
COM_BUZZER = COMMA + 'Buzzer/Com_Buzzer.txt'

# ---------------------------------------------------------------------------------------
#                                  Botton no touch
# ---------------------------------------------------------------------------------------

# Archivo habilitar o desactivar boton no touch
STATUS_BUTTON_NOTOUCH = CONF + 'NoTouch/status.txt'

# ---------------------------------------------------------------------------------------
#                                  Sensor QR
# ---------------------------------------------------------------------------------------

# Datos leidos del qr
COM_QR = COMMA + 'Qr/Com_Qr.txt'
STATUS_QR = STATUS + 'Qr/Status_Qr.txt'                           # Estado del qr
# Estado de repeticion del qr
STATUS_REPEAT_QR = STATUS + 'Qr/Repeat_Qr.txt'

# Datos leidos del qr
COM_QR_S1 = COMMA + 'Qr/Com_Qr_S1.txt'
STATUS_QR_S1 = STATUS + 'Qr/Status_Qr_S1.txt'                        # Estado del qr

# Datos leidos del qr
COM_QR_S2 = COMMA + 'Qr/Com_Qr_S2.txt'
STATUS_QR_S2 = STATUS + 'Qr/Status_Qr_S2.txt'                        # Estado del qr
# ---------------------------------------------------------------------------------------
#                                   Teclado
# ---------------------------------------------------------------------------------------

#-------------- imagenes

# Imagen Teclado normal
FONDO_1 = FIRM + IMG + "Teclado/keypad-fondo.png"
# Imagen Teclado Borrar amarillo
FONDO_2 = FIRM + IMG + "Teclado/Keypad-Borrar_Amarillo.png"
# Imagen X denegado
Link_Denegado = FIRM + IMG + "Teclado/denegado.png"
# Imagen chulo permitido
Link_Permitido = FIRM + IMG + "Teclado/permitido.png"
# Imagen flecha a la derecha
Link_Per_Derecha = FIRM + IMG + "Teclado/derecha.png"
# Imagen Alerta de qr repetido
Link_Alerta = FIRM + IMG + "Teclado/alerta2.png"

# -------------- comados y estados

# comandos teclados o lo digitado
COM_TECLADO = COMMA + 'Teclado/Com_Teclado.txt'
# Estados teclados o si digito
STATUS_TECLADO = STATUS + 'Teclado/Status_Teclado.txt'
# comandos teclados o lo digitado
COM_TECLADO_S1 = COMMA + 'Teclado/Com_Teclado_S1.txt'
# Estados teclados o si digito
STATUS_TECLADO_S1 = STATUS + 'Teclado/Status_Teclado_S1.txt'
# comandos teclados o lo digitado
COM_TECLADO_S2 = COMMA + 'Teclado/Com_Teclado_S2.txt'
# Estados teclados o si digito
STATUS_TECLADO_S2 = STATUS + 'Teclado/Status_Teclado_S2.txt'

# -------------- Configuraciones ----

# Configuracion de flecha o teclado
CONF_FLECHA_TECLADO = CONF + 'Teclado/Flecha_Teclado.txt'

# ---------------------------------------------------------------------------------------
#                                   Red
# ---------------------------------------------------------------------------------------

# Estados de la red ethernet y wifi
STATUS_RED = STATUS + 'Red/Status_Red.txt'

#-------------- Configuraciones

# archivo para configuracion red wifi
CONF_WIF_ETHE = '/etc/wpa_supplicant/wpa_supplicant.conf'
# para ip estatica wifi y ethernet
CONF_IP_STATIC = '/etc/dhcpcd.conf'
# ---------------------------------------------------------------------------------------
#                                   Usuarios
# ---------------------------------------------------------------------------------------

# Estado de Usuarios
STATUS_USER = STATUS + 'Usuario/Status_User.txt'

# ---------------------------------------------------------------------------------------
#                                   CONTER_Comunicaciones
# ---------------------------------------------------------------------------------------

# datos autorizados por el dispositivo
CONT_SEND_DATA_PATH = '/home/pi/Firmware/ComCounter/db/datatosend.txt'
# Bandera de control de escritura
CONT_SEND_FLAG_PATH = '/home/pi/Firmware/ComCounter/db/flagtosend.txt'

# Actualizar Usuarios
CONT_RECEIVED_DATA_PATH = '/home/pi/Firmware/ComCounter/db/datareceived.txt'
# Bandera de control de escritura
CONT_RECEIVED_FLAG_PATH = '/home/pi/Firmware/ComCounter/db/flagreceived.txt'

# ---------------------------------------------------------------------------------------
#                                   Configuracion de autorizaciones
# ---------------------------------------------------------------------------------------

# para quien autoriza primero servidor counter dispo
CONF_AUTORIZACION_QR = CONF + 'Autorizaciones/Qr/Tipos.txt'
# para quien autoriza primero servidor counter dispo
CONF_AUTORIZACION_TECLADO = CONF + 'Autorizaciones/Teclado/Tipos.txt'
# para quien autoriza primero servidor counter dispo
CONF_AUTORIZACION_NFC = CONF + 'Autorizaciones/Nfc/Tipos.txt'

# ---------------------------------------------------------------------------------------
#                                   Servidor
# ---------------------------------------------------------------------------------------

CONF_DOMI_SERVER = CONF + 'Server/Dominio_Servidor.txt'                 # Dominio
CONF_IP_SERVER = CONF + 'Server/IP_Servidor.txt'                      # IP dominio
CONF_M_CONEX_SERVER = CONF + \
    'Server/Mejor_Conexion.txt'                   # mejor coneccion

# ---------------------------------------------------------------------------------------
#                                   Menu Web
# ---------------------------------------------------------------------------------------

COM_WEB_ANTES = FIRM + STATUS + 'Web/Comandos_Web.txt'                       #
PRO_WEB = FIRM + STATUS + 'Web/Procesos_web.txt'                       #
COM_WEB = DWEB + 'Admin/include/Control_Web.txt'                       #

# ---------------------------------------------------------------------------------------
#                                   Actualizador
# ---------------------------------------------------------------------------------------

RESP_PET_FIRMWARE = ACTUALI + 'db/Respuesta_Peticion_Firmware.txt'            #
STATUS_ACTUALIZADOR = ACTUALI + 'db/Estado_Actualizador.txt'                    #
MEM_ACTUALIZADOR = ACTUALI + 'db/Memoria_Actualizador.txt'                   #
COM_ACTUALIZADOR = COMMA + 'Actualizador/Forzar_Actualizador.txt'     #

# ---------------------------------------------------------------------------------------
#                                   NFC
# ---------------------------------------------------------------------------------------

# Datos leidos del Nfc
COM_NFC = COMMA + 'Nfc/Com_Nfc.txt'
STATUS_NFC = STATUS + 'Nfc/Status_Nfc.txt'                      # Estado del Nfc
# Estado de repeticion del Nfc
STATUS_REPEAT_NFC = STATUS + 'Nfc/Repeat_Nfc.txt'
# Datos leidos del Nfc
COM_NFC_S1 = COMMA + 'Nfc/Com_Nfc_S1.txt'
STATUS_NFC_S1 = STATUS + 'Nfc/Status_Nfc_S1.txt'                    # Estado del Nfc
# Datos leidos del Nfc
COM_NFC_S2 = COMMA + 'Nfc/Com_Nfc_S2.txt'
STATUS_NFC_S2 = STATUS + 'Nfc/Status_Nfc_S2.txt'                    # Estado del Nfc

# ---------------------------------------------------------------------------------------
#                                  Serial_Modbus --- posiblemente se elimine en revicion ----
# ---------------------------------------------------------------------------------------

RX_MODBUS = COMMA + 'Serial_Modbus/RX_Modbus.txt'            # Datos leidos del Nfc
TX_MODBUS = COMMA + 'Serial_Modbus/TX_Modbus.txt'            # Datos leidos del Nfc
PILA_MODBUS = COMMA + 'Serial_Modbus/PILA_Modbus.txt'          # Datos leidos del Nfc

# Datos leidos del Nfc
ID_MOD_USUARIOS = COMMA + 'Serial_Modbus/ID_MOD_Usuarios.txt'
ID_MOD_RELES = COMMA + 'Serial_Modbus/ID_MOD_Reles.txt'        # Datos leidos del Nfc

# ---------------------------------------------------------------------------------------
#                                   Lectoras
# ---------------------------------------------------------------------------------------

# conficugacion basica de tipos de lectoras
CONF_LECTORAS = CONF + 'Lectoras/Configuraciones.txt'

# ---------------------------------------------------------------------------------------
#                                   Salidas
# ---------------------------------------------------------------------------------------

# conficugacion basica de tipos de lectoras
CONF_SALIDAS = CONF + 'Salidas/Configuraciones.txt'

# ---------------------------------------------------------------------------------------
#                                   Sedes
# ---------------------------------------------------------------------------------------

# Configuracion de toda la sede y cuantas sedes
CONF_SEDES = CONF + 'Locaciones/Configuraciones.txt'


# ---------------------------------------------------------------------------------------
#                                   Modulo respuesta
# ---------------------------------------------------------------------------------------

COM_RES = COMMA + 'Mod_Respuesta/Com_Res.txt'
COM_RES_S1 = COMMA + 'Mod_Respuesta/Com_Res_S1.txt'
COM_RES_S2 = COMMA + 'Mod_Respuesta/Com_Res_S2.txt'
