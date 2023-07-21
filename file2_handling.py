
for i in range(1,11,1):
    print('Welcome to pizza shop!')
    pizza_shop=open("reya_files/new_file.txt","a+")
    customer_name=input("Please enter your name:")
    pizza_shop.write(f"\nCustomer name:{customer_name}\n")
    date=input("Enter date and time of your order:")
    pizza_shop.write(f"Purchase date and time:{date}\n")
    print("Pizza:")
    pizza={"basic":350,"vegetarian":400,"hawaiian":425,"nepali fireball":400}
    for key,value in pizza.items():
        print(key,value)
    print("Toppings:")
    toppings={"onion":30,"tomato":30,"chicken":70,"bacon":80,"black olive":50}
    for key,value in toppings.items():
        print(key,value)
    bill=0
    customer=input("Enter any pizza you would like to have :")
    bill+=pizza[customer]
    while True:
        key=input("Enter any toppings:")
        if key=="done":
            break
        bill+=toppings[key]
    pizza_shop.write(f"{customer_name} bill is {bill}\n")
    pizza_shop.close()












    



