import random

names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

name_list = len(names)

random_name = random.randint(0, name_list - 1)
person_paying = names[random_name]

print(person_paying + " is buying food today!")