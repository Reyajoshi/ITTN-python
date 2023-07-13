d={"clock":5000,"tv":10000,"laptop":20000,"mobile":13000,"fridge":50000}
for key,value in d.items():
    print(key,value)
bill_amount=0
while True:
    key=input("Enter a product name:")
    if key=="done":
        break
    bill_amount+=d[key] 

if bill_amount>10000:
    bill_amount_final= bill_amount-(bill_amount*(10/100))
    print("The actual price is:",bill_amount)
    print("The total amount of your product is:",bill_amount_final)
elif bill_amount<=10000:
    print("The total amount of your product is:",bill_amount)
print("The program has ended")








    


    
