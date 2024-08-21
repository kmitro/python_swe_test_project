import csv

def read_data(file_path):
    data = []
    with open(file_path, mode='r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            data.append(row)
    return data

def process_data(data):
    processed_data = []
    for row in data:
        processed_row = [item.strip().upper() for item in row]
        processed_data.append(processed_row)
    return processed_data

def write_data(file_path, data):
    with open(file_path, mode='w', newline='') as file:
        csv_writer = csv.writer(file)
        csv_writer.writerows(data)

def main():
    input_file = 'input.csv'
    output_file = 'output.csv'

    print("Reading data from", input_file)
    data = read_data(input_file)

    print("Processing data")
    processed_data = process_data(data)

    print("Writing data to", output_file)
    write_data(output_file, processed_data)

    print("Data processing complete")

if __name__ == "__main__":
    main()