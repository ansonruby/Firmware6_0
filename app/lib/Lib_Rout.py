#---------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------
"""

Autor:  Luding Castaneda,
        Anderson Amaya Pulido

Libreria personal para el manejo de rutas del aplicativo.











"""
#---------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------
import os

#---------------------------------------------------------------------------------------
#                                   Rutas Generales
#---------------------------------------------------------------------------------------

FIRMBK              = '/home/pi/FirmwareBK/'                                        # Ruta      FirmwareBK o anterior
FIRM                = '/home/pi/Firmware/'                                          # Ruta      Firmware
FIRM = os.path.dirname(os.path.realpath(__file__))+"/../../"                        # Ruta      Firmware

IMG                 = 'img/'                                                        # Ruta      Imagenes del firmware
DISP                = '/home/pi/.ID/'                                               # Ruta      Informacion Dispositivo
DWEB                = '/var/www/html/'                                              # Ruta      WEB
ACTUALI             = '/home/pi/Actualizador/'                                      # Ruta      Actualizador
#--------- data del firmware y de las sedes
COMMA               = 'Command/'                                                    # Ruta      Comandos
CONF                = 'Config/'                                                     # Ruta      Configuraciones
STATUS              = 'Status/'                                                     # Ruta      Estados
DATA                = 'Data/'                                                       # Ruta      Base de datos

S0                  = FIRM +'db/S0/'                                                # Ruta      Actualizador
S1                  = FIRM +'db/S1/'                                                # Ruta      Actualizador
S2                  = FIRM +'db/S2/'                                                # Ruta      Actualizador
HUB                 = FIRM +'db/HUB/'                                               # Ruta      Actualizador

#---------------------------------------------------------------------------------------
#                                  Datos del dispositivo
#---------------------------------------------------------------------------------------

INF_FIRMWARE        = FIRM + 'README.md'                                            # Datos y contenido del repositorio git
INF_VERCION         = CONF + 'Vercion/Vercion_Firmware.txt'                         # Datos de la vercion del Firmware
INF_DISPO           = DISP + 'Datos_Creacion.txt'                                   # Datos propios del dispositivo pieza 1 UUID
KEY_DISPO           = DISP + 'Key.txt'                                              # Datos propios del dispositivo

#---------------------------------------------------------------------------------------
#                                  Firmware
#---------------------------------------------------------------------------------------
CONF_HUB            = HUB + CONF + 'Config.json'                                    # Configuracion global
CONF_INTER_DISPO    = HUB + CONF + 'Config_Inter_Dispo.json'                        # Configuracion Interna_dispositivo
COM_FIRMWARE        = COMMA + 'Firmware/Com_Firmware.txt'                           # Configuraciones personalizadas del Firmware

#---------------------------------------------------------------------------------------
#                                  Base de datos separacion por tipos de qr
#---------------------------------------------------------------------------------------

#-------------- Tipos de qr

#TAB_USER_TIPO_1_1   = DATA + 'Tipo_1_1/Tabla_Usuarios.txt'                   # Usuarios del servidor o counter
#TAB_AUTO_TIPO_1_1   = DATA + 'Tipo_1_1/Tabla_Autorizados.txt'                # Registro de usuarios autorizados entrada y salida
#TAB_USER_TIPO_1     = DATA + 'Tipo_1/Tabla_Usuarios.txt'                     # Usuarios del servidor o counter
#TAB_AUTO_TIPO_1     = DATA + 'Tipo_1/Tabla_Autorizados.txt'                  # Registro de usuarios autorizados entrada y salida
#TAB_USER_TIPO_2     = DATA + 'Tipo_2/Tabla_Usuarios.txt'                     # Usuarios del servidor o counter
#TAB_PINES_TIPO_1    = DATA + 'Tipo_1/Tabla_Pines.txt'                        # pines de usuarios generados
#TAB_AUTO_TIPO_2     = DATA + 'Tipo_2/Tabla_Autorizados.txt'                  # Registro de usuarios autorizados entrada y salida
#TAB_USER_TIPO_2_1   = DATA + 'Tipo_2_1/Tabla_Usuarios.txt'                   # Usuarios del servidor o counter
#TAB_AUTO_TIPO_2_1   = DATA + 'Tipo_2_1/Tabla_Autorizados.txt'                # Registro de usuarios autorizados entrada y salida
#TAB_USER_TIPO_3     = DATA + 'Tipo_3/Tabla_Usuarios.txt'                     # Usuarios del servidor o counter
#TAB_AUTO_TIPO_3     = DATA + 'Tipo_3/Tabla_Autorizados.txt'                  # Registro de usuarios autorizados entrada y salida

#-------------- Tipos de tag o targetas

