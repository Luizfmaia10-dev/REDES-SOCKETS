# -*- coding: utf-8 -*-
import socket
import _thread

HOST = '127.0.0.1'  # Endereço IP do Servidor
PORT = 50000        # Porta em que o Servidor está escutando


def conectado(con, cliente):
    print('\nCliente conectado:', cliente)
    while True:
        msg = con.recv(1024)
        if not msg:
            break
        print('\nCliente..:', cliente)
        print('Mensagem.:', msg.decode())

    print('\nFinalizando conexao do cliente', cliente)
    con.close()
    _thread.exit()


tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
orig = (HOST, PORT)

tcp.bind(orig)
tcp.listen(1)

print('\nServidor TCP concorrente iniciado no IP', HOST, 'na porta', PORT)

while True:
    con, cliente = tcp.accept()
    print('\nNova thread iniciada para essa conexão')
    _thread.start_new_thread(conectado, (con, cliente))

tcp.close()