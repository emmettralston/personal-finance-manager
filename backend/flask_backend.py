from flask import Flask, request, jsonify
import sqlite3
import manage_data

app = Flask(__name__)

#Route to add a new user
@app.route('/add_user', methods=['POST'])
def add_user():
    data = request.json
    name = data['name']
    email = data['email']
    password = data['password']

    manage_data.add_user(name, email, password)

    return jsonify({'message': 'User added successfully.'})

@app.route('/add_transaction', methods=['POST'])
def add_transaction():
    data =request.json
    user_id = data['user_id']
    amount = data['amount']
    category = data['category']
    date = data['date']
    description = data['description']
    
    manage_data.add_transaction(user_id, amount, category, date, description)
    return jsonify({'message': 'Transaction added successfully.'})

@app.route('/get_transactions/<int:user_id>', methods=['GET'])
def get_transactions(user_id):
    transactions = manage_data.get_transactions(user_id)
    formatted_transactions = [
        {
            'transaction_id': t[0],
            'user_id': t[1],
            'amount': t[2],
            'category': t[3],
            'date': t[4],
            'description': t[5]
        }
        for t in transactions
    ]

    return jsonify({'transactions': formatted_transactions})

@app.route('/add_goal', methods=['POST'])
def add_goal():
    data =request.json
    user_id = data['user_id']
    goal_name = data['goal_name']
    target_amount = data['target_amount']
    saved_amount = data['saved_amount']
    deadline = data['deadline']
    manage_data.add_goal(user_id, goal_name, target_amount, saved_amount, deadline)

    return jsonify({'message': 'Goal added successfully.'})

@app.route('/get_goal/<int:goal_id>', methods=['GET'])
def get_goal(goal_id):
    goal_data = manage_data.get_goal(goal_id)

    if goal_data:
        return jsonify({'goal': goal_data})
    else:
        return jsonify({'message': 'Goal not found'})


if __name__ == '__main__':
    app.run(debug=True)
