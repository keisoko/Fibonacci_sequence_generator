def fibonacci_sequence_generator(start: int, end: int) -> str:
    fiblist = [0, 1]
    for _ in range(start, end + 1):
        fiblist.append(fiblist[-1] + fiblist[-2])
    return f"The {sequence!r} consist of the {len(fiblist)} Fibonacci numbers:\n\n{fiblist}"


fibonacci_sequences = {
    "first_sequence": {"start": 1, "end": 19},
    "second_sequence": {"start": 1, "end": 24}
}

for sequence, value in fibonacci_sequences.items():
    print(fibonacci_sequence_generator(**value), end="\n\n")
