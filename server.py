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

tail = ''

logging.basicConfig(filename="sample.log", level=logging.INFO)
logger = logging.getLogger("server")
logger.setLevel(logging.INFO)
while True:
    print('Ожидание соединения...')
    connection, client_address = sock.accept()
    try:
        print('Подключено к:', client_address)
        while data := connection.recv(4096).decode("utf-8"):
            records = f'{tail}{data}'.split('\n')
            # len = int(connection.recv(2).decode("utf-8"))
            # data = connection.recv(len).decode("utf-8").rstrip()
            for record in records:
                if len(record) == 23:
                    bbbb, nn, hh, mm, ss_zsh, gg = re.split(' |:', record)
                    if gg == '00':
                        print(f'cпортсмен, нагрудный номер {bbbb} прошёл отсечку {nn} в «{hh}:{mm}:{ss_zsh[:4]}»')
                    logging.info(record)
                else:
                    tail = record

    except ValueError:
        connection.close()
        logging.info('ValueError. Connection close.')
