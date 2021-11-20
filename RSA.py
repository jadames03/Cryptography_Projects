import random

# Use Euclidean Algorithm to evaluate gcd
def EA_GCD(x,y):
    while y:
        x, y = y, x % y
    return x
# Use Extended Euclidean Algorithm
def EEA_GCD(a,b):
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = EEA_GCD(b%a,a)
    x= y1-(b//a)* x1
    y=x1
    return gcd, x, y
# Find modular inverse of the value
def modInverse(b, n):
    gcd, _, t = EEA_GCD(n,b)
    if gcd == 1:
        i=t%n
    elif gcd !=1:
        print("no inverse")
    return i
# Square and multiply algorithm to evaluate exponentiation
def powMod_sm(base,exp,n):
    exp_b=bin(exp)
    value=base 
    for i in range(3,len(exp_b)):
        value = (value**2)%n
        if exp_b[i:i+1]=='1':
            value =(value *base)%n
        return n
# Use Miller-Rabin Primality Test to choose prime number with s=512 bits and
def mrt(p):
    if p==2 or p==3:
        return True
    if p<=1 or p%2 ==0:
        return False
    p1=p-1
    t=15
    u=0
    r=p1
    while r%2==0:
        u=u+1
        r=r/2
    for i in range(t,1):
        a= random.randint(2,p-2)
        z=powMod_sm(a, int(r),p)
        if z!=1 and z!=p1:
            j=1
            while j<u and z!=p1:
                z=powMod_sm(z,2,p)
                if z==1:
                    return False
                j+=1
            if z!=p1:
                return False
    return True
def isPrime(n):
    if n % 2 == 0:
        return True
def genPrime(min, max):
    x = random.randint(min, max)
    while(not (isPrime(x))):
        x = random.randint(min, max) 
    return x

def rsa_keyGeneration(p,q):
    n=p*q
    phi_n=(p-1)*(q-1)
    for i in range(2,24):
        if EA_GCD(i, phi_n)==1:
            e=i
            break
    d=modInverse(e,phi_n)
    return n,e,d

def enc(pk, orginal_msg):
    key, n = pk
    c = [pow(ord(char), key, n) for char in orginal_msg]
    return c

def dec(pk, enc_msg):
    key, n = pk
    u = [str(pow(char, key, n)) for char in enc_msg]
    org = [chr(int(char2)) for char2 in u]
    return ''.join(org)

def main():

    p = genPrime(2**512,2**513)
    q = genPrime(2**512,2**513)
    
    print("First prime is ->", p)
    print("Second prime is ->", q)

    n, e, d = rsa_keyGeneration(p, q)
    print("Your public key is ")
    print("Exponent e: ", e)
    print("N :", n)
    print("Your private key is ")
    print("Exponent e: ", d)
    print("N :", n)

    msg = 740
    print("The orginal message: ", msg)
    y=int(powMod_sm(msg,e,n))
    print("The encrypted message: ", y)
    x=int(powMod_sm(y,int(d),n))
    print("Original message after decrytion: ", x)
main()