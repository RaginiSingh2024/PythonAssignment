# Encapsulation
class Employee:
    def __init__(self, name, salary):
        self.__name = name 
        self.__salary = salary

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_salary(self):
        return self.__salary

    def set_salary(self, salary):
        if salary >= 0:
            self.__salary = salary
        else:
            print("Invalid salary!")

# Example Usage
employee1 = Employee("John Doe", 50000)
print(employee1.get_name()) 
employee1.set_salary(55000)
print(employee1.get_salary())