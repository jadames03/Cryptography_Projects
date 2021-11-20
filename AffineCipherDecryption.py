# ECB mode Decryption using Affine Cipher
def ecb_dec(ys):
    xs = []     # ascii plaintext
    key = int("0X08", 16)
    for i in range(0, len(ys)):
        xi = chr((163 * ((int(ys[i], 16)) - key)) % 256)
        xs.append(xi)
    return xs

# OFB mode    
def ofb_dec(ys):
    xs = []     # ascii plaintext
    key = int("0X08", 16)
    iv = int("0XAA", 16)
    ss = []
    s0 = (key + 11 * iv) % 256
    x0 =  chr(s0 ^ (int(ys[0], 16)))
    ss.append(s0)
    xs.append(x0)                
    for i in range(1, len(ys)):     # general block
        si = (key + 11 * ss[i-1]) % 256
        ss.append(si)
        xi = chr(ss[i] ^ int(ys[i], 16))
        xs.append(xi)
    return xs

# CTR mode
def ctr_dec(ys):
    xs = []
    ss = ['10101000', '10101001', '10101010', '10101011', '10101100']
    key = int('0X08', 16)
    for i in range(len(ys)):
        ei = (key + 11 * int(ss[i], 2)) % 256
        xs.append(chr(int(ys[i],16) ^ ei))
    return xs 

# CBC mode
def cbc_dec(ys):
    xs = []
    key = int("0X08", 16)
    iv = int("0XAA", 16)
    x0 = chr(((163 * (int(ys[0], 16)-key)) % 256) ^ iv)
    xs.append(x0)
    for i in range(1, len(ys)):
        xi = chr(((163 * (int(ys[i], 16) - key)) % 256) ^ int(ys[i-1], 16))
        xs.append(xi)
    return xs

# CFB mode
def cfb_dec(ys):
    xs = []
    key = int("0X08", 16)
    iv = int("0XAA", 16)
    x0 = chr(((key + 11 * iv) % 256) ^ int(ys[0], 16))
    xs.append(x0)
    for i in range(1, len(ys)):
        xi = chr(((key + 11 * int(ys[i-1], 16)) % 256) ^ int(ys[i], 16))
        xs.append(xi)
    return xs

def main():
    cipher_ecb = ["0X3E", "0XAC", "0X33", "0X80"]
    xs_ecb = ecb_dec(cipher_ecb)
    print("\nECB decryption ", xs_ecb)

    cipher_ofb = ['0X3b', '0Xd5', '0X69', '0X39', '0X53']
    xs_ofb = ofb_dec(cipher_ofb)
    print("\nOFB decryption ", xs_ofb)

    cipher_cbc = ['0X8a', '0Xdf', '0X98', '0X021', '0Xf4']
    xs_cbc = cbc_dec(cipher_cbc)
    print("\nCBC decryption ", xs_cbc)

    cipher_ctr = ['0X22', '0X27', '0X37', '0X09']
    xs_ctr = ctr_dec(cipher_ctr)
    print("\nCTR decryption ", xs_ctr)

    cipher_cfb = ['0X31', '0X4c', '0X23', '0Xfa', '0Xa3']
    xs_cfb = cfb_dec(cipher_cfb)
    print("\nCFB decryption ", xs_cfb)

    # cipher_cbc = ["0X8A", "0XDF", "0X98", "0X021", "0XF4"]
    # xs_cbc = cbc_dec(cipher_cbc)
    # print("\nCBC decryption ", xs_cbc)

main()

