## Check Leap Year
def is_leap_year(year):
  """
  Determines if a given year is a leap year.

  Args:
    year: The year to check.

  Returns:
    True if the year is a leap year, False otherwise.
  """
  if year % 4 == 0:
    if year % 100 == 0:
      return year % 400 == 0
    else:
      return True
  else:
    return False

# Example usage
year = int(input("Enter a year: "))
if is_leap_year(year):
  print(year, "is a leap year.")
else:
  print(year, "is not a leap year.")