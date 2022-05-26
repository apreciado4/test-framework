import csv


def get_cvs_data(file_name):
    # Create an Empty List to store rows
    data_list = []

    # Open CSV file
    with open(file_name, 'r') as csv_file:
        # Create Reader for csv file
        reader = csv.reader(csv_file)
        # Skip Header
        next(reader)
        for row in reader:
            # Add row from reader to list
            data_list.append(row)
    # Return List
    return data_list
