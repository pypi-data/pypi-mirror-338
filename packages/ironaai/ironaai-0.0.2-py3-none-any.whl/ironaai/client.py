"""
This module provides a client for the IronaAI API.
"""

import os
from functools import wraps
from typing import Any, Callable, Dict, List, Optional, Union, Type
import litellm
import json
import requests
from dotenv import load_dotenv
from pydantic import BaseModel

from .config import DEFAULT_MODEL, MAX_RETRIES, DEFAULT_API_URL, GIST_URL, MODEL_SELECT_ENDPOINT

# Load environment variables from .env file
load_dotenv()

class IronaAI:
    def __init__(self, model_list: Optional[List[str]] = None):
        self.api_key = os.getenv("IRONAAI_API_KEY")
        if model_list is None:
            model_list = self._fetch_model_list_from_gist()
        
        self.default_model = DEFAULT_MODEL
        self.model_list = model_list
        self.iai_api_url = DEFAULT_API_URL
        self.default_fallback_models = [ "openai/gpt-4o-mini","anthropic/claude-3-haiku-20240307"]

    def _fetch_model_list_from_gist(self):
        url = GIST_URL
        try:
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()
            model_list = []
            for provider, info in data.items():
                if "models" in info:
                    # Get model_prefix dictionary, default to empty dict if not present
                    prefix_dict = info.get("model_prefix", {})
                    for model in info["models"]:
                        if prefix_dict:
                            if model in prefix_dict:
                                prefix = prefix_dict[model]
                                full_model = f"{provider}/{prefix}/{model}"
                            else:
                                raise ValueError(
                                    f"Model '{model}' for provider '{provider}' does not have a prefix specified in model_prefix."
                                )
                        else:
                            full_model = f"{provider}/{model}"
                        model_list.append(full_model)
            return model_list
        except requests.RequestException as e:
            raise ValueError(f"Failed to fetch model list from Gist: {e}")
        except json.JSONDecodeError as e:
            raise ValueError(f"Failed to parse JSON from Gist: {e}")
        
    def error_handler(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(MAX_RETRIES):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    if attempt == MAX_RETRIES - 1:
                        raise e
                    print(f"Error occurred: {e}. Retrying...")
        return wrapper

    def _model_select(
        self,
        messages: List[Dict[str, str]],
        model_list: Optional[List[str]] = None,
        max_model_depth: int = None,
        hash_content: bool = False,
        tradeoff: Optional[str] = None,  # latency, cost, accuracy
        preference_id: Optional[str] = None,
        previous_session: Optional[str] = None,
        api_key: Optional[str] = None,
    ) -> str:
        url = MODEL_SELECT_ENDPOINT
        
        active_api_key = api_key or self.api_key
        if not active_api_key:
            raise ValueError("API key is required for model selection")
        active_model_list = model_list if model_list is not None else self.model_list

        model_mapping = {}
        llm_providers = []
        
        for full_model in active_model_list:
            parts = full_model.split("/")
            provider = parts[0]
            if len(parts) == 2:
                model_name = parts[1]
            elif len(parts) == 3:
                model_name = parts[2]
            else:
                raise ValueError(f"Invalid model format: {full_model}")
            llm_providers.append({"provider": provider, "model": model_name})
            model_mapping[(provider, model_name)] = full_model
        
        payload = {
            "messages": messages,
            "llm_providers": llm_providers,
            "max_model_depth": max_model_depth or len(active_model_list),
            "hash_content": hash_content,
        }
        if tradeoff:
            payload["tradeoff"] = tradeoff
        if preference_id:
            payload["preference_id"] = preference_id
        if previous_session:
            payload["previous_session"] = previous_session

        headers = {"Authorization": f"Bearer {active_api_key}"}
        response = requests.post(url, json=payload, headers=headers)
        response.raise_for_status()
        data = response.json()
        
        if "error" in data:
            raise ValueError(f"Model selection failed: {data['error']}")
        
        selected_provider = data["providers"][0]["provider"]
        selected_model_name = data["providers"][0]["model"]
        
        try:
            best_model = model_mapping[(selected_provider, selected_model_name)]
        except KeyError:
            raise ValueError(f"Selected model {selected_provider}/{selected_model_name} not found in model list.")
        
        return best_model

    def _get_litellm_params(self, selected_model: str) -> str:
        special_provider_map = {
            "togetherai": {"litellm_provider": "together_ai", "model_extract": lambda parts: "/".join(parts[1:])},
            "google": {"litellm_provider": "gemini", "model_extract": lambda parts: parts[-1]},
            "replicate": {"litellm_provider": "replicate", "model_extract": lambda parts: "/".join(parts[1:])},
            "openai": {"litellm_provider": "openai", "model_extract": lambda parts: "/".join(parts[1:])},
            "anthropic": {"litellm_provider": "anthropic", "model_extract": lambda parts: "/".join(parts[1:])},
            "cohere": {"litellm_provider": "cohere", "model_extract": lambda parts: "/".join(parts[1:])},
            "mistral": {"litellm_provider": "mistral", "model_extract": lambda parts: "/".join(parts[1:])},
            "perplexity": {"litellm_provider": "perplexity", "model_extract": lambda parts: "/".join(parts[1:])},
        }
        parts = selected_model.split("/")
        provider = parts[0]
        if provider in special_provider_map:
            litellm_provider = special_provider_map[provider]["litellm_provider"]
            model_name = special_provider_map[provider]["model_extract"](parts)
        else:
            litellm_provider = provider
            model_name = "/".join(parts[1:])
        full_model_string = f"{litellm_provider}/{model_name}"
        return full_model_string

    @error_handler
    def completion(
        self,
        messages: List[Dict[str, str]],
        model: Optional[str] = None,
        model_list: Optional[List[str]] = None,
        max_model_depth: Optional[int] = None,
        hash_content: bool = False,
        tradeoff: Optional[str] = None,
        preference_id: Optional[str] = None,
        previous_session: Optional[str] = None,
        stream: bool = False,
        tools: Optional[List[Dict]] = None,
        tool_choice: Optional[str] = "auto",
        response_format: Optional[Union[Dict[str, Any], Type[BaseModel]]] = None,
        fallback_models: Optional[List[str]] = None,
        api_key: Optional[str] = None,
        **kwargs,
    ) -> Any:
        """
        :param messages: List of message dictionaries with role and content.
        :param model: Optional model specification.
        :param max_model_depth: Maximum depth for model selection.
        :param hash_content: Whether to hash message content (default: False).
        :param tradeoff: Tradeoff between latency, cost, accuracy.
        :param preference_id: Identifier for preferences.
        :param previous_session: ID of a previous session.
        :param stream: Whether to stream the response (default: False).
        :param tools: List of tool dictionaries for function calling.
        :param tool_choice: How the model should use tools (default: "auto").
        :param response_format: Desired response format (dict or Pydantic model).
        :param fallback_models: List of fallback models to use if the primary model fails.
        :param api_key: API key for model selection.
        :param kwargs: Additional arguments for litellm.completion.
        :return: Response object from litellm.completion.
        """
        if tools and response_format:
            raise ValueError("Cannot use both 'tools' and 'response_format' simultaneously.")

        def message_to_dict(message):
            if isinstance(message, dict):
                return message
            msg_dict = {
                "role": message.role,
                "content": message.content if message.content is not None else "",  # Use "" instead of None
            }
            if getattr(message, "tool_calls", None):
                msg_dict["tool_calls"] = [
                    {
                        "id": tool_call.id,
                        "function": {
                            "name": tool_call.function.name,
                        "type": tool_call.type,
                            "arguments": tool_call.function.arguments,
                        },
                    }
                    for tool_call in message.tool_calls
                ]
            return msg_dict

        serializable_messages = [message_to_dict(msg) for msg in messages]

        #Use the user-provided model if given, otherwise select one
        if model is not None:
            models_to_try = [model]
        else:
            try:
                selected_model = self._model_select(
                    serializable_messages,
                    model_list,
                    max_model_depth,
                    hash_content,
                    tradeoff,
                    preference_id,
                    previous_session,
                    api_key=api_key,
                )
                models_to_try = [selected_model]
            except Exception as e:
                print(f"Model selection failed: {e}. Using fallback models.")
                # Use user-provided fallback models if available, otherwise default ones
                models_to_try = fallback_models or self.default_fallback_models
                
        exceptions = []  # Initialize list to store exceptions       
        for try_model in models_to_try:
            try:
                full_model_string=self._get_litellm_params(try_model)
                provider = full_model_string.split("/")[0]
                model_name = "/".join(full_model_string.split("/")[1:])
                supported_params = litellm.get_supported_openai_params(model=model_name, custom_llm_provider=provider)
                completion_kwargs = {
                    "model": full_model_string,
                    "messages": messages,
                    "stream": stream,
                    **kwargs,
                }

                if tools:
                    completion_kwargs["tools"] = tools
                    completion_kwargs["tool_choice"] = tool_choice

                if response_format:
                    if isinstance(response_format, dict):
                        # Handle dictionary response_format (e.g., {"type": "json_object"})
                        if "type" not in response_format or not isinstance(response_format["type"], str):
                            raise ValueError("response_format must have a 'type' key with a string value.")
                        if response_format["type"] == "json_object":
                            if "response_format" not in supported_params:
                                raise ValueError(f"Model {try_model} does not support JSON output (json_object).")
                            completion_kwargs["response_format"] = response_format
                        else:
                            raise ValueError(f"Unsupported response_format type: {response_format['type']}")
                    
                    elif isinstance(response_format, type) and issubclass(response_format, BaseModel):
                        # Handle Pydantic model directly
                        if not litellm.supports_response_schema(model=model_name, custom_llm_provider=provider):
                            # Enable client-side validation for models that don’t support structured outputs
                            litellm.enable_json_schema_validation = True
                            # Do NOT pass response_format to the API, let LiteLLM validate the response locally
                        else:
                            # Model supports structured outputs natively, pass response_format to API
                            completion_kwargs["response_format"] = response_format
                    
                    else:
                        raise ValueError("response_format must be a dict or a Pydantic model class.")

                # Define API key environment variable mapping
                api_key_env_map = {
                    "together_ai": "TOGETHER_API_KEY",
                    "gemini": "GOOGLE_API_KEY",
                    "openai": "OPENAI_API_KEY",
                    "anthropic": "ANTHROPIC_API_KEY",
                    "replicate": "REPLICATE_API_KEY",
                    "cohere": "COHERE_API_KEY",
                    "mistral": "MISTRAL_API_KEY",
                    "perplexity": "PERPLEXITY_API_KEY",
                }

                # Check if the provider exists in the map; raise an error if not
                if provider not in api_key_env_map:
                    raise ValueError(f"Provider '{provider}' not supported. Supported providers are: {list(api_key_env_map.keys())}")

                # Get the environment variable name from the map
                api_key_env_var = api_key_env_map[provider]
                api_key = os.getenv(api_key_env_var)
                if not api_key:
                    raise ValueError(f"Environment variable '{api_key_env_var}' not found")

                completion_kwargs["api_key"] = api_key
                response = litellm.completion(**completion_kwargs)
                return response
            except Exception as e:
                print(f"Completion with model {try_model} failed: {e}")
                exceptions.append(e)
                continue  # Try the next model in the list
        if exceptions:
            raise exceptions[-1]  # Raise the last exception if all attempts fail

        raise ValueError("All attempted models failed.")

    def stream_completion(self, *args, **kwargs):
        kwargs["stream"] = True
        return self.completion(*args, **kwargs)

    def function_call(
        self, messages: List[Dict[str, str]], tools: List[Dict], tool_choice: str = "auto", **kwargs
    ):
        return self.completion(messages=messages, tools=tools, tool_choice=tool_choice, **kwargs)

    def bind_tools(self, tools: List[Union[Dict[str, Any], Callable]]):
        tools_list = []
        for tool in tools:
            if isinstance(tool, dict):
                if "type" in tool:
                    tools_list.append(tool)
                else:
                    tools_list.append({"type": "function", "function": tool})
            elif callable(tool):
                function_dict = litellm.utils.function_to_dict(tool)
                tools_list.append({"type": "function", "function": function_dict})
        return lambda messages, **kwargs: self.completion(messages=messages, tools=tools_list, **kwargs)

    def supports_function_calling(self, model: str) -> bool:
        return litellm.supports_function_calling(model=model)

    def supports_json_mode(self, model: str) -> bool:
        provider, model_name = model.split("/", 1)
        params = litellm.get_supported_openai_params(model=model_name, custom_llm_provider=provider)
        return "response_format" in params