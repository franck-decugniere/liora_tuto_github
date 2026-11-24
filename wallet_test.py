from wallet import Wallet, InsufficientAmount
import pytest

@pytest.fixture
def empty_wallet():
    '''Returns a Wallet instance with a zero balance'''
    return Wallet()

@pytest.fixture
def wallet():
    '''Returns a Wallet instance with a balance of 20'''
    return Wallet(20)


def test_wallet_initialization():
    wallet = Wallet()
    assert wallet.balance == 0

    wallet_with_balance = Wallet(balance=100)
    assert wallet_with_balance.balance == 100


def test_wallet_add_cash(empty_wallet):
    empty_wallet.add_cash(50)
    assert empty_wallet.balance == 50


def test_wallet_spend_cash(wallet):
    wallet.spend_cash(10)
    assert wallet.balance == 10


def test_wallet_spend_cash_insufficient_funds(wallet):
    with pytest.raises(InsufficientAmount):
        wallet.spend_cash(150)

