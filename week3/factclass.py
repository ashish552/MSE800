class NumberAnalyzer:
    def __init__(self, number):
        self.number = number

    def calculate_factorial(self):
        if self.number < 0:
            return "Factorial is not defined for negative numbers."
        factorial = 1
        for i in range(1, self.number + 1):
            factorial *= i
        return factorial

    def is_prime(self):
        if self.number <= 1:
            return False
        for i in range(2, int(self.number ** 0.5) + 1):
            if self.number % i == 0:
                return False
        return True



def main():
    try:
        user_input = int(input("Enter a number: "))
        analyzer = NumberAnalyzer(user_input)

        
        factorial = analyzer.calculate_factorial()
        print(f"Factorial of {user_input} is: {factorial}")

        
        if analyzer.is_prime():
            print(f"{user_input} is a prime number.")
        else:
            print(f"{user_input} is not a prime number.")

    except ValueError:
        print("Invalid input. Please enter an integer.")



if __name__ == "__main__":
    main()
