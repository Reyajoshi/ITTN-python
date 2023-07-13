
def prime_number(number):
    if number==1:
        return False
    if number==2:
        return True
    if number>1:
        for i in range(2,number):
            if number%i==0:
               return False
        else:
            return True
for i in range(1,11,1):
    number=int(input("Enter any number:"))
    if prime_number(number)==True:
        print(f"{number} is prime")
    else:
        print(f"{number} is composite ")





            

    


