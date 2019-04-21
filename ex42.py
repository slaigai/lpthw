# Note inheriting from object is optional in Python 3 but it is convention to include it to be explicit.

# Python supports multiple inheritance but it makes code more complex, ambiguous, and probably causes problems down
# the line...


# Animal is a object
class Animal(object):
    pass


# Dog is a Animal
class Dog(Animal):

    def __init__(self, name):
        # Dog has a name attribute
        self.name = name


# Cat is a Animal
class Cat(Animal):

    def __init__(self, name):
        # Cat has a name attribute
        self.name = name


# Person is a object
class Person(object):

    def __init__(self, name):
        # Person has a name attribute
        self.name = name
        # Person has a pet attribute (declared)
        self.pet = None


# Employee is a Person
class Employee(Person):

    def __init__(self, name, salary):
        # Call superclass constructor
        super(Employee, self).__init__(name)
        # Employee has a salary attribute (and name from Person)
        self.salary = salary


# Fish is a object
class Fish(object):
    pass


# Salmon is a Fish
class Salmon(Fish):
    pass


# Halibut is a Fish
class Halibut(Fish):
    pass


# rover is a Dog with name "Rover"
rover = Dog("Rover")

# satan is a Cat with name "Satan"
satan = Cat("Satan")

# mary is a Person with name "Mary"
mary = Person("Mary")

# mary has a pet satan
mary.pet = satan

# frank is a Employee with name "Frank" and salary 120000
frank = Employee("Frank", 120000)

# frank has a pet rover
frank.pet = rover

# flipper is a Fish
flipper = Fish()

# crouse is a Salmon
crouse = Salmon()

# harry is a Halibut
harry = Halibut()
