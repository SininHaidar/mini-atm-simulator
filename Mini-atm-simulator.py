Balance = 1000
print("Your Balance is 1000"+"\n"+"1. Check Balance"+"\n"+"2. Deposit Money"+"\n"+"3. Withdraw Money"+"\n"+"4. Exist")

pick_number = int(input("Choose an option:"))
while pick_number != 4:
    
    if pick_number == 1:
        print("Your Balance is ", Balance)
    elif pick_number == 2:
        Deposit_amount = int(input("Enter amount to deposit:"))
        Balance = Balance + Deposit_amount
        print("Deposit successful. New Balance:", Balance)
    else:
        if pick_number == 3:
            withdraw_amount = int(input("Enter amount to Withdraw:"))
            Balance = Balance - withdraw_amount
            print("Withdrawal successful. New Balance:", Balance)
    pick_number = int(input("Choose an option:"))
    
print("Goodbye!")
                    







