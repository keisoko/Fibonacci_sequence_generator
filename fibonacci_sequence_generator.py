from logzero import logger, logfile


def fibonacci_sequence_generator(start, end):
    fibonacci_numbers_beginning = [0, 1]
    for _ in range(end + 1):
        fibonacci_numbers_beginning.append(
            fibonacci_numbers_beginning[-1] + fibonacci_numbers_beginning[-2])
    return fibonacci_numbers_beginning


fibonacci_numbers_beginning = fibonacci_sequence_generator(start=1, end=20)
amount_of_numbers = len(fibonacci_numbers_beginning)
print()
# logzero.logfile('test.log')
logger.info(f"Fibonacci number sequence of {amount_of_numbers} numbers is: \n\n{fibonacci_numbers_beginning}")
