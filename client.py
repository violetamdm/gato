import socket
from keyboard import is_pressed
from basededatossql import user
HOST = "127.0.0.1"
PORT = 6666
BUFFER_SIZE = 1024

def run():
    while not is_pressed("q"):
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
            nombre_usuario= input("Nombre: ")
            ip_usuario= input("Direccion IP: ")
            usuario = user(ip=ip_usuario, nombre=nombre_usuario)
            user_input = str.encode(input("Enter message: "))
            s.sendto(user_input, (HOST, PORT))
            s.sendto(usuario, (HOST, PORT)) ### ### ### ###

if __name__ == "__main__":
    run()