import json
from typing import Dict, Union
from pathlib import Path

# Define types for better type hints
TokenCosts = Dict[str, float]
ModelPricing = Dict[str, Union[int, str, float]]


def get_token_costs(model: str, provider: str) -> TokenCosts:
    """
    Get token costs for a given model and provider.

    Args:
        model: The model name (e.g., 'gpt-4-turbo')
        provider: The provider name (e.g., 'openai')

    Returns:
        Dict containing input_cost_per_token and output_cost_per_token

    Raises:
        ValueError: If provider or model is not found in pricing configuration
    """
    # Get the path to the pricing JSON file
    pricing_file = (
        Path(__file__).parent.parent
        / "constants"
        / "provider_model_pricing.json"
    )

    # Read and parse the pricing data
    with open(pricing_file, "r") as f:
        model_pricing = json.load(f)

    # Try different model key patterns to find pricing data
    model_price = model_pricing.get(model)
    if not model_price:
        model_price = model_pricing.get(f"{provider}/{model}")
        if not model_price:
            model_price = model_pricing.get(f"openrouter/{provider}/{model}")
            if not model_price:
                # Try to find any key containing the model name
                matching_key = next(
                    (key for key in model_pricing.keys() if model in key), None
                )
                if matching_key:
                    model_price = model_pricing[matching_key]
                else:
                    raise ValueError(
                        f"Model '{model}' with provider '{provider}' not found in pricing configuration"
                    )

    return {
        "input_cost_per_token": float(
            model_price.get("input_cost_per_token", 0.0)
        ),
        "output_cost_per_token": float(
            model_price.get("output_cost_per_token", 0.0)
        ),
    }