TAB_USER_TIPO_6     = DATA + 'Tipo_6/Tabla_Usuarios.txt'                     # Usuarios del servidor o counter
TAB_AUTO_TIPO_6     = DATA + 'Tipo_6/Tabla_Autorizados.txt'                  # Registro de usuarios autorizados entrada y salida

#-------------- Control de autorizaciones Autorizaciones

TAB_ENV_SERVER      = DATA + 'Autorizaciones/Tabla_Envio_server.txt'         # Registro de usuarios autorizados por el dispositivo
TAB_USER_AUTO       = DATA + 'Autorizaciones/Tabla_Usuarios_Autorisados.txt' # Registro de usuarios autorizados por el dispositivo
TAB_USER_IN       = DATA + 'Autorizaciones/Tabla_Usuarios_Autorisados.json' # Registro de usuarios autorizados por el dispositivo

#---------------------------------------------------------------------------------------
#                                  Led RGB -> WS2812B
#---------------------------------------------------------------------------------------

COM_LED             = COMMA + 'Led_RGB/Com_Led.txt'                           # Comandos para el control de los led

#---------------------------------------------------------------------------------------
#                                  Rele dual
#---------------------------------------------------------------------------------------

#CONF_TIEM_RELE      = CONF + 'Rele/Tiempo_Rele.txt'                           # Configuracion rele
#CONF_DIREC_RELE     = CONF + 'Rele/Direccion_Rele.txt'                        # Configuracion Direccion rele
#CONF_COMU_RELE      = CONF + 'Rele/Tipo_Rele.txt'                             # Configuracion de tipo de relevos
#COM_TX_RELE         = COMMA + 'Rele/Com_Tx_Rele.txt'                          # Comando de comunicaiones relevos serial
COM_RELE_S0            = COMMA + 'Rele/Com_Rele_S0.txt'                             # Comando relevos
COM_RELE_S1            = COMMA + 'Rele/Com_Rele_S1.txt'                             # Comando relevos
COM_RELE_S2            = COMMA + 'Rele/Com_Rele_S2.txt'                             # Comando relevos

#---------------------------------------------------------------------------------------
#                                  Buzzer 5V
#---------------------------------------------------------------------------------------

COM_BUZZER          = COMMA + 'Buzzer/Com_Buzzer.txt'                         # Archivo de comandos

#---------------------------------------------------------------------------------------
#                                  Botton no touch
#---------------------------------------------------------------------------------------

STATUS_BUTTON_NOTOUCH      = CONF + 'NoTouch/status.txt'                     # Archivo habilitar o desactivar boton no touch

#---------------------------------------------------------------------------------------
#                                  Sensor QR
#---------------------------------------------------------------------------------------

COM_QR              = COMMA  + 'Qr/Com_Qr.txt'                              # Datos leidos del qr
STATUS_QR           = STATUS + 'Qr/Status_Qr.txt'                           # Estado del qr
STATUS_REPEAT_QR    = STATUS + 'Qr/Repeat_Qr.txt'                           # Estado de repeticion del qr

COM_QR_S1           = COMMA  + 'Qr/Com_Qr_S1.txt'                           # Datos leidos del qr
STATUS_QR_S1        = STATUS + 'Qr/Status_Qr_S1.txt'                        # Estado del qr

COM_QR_S2           = COMMA  + 'Qr/Com_Qr_S2.txt'                           # Datos leidos del qr
STATUS_QR_S2        = STATUS + 'Qr/Status_Qr_S2.txt'                        # Estado del qr
#---------------------------------------------------------------------------------------
#                                   Teclado
#---------------------------------------------------------------------------------------

#-------------- imagenes

FONDO_1             = FIRM + IMG + "Teclado/keypad-fondo.png"                       # Imagen Teclado normal
FONDO_2             = FIRM + IMG + "Teclado/Keypad-Borrar_Amarillo.png"             # Imagen Teclado Borrar amarillo
Link_Denegado       = FIRM + IMG + "Teclado/denegado.png"                           # Imagen X denegado
Link_Permitido      = FIRM + IMG + "Teclado/permitido.png"                          # Imagen chulo permitido
Link_Per_Derecha    = FIRM + IMG + "Teclado/derecha.png"                            # Imagen flecha a la derecha
Link_Alerta         = FIRM + IMG + "Teclado/alerta2.png"                            # Imagen Alerta de qr repetido

#-------------- comados y estados

