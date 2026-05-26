"""
Unit tests for Text-to-SQL module.
"""

import pytest
from unittest.mock import MagicMock, patch


class TestTextToSQLAgent:

    def test_clean_sql_strips_markdown(self):
        """SQL returned by LLM often has markdown fences — must be stripped."""
        from backend.sql_gen.text_to_sql import TextToSQLAgent
        agent = TextToSQLAgent.__new__(TextToSQLAgent)
        raw = "```sql\nSELECT * FROM orders;\n```"
        assert agent._clean_sql(raw) == "SELECT * FROM orders;"

    def test_clean_sql_handles_plain_sql(self):
        from backend.sql_gen.text_to_sql import TextToSQLAgent
        agent = TextToSQLAgent.__new__(TextToSQLAgent)
        raw = "SELECT id, name FROM customers WHERE active = true"
        assert agent._clean_sql(raw) == raw

    def test_correction_prompt_includes_error(self):
        from backend.sql_gen.text_to_sql import TextToSQLAgent
        agent = TextToSQLAgent.__new__(TextToSQLAgent)
        prompt = agent._build_correction_prompt(
            "How many orders were placed last month?",
            "SELECT * FORM orders",
            "syntax error at or near FORM"
        )
        assert "syntax error" in prompt
        assert "FORM orders" in prompt

    def test_evaluate_accuracy_empty(self):
        from backend.sql_gen.text_to_sql import evaluate_accuracy
        mock_agent = MagicMock()
        result = evaluate_accuracy(mock_agent, [])
        assert result["accuracy"] == 0
        assert result["total"] == 0


class TestAnomalyDetector:

    def test_detect_raises_before_fit(self):
        from backend.ml.forecasting import AnomalyDetector
        import pandas as pd
        detector = AnomalyDetector()
        with pytest.raises(RuntimeError, match="Call fit()"):
            detector.detect(pd.DataFrame({"value": [1, 2, 3]}))

    def test_forecaster_raises_before_fit(self):
        from backend.ml.forecasting import ProphetForecaster
        forecaster = ProphetForecaster()
        with pytest.raises(RuntimeError, match="Call fit()"):
            forecaster.predict()
