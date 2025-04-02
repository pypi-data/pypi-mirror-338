import os

import mlflow
import logging

from ml_observability.core import ModelhubCredential
from ml_observability.observability.tracing import Observability
from ml_observability.observability.cost_tracking import CostTracker
from ml_observability.core.mlflow_client import MLflowClient

logger = logging.getLogger(__name__)

# Global instances
_mlflow_client: MLflowClient
_observability: Observability
_cost_tracker: CostTracker


def initialize(cost_rates: dict = None, experiment_name: str = None):
    """
    Initialize the MLflowClient, Observability, and CostTracker.
    Must be called once at startup.

    Optionally, specify an experiment_name to set the active MLflow experiment.
    """
    global _mlflow_client, _observability, _cost_tracker

    # Create a ModelhubCredential instance using environment variables.
    credential = ModelhubCredential(
        modelhub_url=os.getenv("MODELHUB_BASE_URL"),
        client_id=os.getenv("MODELHUB_CLIENT_ID"),
        client_secret=os.getenv("MODELHUB_CLIENT_SECRET")
    )

    _mlflow_client = MLflowClient(
        credential=credential,
    )
    experiment_name = experiment_name or os.getenv("EXPERIMENT_NAME")
    if experiment_name:
        _mlflow_client.set_experiment(experiment_name=experiment_name)
    _observability = Observability(_mlflow_client)
    _cost_tracker = CostTracker(cost_rates=cost_rates)
    logger.info("Observability system initialized.")


def monitor(client, provider: str = None, cost_rates: dict = None, experiment_name: str = None):
    """
    Enable monitoring on an LLM client.
    Supports multiple providers: 'openai', 'azure_openai', 'anthropic', etc.
    If provider is not provided, it is inferred from the client's module.

    You can also provide an experiment_name which will be used to configure MLflow.
    """
    initialize(cost_rates=cost_rates, experiment_name=experiment_name)
    if provider is None:
        mod = client.__class__.__module__.lower()
        if "openai" in mod:
            provider = "openai"
        elif "azure" in mod:
            provider = "azure_openai"
        elif "anthropic" in mod:
            provider = "anthropic"
        else:
            provider = "unknown"

    logger.debug("Provider: %s", provider)

    if provider in ("openai", "azure_openai"):
        _mlflow_client.mlflow.openai.autolog()
        wrap_openai(client)
    elif provider == "anthropic":
        _mlflow_client.mlflow.anthropic.autolog()
        wrap_anthropic(client)
    else:
        logger.warning("Monitoring not implemented for provider %s", provider)


def wrap_openai(client):
    # Wrap synchronous completions.create
    if hasattr(client.chat, "completions") and hasattr(client.chat.completions, "create"):
        original_create = client.chat.completions.create

        def wrapped_create(*args, **kwargs):
            active = mlflow.active_run()
            logger.info("Active run: %s", active)
            started_run = False
            if not active:
                run = mlflow.start_run(run_name="llm_call_auto")
                started_run = True
            else:
                run = active
            try:
                result = original_create(*args, **kwargs)
                messages = kwargs.get("messages", [])
                prompt = messages[0].get("content", "") if messages else ""
                prompt_tokens = len(prompt.split())
                completion_tokens = 5  # Simulated; extract real value if available.
                _cost_tracker.track_cost(
                    model_name=kwargs.get("model", "gpt-3.5-turbo"),
                    input_tokens=prompt_tokens,
                    output_tokens=completion_tokens,
                    run_id=run.info.run_id
                )
                return result
            finally:
                if started_run:
                    mlflow.end_run()

        client.chat.completions.create = wrapped_create

    # Wrap asynchronous completions.create (acreate)
    if hasattr(client, "chat") and hasattr(client.chat, "completions"):
        # Check if the client is an AsyncOpenAI instance
        if hasattr(client.chat.completions, "create") and callable(
                client.chat.completions.create) and client.__class__.__name__ == "AsyncOpenAI":
            original_async_create = client.chat.completions.create

            async def wrapped_async_create(*args, **kwargs):
                active = mlflow.active_run()
                logger.info("Active async run: %s", active)
                started_run = False
                if not active:
                    run = mlflow.start_run(run_name="async_llm_call_auto")
                    started_run = True
                else:
                    run = active

                try:
                    result = await original_async_create(*args, **kwargs)
                    messages = kwargs.get("messages", [])
                    prompt = messages[0].get("content", "") if messages else ""
                    prompt_tokens = len(prompt.split())
                    completion_tokens = 5  # Simulated; extract real value if available.
                    _cost_tracker.track_cost(
                        model_name=kwargs.get("model", "gpt-3.5-turbo"),
                        input_tokens=prompt_tokens,
                        output_tokens=completion_tokens,
                        run_id=run.info.run_id
                    )
                    return result
                finally:
                    if started_run:
                        mlflow.end_run()

            client.chat.completions.create = wrapped_async_create

    logger.info("Monitoring enabled for OpenAI/AzureOpenAI client.")


