def is_power_of_four(n):
    return n > 0 and (n & (n - 1)) == 0 and (n - 1) % 3 == 0

# Example usage
number = int(input("Enter a number: "))
if is_power_of_four(number):
    print(f"{number} is a power of 4.")
else:
    print(f"{number} is not a power of 4.")
