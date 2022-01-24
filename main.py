"""Encription
Author: Andy Daubner - 22.01.2022
"""
from json import load, dump
from random import SystemRandom
from sympy import nextprime, primerange
from math import gcd

numgen = SystemRandom()


KEYS_PATH = r"keys.json"


def read_keys():
    with open(KEYS_PATH, "r") as f:
        keys = load(f)
        return keys


def write_keys(n, e, d):
    with open(KEYS_PATH, "w") as f:
        dump({"public": [e, n], "private": [d, n]}, f, indent=4)


def generate_keys():
    """RSA encryption
    https://baloian.medium.com/how-to-generate-public-and-private-keys-for-the-blockchain-db6d057432fb
    """
    # Generate primes
    p = numgen.choice(list(primerange(10000, 400000)))
    q = numgen.choice(list(primerange(10000, 400000)))
    z = (p - 1) * (q - 1)  # Mod wheel
    e = 65537
    while gcd(65537, z) != 1:
        p = numgen.choice(list(primerange(10000, 400000)))
        q = numgen.choice(list(primerange(10000, 400000)))
        z = (p - 1) * (q - 1)  # Mod wheel
    n = p * q
    d = pow(e, -1, z)
    return n, e, d


def generate_e(z):
    prime = nextprime(0)
    while gcd(prime, z) != 1:
        prime = nextprime(prime)
    return prime


def create_key_pair():
    n, e, d = generate_keys()
    write_keys(n, e, d)


def main():
    create_key_pair()
    # print(read_keys())
    # write_keys({"public": "sadfasdf", "private": "hello"})


if __name__ == "__main__":
    main()
