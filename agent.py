from swarm import Swarm, Agent

client = Swarm()
mini_model = "gpt-4o-mini"

# Coordinator function
def transfer_to_agent_b():
    return agent_b

# Agent A
agent_a = Agent(
    name="Agent A",
    instructions="You are a helpful assistant.",
    functions=[transfer_to_agent_b],
)

# Agent B
agent_b = Agent(
    name="Agent B",
    model=mini_model,
    instructions="You speak only in Finnish.",
)

response = client.run(
    agent=agent_a,
    messages=[{"role": "user", "content": "I want to talk to Agent B."}],
    debug=False,
)

print(response.messages[-1]["content"])