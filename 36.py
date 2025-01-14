#Guess the Number (Game)
def guess_the_number():
  """Guess the Number game."""
  secret_number = random.randint(1, 10)
  guesses = 0
  while True:
    guess = int(input("Guess a number between 1 and 10: "))
    guesses += 1
    if guess == secret_number:
      print(f"Congratulations! You guessed the number in {guesses} tries.")
      break
    elif guess < secret_number:
      print("Too low. Try again.")
    else:
      print("Too high. Try again.")