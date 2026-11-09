import time
import os

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def show_balance(balance):
    print(f"Your current balance is ${balance:.2f}")

def deposit():
    try:
        amount = float(input("Please enter an amount to deposit: "))
        if amount <= 0:
            print("Amount must be greater than $0.")
            return 0
        print("-----------------------------------------------------")
        print(f"Your account has been credited with ${amount:.2f}")
        print("-----------------------------------------------------")
        return amount
    except ValueError:
        print("Invalid entry! Please enter a valid number.")
        return 0

def withdraw(balance):
    try:
        amount = float(input("How much would you like to withdraw: "))
        if amount <= 0:
            print("Withdrawal amount must be greater than $0.")
            return 0
        if amount > balance:
            print(f"Insufficient funds. Your current balance is ${balance:.2f}")
            return 0
        print("-----------------------------------------------------")
        print(f"You have withdrawn ${amount:.2f}")
        print("-----------------------------------------------------")
        return amount
    except ValueError:
        print("Invalid entry! Please enter a valid number.")
        return 0

def main():
    balance = 0.0
    running = True

    print("Welcome to the bank!")
    print("---------------------")
    time.sleep(1)
    clear_screen()

    while running:
        print("\nWould you like to:")
        print("  (1) Check your balance")
        print("  (2) Deposit money")
        print("  (3) Withdraw cash")
        print("  (4) Exit")

        choice = input("Select an option (1-4): ").strip()

        if choice == "1":
            show_balance(balance)
        elif choice == "2":
            balance += deposit()
        elif choice == "3":
            balance -= withdraw(balance)
        elif choice == "4":
            print("Thank you for banking with us. Goodbye!")
            print("----------------")
            running = False
        else:
            print("Choice not valid. Please select a number between 1 and 4.")

if __name__ == "__main__":
    main()
