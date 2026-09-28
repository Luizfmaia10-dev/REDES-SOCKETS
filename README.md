# Programação com Sockets em Python: UDP, TCP e TCP Concorrente

Este repositório contém implementações práticas e didáticas de comunicação em rede utilizando a API de **Sockets em Python**. São apresentados exemplos dos protocolos **UDP** (não orientado à conexão), **TCP Iterativo** (orientado à conexão simples) e **TCP Concorrente** (suporte a múltiplos clientes via multithreading).

---

## 📌 Conteúdo do Repositório

* **UDP (User Datagram Protocol)**
  * `UDPClient.py`: Cliente UDP que envia mensagens sem estabelecimento prévio de conexão.
  * `UDPServer.py`: Servidor UDP que recebe datagramas e responde com o texto em letras maiúsculas.
* **TCP Iterativo (Transmission Control Protocol)**
  * `TCPClient.py`: Cliente TCP que realiza a conexão de 3 vias (*three-way handshake*) e envia dados ao servidor.
  * `TCPServer.py`: Servidor TCP monotrefa que processa um cliente por vez.
* **TCP Concorrente (Multithread)**
  * `TCPClientConc.py`: Cliente TCP capaz de manter uma conexão contínua enviando mensagens sequenciais.
  * `TCPServerConc.py`: Servidor TCP multithreaded que cria uma nova thread para cada cliente conectado.

---

## 🚀 Como Executar

### Pré-requisitos
* **Python 3.x** instalado.

---

### 1. Aplicação UDP (Datagramas)

1. Abra o primeiro terminal e inicie o servidor:
   ```bash
   python3 UDPServer.py
   ```
2. Em um segundo terminal, execute o cliente:
   ```bash
   python3 UDPClient.py
   ```
3. Digite uma mensagem em minúsculas e veja a resposta em maiúsculas vinda do servidor.

> **Dica (Cliente Alternativo):** Você também pode testar o servidor UDP usando o utilitário `netcat`:
> ```bash
> nc -u 127.0.0.1 12000
> ```

---

### 2. Aplicação TCP Iterativo

1. Em um terminal, inicie o servidor TCP:
   ```bash
   python3 TCPServer.py
   ```
2. Em outro terminal, inicie o cliente TCP:
   ```bash
   python3 TCPClient.py
   ```
3. Digite o texto solicitado para receber a resposta convertida.

> **Dica (Cliente Alternativo):** Pode-se conectar ao servidor usando `netcat`:
> ```bash
> nc 127.0.0.1 12000
> ```

---

### 3. Aplicação TCP Concorrente (Múltiplos Clientes)

1. Em um terminal, inicie o servidor TCP Concorrente:
   ```bash
   python3 TCPServerConc.py
   ```
2. Em **dois ou mais** terminais diferentes, abra múltiplos clientes:
   ```bash
   python3 TCPClientConc.py
   ```
3. Envie mensagens a partir de qualquer cliente. O servidor identificará de qual cliente (endereço IP/Porta) a mensagem veio e processará todos simultaneamente sem bloquear.
4. Para encerrar o cliente, pressione a combinação de teclas `CTRL + X` e dê Enter.

---

## 🧠 Conceitos e Diferenças

| Característica | UDP | TCP Iterativo | TCP Concorrente |
| :--- | :--- | :--- | :--- |
| **Tipo de Socket** | `SOCK_DGRAM` | `SOCK_STREAM` | `SOCK_STREAM` |
| **Conexão** | Não orientada a conexão | Orientada a conexão | Orientada a conexão |
| **Confiabilidade** | Sem garantia de entrega/ordem | Garantia de entrega e ordem | Garantia de entrega e ordem |
| **Atendimento** | Por datagramas individuais | 1 cliente por vez (bloqueante) | Múltiplos clientes simultâneos |
| **Parâmetros de Socket** | Identificado por `(IP, Porta Destino)` | Socket de escuta + Socket de dados dedicado | Socket de escuta + Socket por Thread |

### Resumo do Funcionamento:
1. **UDP**: O servidor escuta em um socket compartilhado. As mensagens são enviadas diretamente sem negociação prévia.
2. **TCP Iterativo**: O servidor aceita uma conexão (`accept()`), processa os dados, envia a resposta e fecha a conexão antes de poder atender o próximo cliente na fila.
3. **TCP Concorrente**: O socket principal (*Listener Socket*) fica dedicado exclusivamente a aceitar novas conexões. Ao receber uma solicitação, ele cria um novo socket de dados e delega o atendimento para uma thread separada (`_thread.start_new_thread`), mantendo-se livre para novos clientes.

---

## 🛠️ Tecnologias
* **Linguagem:** Python 3
* **Biblioteca Padrão:** `socket`, `_thread`

## Repositorio:
GitHub:https://github.com/Luizfmaia10-dev/REDES-SOCKETS