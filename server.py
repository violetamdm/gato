import socket
from string import ascii_letters
from playsound import playsound
from basededatossql import SessionLocal, usuario
from sqlalchemy.orm import Session

HOST = "0.0.0.0"
PORT = 6666
BUFFER_SIZE = 1024

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db: Session = get_db()

def run():
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        s.bind((HOST, PORT))
        while True:
            message, address = s.recvfrom(BUFFER_SIZE)
            print("Message: %s" % str(message))
            print("Address: %s" % str(address))
            answer = ""
            for l in message:
                if chr(l) in ascii_letters:
                    answer += chr(l)
            print("Answer: %s" % answer)
            if answer == "meow":
                playsound("cat-3-43850.mp3")
            else:
                print("Oh nyo! :C")

def registrar(u: usuario):
    db.add(u)
    db.commit()
    db.refresh(u)

if __name__ == "__main__":
    run()

"""

recibe conexion tcp
si un cliente le hace un quien soy yo
miau alex y envia el miau a alex

cliente envia miau y nombre

miau : suena y mostrar la foto del gato 

bbdd sql
id nombre dirip
alex 17
"""