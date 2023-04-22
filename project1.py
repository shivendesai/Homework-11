#Written by Shiven Desai
# create a new Pet object with default values
class Pet:
    def __init__(self, name, animal_type, age):
        self.__name = name
        self.__animal_type = animal_type
        self.__age = age

    def set_name(self, name):
        self.__name = name

    def set_animal_type(self, animal_type):
        self.__animal_type = animal_type

    def set_age(self, age):
        self.__age = age

    def get_name(self):
        return self.__name

    def get_animal_type(self):
        return self.__animal_type

    def get_age(self):
        return self.__age


# create a new Pet object with default values
pet = Pet("", "", 0)

# prompt the user to enter the pet's name, type, and age
name = input("Enter the pet's name: ")
type = input("Enter the pet's animal type: ")
age = int(input("Enter the pet's age: "))

# set the pet's attributes using the object's setter methods
pet.set_name(name)
pet.set_animal_type(type)
pet.set_age(age)

# display the pet's attributes using the object's getter methods
print("Pet's name: ", pet.get_name())
print("Pet's animal type: ", pet.get_animal_type())
print("Pet's age: ", pet.get_age())
