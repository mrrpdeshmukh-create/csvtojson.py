import csv
import json

def read_csv(filename):
    with open(filename, "r", newline="") as f:
        return list(csv.DictReader(f))

def write_json(data, filename):
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)

def convert_csv_to_json(input_file, output_file):
    data = read_csv(input_file)
    write_json(data, output_file)

if __name__ == "__main__":
    input_file = "student.csv"
    output_file = "student.json"

    data = read_csv(input_file)

    print("CSV Data:")
    for row in data:
        print(row)

    convert_csv_to_json(input_file, output_file)

    print(f"\n{len(data)} rows converted successfully.")
    
    with open(output_file, "r") as f:
        print("\nJSON Data:")
        print(f.read())