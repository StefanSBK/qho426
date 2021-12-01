# Program wich creates a menu, where user can either get a nice message, calculate an area of rectangle/triangle or print out a times table for number
while True:
 print("Please choose one of the following options:\n\n1-Nice message\n2-Area of a rectangle\n3-Area of a triangle\n4-Times table\n0-Exit")

 opt = int(input())

 if opt == 1:
    print("You do not smell so bad today!")
 elif opt == 2:
    w = float(input("Enter the width of the rectangle: "))
    l = float(input("Enter the lenght of the rectangle "))
    area = w*1
    print("The area is {}".format(area))
 elif opt == 3:
    l = float(input("Enter the lenght of the triangle "))
    h = float(input("Enter the height of the triangle "))
    area = h*l/2
    print("The area is {}".format(area))
 elif opt == 4:
    n = int(input("Enter a whole number: "))
    for i in range(1, 11):
      print(f"{i}x{n} = {i*n}")
    print("This is it")
 elif opt == o:
    break
 else:
    print("Whooopsie - no such option available")