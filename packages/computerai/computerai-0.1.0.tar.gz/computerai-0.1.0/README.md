# computerai

A minimal framework for creating computer use agents.

## Installation

```bash
pip install computerai
```

## Usage

```python
from computerai import create_agent

# Create a new agent
agent = create_agent(name="MyAgent")

# Execute a command with the agent
result = agent.execute("open browser")
print(result)  # "Executed: open browser"
```

## License

MIT
