import axios from 'axios';

const API_BASE_URL = 'http://127.0.0.1:5000'

//add user
export const addUser = async (userData) => {
    return await axios.post('${API_BASE_URL}/add_user', userData);
};

//add a new transaction
export const addTransaction = async (transactionData) => {
    return await axios.post('${API_BASE_URL}/add_transaction', transactionData);
};

//get transactions
export const getTransactions = async (userId) => {
    return await axios.get('${API_BASE_URL/get_transactions/${userId}');
}

//add a new goal
export const addGoal = async (goalData) => {
    return await axios.post('${API_BASE_URL/add_goal', goalData);
};

//get specific goal
export const getGoal = async (goalId) => {
    return await axios.get('${API_BASE_URL}/get_goal/${goalId}');
}