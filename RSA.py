import random
import math
from sympy import randprime, mod_inverse

def generate_large_prime(bits=512):
    #Generate a large prime number using sympy.randprime for efficiency.
    return randprime(2**(bits-1), 2**bits)

def generate_rsa_keys():
    #Generate RSA public and private keys.
    # Generate two large prime numbers p and q
    p = generate_large_prime()
    q = generate_large_prime()

    while p == q:  # Ensure p and q are distinct
        q = generate_large_prime()

    # Compute n and φ(n)
    n = p * q
    phi_n = (p - 1) * (q - 1)

    # Choose a common public exponent e (65537 is a good choice)
    e = 65537
    while math.gcd(e, phi_n) != 1:  # Ensure e is coprime to φ(n)
        e = random.randint(3, phi_n - 1)

    # Compute the private key d using modular inverse
    d = mod_inverse(e, phi_n)

    return (e, n), (d, n)

# Generate and print RSA keys
public_key, private_key = generate_rsa_keys()
print(f"Public Key: {public_key}")

print(f"Private Key: {private_key}")
 

