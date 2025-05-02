def factorial(z):
  y = 1
  fact = 1 
  while y <= z:
   
    fact =  fact * y
    y = y +1

  return fact
z = int(input("Enter a number "))   
print(f"factorial is {factorial(z)}")  



