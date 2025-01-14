#CSV Reader
import csv

def read_csv(filename):
  """Reads a CSV file and prints each row."""
  try:
    with open(filename, 'r') as file:
      reader = csv.reader(file)
      for row in reader:
        print(row)
  except FileNotFoundError:
    print(f"Error: File '{filename}' not found.")
  except csv.Error as e:
    print(f"CSV Error: {e}")

# Example usage:
read_csv("my_data.csv")