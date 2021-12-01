#Code to find out two large prime numbers, wich can be used in RSA encryption. It is made of 3 functions. First one will be used to establish if number is prime, second function will find a prime number inside of a given range and last function will output the product of the two primes"

def isPrime(n):
  for thing in range(2, n):
    if n % thing == 0:
      return False
  return True

def findPrime(s, e):
  for i in range(s,e):
    if isPrime(i):
      return i
    

def encrypt():
  x = int(input("Provide a starting point: "))
  y = int(input("Provide an end point: "))
  p1 = findPrime(x,y)
  x = int(input("Provide a starting point: "))
  y = int(input("Provide an end point: "))
  p2 = findPrime(x,y)
  return p1*p2


print(encrypt())