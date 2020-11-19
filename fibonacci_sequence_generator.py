def fibonacci_sequence_generator(start, end):
    fiblist = [0, 1]
    for _ in range(start, end + 1):
        fiblist.append(fiblist[-1] + fiblist[-2])
    return fiblist


fiblist = fibonacci_sequence_generator(start=1, end=19)
print()
print(f"The sequence of the {len(fiblist)} fibonacci numbers is:\n\n{fiblist}")

# Output:
# The sequence of the 21 fibonacci numbers is:

#     [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765]

# [Done] exited with code=0 in 0.116 seconds