COM_TECLADO         = COMMA + 'Teclado/Com_Teclado.txt'                      # comandos teclados o lo digitado
STATUS_TECLADO      = STATUS + 'Teclado/Status_Teclado.txt'                  # Estados teclados o si digito
COM_TECLADO_S1      = COMMA + 'Teclado/Com_Teclado_S1.txt'          # comandos teclados o lo digitado
STATUS_TECLADO_S1   = STATUS + 'Teclado/Status_Teclado_S1.txt'      # Estados teclados o si digito
COM_TECLADO_S2      = COMMA + 'Teclado/Com_Teclado_S2.txt'          # comandos teclados o lo digitado
STATUS_TECLADO_S2   = STATUS + 'Teclado/Status_Teclado_S2.txt'      # Estados teclados o si digito

#-------------- Configuraciones ----

CONF_FLECHA_TECLADO = CONF + 'Teclado/Flecha_Teclado.txt'                    # Configuracion de flecha o teclado

#---------------------------------------------------------------------------------------
#                                   Red
#---------------------------------------------------------------------------------------

STATUS_RED          = STATUS + 'Red/Status_Red.txt'                          # Estados de la red ethernet y wifi

#-------------- Configuraciones

CONF_WIF_ETHE       ='/etc/wpa_supplicant/wpa_supplicant.conf'                      # archivo para configuracion red wifi
CONF_IP_STATIC      ='/etc/dhcpcd.conf'                                             # para ip estatica wifi y ethernet
#---------------------------------------------------------------------------------------
#                                   Usuarios
#---------------------------------------------------------------------------------------

STATUS_USER     = STATUS + 'Usuario/Status_User.txt'                         # Estado de Usuarios

#---------------------------------------------------------------------------------------
#                                   CONTER_Comunicaciones
#---------------------------------------------------------------------------------------

#CONT_SEND_DATA_PATH = '/home/pi/Firmware/ComCounter/db/datatosend.txt'              # datos autorizados por el dispositivo
#CONT_SEND_FLAG_PATH = '/home/pi/Firmware/ComCounter/db/flagtosend.txt'              # Bandera de control de escritura

#CONT_RECEIVED_DATA_PATH = '/home/pi/Firmware/ComCounter/db/datareceived.txt'        # Actualizar Usuarios
#CONT_RECEIVED_FLAG_PATH = '/home/pi/Firmware/ComCounter/db/flagreceived.txt'        # Bandera de control de escritura

#---------------------------------------------------------------------------------------
#                                   Configuracion de autorizaciones
#---------------------------------------------------------------------------------------

CONF_AUTORIZACION_QR       = CONF + 'Autorizaciones/Qr/Tipos.txt'            # para quien autoriza primero servidor counter dispo
CONF_AUTORIZACION_TECLADO  = CONF + 'Autorizaciones/Teclado/Tipos.txt'       # para quien autoriza primero servidor counter dispo
CONF_AUTORIZACION_NFC      = CONF + 'Autorizaciones/Nfc/Tipos.txt'           # para quien autoriza primero servidor counter dispo

#---------------------------------------------------------------------------------------
#                                   Servidor
#---------------------------------------------------------------------------------------

#CONF_DOMI_SERVER      = CONF + 'Server/Dominio_Servidor.txt'                 # Dominio
#CONF_IP_SERVER        = CONF + 'Server/IP_Servidor.txt'                      # IP dominio
#CONF_M_CONEX_SERVER   = CONF + 'Server/Mejor_Conexion.txt'                   # mejor coneccion

#---------------------------------------------------------------------------------------
#                                   Menu Web
#---------------------------------------------------------------------------------------

COM_WEB_ANTES         = FIRM + STATUS+ 'Web/Comandos_Web.txt'                       #
PRO_WEB               = FIRM + STATUS+ 'Web/Procesos_web.txt'                       #
COM_WEB               = DWEB +'Admin/include/Control_Web.txt'                       #

#---------------------------------------------------------------------------------------
#                                   Actualizador
#---------------------------------------------------------------------------------------

RESP_PET_FIRMWARE       = ACTUALI + 'db/Respuesta_Peticion_Firmware.txt'            #
STATUS_ACTUALIZADOR     = ACTUALI + 'db/Estado_Actualizador.txt'                    #
MEM_ACTUALIZADOR        = ACTUALI + 'db/Memoria_Actualizador.txt'                   #
COM_ACTUALIZADOR        = COMMA + 'Actualizador/Forzar_Actualizador.txt'     #

#---------------------------------------------------------------------------------------
#                                   NFC
#---------------------------------------------------------------------------------------

COM_NFC                 = COMMA + 'Nfc/Com_Nfc.txt'                          # Datos leidos del Nfc
STATUS_NFC              = STATUS + 'Nfc/Status_Nfc.txt'                      # Estado del Nfc
STATUS_REPEAT_NFC       = STATUS + 'Nfc/Repeat_Nfc.txt'                      # Estado de repeticion del Nfc
COM_NFC_S1              = COMMA + 'Nfc/Com_Nfc_S1.txt'                        # Datos leidos del Nfc
STATUS_NFC_S1           = STATUS + 'Nfc/Status_Nfc_S1.txt'                    # Estado del Nfc
COM_NFC_S2              = COMMA + 'Nfc/Com_Nfc_S2.txt'                        # Datos leidos del Nfc
STATUS_NFC_S2           = STATUS + 'Nfc/Status_Nfc_S2.txt'                    # Estado del Nfc

