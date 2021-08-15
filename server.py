import logging
import re
import socket

# создаемTCP/IP сокет
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Привязываем сокет к порту
server_address = ('localhost', 10000)
print('Старт сервера на {} порт {}'.format(*server_address))
sock.bind(server_address)

# Слушаем входящие подключения
sock.listen(1)

logging.basicConfig(filename="sample.log", level=logging.INFO)
logger = logging.getLogger("server")
logger.setLevel(logging.INFO)
while True:
    print('Ожидание соединения...')
    connection, client_address = sock.accept()
    try:
        print('Подключено к:', client_address)
        while True:
            data = connection.recv(24).decode("utf-8").rstrip()
            # if not data:
            #     break
            bbbb, nn, hh, mm, ss_zsh, gg = re.split(' |:', data)
            if gg == '00':
                print(f'cпортсмен, нагрудный номер {bbbb} прошёл отсечку {nn} в «{hh}:{mm}:{ss_zsh[:4]}»')
            logging.info(data)
    except ValueError:
        connection.close()
        logging.info('ValueError. Connection close.')
