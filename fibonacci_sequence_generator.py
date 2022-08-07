"""Fibonacci Sequence Generator"""

START_OF_SEQUENCE: int = 1

import pprint


def fibonacci_sequence_generator(end: int) -> list[int]:
    """Generates a list of fibonacci sequence numbers from a given sequence"""

    if START_OF_SEQUENCE < 1:
        return []

    fib_list = [0, 1]
    fib_list.extend(
        fib_list[-1] + fib_list[-2] for _ in range(START_OF_SEQUENCE, end + 1)
    )

    fib_list.insert(0, len(fib_list))

    return fib_list


def main():
    """Main program"""
    pp = pprint.PrettyPrinter(underscore_numbers=True, width=200)

    pp.pprint(fibonacci_sequence_generator(end=19))
    pp.pprint(fibonacci_sequence_generator(end=24))
    pp.pprint(fibonacci_sequence_generator(end=22))


if __name__ == "__main__":
    main()
