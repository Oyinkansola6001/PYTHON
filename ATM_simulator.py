account_balance = 10_000       # balance of the account.

print("Welcome dear customer!")    # greeting message.

while True:
    print("1. Check balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")
    option = int(input("Choose an option: "))      # user chooses an option.
    if option == 1:           
        print("Account balance: " + "#" + str(account_balance))    
    elif option == 2:
        deposit = int(input("Enter amount to deposit: "))
        account_balance += deposit
        print("Deposit successful. New balance is: " + str(account_balance))
    elif option == 3:
        withdraw = int(input("Enter amount to withdraw: "))
        if withdraw > account_balance:
            print("Insufficient funds.")
        withdraw = int(input("Enter amount to withdraw: "))
        account_balance -= withdraw
        print("Withdrawal successful. New balance is: " + str(account_balance))
    else:
        option == 4
        print("Thank you for banking with us.")

    break

