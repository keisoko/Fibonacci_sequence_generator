from logzero import logger, logfile


def fibonacci_sequence_generator(end):
    fibonacci_numbers_beginning = [0, 1]
    for _ in range(end + 1):
        fibonacci_numbers_beginning.append(
            fibonacci_numbers_beginning[-1] + fibonacci_numbers_beginning[-2])
    return fibonacci_numbers_beginning


fibonacci_numbers_beginning = fibonacci_sequence_generator(end=12)
print()
# logzero.logfile('test.log')
logger.info(f"Fibonacci number sequence is: \n\n{fibonacci_numbers_beginning}")
