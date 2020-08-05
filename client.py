import socket
import bitarray
import random
from hamming import encode 

# host and port to sent data
HOST = '127.0.0.1' 
PORT = 7777 

# Algorithm to use
hamming_bool = True

# Message
msm = "Luis Diego Fernandez"

# verification
msm_bit = bitarray.bitarray()
msm_bit.frombytes(msm.encode('utf-8'))

# Hamming Code
if hamming_bool:

    msm_bit_encoded = encode(msm_bit.to01())

    msm_bit.clear()
    msm_bit.extend(msm_bit_encoded)

# Noise
probabilidad = 1/200                            # estimated errors every x bits
bitchange = lambda x: 1 if x == 0 else 0    # change a single bit

counter = 0
for i in range(len(msm_bit)):

    toss = random.uniform(0, 1)
    if toss < probabilidad:
        counter += 1
        msm_bit[i] = bitchange(msm_bit[i])

print("Noise = " + str(counter) + " bits, de " + str(len(msm_bit)) + " bits")



# sent message
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
s.connect((HOST, PORT))
s.sendall(msm_bit)

# receive host response
data = s.recv(1024)
print(repr(data))

