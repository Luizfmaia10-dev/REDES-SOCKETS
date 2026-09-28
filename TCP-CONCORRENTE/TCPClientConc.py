import socket

HOST = '127.0.0.1'  # Endereço IP do Servidor
PORT = 50000        # Porta em que o Servidor está

tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
destino = (HOST, PORT)
tcp.connect(destino)

print('\nDigite suas mensagens')
print('Para sair use CTRL+X\n')

mensagem = input()

# Permanece enviando mensagens até o usuário pressionar CTRL+X (código ASCII \x18)
while mensagem != '\x18':
    tcp.send(mensagem.encode())
    mensagem = input()

tcp.close()