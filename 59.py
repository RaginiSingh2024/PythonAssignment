#Command-Line Arguments
import sys

def print_arguments():
  """Prints command-line arguments."""
  print("Command-line arguments:")
  for arg in sys.argv[1:]:
    print(arg)

# Example usage:
if __name__ == "__main__":
  print_arguments()