def fibonacci_sequence_generator(start, end):
    fiblist = [0, 1]
    for _ in range(start, end + 1):
        fiblist.append(fiblist[-1] + fiblist[-2])
    return f"The sequence consisting of the {len(fiblist)} fibonacci numbers is:\n\n{fiblist}"


fibonacci_sequences = {
    "first_sequence": {"start": 1, "end": 19},
    "second_sequence": {"start": 1, "end": 24}
}

for key in fibonacci_sequences.keys():
    print(fibonacci_sequence_generator(**fibonacci_sequences[key]), end="\n\n")
