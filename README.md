## Implementation of DP approach and Q-learning
### DP Approach:
- Converged after 88 iterations
- Time taken: 11.82 seconds
  ![image](https://github.com/user-attachments/assets/78be301e-b0f7-4a6d-b58e-636f8d8d3c07)

### Q-Learning:
- Ran for 1000 episodes
- Time taken: 46.59 seconds
- ![image](https://github.com/user-attachments/assets/18a594ba-d72f-4be5-8732-3a2f8cc1818a)


## Recommendation System using Multi Armed Bandit algorithm
### Assumptions made:
-  After each recommendation (choosing an arm), a binary feedback — a reward of 1 for a positive outcome (e.g., user engagement), 0 otherwise is recieved.
-  Each arm is independent of others, and choosing an arm doesnot impact the success probability of other arms
-  A stationary reward function is considered
-  The epsilon greedy strategy is used where a small probability ε allows for exploration, while the majority of the time the agent exploits the arm with the highest expected reward.
-  With probability ε, exploration is done by choosing a random arm. With probability 1 - ε, exploitation is done by choosing the arm with the highest observed average reward.

### Result:
Arm Selection Counts: [ 39.  25. 790.  21. 125.]
Estimated Values for each Arm: [0.20512821 0.32       0.73037975 0.         0.56      ]
Total Reward: 663.0

#### Learning curve:
![image](https://github.com/user-attachments/assets/22dff784-4d41-405b-ae00-053133c28ba4)

