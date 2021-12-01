"""Fibonacci Sequence Generator"""

def fibonacci_sequence_generator(START_OF_SEQUENCE: int, end: int) -> str:
    """Generates a list of fibonacci sequence numbers from a given sequence"""
    fiblist = [0, 1]
    for _ in range(START_OF_SEQUENCE, end + 1):
        fiblist.append(fiblist[-1] + fiblist[-2])
    return f"The {sequence!r} consist of the {len(fiblist)} Fibonacci numbers:\n\n{fiblist}"


fibonacci_sequences = {
    "first_sequence": {"START_OF_SEQUENCE": 1, "end": 19},
    "second_sequence": {"START_OF_SEQUENCE": 1, "end": 24}
}

sequence = None

for sequence, value in fibonacci_sequences.items():
    print(fibonacci_sequence_generator(**value), end="\n\n")