def wrap_anthropic(client):
    # Wrap synchronous messages.create.
    if hasattr(client, "messages") and hasattr(client.messages, "create"):
        original_create = client.messages.create

        def wrapped_create(*args, **kwargs):
            active = mlflow.active_run()
            started_run = False
            if not active:
                run = mlflow.start_run(run_name="llm_call_auto")
                started_run = True
            else:
                run = active
            try:
                result = original_create(*args, **kwargs)
                messages = kwargs.get("messages", [])
                prompt = messages[0].get("content", "") if messages else ""
                prompt_tokens = len(prompt.split())
                completion_tokens = 5  # Simulated; replace with real value if available.
                _cost_tracker.track_cost(
                    model_name=kwargs.get("model", "anthropic-default"),
                    input_tokens=prompt_tokens,
                    output_tokens=completion_tokens,
                    run_id=run.info.run_id
                )
                _mlflow_client.log_param("prompt", prompt)
                _mlflow_client.log_param("model", kwargs.get("model", "anthropic-default"))
                return result
            finally:
                if started_run:
                    mlflow.end_run()

        client.messages.create = wrapped_create

    # Wrap asynchronous messages.acreate if available.
    if hasattr(client, "messages") and hasattr(client.messages, "acreate"):
        original_acreate = client.messages.acreate

        async def wrapped_acreate(*args, **kwargs):
            active = mlflow.active_run()
            started_run = False
            if not active:
                run = mlflow.start_run(run_name="llm_call_auto")
                started_run = True
            else:
                run = active
            try:
                result = await original_acreate(*args, **kwargs)
                messages = kwargs.get("messages", [])
                prompt = messages[0].get("content", "") if messages else ""
                prompt_tokens = len(prompt.split())
                completion_tokens = 5  # Simulated value.
                _cost_tracker.track_cost(
                    model_name=kwargs.get("model", "anthropic-default"),
                    input_tokens=prompt_tokens,
                    output_tokens=completion_tokens,
                    run_id=run.info.run_id
                )
                _mlflow_client.log_param("prompt", prompt)
                _mlflow_client.log_param("model", kwargs.get("model", "anthropic-default"))
                return result
            finally:
                if started_run:
                    mlflow.end_run()

        client.messages.acreate = wrapped_acreate

    logger.info("Monitoring enabled for Anthropics client.")


def agent(name=None, tags=None):
    """
    Decorator for agent functions.
    Automatically wraps the function execution in an MLflow run.
    """

    def decorator(fn):
        def wrapper(*args, **kwargs):
            active = mlflow.active_run()
            started_run = False
            if not active:
                run = mlflow.start_run(run_name=name or fn.__name__)
                started_run = True
            else:
                run = active
            try:
                return fn(*args, **kwargs)
            finally:
                if started_run:
                    mlflow.end_run()

        return wrapper

    return decorator


def tool(name=None):
    """
    Decorator for tool functions.
    """

    def decorator(fn):
        def wrapper(*args, **kwargs):
            active = mlflow.active_run()
            started_run = False
            if not active:
                run = mlflow.start_run(run_name=name or fn.__name__)
                started_run = True
            else:
                run = active
            try:
                return fn(*args, **kwargs)
            finally:
                if started_run:
                    mlflow.end_run()

        return wrapper

    return decorator


class Identify:
    """
    A simple context manager for setting user context (if needed).
    """

    def __init__(self, user_props=None):
        self.user_props = user_props

    def __enter__(self):
        # Set user context here if desired.
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        # Clear user context.
        pass


def identify(user_props=None):
    return Identify(user_props)