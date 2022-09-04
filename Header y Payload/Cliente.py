#Importar la libreria de los sockets.
import socket
from time import time

HOST = "127.0.0.1" # Direccion del servidor a conectar.
PORT = 65123       # Puerto de Envio para entrar.
HEADER = 10

# El bloque with es para abrir y cerrar el sockets. socket(IP, TCP)
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # Hacer la conneccion con el Servidor (Aqui deja de estar bloqueado el Servidor).
    s.connect((HOST, PORT))

    # Datos en una lista.
    names = ['Josue', 'Raul', '', 'Sandra']

for name in names:
    # <HEADER><PAYLOAD>
    strData = str(name)
    data_len = str(len(strData))

    # Formato para la serealizacion.
    data = f"{data_len:<{HEADER}}{strData}".encode('utf-8')

    # El cliente resivira lo que le envia el servidor.
    s.send(data)
    time.sleep(1)
    
