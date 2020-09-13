#!/usr/bin/python3

import socket

HOST = 'localhost'
PORT = 50000

sct = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sct.bind((HOST, PORT))

sct.listen()
print('Aguardando conexão.')

conn, ender = sct.accept()

print ('Conectado em', ender)

while True:
    data = conn.recv(1024)
    if not data:
        print ('Fechando a conexão')
        conn.close()
        break
    
    print('Oque o servidor recebeu : ', data)
    # soma = data.split(' ')
    # resultado = soma[0] + soma[1]
    # print('Soma : ', soma)

    conn.sendall(data)
    print('Enviou')
