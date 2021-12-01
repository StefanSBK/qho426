#Initialise empty dictionary
phonebook = {}
d2 = dict()

#Initialise non-empty dictionary
Stefan_data = {"Name": "Stefan", "Age" :55, "Doggo": False, "Title" : "Mr"}

#Print full dictionary
print(Stefan_data)

#Use part of the dictionary for printing purposes
x = Stefan_data["Name"]
y = Stefan_data["Age"]
print(f"{x} is {y} years old")

#Adding elements to a dictionary
phonebook["Max"] = "+7789564839"
phonebook["Ugabuga"] = "+56765654444"
phonebook["Lucy"] = None

print(phonebook)

#Add more people to the phonebook
for i in range(3):
  n = input("Enter the name: ")
  numb = input(f"Enter {n}'s their number: ")
  phonebook[n] = numb

name = input("Who would you like to call?")

if name in phonebook:
  print(f"Calling {name} with phone number {phonebook[name]}")
else:
  print(f"{name} is not in your phonebook")