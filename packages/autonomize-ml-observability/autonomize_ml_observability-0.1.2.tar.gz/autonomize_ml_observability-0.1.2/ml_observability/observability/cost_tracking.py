import json
import os
import tempfile
from datetime import datetime
from typing import Any, Dict, List, Optional

import mlflow
import pandas as pd

from ml_observability.utils import setup_logger

logger = setup_logger(__name__)

# Default cost rates per 1K tokens (as of April 2025)
DEFAULT_COST_RATES = {
    "gpt-4o": {"input": 5.0, "output": 15.0},
    "gpt-4o-mini": {"input": 0.15, "output": 0.6},
    "gpt-4": {"input": 10.0, "output": 30.0},
    "gpt-4-turbo": {"input": 10.0, "output": 30.0},
    "gpt-3.5-turbo": {"input": 0.5, "output": 1.5},
    "claude-3-opus": {"input": 15.0, "output": 75.0},
    "claude-3-sonnet": {"input": 3.0, "output": 15.0},
    "claude-3-haiku": {"input": 0.25, "output": 1.25},
    "claude-3-7-sonnet-20250219": {"input": 3.0, "output": 15.0},
    "mistral-7b": {"input": 0.2, "output": 0.6},
    "mistral-large": {"input": 2.0, "output": 6.0},
}

