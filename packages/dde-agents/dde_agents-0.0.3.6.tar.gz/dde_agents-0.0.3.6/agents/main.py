from Agent import Agent
from Config import ModelConfig

#ModelConfig.setDefaultModel("gpt-4o", True)

agent = Agent(
    name="agent",
    instruction="you're a customer support agent",
)

if __name__ == "__main__":
    print(agent.run("Im getting a bsod", debug=True))
