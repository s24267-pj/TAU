import pytest
import asyncio
from unittest import mock
from bank_system import Account, Bank, InsufficientFundsError


# Fixture dla konta
@pytest.fixture
def account():
    return Account("123", "Alice", 100.0)


# Fixture dla banku
@pytest.fixture
def bank():
    return Bank()


# Testy dla klasy Account
@pytest.mark.asyncio
async def test_deposit(account):
    await account.deposit(50.0)
    assert account.balance == 150.0


@pytest.mark.asyncio
async def test_withdraw(account):
    await account.withdraw(30.0)
    assert account.balance == 70.0


@pytest.mark.asyncio
async def test_withdraw_insufficient_funds(account):
    with pytest.raises(InsufficientFundsError):
        await account.withdraw(200.0)


# Parametryzacja testu transferu
@pytest.mark.asyncio
@pytest.mark.parametrize(
    "initial_balance, transfer_amount, expected_balance, expected_to_account_balance",
    [
        (100.0, 30.0, 70.0, 80.0),  # Normalny przypadek
        (100.0, 200.0, 100.0, 50.0),  # Zbyt duży transfer
    ]
)
async def test_transfer(account, bank, initial_balance, transfer_amount, expected_balance, expected_to_account_balance):
    account.balance = initial_balance
    to_account = bank.create_account("456", "Bob", 50.0)

    if initial_balance < transfer_amount:
        with pytest.raises(InsufficientFundsError):
            await account.transfer(to_account, transfer_amount)
    else:
        await account.transfer(to_account, transfer_amount)
        assert account.balance == expected_balance
        assert to_account.balance == expected_to_account_balance


# Testy dla klasy Bank
def test_create_account():
    bank = Bank()
    account = bank.create_account("123", "Alice", 100.0)
    assert account.account_number == "123"
    assert account.owner == "Alice"
    assert account.balance == 100.0


def test_get_account():
    bank = Bank()
    account = bank.create_account("123", "Alice", 100.0)
    retrieved_account = bank.get_account("123")
    assert retrieved_account == account


def test_get_account_not_found():
    bank = Bank()
    with pytest.raises(ValueError):
        bank.get_account("123")


# Mockowanie zewnętrznej usługi
@pytest.mark.asyncio
@mock.patch('bank_system.Account.withdraw')
async def test_mock_withdraw(mock_withdraw):
    mock_withdraw.return_value = None
    account = Account("123", "Alice", 100.0)
    await account.withdraw(50.0)
    mock_withdraw.assert_called_with(50.0)


# Testowanie wyjątków
@pytest.mark.parametrize(
    "account_number, expected_exception",
    [
        ("", ValueError),  # Nieprawidłowy numer konta
        (None, ValueError)  # Nieprawidłowy numer konta
    ]
)
def test_invalid_account_number(account_number, expected_exception):
    with pytest.raises(expected_exception):
        Account(account_number, "Alice", 100.0)


# Testy dla symulacji wyścigu o zasoby (race condition)
@pytest.mark.asyncio
async def test_transfer_race_condition(account, bank):
    account.balance = 200.0
    to_account = bank.create_account("456", "Bob", 50.0)

    async def transfer_1():
        await account.transfer(to_account, 60.0)

    async def transfer_2():
        await account.transfer(to_account, 60.0)

    await asyncio.gather(transfer_1(), transfer_2())

    assert account.balance == 80.0
    assert to_account.balance == 170.0


@pytest.mark.asyncio
async def test_transfer_race_condition_multiple(account, bank):
    account.balance = 200.0
    to_account = bank.create_account("456", "Bob", 50.0)

    async def transfer():
        await account.transfer(to_account, 20.0)

    await asyncio.gather(*(transfer() for _ in range(10)))

    assert account.balance == 0.0
    assert to_account.balance == 250.0
