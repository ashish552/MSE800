class Factorial:
    
    @staticmethod
    def factorial(num):
        result = 1
        for i in range(1, num + 1):
            result *= i
        return result

    @staticmethod
    def check_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    @staticmethod
    def display(num):
        print("Factorial is", Factorial.factorial(num))
        if Factorial.check_prime(num):
            print(f"{num} is a prime number.")
        else:
            print(f"{num} is not a prime number.")


Factorial.display(10)
