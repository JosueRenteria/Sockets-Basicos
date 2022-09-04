from socket import *
import sys # Terminar la ejecucion del codigo.

# Dirreccion Loopback y puerto de Envio.
direccion_servidor = "127.0.0.1"
puerto_servidor = 9099 

# Declaracion del socket del cliente.
socket_cliente = socket(AF_INET, SOCK_STREAM)
socket_cliente.connect((direccion_servidor, puerto_servidor))

# Mensaje de Bienvenida.
print("BUENVENIDO AL CHAT CON EL SERVIDOR")

while True:
    # Entradas del programa.
    mensaje = input()

    if mensaje != 'Salir':

        # Enviar Mensaje.
        socket_cliente.send(mensaje.encode())
        
        # Resivimos mensaje del Servidor.
        respuesta = socket_cliente.recv(4096).decode()
        print(f"Servidor-{respuesta}")
    
    else:

        # Eviamos mensaje.
        socket_cliente.send(mensaje.encode())

        # Cerramos socket.
        socket_cliente.close()
        sys.exit()