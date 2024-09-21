def power(x, y):
    result = 1  
    while y > 0:
        
        if y & 1:
            result *= x
       
        y >>= 1
       
        x *= x
    return result

x = int(input("Enter the number you want to exponent: "))
y = int(input("Enter the exponential number: "))
result = power(x, y)
print(f"{x} ** {y} = {result}")
