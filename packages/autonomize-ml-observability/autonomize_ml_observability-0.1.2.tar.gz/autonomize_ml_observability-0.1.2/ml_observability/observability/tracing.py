import time
import asyncio
from ml_observability.core.mlflow_client import MLflowClient

class Observability:
    def __init__(self, mlflow_client: MLflowClient, cost_per_token: float = 0.00002):
        """
        Args:
            mlflow_client: An instance of your MLflowClient.
            cost_per_token: Default cost per token for a simple cost calculation.
        """
        self.mlflow_client = mlflow_client
        self.cost_per_token = cost_per_token

    def log_trace_and_cost(self, func):
        """
        Synchronous decorator.
        Automatically starts an MLflow run (if none is active), times the call,
        extracts a trace (expecting a dict with keys: prompt, response, model, token_usage),
        logs parameters and a simple cost metric, and ends the run if started.
        """
        def wrapper(*args, **kwargs):
            active = self.mlflow_client.mlflow.active_run()
            started_run = False
            if not active:
                run = self.mlflow_client.mlflow.start_run(run_name=func.__name__)
                started_run = True
            else:
                run = active

            start_time = time.time()
            result = func(*args, **kwargs)
            latency = time.time() - start_time

            trace = result.get("trace", {})
            prompt = trace.get("prompt")
            response = trace.get("response")
            model = trace.get("model")
            token_usage = trace.get("token_usage", {})

            self.mlflow_client.log_param("prompt", prompt)
            self.mlflow_client.log_param("response", response)
            self.mlflow_client.log_param("model", model)
            self.mlflow_client.log_metric("latency", latency)

            prompt_tokens = token_usage.get("prompt", 0)
            completion_tokens = token_usage.get("completion", 0)
            total_tokens = prompt_tokens + completion_tokens
            cost = total_tokens * self.cost_per_token
            self.mlflow_client.log_metric("cost", cost)

            if started_run:
                self.mlflow_client.mlflow.end_run()

            return result
        return wrapper

    def async_log_trace_and_cost(self, func):
        """
        Asynchronous decorator.
        """
        async def wrapper(*args, **kwargs):
            active = self.mlflow_client.mlflow.active_run()
            started_run = False
            if not active:
                run = self.mlflow_client.mlflow.start_run(run_name=func.__name__)
                started_run = True
            else:
                run = active

            start_time = time.time()
            result = await func(*args, **kwargs)
            latency = time.time() - start_time

            trace = result.get("trace", {})
            prompt = trace.get("prompt")
            response = trace.get("response")
            model = trace.get("model")
            token_usage = trace.get("token_usage", {})

            self.mlflow_client.log_param("prompt", prompt)
            self.mlflow_client.log_param("response", response)
            self.mlflow_client.log_param("model", model)
            self.mlflow_client.log_metric("latency", latency)

            prompt_tokens = token_usage.get("prompt", 0)
            completion_tokens = token_usage.get("completion", 0)
            total_tokens = prompt_tokens + completion_tokens
            cost = total_tokens * self.cost_per_token
            self.mlflow_client.log_metric("cost", cost)

            if started_run:
                self.mlflow_client.mlflow.end_run()

            return result
        return wrapper