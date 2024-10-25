import requests
import unittest


BASE_URL = 'http://127.0.0.1:5000'

class TestFlaskAPI(unittest.TestCase):

    
    def test_add_user(self):
        # Data to add a new user
        user_data = {
            'name': 'John Doe',
            'email': 'john.doe@example.com',
            'password': 'password'
        }
        response = requests.post(f'{BASE_URL}/add_user', json=user_data)
        self.assertEqual(response.status_code, 200)
        self.assertIn('User added successfully.', response.json().get('message', ''))
    
    def test_add_transaction(self):
        transaction_data = {
            'user_id': 1,  
            'amount': 100.0,
            'category': 'Groceries',
            'date': '2024-10-15',
            'description': 'Shopping'
        }
        response = requests.post(f'{BASE_URL}/add_transaction', json=transaction_data)
        self.assertEqual(response.status_code, 200)
        self.assertIn('Transaction added successfully.', response.json().get('message', ''))

    def test_get_transactions(self):
        response = requests.get(f'{BASE_URL}/get_transactions/1')
        self.assertEqual(response.status_code, 200)
        transactions = response.json().get('transactions', [])
        self.assertIsInstance(transactions, list) 

    def test_add_goal(self):
        goal_data = {
            'user_id': 1,
            'goal_name': 'Vacation',
            'target_amount': 2000.0,
            'saved_amount': 150.0,
            'deadline': '2025-01-01'
        }
        response = requests.post(f'{BASE_URL}/add_goal', json=goal_data)
        self.assertEqual(response.status_code, 200)
        self.assertIn('Goal added successfully.', response.json().get('message', ''))

    def test_get_goal(self):
        response = requests.get(f'{BASE_URL}/get_goal/1') 
        if response.status_code == 200:
            goal = response.json().get('goal', {})
            self.assertIsInstance(goal, dict) 
        else:
            self.assertEqual(response.status_code, 404) 

if __name__ == '__main__':
    unittest.main()
