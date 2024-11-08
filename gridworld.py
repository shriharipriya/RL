import time
import numpy as np
import random
from collections import defaultdict

GRID_SIZE = 100
OBSTACLE_PROB = 0.2

# Initializing grid with obstacles
def create_grid():
    grid = np.zeros((GRID_SIZE, GRID_SIZE))
    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE):
            if random.random() < OBSTACLE_PROB:
                grid[i][j] = -1  # Obstacle
    return grid

#Setting random start and end points in the grid
def set_random_points(grid):
    start = (random.randint(0, GRID_SIZE-1), random.randint(0, GRID_SIZE-1))
    goal = (random.randint(0, GRID_SIZE-1), random.randint(0, GRID_SIZE-1))
    while grid[start] == -1 or grid[goal] == -1 or start == goal:
        start = (random.randint(0, GRID_SIZE-1), random.randint(0, GRID_SIZE-1))
        goal = (random.randint(0, GRID_SIZE-1), random.randint(0, GRID_SIZE-1))
    return start, goal

# Grid env definition
class GridWorld:
    def __init__(self, grid, start, goal):
        self.grid = grid
        self.start = start
        self.goal = goal
        self.actions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # up, down, left, right

    def is_terminal(self, state):
        return state == self.goal

    def get_next_state(self, state, action):
        if self.is_terminal(state):
            return state
        x, y = state
        dx, dy = action
        new_state = (x + dx, y + dy)
        if 0 <= new_state[0] < GRID_SIZE and 0 <= new_state[1] < GRID_SIZE and self.grid[new_state] != -1:
            return new_state
        return state  # if out of bounds or obstacle, stay in the same state

    def get_reward(self, state):
        return 1 if state == self.goal else -0.01  # reward for reaching goal, small penalty otherwise

def value_iteration(env, discount=0.9, theta=1e-4):
    V = np.zeros((GRID_SIZE, GRID_SIZE))  # value table
    policy = defaultdict(lambda: random.choice(env.actions))

    start_time = time.time()
    iterations = 0

    while True:
        delta = 0
        for x in range(GRID_SIZE):
            for y in range(GRID_SIZE):
                state = (x, y)
                if env.is_terminal(state) or env.grid[state] == -1:
                    continue

                old_value = V[state]
                best_value = float('-inf')
                best_action = None

                for action in env.actions:
                    next_state = env.get_next_state(state, action)
                    reward = env.get_reward(next_state)
                    value = reward + discount * V[next_state]
                    if value > best_value:
                        best_value = value
                        best_action = action

                V[state] = best_value
                policy[state] = best_action
                delta = max(delta, abs(old_value - V[state]))

        iterations += 1
        # Check for convergence
        if delta < theta:
            break

    end_time = time.time()
    print(f"Value Iteration converged in {iterations} iterations, taking {end_time - start_time:.2f} seconds.")
    return V, policy

def q_learning(env, episodes=1000, alpha=0.1, gamma=0.9, epsilon=0.1):
    Q = defaultdict(lambda: np.zeros(len(env.actions)))

    start_time = time.time()

    for episode in range(episodes):
        state = env.start
        done = False

        while not env.is_terminal(state):
            # epsilon-greedy method
            if random.random() < epsilon:
                action = random.choice(range(len(env.actions)))
            else:
                action = np.argmax(Q[state])

            next_state = env.get_next_state(state, env.actions[action])
            reward = env.get_reward(next_state)

            # Update Q value
            best_next_action = np.argmax(Q[next_state])
            Q[state][action] += alpha * (reward + gamma * Q[next_state][best_next_action] - Q[state][action])
            state = next_state

    end_time = time.time()
    
    print(f"Q-learning ran for {episodes} episodes, taking {end_time - start_time:.2f} seconds.")
    policy = {state: env.actions[np.argmax(actions)] for state, actions in Q.items()}
    return Q, policy

grid = create_grid()
start, goal = set_random_points(grid)
env = GridWorld(grid, start, goal)

V, dp_policy = value_iteration(env)
Q, q_policy = q_learning(env)
