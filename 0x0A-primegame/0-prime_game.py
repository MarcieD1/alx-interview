#!/usr/bin/python3

def sieve_of_eratosthenes(max_n):
    """Returns a list of primes up to max_n using the Sieve of Eratosthenes."""
    is_prime = [True] * (max_n + 1)
    p = 2
    while (p * p <= max_n):
        if (is_prime[p]):
            for i in range(p * p, max_n + 1, p):
                is_prime[i] = False
        p += 1
    return [p for p in range(2, max_n + 1) if is_prime[p]]

def play_game(n):
    """Simulates the game for a given n and returns the winner."""
    primes = sieve_of_eratosthenes(n)
    prime_count = len(primes)
    
    # The winner is determined by the number of primes
    # If the count is odd, Maria wins; if even, Ben wins
    return 'Maria' if prime_count % 2 == 1 else 'Ben'

def isWinner(x, nums):
    """Determines the overall winner of x rounds."""
    maria_wins = 0
    ben_wins = 0
    
    for n in nums:
        winner = play_game(n)
        if winner == 'Maria':
            maria_wins += 1
        else:
            ben_wins += 1
    
    if maria_wins > ben_wins:
        return 'Maria'
    elif ben_wins > maria_wins:
        return 'Ben'
    else:
        return None

# Example usage
if __name__ == "__main__":
    print("Winner: {}".format(isWinner(5, [2, 5, 1, 4, 3])))
