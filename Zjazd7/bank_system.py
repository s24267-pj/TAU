import asyncio


class InsufficientFundsError(Exception):
    pass


class Account:
    def __init__(self, account_number: str, owner: str, balance: float):
        if not account_number:
            raise ValueError("Account number cannot be empty or None.")
        self.account_number = account_number
        self.owner = owner
        self.balance = balance
        self.lock = asyncio.Lock()

    async def deposit(self, amount: float):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self.balance += amount

    async def withdraw(self, amount: float):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        if self.balance < amount:
            raise InsufficientFundsError("Insufficient funds for this transaction.")
        self.balance -= amount

    async def transfer(self, to_account: "Account", amount: float):
        async with self.lock:
            await self.withdraw(amount)
            await to_account.deposit(amount)


class Bank:
    def __init__(self):
        self.accounts = {}

    def create_account(self, account_number: str, owner: str, initial_balance: float = 0.0):
        if account_number in self.accounts:
            raise ValueError("Account already exists.")
        account = Account(account_number, owner, initial_balance)
        self.accounts[account_number] = account
        return account

    def get_account(self, account_number: str) -> Account:
        if account_number not in self.accounts:
            raise ValueError("Account not found.")
        return self.accounts[account_number]

    async def process_transaction(self, transaction_func):
        await asyncio.sleep(1)
        return await transaction_func
