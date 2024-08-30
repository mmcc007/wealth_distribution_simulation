import random
import numpy as np
import matplotlib.pyplot as plt

class Agent:
    def __init__(self, initial_wealth):
        self.wealth = initial_wealth
        self.work_success_rate = random.uniform(0.5, 1.0)
        self.trade_success_rate = random.uniform(0.5, 1.0)

    def work(self):
        """Simulate the agent working."""
        if random.random() < self.work_success_rate:
            self.wealth += random.randint(1, 10)

    def trade(self, other_agent):
        """Simulate trading with another agent."""
        trade_amount = random.randint(1, 5)
        if random.random() < self.trade_success_rate:
            if other_agent.wealth >= trade_amount:
                self.wealth += trade_amount
                other_agent.wealth -= trade_amount
        else:
            if self.wealth >= trade_amount:
                self.wealth -= trade_amount
                other_agent.wealth += trade_amount

class Society:
    def __init__(self, num_agents, initial_wealth):
        self.agents = [Agent(initial_wealth) for _ in range(num_agents)]
        self.wealth_history = []

    def simulate_step(self):
        """Simulate one step in the society."""
        # Work
        for agent in self.agents:
            agent.work()

        # Trade
        num_trades = random.randint(1, len(self.agents) // 2)
        for _ in range(num_trades):
            agent1, agent2 = random.sample(self.agents, 2)
            agent1.trade(agent2)

        self.wealth_history.append([agent.wealth for agent in self.agents])

    def run_simulation(self, num_steps):
        """Run the simulation for a specified number of steps."""
        for _ in range(num_steps):
            self.simulate_step()

    def plot_wealth_distribution(self):
        """Plot the wealth distribution and calculate Gini coefficient."""
        wealth_history = np.array(self.wealth_history)
        
        plt.figure(figsize=(12, 6))
        
        # Wealth distribution over time
        plt.subplot(121)
        plt.plot(wealth_history)
        plt.title('Wealth Distribution Over Time')
        plt.xlabel('Time Steps')
        plt.ylabel('Wealth')
        
        # Final wealth distribution
        plt.subplot(122)
        plt.hist(wealth_history[-1], bins=20)
        plt.title('Final Wealth Distribution')
        plt.xlabel('Wealth')
        plt.ylabel('Number of Agents')
        
        plt.tight_layout()
        plt.show()

        # Calculate and print Gini coefficient
        final_wealth = wealth_history[-1]
        gini = self.gini_coefficient(final_wealth)
        print(f"Final Gini Coefficient: {gini:.4f}")

    @staticmethod
    def gini_coefficient(wealth):
        """Calculate the Gini coefficient of the given wealth distribution."""
        sorted_wealth = np.sort(wealth)
        index = np.arange(1, len(wealth) + 1)
        return (np.sum((2 * index - len(wealth) - 1) * sorted_wealth)) / (len(wealth) * np.sum(sorted_wealth))

def main():
    # Simulation parameters
    num_agents = 100
    initial_wealth = 100
    num_steps = 100000

    # Run the simulation
    society = Society(num_agents, initial_wealth)
    society.run_simulation(num_steps)
    society.plot_wealth_distribution()

if __name__ == "__main__":
    main()