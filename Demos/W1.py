name = input("What is your name? ")
job = input("What is your occupation? ")
salary = float(input("How much do you earn? "))

salary = salary - 0.1*salary

print(type(salary))
print("Welcome!")
print("Nice to meet you {}, Do you like your job as a {}? Whatever is your answer, your salary is reduced. HAHA. It's now{} ".format(name,job) )

#string - A collection of characters


# integer - whole number
# float - any number (can contain decimal)
# boolean - true or false
# char - single characters