#---------------------------------------------------------------------------------------
#                                  Serial_Modbus --- posiblemente se elimine en revicion ----
#---------------------------------------------------------------------------------------

#RX_MODBUS                 = COMMA + 'Serial_Modbus/RX_Modbus.txt'            # Datos leidos del Nfc
#TX_MODBUS                 = COMMA + 'Serial_Modbus/TX_Modbus.txt'            # Datos leidos del Nfc
#PILA_MODBUS               = COMMA + 'Serial_Modbus/PILA_Modbus.txt'          # Datos leidos del Nfc

#ID_MOD_USUARIOS           = COMMA + 'Serial_Modbus/ID_MOD_Usuarios.txt'      # Datos leidos del Nfc
#ID_MOD_RELES              = COMMA + 'Serial_Modbus/ID_MOD_Reles.txt'        # Datos leidos del Nfc

#---------------------------------------------------------------------------------------
#                                   Lectoras
#---------------------------------------------------------------------------------------
#CONF_LECTORAS             = CONF + 'Lectoras/Configuraciones.txt'                   # conficugacion basica de tipos de lectoras
#---------------------------------------------------------------------------------------
#                                   Salidas
#---------------------------------------------------------------------------------------
#CONF_SALIDAS              = CONF + 'Salidas/Configuraciones.txt'                   # conficugacion basica de tipos de lectoras
#---------------------------------------------------------------------------------------
#                                   Sedes
#---------------------------------------------------------------------------------------
#CONF_SEDES                = CONF + 'Locaciones/Configuraciones.txt'                      # Configuracion de toda la sede y cuantas sedes

#---------------------------------------------------------------------------------------
#                                   Modulo respuesta
#---------------------------------------------------------------------------------------

COM_RES               = COMMA + 'Mod_Respuesta/Com_Res_S0.txt'
COM_RES_S1            = COMMA + 'Mod_Respuesta/Com_Res_S1.txt'
COM_RES_S2            = COMMA + 'Mod_Respuesta/Com_Res_S2.txt'


#---------------------------------------------------------------------------------------
#                                   Temporal: Nuevos QRS
#---------------------------------------------------------------------------------------

NEW_DATA                = DATA + 'NewData/'                                                       # Ruta      Base de datos
NEW_TAB_USER_TIPO_1     = NEW_DATA + 'Tipo_1.txt'                     # Usuarios del servidor o counter
NEW_TAB_USER_TIPO_2     = NEW_DATA + 'Tipo_2.txt'                     # Usuarios del servidor o counter
NEW_TAB_USER_TIPO_3     = NEW_DATA + 'Tipo_3.txt'                     # Usuarios del servidor o counter
NEW_TAB_USER_TIPO_4     = NEW_DATA + 'Tipo_4.txt'                     # Usuarios del servidor o counter
NEW_TAB_USER_TIPO_5     = NEW_DATA + 'Tipo_5.txt'                     # Usuarios del servidor o counter
NEW_TAB_USER_TIPO_6     = NEW_DATA + 'Tipo_6.txt'                     # Usuarios del servidor o counter
NEW_TAB_USER_TIPO_7     = NEW_DATA + 'Tipo_7.txt'                     # Usuarios del servidor o counter

                                                     # Ruta      Base de datos
NEW_AUTO_USER_TIPO_1     = DATA + 'Autorizaciones/Tipo_1.txt'        # Usuarios del servidor o counter
NEW_AUTO_USER_TIPO_2     = DATA + 'Autorizaciones/Tipo_2.txt'        # Usuarios del servidor o counter
NEW_AUTO_USER_TIPO_3     = DATA + 'Autorizaciones/Tipo_3.txt'        # Usuarios del servidor o counter
NEW_AUTO_USER_TIPO_4     = DATA + 'Autorizaciones/Tipo_4.txt'        # Usuarios del servidor o counter
NEW_AUTO_USER_TIPO_5     = DATA + 'Autorizaciones/Tipo_5.txt'        # Usuarios del servidor o counter
NEW_AUTO_USER_TIPO_6     = DATA + 'Autorizaciones/Tipo_6.txt'        # Usuarios del servidor o counter
NEW_AUTO_USER_TIPO_7     = DATA + 'Autorizaciones/Tipo_7.txt'        # Usuarios del servidor o counter
