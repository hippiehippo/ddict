import socket
import configuration
import struct

def increment_string(s, num=1):
    ret = s
    for i in xrange(num):
        ascii_vals = [ord(char) for char in ret]
        for j in range(1, len(ascii_vals) + 1):
            if ascii_vals[-j] < ord(configuration.LAST_PRINTABLE_CHAR_IN_ASCII):
                ascii_vals[-j] += 1
                break

            ascii_vals[-j] = ord(configuration.FIRST_PRINTABLE_CHAR)
            if j == len(ascii_vals):
                ascii_vals.append(ord(configuration.FIRST_PRINTABLE_CHAR))

        ret = ''.join([chr(ascii_val) for ascii_val in ascii_vals])

    return ret


def generate_password_batch(start, size):
    test = start
    yield start
    for i in range(size):
        test = increment_string(test)
        yield test


# String comparer
def try_find_password_in_batch(start, batch):
    for test in generate_password_batch(start, batch):
        if test == configuration.TRUE_PASS:
            return 1

    return 0


def main():
    # what to do when found is true
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(configuration.TIMEOUT)
    ip = configuration.SERVER_IP
    port = configuration.SERVER_PORT
    found = False
    while True:
        sock.connect((ip, port))
        sock.send(found)
        try:
            initial_pass_len = struct.unpack("<I", sock.recv(struct.calcsize("<I")))
            initial_password = sock.recv(initial_pass_len)
            batch = struct.unpack("<I", sock.recv(struct.calcsize("<I")))

        except socket.error:
            break

        found, correct_pass = try_find_password_in_batch(initial_password, batch)
        sock.send(struct.pack("<I",found))
        if found:
            sock.send(struct.pack("<I", len(correct_pass)) + correct_pass)

        sock.close()

def test():
    if try_find_password_in_batch('loloa', 500):
        print 'yes'


if __name__ == '__main__':
    main()
    # test()