import numpy as np
import random

class MultiArmedBandit:
    def __init__(self, n_arms, epsilon=0.1):
        self.n_arms = n_arms                # Number of items or arms
        self.epsilon = epsilon              # Exploration rate
        self.counts = np.zeros(n_arms)      # Number of times each arm has been pulled
        self.values = np.zeros(n_arms)      # Estimated value (reward) for each arm

    def select_arm(self):
        # using epsilon-greedy selection
        if random.random() < self.epsilon:
            return random.randint(0, self.n_arms - 1)  # Exploration: random choice
        else:
            return np.argmax(self.values)  # Exploitation: arm with the highest estimated reward

    def update(self, chosen_arm, reward):
        # Incremental update for the selected arm's estimated value
        self.counts[chosen_arm] += 1
        n = self.counts[chosen_arm]
        current_value = self.values[chosen_arm]
        
        # Update the estimated value of the chosen arm
        new_value = current_value + (1 / n) * (reward - current_value)
        self.values[chosen_arm] = new_value

# recommendation system 
def run_bandit(n_arms, n_rounds, true_rewards, epsilon=0.1):
    bandit = MultiArmedBandit(n_arms, epsilon)
    rewards = np.zeros(n_rounds)

    for i in range(n_rounds):
        # Select an arm to "recommend"
        chosen_arm = bandit.select_arm()

        # Simulate reward from reward distribution
        reward = np.random.binomial(1, true_rewards[chosen_arm]) #based on success probability
        bandit.update(chosen_arm, reward)
        rewards[i] = reward

    print("Arm Selection Counts:", bandit.counts)
    print("Estimated Values for each Arm:", bandit.values)
    print("Total Reward:", rewards.sum())
    return rewards, bandit

n_arms = 5                      # nItems to recommend
n_rounds = 1000                 # nRecommendations to simulate
true_rewards = [0.2, 0.5, 0.75, 0.1, 0.6]  # True reward probabilities for each arm

rewards, trained_bandit = run_bandit(n_arms, n_rounds, true_rewards)
