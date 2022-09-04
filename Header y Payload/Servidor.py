#Importar la libreria de los sockets.
import socket
from sqlite3 import connect

HOST = "127.0.0.1" # Direccion del loopback
PORT = 65123       # > 1023 (Puerto de Escucha)
HEADER = 10        # Caracteres que va a leer.

# El bloque with es para abrir y cerrar el sockets. socket(IP, TCP)
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # Asociar el socket.
    s.bind((HOST, PORT))

    # Poner el socket en modo escucha.
    s.listen()

    # Aceptar conecciones entrantes (conn = socket del cliente, addr = direccion del socket entrante).
    conn, addr = s.accept()

    # Enviar un mensaje al servidor.
    with conn:
        # Muestra la direccion IP del cliente.
        print(f"Conectado a {addr}")
        while True:
            # Observar el numero de caracteres a resibir.
            data_len = conn.recv(HEADER)

            # Ver si el usuario envio algo.
            if not data_len:
                break
            else:
                #Dato que se resive.
                data = conn.recv(int(data_len))
                strData = data.decode('utf-8')
                print(strData)
        
        # Cerramos la conecion de Nuestro Cliente.
        print(f"Desconectando a {addr}")
        conn.close()