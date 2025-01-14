#Simple Logging
import logging

def log_example():
  """Logs info and error messages using the logging module."""
  logging.basicConfig(filename='my_log.log', level=logging.INFO)

  logging.info("This is an info message.")
  try:
    # Simulate an error
    10 / 0
  except ZeroDivisionError:
    logging.error("Error: Division by zero occurred.")

# Example usage:
log_example()