"""Encription
Author: Andy Daubner - 22.01.2022
"""
from json import load, dump
from random import SystemRandom
from sympy import nextprime, primerange
from math import gcd

numgen = SystemRandom()


KEYS_PATH = "keys.json"


def read_keys():
    with open(KEYS_PATH, "r") as f:
        keys = load(f)
        return keys


def write_keys(keys):
    with open(KEYS_PATH, "w") as f:
        dump(keys, f, indent=4)


def generate_keys():
    """RSA encryption
    https://baloian.medium.com/how-to-generate-public-and-private-keys-for-the-blockchain-db6d057432fb
    """
    # Generate primes
    p = numgen.choice(list(primerange(10000, 400000)))
    q = numgen.choice(list(primerange(10000, 400000)))
    n = p * q
    z = (p - 1) * (q - 1)  # Mod wheel
    # encryption
    e = generate_e(z)
    d = pow(e, -1, z)
    print(e, d, z)


def generate_e(z):
    prime = nextprime(0)
    while gcd(prime, z) != 1:
        prime = nextprime(prime)
    return prime


def main():
    generate_keys()
    # print(read_keys())
    # write_keys({"public": "sadfasdf", "private": "hello"})


if __name__ == "__main__":
    main()
