age = int(input("Enter your age: "))
ch = int(input("Enter the number of children you have: "))

if age < 25 and ch > 0:
  print("You are a young parent!")
  print(f"Next year you will be {age+1} though")
elif age > 55 and ch > 0:
  print("Good to know you have {} children".format(ch))
elif age < 18 or ch == 0:
  print("You have plenty of time for a child")
else:
  print("You are not so young!")
  print("We are all going to live long anyway!")