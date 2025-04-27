class Factorial:
    def __init__(self, number):
        self.number = number
    def factorial(self):
        y = 1
        fact = 1
        while y <= self.number:
            fact = fact * y
            y = y+1
        return fact
        
z = int(input("Enter a number: "))
calculate = Factorial(z)
print(f"The factorial is: {calculate.factorial()}")


