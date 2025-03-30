# Returns sum of primes in range from 1 to n.
def sum_of_primes(n):
    summ=0
    # List to store prime numbers
    prime = [True] * (n + 1)

    # 0 and 1 are not prime numbers
    prime[0] = prime[1] = False

    for p in range(2, int(n**0.5) + 1):
        # If prime[p] is true, it is a prime
        if prime[p]:
            # Mark all multiples of p as non-prime
            for i in range(p * p, n + 1, p):
                prime[i] = False

    # Return sum of primes
    for i in range(2,n+1):
        if prime[i]==True:
            summ+=i
    return summ

n = 10
print(sum_of_primes(n))
