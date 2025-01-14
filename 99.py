# Multiple Inheritance
class Flyer:
    def fly(self):
        print("I can fly!")

class Swimmer:
    def swim(self):
        print("I can swim!")

class FlyingFish(Flyer, Swimmer):
    pass

# Example Usage
flying_fish = FlyingFish()
flying_fish.fly() 
flying_fish.swim()