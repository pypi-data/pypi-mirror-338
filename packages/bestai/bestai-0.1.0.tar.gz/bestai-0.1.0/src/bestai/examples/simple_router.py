"""Simple example demonstrating the use of the BestAI router."""

import os
from typing import Dict, Any

from dotenv import load_dotenv

from bestai.client import AnthropicClient, ClientFactory, OpenAIClient, RoutedLLMClient
from bestai.router import (
    CapabilityBasedRoutingStrategy,
    CostBasedRoutingStrategy,
    ModelProvider,
    ModelRouter,
)
from bestai.utils import setup_logging, validate_api_keys

# Load environment variables from .env file
load_dotenv()

# Set up logging
setup_logging()


def create_cost_based_router() -> ModelRouter:
    """Create a router based on cost efficiency."""
    # Define model configurations
    models = {
        "gpt-3.5-turbo": {
            "provider": ModelProvider.OPENAI,
            "model_name": "gpt-3.5-turbo",
            "cost_per_1k_tokens": 0.002,
            "capabilities": ["text_generation", "summarization"],
        },
        "gpt-4": {
            "provider": ModelProvider.OPENAI,
            "model_name": "gpt-4",
            "cost_per_1k_tokens": 0.05,
            "capabilities": ["text_generation", "summarization", "code_generation", "reasoning"],
        },
        "claude-2": {
            "provider": ModelProvider.ANTHROPIC,
            "model_name": "claude-2",
            "cost_per_1k_tokens": 0.03,
            "capabilities": ["text_generation", "summarization", "code_generation", "reasoning"],
        },
    }
    
    # Define model costs for the strategy
    model_costs = {
        model_id: config["cost_per_1k_tokens"]
        for model_id, config in models.items()
    }
    
    # Create the routing strategy
    strategy = CostBasedRoutingStrategy(model_costs, default_model="gpt-3.5-turbo")
    
    # Create the router
    return ModelRouter(models, strategy, default_model="gpt-3.5-turbo")


def create_capability_based_router() -> ModelRouter:
    """Create a router based on model capabilities."""
    # Define model configurations
    models = {
        "gpt-3.5-turbo": {
            "provider": ModelProvider.OPENAI,
            "model_name": "gpt-3.5-turbo",
            "capabilities": ["text_generation", "summarization"],
        },
        "gpt-4": {
            "provider": ModelProvider.OPENAI,
            "model_name": "gpt-4",
            "capabilities": ["text_generation", "summarization", "code_generation", "reasoning"],
        },
        "claude-2": {
            "provider": ModelProvider.ANTHROPIC,
            "model_name": "claude-2",
            "capabilities": ["text_generation", "summarization", "code_generation", "reasoning"],
        },
    }
    
    # Extract capabilities for the strategy
    model_capabilities = {
        model_id: config["capabilities"]
        for model_id, config in models.items()
    }
    
    # Create the routing strategy
    strategy = CapabilityBasedRoutingStrategy(model_capabilities, default_model="gpt-3.5-turbo")
    
    # Create the router
    return ModelRouter(models, strategy, default_model="gpt-3.5-turbo")


def create_clients(router: ModelRouter) -> Dict[str, Any]:
    """Create clients for all the models defined in the router."""
    clients = {}
    
    for model_id, config in router.models.items():
        provider = config["provider"]
        model_name = config.get("model_name", model_id)
        
        try:
            if provider == ModelProvider.OPENAI:
                clients[model_id] = OpenAIClient(model=model_name)
            elif provider == ModelProvider.ANTHROPIC:
                clients[model_id] = AnthropicClient(model=model_name)
            # Add more providers as needed
        except ValueError as e:
            print(f"Could not create client for {model_id}: {str(e)}")
    
    return clients


def main():
    """Run the example."""
    # Check if API keys are available
    available_keys = validate_api_keys()
    
    if not available_keys["openai"] and not available_keys["anthropic"]:
        print("No API keys found. Please set environment variables.")
        return
    
    # Create the router (choose one)
    # router = create_cost_based_router()
    router = create_capability_based_router()
    
    # Create clients
    clients = create_clients(router)
    
    # Create the routed client
    routed_client = RoutedLLMClient(router, clients)
    
    # Example prompts
    prompts = [
        "What is the capital of France?",
        "Summarize the principles of machine learning in 3 sentences.",
        "Write a Python function to calculate the Fibonacci sequence.",
    ]
    
    # Generate responses
    for prompt in prompts:
        print(f"\nPrompt: {prompt}")
        try:
            selected_model = router.route(prompt)
            print(f"Selected model: {selected_model}")
            
            response = routed_client.generate(prompt)
            print(f"Response: {response}\n")
        except Exception as e:
            print(f"Error: {str(e)}")


if __name__ == "__main__":
    main() 