import random

output_file_name = input('Enter output file name:')
limit = int(input('Enter the count of random numbers to be generated:'))
start = int(input('Enter the start range (inclusive):'))
stop = int(input('Enter the stop range (exclusive):'))

with open(output_file_name, 'w') as output_file:
    for i in range(limit):
        output_file.write(str(random.randrange(start, stop)) + '\n')
