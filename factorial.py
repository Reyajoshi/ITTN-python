def factorial(n):
    if n==1:
        return 1
    elif n<0:
        print("Please enter non-negative integer!") 
    else:
        return n * factorial(n-1)
for i in range(1,11,1):
    number=int(input("Enter any positive integer:"))
    result=factorial(number)
    print(f"The factorial of {number} is {result}")
    