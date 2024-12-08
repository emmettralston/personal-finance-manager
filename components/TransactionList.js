import React, { useState, useEffect } from 'react';
import { getTransactions } from '../api/api'; 

const TransactionList = ({ userId }) => {
    const [transactions, setTransactions] = useState([]);
    useEffect(() => {
        const fetchTransactions = async () => {
            try {
                const response = await getTransactions(userId);
                setTransactions(response.data);
            }
            catch (error) {
                console.error('Error fetching transactions:', error);
            }
        };
        fetchTransactions();
    }, [userId]);

    return (
        <div>
            <h2>Transactions List</h2>
            <ul>
                {transactions.map((transaction, index) => (
                    <li key={index}>
                        {transaction.date}: {transaction.description} - ${transaction.amount}
                    </li>
                ))}
            </ul>
        </div>
    );
};

export default TransactionList;