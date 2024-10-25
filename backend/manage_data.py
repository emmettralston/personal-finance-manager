import sqlite3

#function to add a new user
def add_user(name, email, password):
    connection = sqlite3.connect('personal_finance_manager.db')
    cursor = connection.cursor()
    cursor.execute('INSERT INTO users (name, email, password) VALUES(?,?,?)', (name, email, password))
    connection.commit()
    connection.close()

#Function to add transaction
def add_transaction(user_id, amount, category, date, description):
    connection =sqlite3.connect('personal_finance_manager.db')
    cursor = connection.cursor()
    cursor.execute('''INSERT INTO transactions (user_id, amount, category, date, description)
                   VALUES (?,?,?,?,?)''', (user_id, amount,category, date, description))
    connection.commit()
    connection.close()

#function to query all user transactions 
def get_transactions(user_id): 
    connection = sqlite3.connect('personal_finance_manager.db')
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM transactions WHERE user_id = ?', (user_id,))
    transactions = cursor.fetchall()
    connection.close()
    return transactions

#Funstion to add goal
def add_goal(user_id, goal_name, target_amount, saved_amount, deadline):
    connection = sqlite3.connect('personal_finance_manager.db')
    cursor = connection.cursor()
    cursor.execute('''INSERT INTO goals (user_id, goal_name, target_amount, saved_amount, deadline)
                          VALUES (?, ?, ?, ?, ?)''', 
                       (user_id, goal_name, target_amount, saved_amount, deadline))
    connection.commit()
    connection.close()

#Function to query all user goals
def get_goal(goal_id):
    connection = sqlite3.connect('personal_finance_manager.db')
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM goals WHERE goal_id = ?', (goal_id,))
    goal = cursor.fetchone()
    connection.close()
    goal_data = {
            'goal_id': goal[0],
            'user_id': goal[1],
            'goal_name': goal[2],
            'target_amount': goal[3],
            'saved_amount': goal[4],
            'deadline': goal[5]}
    return goal_data
    
#name gaurd
if __name__=='__main__':
    add_user('tester', 'tester@example.com', 'password123')
    user_transactions = get_transactions(1)
    print(user_transactions)
