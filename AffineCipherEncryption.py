# ECB mode Encryption using Affine Cipher
def ecb(word):
    # separates the word in the list of letters
    list_of_letters = list(word)
    xs = []     # list of decimal plaintexts
    for i in list_of_letters:
        dec = ord(i)
        xs.append(dec)
    # Affine Cipher Encryption
    key = int("0X08", 16)
    ys = []     # list of hex ciphertext
    for xi in xs:
        yi = hex((key + 11 * xi) % 256)
        ys.append(yi)
    return xs, ys

# OFB mode


def ofb(word):
    list_of_letters = list(word)
    xs = []
    for i in list_of_letters:
        dec = ord(i)
        xs.append(dec)
    iv = int("0XAA", 16)
    key = int("0X08", 16)
    ss = []
    ys = []
    s0 = (key + 11 * iv) % 256
    y0 = hex(xs[0] ^ s0)
    ss.append(s0)
    ys.append(y0)
    for i in range(1, len(xs)):
        si = (key + 11 * ss[i-1]) % 256
        ss.append(si)
        yi = hex(xs[i] ^ ss[i])
        ys.append(yi)
    return xs, ys

# CTR mode


def ctr(word):
    list_of_letters = list(word)
    xs = []
    for i in list_of_letters:
        dec = ord(i)
        xs.append(dec)
    ss = ["10101000", "10101001", "10101010", "10101011", "10101100"]
    key = int("0X08", 16)
    ys = []
    for i in range(len(xs)):
        ei = (key + 11 * int(ss[i], 2)) % 256
        yi = hex(xs[i] ^ ei)
        ys.append(yi)
    return xs, ys

# CBC mode


def cbc(word):
    list_of_letters = list(word)
    xs = []
    for i in list_of_letters:
        dec = ord(i)
        xs.append(dec)
    key = int("0X08", 16)
    iv = int("0XAA", 16)
    ys = []
    y0 = hex((key + 11 * (xs[0] ^ iv)) % 256)
    ys.append(y0)
    for i in range(1, len(xs)):
        yi = hex((key + 11 * (xs[i] ^ int(ys[i-1], 16))) % 256)
        ys.append(yi)
    return xs, ys

# CFB mode


def cfb(word):
    list_of_letters = list(word)
    xs = []
    for i in list_of_letters:
        dec = ord(i)
        xs.append(dec)
    key = int("0X08", 16)
    iv = int("0XAA", 16)
    ys = []
    y0 = hex(((key + 11 * iv) ^ xs[0]) % 256)
    ys.append(y0)
    for i in range(1, len(xs)):
        yi = hex(((key + 11 * int(ys[i-1], 16)) ^ xs[i]) % 256)
        ys.append(yi)
    return xs, ys


def main():
    word_ecb = "neary"
    xs_ecb, ys_ecb = ecb(word_ecb)

    print("\nECB plaintext", xs_ecb)
    print("\nECB Mode ciphertext =", ys_ecb)

    word_ofb = "bleary"
    xs_ofb, ys_ofb = ofb(word_ofb)

    print("\nOFB plaintext", xs_ofb)
    print("\nOFB Mode ciphertext =", ys_ofb)

    word_ctr = "beery"
    xs_ctr, ys_ctr = ctr(word_ctr)

    print("\nCTR plaintext", xs_ctr)
    print("\nCTR Mode ciphertext =", ys_ctr)

    word_cfb = "leary"
    xs_cfb, ys_cfb = cfb(word_cfb)

    print("\nCFB plaintext", xs_cfb)
    print("\nCFB Mode ciphertext =", ys_cfb)

    word_cbc = "weary"
    xs_cbc, ys_cbc = cbc(word_cbc)

    print("\nCBC plaintext", xs_cbc)
    print("\nCBC Mode ciphertext =", ys_cbc)


main()
