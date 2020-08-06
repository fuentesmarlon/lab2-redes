import math

def encode(org): 

    # Bits string values
    m = len(org)
    r = 0
    enc = ''

    # Calc. redundant bits
    for i in range(m): 

        if 2**i >= m + i + 1: 
            r =  i 
            break

    # insert 0 in redundant bits
    j = 0
    k = 1
    for i in range(1, m + r + 1): 
        
        # power of 2 -> insert 0
        if i == 2**j: 
            enc = enc + '0'
            j += 1

        # append data
        else: 
            enc = enc + org[-1 * k]
            k += 1

    # reverse data
    enc = enc[::-1] 
    n = len(enc) 

    # find r parity bits
    for i in range(r): 
        
        k = 0
        for j in range(1, n + 1): 

            if j & (2**i) == (2**i): 
                k = k ^ int(enc[-1 * j]) 

        enc = enc[:n-(2**i)] + str(k) + enc[n-(2**i)+1:] 

    return enc

def decode(enc):

    dec = list(enc)[::-1]
    m = len(enc)
    r = []

    # Calc. redundant bits
    j = 0
    for i in range(m): 

        if 2**j == i: 
            r.append(i - 1)
            j += 1

    r = r[::-1]

    # erase redundat bits
    for i in r:
        dec.pop(i)

    dec = dec[::-1]

    return "".join(dec)

def errorcheck(org): 
    n = len(org)
    r = 0
    enc = org
    dec = list(enc)

    # trim down
    tmp_n = 8 * math.floor((n-1)/8)
    tmp_r = 0

    for i in range(tmp_n):          #trimmer redundat

        if 2**i >= tmp_n + i + 1: 
            tmp_r =  i 
            break

    if n > tmp_n + tmp_r:           # trimmer condition

        to_del = n - tmp_n - tmp_r
        
        for i in range(to_del):
            dec.pop()

        n = tmp_n + tmp_r
        enc = "".join(dec)
        
    # Calc. redundant bits
    for i in range(n): 

        if 2**i >= n + i + 1: 
            r =  i 
            break
    
    # change bits
    bitchange = lambda x: '1' if x == '0' else '0'

    res = 0

    # find r parity bits
    for i in range(r): 
        
        k = 0
        for j in range(1, n + 1): 

            if(j & (2**i) == (2**i)): 
                k = k ^ int(enc[-1 * j]) 

        res = res + k*(10**i) 
        pos = n - int(str(res), 2)
        
        if pos < 0:
            return "M"

    # Convert binary to decimal
    try: 
        pos = n - int(str(res), 2)
        dec[pos] = bitchange(dec[pos])
        return "".join(dec)

    except:
        return "".join(dec)

def bit_compare(a, b):

    counter = 0
    for i in range(len(a)):
        if a[i] != b[i]:
            counter += 1

    return counter








