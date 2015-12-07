def is_prime(n):
    return True if all([((n%i)!=0) for i in range(2, n)]) else False

def find_next_prime(n):
    while True:
        n += 1
        if is_prime(n): return n

''' This function returns the prime factorization results of any number'''
def factor(number):
    factors = {}
    prime = 2
    while (True):
        if number == 1:
            return factors
        if number % prime == 0:     # if fully divisible with this prime
            if (prime in factors.keys()):
                factors[prime] += 1
            else:
                factors[prime] = 1

            number = number/prime
        else:
            prime = find_next_prime(prime)

print factor(123)
print factor(3112)
print factor(1517)
