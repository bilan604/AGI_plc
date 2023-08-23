"""
Here's the final Python function that calculates the number of primes in the range [100, 10,000] (inclusive):      

```python
def count_primes(start, end):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    prime_count = 0
    for num in range(start, end + 1):
        if is_prime(num):
            prime_count += 1
    return prime_count

# Test function
print(count_primes(100, 10000))  # Output should be 1204
```
This function works by iterating over each number in the given range and then checking if it's a prime number by trying to divide it with all numbers from 2 to the square root of the number. If the number can be divided with no remainder, it's not a prime number. We count all prime numbers in the given range and return the total count. 
"""

def count_primes(start, end):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    prime_count = 0
    for num in range(start, end + 1):
        if is_prime(num):
            prime_count += 1
    return prime_count

# Test function
print(count_primes(100, 10000))  # Output should be 1204