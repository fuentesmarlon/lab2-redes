import socket
import bitarray

# host and port to recieve data
HOST = '127.0.0.1'
PORT = 7777      

# mount host
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))

# conection
s.listen()
conn, addr = s.accept()
print('Connected by', addr)

# received data
try:
    data = conn.recv(2048)
    data_bit = bitarray.bitarray()
    data_bit.frombytes(data)

    # error detection algorithm TODO

    # error corection algorithm TODO

    conn.sendall(b'OK')

except:
    conn.sendall(b'NOT OK')