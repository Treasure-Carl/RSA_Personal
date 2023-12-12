import math
# def primenumber(p, q):
    
#     p = math(range(2, 101))
#     q = math(range(2, 101))
#     return p * q

# primenumber(7, 9)
# def valueof_privatekey():
#     d = range(2, 1000)
#     public_key = int(input("Public key: "))
#     gcd = int(input("value for gcd(n): "))
#     for i in d:
#         if (public_key * i) % gcd == 1:
#             # new_key = []
#             new_key = i
#             # return new_key
#             print(f'Private Key: {new_key}')


# valueof_privatekey()
# pass

import random
import math

def is_prime(number):
    if number < 2:
        return False
    for i in range(2, number // 2 + 1):
        if number % i == 0:
            return False
        
    return True

def generate_prime(min_value, max_value):
    prime = random.randint(min_value, max_value)
    while not is_prime(prime):
        prime = random.randint(min_value, max_value)

    return prime

def mod_inverse(e, phi):
    for d in range(3, phi):
        if(d * e) % phi == 1:
            return d
        
    raise ValueError("mod_inverse does not exist")


# Here we want to generate the values of p and q using the generate_prime function already created
p, q = generate_prime(1000, 5000), generate_prime(1000, 5000)

# checking if the value for p and q are not the same
# if they are the same regenerate prime for q so q makes a difference 
while p == q:
    q = generate_prime(1000, 5000)

# getting the value of phi
n = p * q
phi_n = (p-1) * (q-1)

e = random.randint(3, phi_n-1)
while math.gcd(e, phi_n) != 1:
    e = random.randint(3, phi_n - 1)


d = mod_inverse(e, phi_n)

print('Public Key: ', e)
print('Private Key: ', d)
print('n: ', n)
print('Phi of n: ', phi_n)
print('p: ', p)
print('q: ', q)



# encryption
message  = "hey there, how are you doing"

message_encoded = [ord(ch) for ch in message]
#  (m ^ e) and n = c
#  Note - we do not use asymentric encryption to chat with people we use it to exchange keys and do some small stuff
ciphertext = [pow(ch, e, n) for ch in message_encoded]
# (c^e) mod n
# pow(c, e, n)
print(ciphertext)


# decryption
message_encoded = [pow(ch, d, n) for ch in ciphertext]

message = "".join(chr(ch) for ch in message_encoded)

print(message)