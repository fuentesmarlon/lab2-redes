import socket
import bitarray

# host and port to sent data
HOST = '127.0.0.1' 
PORT = 7777      

# message
msm = "The silver cat feeds when blue meets yellow in the west."

# verification
msm_bit = bitarray.bitarray()
msm_bit.frombytes(msm.encode('utf-8'))

# noise TODO

# sent message
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
s.connect((HOST, PORT))
s.sendall(msm_bit)
data = s.recv(1024)

# receive host response
print(repr(data))