class CostTracker:
    def __init__(
        self,
        cost_rates: Optional[Dict[str, Dict[str, float]]] = None,
        custom_rates_path: Optional[str] = None
    ):
        self.cost_rates = DEFAULT_COST_RATES.copy()

        env_rates_path = os.getenv("MODELHUB_COST_RATES_PATH")
        if env_rates_path and os.path.exists(env_rates_path):
            self._load_rates_from_file(env_rates_path)
        if custom_rates_path and os.path.exists(custom_rates_path):
            self._load_rates_from_file(custom_rates_path)
        if cost_rates:
            self.cost_rates.update(cost_rates)

        self.tracked_costs: List[Dict[str, Any]] = []
        logger.info("CostTracker initialized with %d model rate configs", len(self.cost_rates))

    def _load_rates_from_file(self, file_path: str):
        try:
            with open(file_path, "r") as f:
                custom_rates = json.load(f)
            self.cost_rates.update(custom_rates)
            logger.info("Loaded custom rates from %s", file_path)
        except Exception as e:
            logger.error("Failed to load custom rates from %s: %s", file_path, str(e))

    def track_cost(
        self,
        model_name: str,
        input_tokens: int,
        output_tokens: int,
        request_id: Optional[str] = None,
        provider: Optional[str] = None,
        metadata: Optional[Dict[str, Any]] = None,
        run_id: Optional[str] = None,
        log_to_mlflow: bool = True
    ) -> Dict[str, Any]:
        model_rates = self._get_model_rates(model_name)
        input_cost = (input_tokens / 1000) * model_rates["input"]
        output_cost = (output_tokens / 1000) * model_rates["output"]
        total_cost = input_cost + output_cost

        timestamp = datetime.now().isoformat()
        cost_entry = {
            "timestamp": timestamp,
            "model": model_name,
            "provider": provider or self._guess_provider(model_name),
            "input_tokens": input_tokens,
            "output_tokens": output_tokens,
            "total_tokens": input_tokens + output_tokens,
            "input_cost": input_cost,
            "output_cost": output_cost,
            "total_cost": total_cost,
            "request_id": request_id,
            "metadata": metadata or {}
        }

        self.tracked_costs.append(cost_entry)

        active_run = mlflow.active_run()
        if log_to_mlflow and (run_id or active_run):
            effective_run_id = run_id or (active_run.info.run_id if active_run else None)
            if effective_run_id:
                self._log_to_mlflow(cost_entry, run_id=effective_run_id)
            else:
                logger.debug("No active MLflow run found for logging costs")
        else:
            logger.debug("No active MLflow run or run_id provided for logging costs")

        logger.debug(
            "Tracked cost for %s: $%.4f (%d input, %d output tokens)",
            model_name, total_cost, input_tokens, output_tokens
        )
        return cost_entry

    def _get_model_rates(self, model_name: str) -> Dict[str, float]:
        if model_name in self.cost_rates:
            return self.cost_rates[model_name]
        for rate_model, rates in self.cost_rates.items():
            if model_name.startswith(rate_model):
                logger.debug("Using cost rates for %s as prefix match for %s", rate_model, model_name)
                return rates
        logger.warning("No cost rates found for model %s, using gpt-3.5-turbo rates as fallback", model_name)
        return self.cost_rates.get("gpt-3.5-turbo", {"input": 0.5, "output": 1.5})

    def _guess_provider(self, model_name: str) -> str:
        model_name = model_name.lower()
        if model_name.startswith("gpt"):
            return "openai"
        elif model_name.startswith("claude"):
            return "anthropic"
        elif model_name.startswith("mistral"):
            return "mistral"
        elif model_name.startswith("llama"):
            return "meta"
        else:
            return "unknown"

    def _log_to_mlflow(self, cost_entry: Dict[str, Any], run_id: Optional[str] = None):
        try:
            active_run = mlflow.active_run()
            if run_id or active_run:
                effective_run_id = run_id or (active_run.info.run_id if active_run else None)
                if effective_run_id:
                    with mlflow.start_run(run_id=effective_run_id, nested=True):
                        metrics = {
                            "llm_cost_total": cost_entry["total_cost"],
                            "llm_cost_input": cost_entry["input_cost"],
                            "llm_cost_output": cost_entry["output_cost"],
                            "llm_tokens_input": cost_entry["input_tokens"],
                            "llm_tokens_output": cost_entry["output_tokens"],
                            "llm_tokens_total": cost_entry["total_tokens"],
                        }
                        for key, value in metrics.items():
                            mlflow.log_metric(key, value)
                        if cost_entry["model"]:
                            mlflow.set_tag("llm_model", cost_entry["model"])
                        if cost_entry["provider"]:
                            mlflow.set_tag("llm_provider", cost_entry["provider"])
                else:
                    logger.debug("No active MLflow run found for logging costs")
            else:
                logger.debug("No active MLflow run or run_id provided for logging costs")
        except Exception as e:
            logger.warning("Failed to log cost metrics to MLflow: %s", str(e))

    def get_cost_summary(self) -> Dict[str, Any]:
        if not self.tracked_costs:
            return {
                "total_cost": 0.0,
                "total_requests": 0,
                "total_tokens": 0,
                "models": {},
                "providers": {}
            }
        df = pd.DataFrame(self.tracked_costs)
        total_cost = df["total_cost"].sum()
        total_requests = len(df)
        total_tokens = df["total_tokens"].sum()
        model_costs = df.groupby("model").agg({
            "total_cost": "sum",
            "input_tokens": "sum",
            "output_tokens": "sum",
            "total_tokens": "sum",
            "timestamp": "count"
        }).rename(columns={"timestamp": "requests"}).to_dict(orient="index")
        provider_costs = df.groupby("provider").agg({
            "total_cost": "sum",
            "input_tokens": "sum",
            "output_tokens": "sum",
            "total_tokens": "sum",
            "timestamp": "count"
        }).rename(columns={"timestamp": "requests"}).to_dict(orient="index")
        return {
            "total_cost": total_cost,
            "total_requests": total_requests,
            "total_tokens": total_tokens,
            "models": model_costs,
            "providers": provider_costs
        }

    def log_cost_summary_to_mlflow(self, run_id: Optional[str] = None):
        if not self.tracked_costs:
            logger.info("No costs to log")
            return
        summary = self.get_cost_summary()
        try:
            models_df = []
            for model_name, stats in summary["models"].items():
                models_df.append({
                    "model": model_name,
                    "requests": stats["requests"],
                    "total_tokens": stats["total_tokens"],
                    "input_tokens": stats["input_tokens"],
                    "output_tokens": stats["output_tokens"],
                    "total_cost": stats["total_cost"],
                })
            models_df = pd.DataFrame(models_df)

            providers_df = []
            for provider_name, stats in summary["providers"].items():
                providers_df.append({
                    "provider": provider_name,
                    "requests": stats["requests"],
                    "total_tokens": stats["total_tokens"],
                    "input_tokens": stats["input_tokens"],
                    "output_tokens": stats["output_tokens"],
                    "total_cost": stats["total_cost"],
                })
            providers_df = pd.DataFrame(providers_df)

            with tempfile.TemporaryDirectory() as tmp_dir:
                model_summary_path = os.path.join(tmp_dir, "cost_summary_by_model.csv")
                models_df.to_csv(model_summary_path, index=False)
                provider_summary_path = os.path.join(tmp_dir, "cost_summary_by_provider.csv")
                providers_df.to_csv(provider_summary_path, index=False)
                details_path = os.path.join(tmp_dir, "cost_details.csv")
                pd.DataFrame(self.tracked_costs).to_csv(details_path, index=False)
                json_path = os.path.join(tmp_dir, "cost_summary.json")
                with open(json_path, "w") as f:
                    json.dump(summary, f, indent=2)
                mlflow.log_artifact(model_summary_path, "cost_tracking")
                mlflow.log_artifact(provider_summary_path, "cost_tracking")
                mlflow.log_artifact(details_path, "cost_tracking")
                mlflow.log_artifact(json_path, "cost_tracking")
                mlflow.log_metric("llm_cost_summary_total", summary["total_cost"])
                mlflow.log_metric("llm_cost_summary_requests", summary["total_requests"])
                mlflow.log_metric("llm_cost_summary_tokens", summary["total_tokens"])
                logger.info(
                    "Logged cost summary to MLflow: $%.4f for %d requests (%d tokens)",
                    summary["total_cost"], summary["total_requests"], summary["total_tokens"]
                )
        except Exception as e:
            logger.warning("Failed to log cost summary to MLflow: %s", str(e))

    def reset(self):
        self.tracked_costs = []