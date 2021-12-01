#Declare empty list
hated = []

#Declare non-empty list
fav = ["Carbonara", "Pizza", "Casatiello", "pierogi"]

#Print full list
print(fav)

#Print a single element
print(fav[2])

#Add elements at the end of the list
hated.append("Tofu")
hated.append("Beans")
fav.append("Lasagne")

#Appending using a loop and user input
for i in range(2):
  print("Enter another hated dish: ")
  dish = input()
  hated.append(dish)

#Print out the lenght/size of my list "hated"
print(len(hated))

print(hated)

#Insert data at any position on the list
print(fav)
fav.insert(1,"Korma")
print(f"The number of favorite dishes is: {len(fav)} ")
fav.insert(3, "Pancakes")
print(f"The number of favorite dishes is: {len(fav)} ")


#Remove item from the list
fav.remove("Casatiello")

print(fav)

#Remove by index (and return)
x = fav.pop(1)

#Delete an item via index (forever and ever)
del fav(2)

print(fav)

#Slicing
print(hated[1:])

for i in range(len(fav)):
  if fav[i] == "Pizza":
    print("Pizza is located in position {i}")

fav.index(f"Pizza is located in position {fav.index('Pizza')")