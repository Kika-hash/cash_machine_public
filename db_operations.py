import psycopg2
from configs import db_configs
import random
import time


def db_connection():
    # Establish the connection to PostgreSQL
    db_conn = psycopg2.connect(db_configs)

    #create a cursor object from connection module
    cursor_object = db_conn.cursor()
    return cursor_object


def fetching_pin(card_id, cursor_object):
    cursor_object.execute("SELECT card_pin FROM card_data WHERE card_id={}".format(card_id))
    result = cursor_object.fetchall()
    if len(result) >= 1:
        card_pin = result[0][0]
        return card_pin
    else:
        return "Wrong card ID"


def fetching_card_balance(card_id, cursor_object):
    cursor_object.execute("SELECT card_balance FROM card_data WHERE card_id={}".format(card_id))
    result = cursor_object.fetchall()
    card_balance = result[0][0]
    return card_balance


def updating_card_balance(action, card_id, new_card_balance, cursor_object):
    if action in ('DEPOSIT', 'WITHDRAW'):
        try:
            # Use parameterized query to avoid SQL injection
            cursor_object.execute("UPDATE card_data SET card_balance = %s WHERE card_id = %s", (new_card_balance, card_id))
            # Commit the transaction to save the changes
            cursor_object.connection.commit()
            cursor_object.close()
            return True
        except psycopg2.Error as e:
            print("Error:", e)
            return False
    elif action == 'DISPLAY':
        return False
