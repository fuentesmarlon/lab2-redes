import socket
import bitarray
from hamming import decode
from hamming import errorcheck

# Host and port to recieve data
HOST = '127.0.0.1'
PORT = 7777    

# Algorithm to use
hamming_bool = True

# Mount host
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))

# Conection
s.listen()
conn, addr = s.accept()
print('Connected by', addr)


# Received data
data = conn.recv(4096)
data_bit = bitarray.bitarray()
data_bit.frombytes(data)

# Error detection algorithm TODO

# Error corection algorithm 
if hamming_bool:

    # Error check
    data_b_str = data_bit.to01()
    data_b_str = errorcheck(data_b_str)

    # Decoding
    data_b_str = decode(data_b_str)

    data_bit.clear()
    data_bit.extend(data_b_str)

    # To normal string
    data_str = data_bit.tobytes().decode('utf-8')

    # To bit to sent back
    data_bit.clear()
    data_bit.frombytes(data_str.encode('utf-8'))

print(data_str)

conn.sendall(data_bit)