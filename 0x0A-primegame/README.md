0x0A. Prime Game

# Prime Game

## Overview

The Prime Game is a competitive game played between two players, Maria and Ben. Given a set of consecutive integers starting from 1 up to and including `n`, players take turns choosing a prime number from the set and removing that number and its multiples. The player who cannot make a move loses the game. The objective of this project is to determine the winner of multiple rounds of the game based on the strategic removal of prime numbers.

## Concepts Used

- **Prime Numbers**: Understanding prime numbers and efficient algorithms for identifying them.
- **Sieve of Eratosthenes**: An efficient algorithm for finding all prime numbers up to a given limit.
- **Game Theory**: Basic principles of competitive games where players take turns and the concept of optimal play.
- **Dynamic Programming/Memoization**: Using previous results to optimize future calculations.
- **Python Programming**: Utilizing loops, conditional statements, and data structures for implementing game logic.

## Requirements

- Python 3.x
- No external libraries are required; the implementation uses standard Python features.

## Usage

To determine the winner of the Prime Game, you can run the provided main script or use the function directly in your code.

### Example

You can run the main script as follows:

The output will display the winner of the game based on the given rounds.

### Function Prototype
- **Parameters**:
  - `x`: The number of rounds (integer).
  - `nums`: A list of integers representing the upper limits for each round.

- **Returns**:
  - The name of the player that won the most rounds. If the winner cannot be determined, it returns `None`.

### Example Input/Output
python 
x = 5 
nums = [2, 5, 1, 4, 3] 
print("Winner: {}".format(isWinner(x, nums)))

Output:Winner: Ben

## Contributing

Contributions are welcome! If you have suggestions for improvements or enhancements, please feel free to create a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Inspired by classic game theory problems and prime number algorithms.
- Special thanks to educational resources on prime numbers and algorithms.
