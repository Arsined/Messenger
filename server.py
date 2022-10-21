import socket, threading  # Импорт библиотек

host = '127.0.0.1'  # Локальный хост компьютера
port = 7976  # Выбор незарезервированного порта

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Инициализация сокета
server.bind((host, port))  # Назначение хоста и порта к сокету
server.listen()

clients = []
nicknames = []


def broadcast(message):  # Функция связи
    for client in clients:
        client.send(message)


def handle(client):
    while True:
        try:  # Получение сообщений от клиента
            message = client.recv(1024)
            broadcast(message)
        except:  # Удаление клиентов
            index = clients.index(client)
            clients.remove(client)
            nickname = nicknames[index]
            nicknames.remove(nickname)
            client.close()
            break


def receive():  # Подключение нескольких клиентов
    while True:
        client, address = server.accept()
        print("Соединён с {}".format(str(address)))
        nickname = client.recv(1024).decode('utf-8')
        nicknames.append(nickname)
        clients.append(client)
        broadcast("{} присоединился!\n".format(nickname).encode('utf-8'))
        client.send('Подключён к серверу!\n'.encode('utf-8'))
        thread = threading.Thread(target=handle, args=(client,))
        thread.start()


receive()
