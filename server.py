import time
import socket
import bitarray
from hamming import decode
from hamming import errorcheck

# Host and port to recieve data
HOST = '127.0.0.1'
PORT = 7777    
socket.setdefaulttimeout(10)

# Algorithm to use
hamming_bool = True

# Mount host
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))

while True:

    # Conection
    s.listen()
    conn, addr = s.accept()

    # Received data
    data = conn.recv(4096)
    data_bit = bitarray.bitarray()
    data_bit.frombytes(data)

    print(data)

    # Error detection algorithm TODO

    # Error corection algorithm 
    if hamming_bool:

        # Error check
        data_b_str = data_bit.to01()
        data_b_str = errorcheck(data_b_str)

        # Decoding
        data_b_str = decode(data_b_str)

        if data_b_str == 'M':

            print('Multiple errors detected')
        
        else:
            data_bit.clear()
            data_bit.extend(data_b_str)
            
            to_transform = bitarray.bitarray()
            to_transform.extend(data_b_str)

            # To normal string
            #data_str = to_transform.tobytes().decode('utf-8')

    conn.sendall(data_bit)