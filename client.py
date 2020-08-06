import socket
import bitarray
import random
from hamming import encode 
from hamming import bit_compare

# host and port to sent data
HOST = '127.0.0.1' 
PORT = 7777 

# Algorithm to use
hamming_bool = True
noise = True


# Message
msm = "Somebody come get her..."

# verification
msm_bit = bitarray.bitarray()
msm_bit.frombytes(msm.encode('utf-8'))

# original bits
original_msm = bitarray.bitarray()
original_msm.frombytes(msm.encode('utf-8'))

# Hamming Code
if hamming_bool:

    msm_bit_encoded = encode(msm_bit.to01())

    msm_bit.clear()
    msm_bit.extend(msm_bit_encoded)

# Noise
noise_bit_cnt = 0
if noise:
    probabilidad = 1/100                         # estimated errors every x bits
    bitchange = lambda x: 1 if x == 0 else 0    # change a single bit

    for i in range(len(msm_bit)):

        toss = random.uniform(0, 1)
        if toss < probabilidad:
            noise_bit_cnt += 1
            msm_bit[i] = bitchange(msm_bit[i])

# sent message
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
s.connect((HOST, PORT))
s.sendall(msm_bit)

# receive host response
data = bitarray.bitarray()
data.frombytes(s.recv(4096))

print(bit_compare(original_msm, data))



