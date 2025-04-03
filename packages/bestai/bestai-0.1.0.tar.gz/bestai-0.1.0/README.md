# BestAI Router

A flexible Python library for routing between different LLM models based on various criteria like cost, capabilities, and performance.

## Features

- Route requests between different LLM models based on:
  - Cost efficiency
  - Model capabilities
  - Performance (custom strategies can be implemented)
- Support for multiple LLM providers:
  - OpenAI
  - Anthropic
  - Easily extendable to other providers
- Simple client API for unified access to different models
- Configurable routing strategies

## Installation

```bash
pip install bestai
```

Or install from source:

```bash
git clone https://github.com/yourusername/bestairouter.git
cd bestairouter
pip install -e .
```

## Quick Start

### Environment Setup

First, set up your API keys in your environment:

```bash
export OPENAI_API_KEY=your_openai_api_key
export ANTHROPIC_API_KEY=your_anthropic_api_key
```

Alternatively, you can create a `.env` file in your project root:

```
OPENAI_API_KEY=your_openai_api_key
ANTHROPIC_API_KEY=your_anthropic_api_key
```

### Basic Usage

Here's a simple example of using the router with a capability-based strategy:

```python
from bestai.router import CapabilityBasedRoutingStrategy, ModelProvider, ModelRouter
from bestai.client import RoutedLLMClient, OpenAIClient, AnthropicClient

# Define models and their capabilities
models = {
    "gpt-3.5-turbo": {
        "provider": ModelProvider.OPENAI,
        "capabilities": ["text_generation", "summarization"],
    },
    "gpt-4": {
        "provider": ModelProvider.OPENAI,
        "capabilities": ["text_generation", "summarization", "code_generation", "reasoning"],
    },
    "claude-2": {
        "provider": ModelProvider.ANTHROPIC,
        "capabilities": ["text_generation", "summarization", "code_generation"],
    },
}

# Extract capabilities for the routing strategy
model_capabilities = {
    model_id: config["capabilities"]
    for model_id, config in models.items()
}

# Create the routing strategy
strategy = CapabilityBasedRoutingStrategy(model_capabilities, default_model="gpt-3.5-turbo")

# Create the router
router = ModelRouter(models, strategy, default_model="gpt-3.5-turbo")

# Create clients for each model
clients = {
    "gpt-3.5-turbo": OpenAIClient(model="gpt-3.5-turbo"),
    "gpt-4": OpenAIClient(model="gpt-4"),
    "claude-2": AnthropicClient(model="claude-2"),
}

# Create the routed client
routed_client = RoutedLLMClient(router, clients)

# Generate a response
response = routed_client.generate("Write a Python function to calculate the Fibonacci sequence.")
print(response)
```

## Advanced Usage

### Cost-Based Routing

Use the cost-based strategy to optimize for cost efficiency:

```python
from bestai.router import CostBasedRoutingStrategy, ModelRouter

# Define model costs
model_costs = {
    "gpt-3.5-turbo": 0.002,  # per 1K tokens
    "gpt-4": 0.05,
    "claude-2": 0.03,
}

# Create the strategy
strategy = CostBasedRoutingStrategy(model_costs, default_model="gpt-3.5-turbo")

# Create the router
router = ModelRouter(models, strategy, default_model="gpt-3.5-turbo")
```

### Custom Routing Strategy

You can implement your own routing strategy by subclassing `RoutingStrategy`:

```python
from bestai.router import RoutingStrategy
from typing import Dict, Optional, Any

class PerformanceBasedStrategy(RoutingStrategy):
    def __init__(self, model_performances: Dict[str, float], default_model: str):
        self.model_performances = model_performances
        self.default_model = default_model
    
    def select_model(self, input_text: str, context: Optional[Dict[str, Any]] = None) -> str:
        # Implement your custom routing logic here
        return self.default_model
```

## Examples

Check out the `examples` directory for more complete examples.

## License

This project is licensed under the Apache License 2.0 - see the LICENSE file for details.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request. 