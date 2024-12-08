import React, { useState, useEffect } from 'react';
import { getGoal } from '../api/api'

const GoalDisplay = ({ goalId }) => {
    const [goal, setGoal] = useState(null);

    useEffect(() => {
        const fetchGoal = async () => {
            try {
                const response = await getGoal(goalId);
                setGoal(response.data);
            }
            catch (error) {
                console.error('Error fetching goal:', error);
            }
        };
        fetchGoal();
    }, [goalId]);
    
    if (!goal) {
        return < div > Loading...</div >;
    }

    return (
        <div>
            <h2>Goal Details</h2>
            <p><strong>Name:</strong> {goal.goal_name}</p>
            <p><strong>Target Amount:</strong> {goal.target_amount}</p>
            <p><strong>Saved Amount::</strong> {goal.saved_amount}</p>
            <p><strong>Deadline:</strong> {goal.deadline}</p>
        </div>
    );
};

export default GoalDisplay;
