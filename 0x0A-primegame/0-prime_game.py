#!/usr/bin/python3

def sieve_of_eratosthenes(max_num):
    """ Return a list of primes up to max_num, using the Sieve of Eratosthenes. """
    is_prime = [True] * (max_num + 1)
    p = 2
    while p * p <= max_num:
        if is_prime[p]:
            for i in range(p * p, max_num + 1, p):
                is_prime[i] = False
        p += 1
    return [p for p in range(2, max_num + 1) if is_prime[p]]

def isWinner(x, nums):
    """ Determine who wins the most rounds in the game. """
    def winner(n):
        if n < 2:
            return 'Ben'
        
        primes = sieve_of_eratosthenes(n)
        count_moves = 0
        
        # Game simulation
        numbers = [True] * (n + 1)  # True means the number is available
        for prime in primes:
            if prime > n:
                break
            if numbers[prime]:
                count_moves += 1
                # Remove prime and its multiples
                for multiple in range(prime, n + 1, prime):
                    numbers[multiple] = False
        
        return 'Maria' if count_moves % 2 != 0 else 'Ben'
    
    maria_wins = ben_wins = 0
    
    for num in nums:
        if winner(num) == 'Maria':
            maria_wins += 1
        else:
            ben_wins += 1
    
    if maria_wins > ben_wins:
        return 'Maria'
    elif ben_wins > maria_wins:
        return 'Ben'
    else:
        return None
