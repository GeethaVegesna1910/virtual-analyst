"""
Forecasting Module — Module 2
Time-series forecasting using Prophet and LSTM.
"""

import pandas as pd
import numpy as np
from typing import Optional
import mlflow
import mlflow.sklearn


class ProphetForecaster:
    """
    Business KPI forecasting using Facebook Prophet.
    Handles trend, seasonality, and holidays.
    Module 2 implementation.
    """

    def __init__(self, horizon_days: int = 30):
        self.horizon_days = horizon_days
        self.model = None

    def fit(self, df: pd.DataFrame, date_col: str = "ds", value_col: str = "y"):
        """
        Fit the Prophet model.
        df must have columns: ds (datetime), y (float)
        """
        try:
            from prophet import Prophet  # type: ignore
        except ImportError:
            raise ImportError("Install prophet: pip install prophet")

        df = df.rename(columns={date_col: "ds", value_col: "y"})

        with mlflow.start_run(run_name="prophet_forecast"):
            self.model = Prophet(
                yearly_seasonality=True,
                weekly_seasonality=True,
                daily_seasonality=False,
            )
            self.model.fit(df)
            mlflow.log_param("horizon_days", self.horizon_days)
            mlflow.log_param("model_type", "prophet")

        return self

    def predict(self) -> pd.DataFrame:
        """Generate forecast for the configured horizon."""
        if self.model is None:
            raise RuntimeError("Call fit() before predict()")
        future = self.model.make_future_dataframe(periods=self.horizon_days)
        forecast = self.model.predict(future)
        return forecast[["ds", "yhat", "yhat_lower", "yhat_upper"]].tail(self.horizon_days)

    def evaluate(self, actual: pd.Series, predicted: pd.Series) -> dict:
        """Calculate MAPE and RMSE."""
        mape = float(np.mean(np.abs((actual - predicted) / actual)) * 100)
        rmse = float(np.sqrt(np.mean((actual - predicted) ** 2)))
        return {"mape": round(mape, 2), "rmse": round(rmse, 4)}


class AnomalyDetector:
    """
    Anomaly detection on business metrics using Isolation Forest.
    Module 2 implementation.
    """

    def __init__(self, contamination: float = 0.05, random_state: int = 42):
        self.contamination = contamination
        self.random_state = random_state
        self.model = None

    def fit(self, X: pd.DataFrame):
        from sklearn.ensemble import IsolationForest  # type: ignore

        with mlflow.start_run(run_name="isolation_forest"):
            self.model = IsolationForest(
                contamination=self.contamination,
                random_state=self.random_state,
            )
            self.model.fit(X)
            mlflow.log_param("contamination", self.contamination)
            mlflow.sklearn.log_model(self.model, "isolation_forest")

        return self

    def detect(self, X: pd.DataFrame) -> pd.DataFrame:
        """Returns DataFrame with anomaly flag (-1 = anomaly, 1 = normal) and score."""
        if self.model is None:
            raise RuntimeError("Call fit() before detect()")
        predictions = self.model.predict(X)
        scores = self.model.score_samples(X)
        result = X.copy()
        result["anomaly"] = predictions
        result["anomaly_score"] = scores
        return result
