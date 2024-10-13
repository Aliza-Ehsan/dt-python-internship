# Class definitions

class Customer:
    def _init_(self, name, address, phone_number, email):
        self.name = name
        self.address = address
        self.phone_number = phone_number
        self.email = email

    def display_details(self):
        print(f"Customer Name: {self.name}")
        print(f"Address: {self.address}")
        print(f"Phone Number: {self.phone_number}")
        print(f"Email: {self.email}")


class Account:
    def _init_(self, account_number, account_type, balance, customer):
        self.account_number = account_number
        self.account_type = account_type
        self.balance = balance
        self.customer = customer

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposit successful. New balance: {self.balance}")
        else:
            print("Invalid deposit amount. It must be positive.")

    def withdraw(self, amount):
        if amount > 0:
            if self.balance >= amount:
                self.balance -= amount
                print(f"Withdrawal successful. New balance: {self.balance}")
            else:
                print("Insufficient funds for withdrawal.")
        else:
            print("Invalid withdrawal amount. It must be positive.")

    def display_account_info(self):
        print(f"Account Number: {self.account_number}")
        print(f"Account Type: {self.account_type}")
        print(f"Balance: {self.balance}")
        self.customer.display_details()


class SavingsAccount(Account):
    def _init_(self, account_number, balance, customer):
        super()._init_(account_number, "Savings", balance, customer)

    def display_account_info(self):
        print("Savings Account Information:")
        super().display_account_info()


class Bank:
    def _init_(self, name):
        self.name = name
        self.branches = []
        self.customers = []
        self.accounts = []

    def add_branch(self, branch_name):
        self.branches.append(branch_name)

    def add_customer(self, customer):
        if isinstance(customer, Customer):
            self.customers.append(customer)
        else:
            print("Invalid customer. Please provide a valid Customer instance.")

    def add_account(self, account):
        if isinstance(account, Account):
            self.accounts.append(account)
        else:
            print("Invalid account. Please provide a valid Account instance.")

    def display_customers(self):
        if self.customers:
            print(f"Customers of {self.name}:")
            for customer in self.customers:
                customer.display_details()
                print("-" * 30)
        else:
            print("No customers to display.")

    def display_accounts(self):
        if self.accounts:
            print(f"Accounts of {self.name}:")
            for account in self.accounts:
                account.display_account_info()
                print("-" * 30)
        else:
            print("No accounts to display.")


# Demonstrating usage of the Bank Management System

# Create a bank
my_bank = Bank("National Bank of Pakistan")

# Add branches
my_bank.add_branch("Karachi")
my_bank.add_branch("Malir")

# Create customers
customer1 = Customer("Muhammad Bilal", "50-A korangi St", "555-1234", "mbilal@346.com")
customer2 = Customer("Aliza Ehsan", "N-45 Malir St", "555-5678", "aliza@678.com")

# Add customers to the bank
my_bank.add_customer(customer1)
my_bank.add_customer(customer2)

# Create accounts for customers
savings_account1 = SavingsAccount("SA123456", 1000, customer1)
savings_account2 = SavingsAccount("SA654321", 2000, customer2)

# Add accounts to the bank
my_bank.add_account(savings_account1)
my_bank.add_account(savings_account2)

# Display bank customers
my_bank.display_customers()

# Display bank accounts
my_bank.display_accounts()

# Perform deposit and withdrawal
savings_account1.deposit(500)
savings_account1.withdraw(300)
savings_account2.withdraw(2500)  # This will trigger insufficient funds error

# Display account info after transactions
my_bank.display_accounts()