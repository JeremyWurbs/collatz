import numpy as np


def is_prime(n):
    """Returns whether input number is prime.

    Reference: https://stackoverflow.com/questions/15285534/isprime-function-for-python-language
    """
    if n == 2 or n == 3: return True
    if n < 2 or n % 2 == 0: return False
    if n < 9: return True
    if n % 3 == 0: return False
    r = int(n ** 0.5)
    # since all primes > 3 are of the form 6n ± 1
    # start with f=5 (which is prime)
    # and test f, f+2 for being prime
    # then loop by 6.
    f = 5
    while f <= r:
        if n % f == 0: return False
        if n % (f + 2) == 0: return False
        f += 6
    return True


def prime_sieve(N):
    """ Input n>=6, Returns an array of primes, 2 <= p < n

    Reference: https://blog.finxter.com/the-fastest-python-method-to-compute-all-primes-n/
    """
    sieve = np.ones(N // 3 + (N % 6 == 2), dtype=np.bool_)
    for i in range(1, int(N ** 0.5) // 3 + 1):
        if sieve[i]:
            k = 3 * i + 1 | 1
            sieve[k * k // 3::2 * k] = False
            sieve[k * (k - 2 * (i & 1) + 4) // 3::2 * k] = False
    return np.r_[2, 3, ((3 * np.nonzero(sieve)[0][1:] + 1) | 1)]
