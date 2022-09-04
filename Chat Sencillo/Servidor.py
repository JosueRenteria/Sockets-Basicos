# Declaramos las librerias del programa.
from socket import *
import sys # Terminar la ejecucion del codigo.

# Dirreccion Loopback y puerto de Escucha.
direccion_servidor = "127.0.0.1"
puerto_servidor = 9099

# Generamos nuestro sicket.
socket_servidor = socket(AF_INET,SOCK_STREAM)
# Establecer la coneccion con el servidor.
socket_servidor.bind((direccion_servidor, puerto_servidor))
socket_servidor.listen()    # Modo escucha del servidor. 

# Mensaje de Bienvenida.
print("BUENVENIDO AL CHAT CON EL CLIENTE")

while True:
    # Establecemos la coneccion.
    socket_conexion, addr = socket_servidor.accept()
    print("Conectamos con el cliente:", addr)

    while True:
        # Recivimos el mensaje del cliente.
        mensaje_resivido = socket_conexion.recv(4096).decode() # Aqui en alguna versiones si o si se tiene que poner el decode.
        print(f"Cliente-{mensaje_resivido}")

        # Condicion para salir del Servidor.
        if mensaje_resivido == 'Salir':
            break
        
        # Mandamos mensaje al cliente.
        socket_conexion.send(input().encode())
    
    # Mensaje de Desconeccion del Cliente
    print("El cliente se esta desconectando", addr)

    # Cerramos conexion.
    socket_conexion.close()
    sys.exit() # Solo por ahora para salir.