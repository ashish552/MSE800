def factorial(x):
  y = 1
  fact = 1 
  while y <= x:
   
    fact =  fact * y
    y = y +1

  return fact
z = int(input("Enter a number "))   
print(f"factorial is {factorial(z)}")  



