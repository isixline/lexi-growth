import csv

# create csv file by given header and data
def create_csv_file(file_path, header, data):
    with open(file_path, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(header)
        writer.writerows(data)