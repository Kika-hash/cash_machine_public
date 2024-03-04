
from db_operations import db_connection, fetching_pin, fetching_card_balance, updating_card_balance


def deposit_money(amount, card_balance):
    """Deposit given amount of money to the account."""
    card_balance += amount
    # save new balance to the database
    return card_balance


def withdraw_money(amount, card_balance):
    """Withdraw given amount of money from the account."""
    card_balance -= amount
    # save new balance to the database
    return card_balance


def log_transaction(action, money, card_balance):
    if action in ('DEPOSIT', 'WITHDRAW'):
        print(action + ": $", money)
    print("Current balance:", card_balance)


def move_money(action, money, card_balance):
    if action == 'DEPOSIT':
        return deposit_money(money, card_balance)
    elif action == 'WITHDRAW':
        return withdraw_money(money, card_balance)
    elif action == 'DISPLAY':
        return card_balance


def get_amount_of_money(action):
    if action == 'DISPLAY':
        return 0.0
    money = input("Enter the sum to " + action + ": ")
    return float(money)


def make_transaction(action, card_balance):
    money = get_amount_of_money(action)
    card_balance = move_money(action, money, card_balance)
    log_transaction(action, money, card_balance)
    new_card_balance = card_balance
    return new_card_balance


def action_mapper(action):
    action_dictionary = {
        1: "DISPLAY",
        2: "WITHDRAW",
        3: "DEPOSIT"
    }
    mapped_action = action_dictionary.get(action)
    return mapped_action



while True:
    cursor_object = db_connection()
    card_number = int(input("Enter card number: "))
    input_pin = int(input("Enter PIN: "))
    fetching_pin(card_number, cursor_object)
    verification_result = input_pin == fetching_pin(card_number, cursor_object)
    if verification_result is True:
        action = int(input("Enter desired action number: 1 - Display || 2 - Withdraw || 3 - Deposit\n"))
        if action in range(1, 4, 1):
            card_balance = fetching_card_balance(card_number, cursor_object)
            new_card_balance = make_transaction(action_mapper(action), card_balance)
            updating_card_balance(action_mapper(action), card_number, new_card_balance, cursor_object)
        else:
            print("Wrong choice - you are going to be killed in 3, 2, 1, ...")
    else:
        print("Incorrect pin!")