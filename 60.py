#JSON Read & Write
import json

def modify_json(filename, key, new_value):
  """Reads data from a JSON file, modifies a value, and writes the updated data back to the file."""
  try:
    with open(filename, 'r') as file:
      data = json.load(file)
    data[key] = new_value
    with open(filename, 'w') as file:
      json.dump(data, file, indent=4)
  except FileNotFoundError:
    print(f"Error: File '{filename}' not found.")
  except json.JSONDecodeError:
    print(f"Error: Invalid JSON data in '{filename}'.")

# Example usage:
modify_json("my_data.json", "name", "New Name")
