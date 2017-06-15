from socket import *
from datetime import *
import configuration 
import struct 
import brute_force
import select
 
  
  
def main():
    current = ' '
    batch = configuration.BATCH_SIZE 
    servsock = socket(AF_INET, SOCK_STREAM)
    serv_l=[servsock]
    client_l=[]
    no_need=[]
    correct_pass=None
    found=False
    servsock.bind(("", configuration.SERVER_PORT)) 
    servsock.listen(1) 

    while not found:
        con_l= select.select(serv_l, client_l,serv_l,0)[0]
        for sock in con_l:
            clientsock, add = sock.accept()
            client_l.append(clientsock)

        for clientsock in client_l:
            data =(struct.unpack("<?",clientsock.recv(struct.calcsize("<?"))))
            print data[0]
            if data[0]:
                correct_pass_len=struct.unpack("<I",clientsock.recv(struct.calcsize("<I")))[0] 
                correct_pass=clientsock.recv(correct_pass_len)
                print correct_pass
                clientsock.send('1')
                clientsock.close()
                found=True
                break
 
            clientsock.send(struct.pack("<I", len(current)) + current + struct.pack("<I", batch)) 
            current = brute_force.increment_string(current, batch)
        servsock.listen(1)
            
    print 'finished, the password is:'
    print correct_pass
    servsock.close()
    for i in client_l:
        i.close()
  
if __name__ == '__main__': 
    main() 
