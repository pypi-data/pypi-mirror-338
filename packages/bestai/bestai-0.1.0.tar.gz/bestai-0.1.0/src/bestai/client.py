"""Client implementations for different LLM providers."""

import json
import logging
import os
from abc import ABC, abstractmethod
from typing import Any, Dict, List, Optional, Union

import requests
from dotenv import load_dotenv

from bestai.router import ModelProvider

load_dotenv()
logger = logging.getLogger(__name__)


class LLMClient(ABC):
    """Base class for LLM clients."""
    
    @abstractmethod
    def generate(self, prompt: str, options: Optional[Dict[str, Any]] = None) -> str:
        """Generate a response from the LLM."""
        pass


class OpenAIClient(LLMClient):
    """Client for OpenAI models."""
    
    def __init__(
        self,
        api_key: Optional[str] = None,
        model: str = "gpt-3.5-turbo",
        base_url: Optional[str] = None,
    ):
        self.api_key = api_key or os.environ.get("OPENAI_API_KEY")
        if not self.api_key:
            raise ValueError("OpenAI API key is required")
        
        self.model = model
        self.base_url = base_url or "https://api.openai.com/v1"
    
    def generate(self, prompt: str, options: Optional[Dict[str, Any]] = None) -> str:
        """Generate a response from an OpenAI model."""
        options = options or {}
        
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.api_key}",
        }
        
        data = {
            "model": options.get("model", self.model),
            "messages": [{"role": "user", "content": prompt}],
            "temperature": options.get("temperature", 0.7),
            "max_tokens": options.get("max_tokens", 1000),
        }
        
        try:
            response = requests.post(
                f"{self.base_url}/chat/completions",
                headers=headers,
                json=data,
                timeout=30,
            )
            response.raise_for_status()
            return response.json()["choices"][0]["message"]["content"]
        except Exception as e:
            logger.error(f"Error in OpenAI API call: {str(e)}")
            raise


class AnthropicClient(LLMClient):
    """Client for Anthropic models."""
    
    def __init__(
        self,
        api_key: Optional[str] = None,
        model: str = "claude-2",
    ):
        self.api_key = api_key or os.environ.get("ANTHROPIC_API_KEY")
        if not self.api_key:
            raise ValueError("Anthropic API key is required")
        
        self.model = model
    
    def generate(self, prompt: str, options: Optional[Dict[str, Any]] = None) -> str:
        """Generate a response from an Anthropic model."""
        options = options or {}
        
        headers = {
            "Content-Type": "application/json",
            "x-api-key": self.api_key,
        }
        
        data = {
            "model": options.get("model", self.model),
            "messages": [{"role": "user", "content": prompt}],
            "max_tokens": options.get("max_tokens", 1000),
            "temperature": options.get("temperature", 0.7),
        }
        
        try:
            response = requests.post(
                "https://api.anthropic.com/v1/messages",
                headers=headers,
                json=data,
                timeout=30,
            )
            response.raise_for_status()
            return response.json()["content"][0]["text"]
        except Exception as e:
            logger.error(f"Error in Anthropic API call: {str(e)}")
            raise


class ClientFactory:
    """Factory for creating LLM clients."""
    
    @staticmethod
    def create_client(
        provider: ModelProvider,
        api_key: Optional[str] = None,
        model: Optional[str] = None,
        **kwargs,
    ) -> LLMClient:
        """Create an LLM client for the specified provider."""
        if provider == ModelProvider.OPENAI:
            return OpenAIClient(api_key=api_key, model=model, **kwargs)
        elif provider == ModelProvider.ANTHROPIC:
            return AnthropicClient(api_key=api_key, model=model, **kwargs)
        else:
            raise ValueError(f"Unsupported provider: {provider}")


class RoutedLLMClient:
    """Client that routes requests to different LLM providers based on a router."""
    
    def __init__(self, router, clients: Dict[str, LLMClient]):
        """
        Initialize the routed client.
        
        Args:
            router: The router to use for routing requests
            clients: Dictionary mapping model identifiers to LLM clients
        """
        self.router = router
        self.clients = clients
    
    def generate(
        self,
        prompt: str,
        context: Optional[Dict[str, Any]] = None,
        options: Optional[Dict[str, Any]] = None,
    ) -> str:
        """
        Generate a response by routing to the appropriate model.
        
        Args:
            prompt: The user input to process
            context: Additional context that might influence routing
            options: Options to pass to the LLM client
            
        Returns:
            The generated response
        """
        model_id = self.router.route(prompt, context)
        client = self.clients.get(model_id)
        
        if not client:
            logger.error(f"No client found for model {model_id}")
            raise ValueError(f"No client found for model {model_id}")
        
        return client.generate(prompt, options) 