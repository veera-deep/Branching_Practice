# ============================================
#        BANK MANAGEMENT SYSTEM
# ============================================

import sys
import datetime


class BankAccount:

    def __init__(self, name, account_number, balance=0):
        self.name = name
        self.account_number = account_number
        self.balance = balance
        self.transactions = []

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.transactions.append(
                f"{datetime.datetime.now()} - Deposited: {amount}"
            )
            print(f"✅ Successfully deposited {amount}")
        else:
            print("❌ Invalid deposit amount")

    def withdraw(self, amount):
        if amount <= 0:
            print("❌ Invalid withdrawal amount")
        elif amount > self.balance:
            print("❌ Insufficient balance")
        else:
            self.balance -= amount
            self.transactions.append(
                f"{datetime.datetime.now()} - Withdrawn: {amount}"
            )
            print(f"✅ Successfully withdrawn {amount}")

    def check_balance(self):
        print(f"💰 Current Balance: {self.balance}")

    def show_transactions(self):
        if not self.transactions:
            print("No transactions yet.")
        else:
            print("\n------ Transaction History ------")
            for t in self.transactions:
                print(t)
            print("----------------------------------")


class Bank:

    def __init__(self):
        self.accounts = {}

    def create_account(self):
        name = input("Enter Account Holder Name and details: ")
        acc_number = input("Enter Account Number: ")

        if acc_number in self.accounts:
            print("❌ Account already exists!")
            return

        account = BankAccount(name, acc_number)
        self.accounts[acc_number] = account
        print("✅ Account created successfully!")

    def get_account(self):
        acc_number = input("Enter Account Number: ")
        if acc_number in self.accounts:
            return self.accounts[acc_number]
        else:
            print("❌ Account not found")
            return None

    def deposit_money(self):
        account = self.get_account()
        if account:
            amount = float(input("Enter amount to deposit: "))
            account.deposit(amount)

    def withdraw_money(self):
        account = self.get_account()
        if account:
            amount = float(input("Enter amount to withdraw: "))
            account.withdraw(amount)

    def check_account_balance(self):
        account = self.get_account()
        if account:
            account.check_balance()

    def show_account_transactions(self):
        account = self.get_account()
        if account:
            account.show_transactions()


def main_menu():
    print("\n========== BANK MENU ==========")
    print("1. Create Account")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Check Balance")
    print("5. Transaction History")
    print("6. Exit")
    print("================================")


def main():
    bank = Bank()

    while True:
        main_menu()
        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            bank.create_account()

        elif choice == "2":
            bank.deposit_money()

        elif choice == "3":
            bank.withdraw_money()

        elif choice == "4":
            bank.check_account_balance()

        elif choice == "5":
            bank.show_account_transactions()

        elif choice == "6":
            print("Thank you for using Bank System!")
            sys.exit()

        else:
            print("❌ Invalid choice. Try again.")


if __name__ == "__main__":
    main()
