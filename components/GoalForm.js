import React, { use, useState } from "react";
import { addGoal } from "../api/api";

const GoalForm = () => {
    const [goalName, setGoalName] = useState('');
    const [targetAmount, setTargetAmount] = useState('');
    const [savedAmount, setSavedAmount] = useState('');
    const [deadline, setDeadline] = useState('');
    const userId = 1 // need to replace with dynamic userId

    const handleSubmit = async (e) => {
        e.preventDefault();
        try {
            const response = await addGoal({
                user_id: userId,
                goal_name: goalName,
                target_amount: targetAmount,
                saved_amount: savedAmount,
                deadline: deadline,
                
            });
        }
        catch (error) {
            console.error('Error adding goal:', error);
        }
    };

    return (
        <form onSubmit={handleSubmit}>
            <h2>Add Goal</h2>
            <input
                type="text"
                placeholder="Goal Name"
                value={goalName}
                onChange={(e) => setGoalName(e.target.value)}
            />
            <input
                type="number"
                placeholder="Target Amount"
                value={targetAmount}
                onChange={(e) => setTargetAmount(e.target.value)}
            />
            <input
                type="number"
                placeholder="Saved Amount"
                value={savedAmount}
                onChange={(e) => setSavedAmount(e.target.value)}
            />
            <input
                type='date'
                value={deadline}
                onChange={(e) => setDeadline(e.target.value)}
            />
        </form>
    );
};

export default GoalForm;
 
