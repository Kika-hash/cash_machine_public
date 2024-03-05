Cash Machine
============
## Description
Simple soft for cash machine with standard features:
* enter card number and PIN
* PIN verification
* display the current balance
* withdraw money
* deposit money

App is writen in Python (3.11) and integrated with PostreSQL DataBase

## Installation

```bash
pip install psycopg2
```

- To configure DataBase, use below command in SQL Shell (psql)

```doctest
CREATE TABLE card_data (
id SERIAL PRIMARY KEY,
name varchar(255),
surname varchar(255),
card_id int,
card_pin int,
card_balance real);

\dt+ = show list of tables

```

- Create first client:

```doctest
INSERT INTO card_data (name, surname, card_id, card_pin, card_balance) VALUES ('John', 'Doe', 9876, 1234, 2000);")
```

- You can also create fake data by running below function

```python
def configure_fake_data():
    n = 0
    cursor_object = db_connection()
    while n < 500:
        card_id = random.randint(1000, 9999)
        card_pin = random.randint(1000, 9999)
        card_balance = random.randint(1, 999999)
        cursor_object.execute("INSERT INTO card_data (card_id, card_pin, card_balance) VALUES ({}, {}, {});".format(card_id, card_pin, card_balance))
        cursor_object.connection.commit()
        n += 1
        time.sleep(0.5)
        print(card_id, card_pin, card_balance)
    print("Configuring fake data - finished")
```

- You can manage your DataBase by using the pgAdmin app f.e.

# Usage

# FAQ

# Support

# Contributing
- Source Code: [Github](https://github.com/Kika-hash/cash_machine_public)

# Contact information

# License

# Acknowledgment