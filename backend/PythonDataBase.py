import sqlite3

def setup_database():
    #Connect to SQlite data base
    connection = sqlite3.connect('personal_finance_manager.db')
    cursor = connection.cursor()

    #Create users table
    cursor.execute('''CREATE TABLE IF NOT EXISTS users(
                user_id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email TEXT NOT NULL UNIQUE,
                password TEXT NOT NULL
    )''')

    #Create transactions table
    cursor.execute('''CREATE TABLE IF NOT EXISTS transactions(
                transaction_id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER,
                amount REAL NOT NULL,
                category TEXT NOT NULL,
                date DATE NOT NULL,
                description TEXT,
                FOREIGN KEY (user_id) REFERENCES users(user_id)           
    )''')

    #Create goals table
    cursor.execute('''CREATE TABLE IF NOT EXISTS goals(
                goal_id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER,
                goal_name TEXT NOT NULL,
                target_amount REAL NOT NULL,
                saved_amount REAL DEFAULT 0,
                deadline DATE,
                FOREIGN KEY (user_id) REFERENCES users(user_id)           
    )''')

    connection.commit()
    connection.close()
    print("Data bases and tables complete.")

if __name__ == '__main__':
    setup_database()

