from socket import *
from datetime import *
import configuration
import struct
import brute_force


def main():
    current = ' '
    batch = configuration.BATCH_SIZE
    servsock = socket(AF_INET, SOCK_STREAM)
    correct_pass=None
    try:
        servsock.bind(("", configuration.SERVER_PORT))
        servsock.listen(1)

        while True:
            clientsock, add = servsock.accept()
            data = bool(struct.unpack("<I",clientsock.recv(struct.calcsize("<I"))))
            if data:
                correct_pass_len=struct.unpack("<I",clientsock.recv(struct.calcsize("<I")))
                correct_pass=struct.unpack("<I",clientsock.recv(correct_pass_lenp))
                clientsock.close()
                break

            clientsock.send(struct.pack("<I", len(current)) + current + struct.pack("<I", batch))
            current = brute_force.increment_string(current, batch)
            clientsock.close()
    finally:
        servsock.close()


if __name__ == '__main__':
    main()
