from AutoAuto import AutoAuto

def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def get_primes(n):
    primes = [2,3,5]
    while len(primes) < n:
        for i in range(primes[-1]+2, 10000000, 2):
            if is_prime(i):
                primes.append(i)
                break
    return primes

from math import log
primes = get_primes(int(log(10000)**(2.718*1.2)))

t = len([p for p in primes if 100<=p<=10000])

import time
time.sleep(5)



objective = \
f"""\
Write a Python function that calculates the number of primes in the range [100, 10,000] (inclusive).
The answer is {t} by the way. Use the answer to verify your function works.
"""

AGI = AutoAuto(objective)
AGI.complete_objective()
print("\n----------->")
print(AGI.result)




