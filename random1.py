import csv
import random

def select_random_persons(csv_file_path, num_persons):
    with openth, 'r') as file:
        reader = csv.reader(file)
        names = [row[0] for row in reader]  # Assuming names are in the first column

    if num_persons > len(names):
        raise ValueError("Number of persons requested exceeds the number of names in the file.")

    return random.sample(names, num_persons)

# Example usage:
csv_file_path = 'names.csv'
num_persons = 3
selected_persons = select_random_persons(csv_file_path, num_persons)
print(selected_persons)