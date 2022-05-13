"""Fibonacci Sequence Generator"""


def fibonacci_sequence_generator(START_OF_SEQUENCE: int, end: int) -> str:
    """Generates a list of fibonacci sequence numbers from a given sequence"""
    fiblist = [0, 1]
    fiblist.extend(fiblist[-1] + fiblist[-2] for _ in range(START_OF_SEQUENCE, end + 1))

    return f"The given sequence consist of the {len(fiblist)} Fibonacci numbers:\n\n{fiblist}"


def main():
    """Main program"""

    print(fibonacci_sequence_generator(START_OF_SEQUENCE=1, end=19), end="\n\n")
    print(fibonacci_sequence_generator(START_OF_SEQUENCE=1, end=24), end="\n\n")
    print(fibonacci_sequence_generator(START_OF_SEQUENCE=1, end=22), end="\n\n")


if __name__ == "__main__":
    main()
