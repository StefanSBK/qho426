#Initialise empty set
s = set()

#Check the type is set
print(type(s))

#Initialise non-empty set
colours = {"blue", "red", "purle", "green"}

print(colours)

#Adding elements to a set
colours.add("black")
colours.add("turquoise")
print(colours)

#Delete an element of a set
colours.remove("blue")

#Check membership
if "blue" not in colours:
  print("Yay - my favorite colour is here!")
else:
  print("You are missing an important colour")

colors = {"yellow", "black", "red", "cyan"}

#Take union of two sets - join them toghether, but do not keep duplicates
print(colours.union(colors))

#Take intersection of two sets - the "common" elements
print(colours.intersection(colors))

#Take set difference - so only keep elements NOT in another collection
print(colours.difference(colors))