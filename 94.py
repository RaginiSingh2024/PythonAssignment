#Class Method & Static Method
class Counter:
    count = 0

    @classmethod
    def increment(cls):
        cls.count += 1

    @staticmethod
    def display_message():
        print("This is a static method.")

# Example Usage
Counter.increment()
Counter.increment()
print("Count:", Counter.count)
Counter.display_message()