for i in range(1,11,1):
    def calc(operation,num_one,num_second):
        f_n=num_one
        s_n=num_second
        if operation == "+":
            print(f_n + s_n)
        elif operation == "-":
            print(f_n - s_n)
        elif operation == "/":
            print(f_n / s_n)
        elif operation == "*":
            print(f_n * s_n) 
    operator=input("Enter any operator(+,-,/,*):")
    first_value=int(input("Enter a first number:"))
    second_value=int(input("Enter a second number:"))

    calc(operator,first_value,second_value)
                    
    

        

