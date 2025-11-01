def is_prime(n):
    # Numbers less than or equal to 1 are not prime by definition. For example, 0, 1, and negative numbers are not prime. The function returns False in this case.
    if n <= 1:
        return False
    # 2 is the smallest and only even prime number. The function returns True in this case.
    if n == 2:
        return True
    # If the number is even and greater than 2, it cannot be prime because it is divisible by 2. The function returns False in this case.
    if n % 2 == 0:
        return False

    # This loop checks if n has any divisors other than 1 and itself. If it does, n is not a prime number, and the function returns False.
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
# range(3, int(n**0.5) + 1, 2): Start: 3 (the loop starts from 3 because we've already handled the case for n == 2 and even numbers). Stop: int(n**0.5) + 1 (the loop runs up to the square root of n). This is because if n has a divisor greater than its square root, it must also have a corresponding divisor smaller than its square root. Checking up to the square root is sufficient. Step: 2 (the loop skips even numbers since we've already checked for divisibility by 2). if n % i == 0:: This checks if n is divisible by the current value of i (i.e., if i is a divisor of n). If n % i == 0, it means n has a divisor other than 1 and itself, so it's not prime, and the function returns False.

    return True

# Getting user input
try:
    user_number = int(input("Enter a number to check if it's prime: "))
    if is_prime(user_number):
        print(f"{user_number} is a prime number.")
    else:
        print(f"{user_number} is not a prime number.")
except ValueError:
    print("Invalid input. Please enter a valid integer.")
