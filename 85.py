# CSV Reader
import csv

def read_csv_file(filename):
  """
  Reads a CSV file and prints each row.

  Args:
    filename: The name of the CSV file to read.
  """
  try:
    with open(filename, 'r') as file:
      reader = csv.reader(file)
      for row in reader:
        print(row)
  except FileNotFoundError:
    print(f"Error: File '{filename}' not found.")

# Example usage:
read_csv_file("my_data.csv")