import random


def generate_random_numbers(output_file_name="random_output",
                            limit=100,
                            start=0,
                            stop=100):
    """Generate a list of random numbers between two numbers and save to file.

    The output file is saved in the current working directory.

    :param output_file_name: The file name where the output will be saved.
    :param limit: The total number of random numbers to be generated.
    :param start: The inclusive start number of the range of random numbers.
    :param stop: The exclusive end number of the range of random numbers.
    :return: None
    """
    with open(output_file_name, 'w') as output_file:
        for i in range(limit):
            output_file.write(str(random.randrange(start, stop)) + '\n')


if __name__ == "__main__":
    output_file_name = input('Enter output file name:')
    limit = int(input('Enter the count of random numbers to be generated:'))
    start = int(input('Enter the start range (inclusive):'))
    stop = int(input('Enter the stop range (exclusive):'))
    generate_random_numbers(output_file_name, limit, start, stop)
