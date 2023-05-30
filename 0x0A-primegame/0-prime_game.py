#!/usr/bin/python3
"""Prime game"""

def isWinner(x, nums):
    def isPrime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    winners = {"Maria": 0, "Ben": 0}

    for i in range(x):
        n = nums[i]
        primes = set()
        for num in range(2, n + 1):
            if isPrime(num):
                primes.add(num)

        turn = "Ben"  # Start with Ben instead of Maria
        while primes:
            prime = min(primes)
            primes.remove(prime)

            # Remove prime and its multiples
            for multiple in range(prime, n + 1, prime):
                if multiple in primes:
                    primes.remove(multiple)

            turn = "Maria" if turn == "Ben" else "Ben"  # Switch turn after each move

        winners[turn] += 1

    if winners["Maria"] > winners["Ben"]:
        return "Maria"
    elif winners["Ben"] > winners["Maria"]:
        return "Ben"
    else:
        return None
