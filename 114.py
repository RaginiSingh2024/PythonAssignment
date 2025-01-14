# Decorators
import time

def timer(func):
  def wrapper_timer(*args, **kwargs):
    start_time = time.time()
    result = func(*args, **kwargs)
    end_time = time.time()
    print(f"Elapsed time: {end_time - start_time} seconds")
    return result
  return wrapper_timer

@timer
def my_function():
  # Some time-consuming operation here
  for _ in range(1000000):
    pass

my_function()
