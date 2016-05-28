from socket import socket, AF_INET, SOCK_STREAM
from struct import unpack

BUF_SIZE = 4096
DECODE_CODE = '!I'

class SecretCode:
    def __init__(self, srv_ip, srv_port):
        """
        :param srv_ip: the ip to connect to (should be unimate most likely)
        :param srv_port: the port to connect to
        :return:
        """
        self.srv_socket = socket(AF_INET, SOCK_STREAM)
        self.srv_socket.connect((srv_ip, srv_port))

    def recv_secret_code(self):
        """
        Waits to recieve the secret code (will block)
        :return:
        """
        print('Waiting to receive secret code...')
        recv_data = self.srv_socket.recv(BUF_SIZE)
        secret_code, = unpack(DECODE_CODE, recv_data)
        print(secret_code)
