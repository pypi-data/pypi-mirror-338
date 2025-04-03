"""Router for switching between different LLM models based on input criteria."""

import logging
from abc import ABC, abstractmethod
from enum import Enum
from typing import Any, Dict, List, Optional, Union

logger = logging.getLogger(__name__)


class ModelProvider(str, Enum):
    """Supported LLM model providers."""
    
    OPENAI = "openai"
    ANTHROPIC = "anthropic"
    GOOGLE = "google"
    MISTRAL = "mistral"
    COHERE = "cohere"
    CUSTOM = "custom"


class RoutingStrategy(ABC):
    """Base class for routing strategies."""
    
    @abstractmethod
    def select_model(self, input_text: str, context: Optional[Dict[str, Any]] = None) -> str:
        """Select a model based on the input and context."""
        pass


class CostBasedRoutingStrategy(RoutingStrategy):
    """Route based on cost efficiency."""
    
    def __init__(self, model_costs: Dict[str, float], default_model: str):
        self.model_costs = model_costs
        self.default_model = default_model
        
    def select_model(self, input_text: str, context: Optional[Dict[str, Any]] = None) -> str:
        """Select the most cost-efficient model based on input complexity."""
        # Simple proxy for complexity is input length
        input_length = len(input_text)
        
        if input_length < 100:
            # For very simple queries, use the cheapest model
            return min(self.model_costs.items(), key=lambda x: x[1])[0]
        elif input_length > 1000:
            # For complex queries, use the model with best quality/cost ratio
            # This would be more sophisticated in production
            return self.default_model
        else:
            # Default case
            return self.default_model


class CapabilityBasedRoutingStrategy(RoutingStrategy):
    """Route based on model capabilities."""
    
    def __init__(
        self,
        model_capabilities: Dict[str, List[str]],
        default_model: str,
    ):
        self.model_capabilities = model_capabilities
        self.default_model = default_model
        
    def select_model(self, input_text: str, context: Optional[Dict[str, Any]] = None) -> str:
        """Select a model based on required capabilities for the input."""
        required_capabilities = self._extract_required_capabilities(input_text, context)
        
        # Find models that satisfy all required capabilities
        suitable_models = []
        for model, capabilities in self.model_capabilities.items():
            if all(cap in capabilities for cap in required_capabilities):
                suitable_models.append(model)
                
        if not suitable_models:
            logger.warning(
                f"No model found with all required capabilities: {required_capabilities}. "
                f"Using default model: {self.default_model}"
            )
            return self.default_model
            
        # If multiple models are suitable, we could apply additional criteria here
        return suitable_models[0]
    
    def _extract_required_capabilities(
        self, input_text: str, context: Optional[Dict[str, Any]] = None
    ) -> List[str]:
        """Extract required capabilities from input text and context."""
        # This would be more sophisticated in production
        capabilities = []
        
        # Simple keyword matching for demonstration
        if "code" in input_text.lower() or "program" in input_text.lower():
            capabilities.append("code_generation")
            
        if "translate" in input_text.lower():
            capabilities.append("translation")
            
        if "summarize" in input_text.lower() or "summary" in input_text.lower():
            capabilities.append("summarization")
            
        # Extract from context if provided
        if context and "required_capabilities" in context:
            capabilities.extend(context["required_capabilities"])
            
        return list(set(capabilities))  # Remove duplicates


class ModelRouter:
    """Router for switching between different LLM models."""
    
    def __init__(
        self,
        models: Dict[str, Dict[str, Any]],
        strategy: RoutingStrategy,
        default_model: str,
    ):
        """
        Initialize the router.
        
        Args:
            models: Dictionary mapping model identifiers to their configurations
            strategy: The routing strategy to use
            default_model: The default model to use when routing fails
        """
        self.models = models
        self.strategy = strategy
        self.default_model = default_model
        
    def route(self, input_text: str, context: Optional[Dict[str, Any]] = None) -> str:
        """
        Route the input to the appropriate model.
        
        Args:
            input_text: The user input to be processed
            context: Additional context that might influence routing
            
        Returns:
            The identifier of the selected model
        """
        try:
            selected_model = self.strategy.select_model(input_text, context)
            
            if selected_model not in self.models:
                logger.warning(
                    f"Selected model {selected_model} not in available models. "
                    f"Using default model: {self.default_model}"
                )
                return self.default_model
                
            logger.info(f"Routed to model: {selected_model}")
            return selected_model
            
        except Exception as e:
            logger.error(f"Error in routing: {str(e)}. Using default model: {self.default_model}")
            return self.default_model
    
    def get_model_config(self, model_id: str) -> Dict[str, Any]:
        """Get the configuration for a model."""
        return self.models.get(model_id, self.models[self.default_model])
    
    def update_strategy(self, strategy: RoutingStrategy) -> None:
        """Update the routing strategy."""
        self.strategy = strategy 