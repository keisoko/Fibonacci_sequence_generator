from logzero import logger

def fibonacci_sequence_generator(start, end):
    fiblist = [0, 1]
    for _ in range(end + 1):
        fiblist.append(fiblist[-1] + fiblist[-2])
    return fiblist

fiblist = fibonacci_sequence_generator(start=1, end=19)
amount_of_numbers = len(fiblist)
print()
logger.info(f"Fibonacci number sequence of {amount_of_numbers} numbers is: \n\n{fiblist}")

# Output:
#
# [I 200411 19:23:22 fibonacci_sequence_generator:15] Fibonacci numbers sequence of 21 numbers is:
#    
#     [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765]
#
# [Done] exited with code=0 in 0.191 seconds
