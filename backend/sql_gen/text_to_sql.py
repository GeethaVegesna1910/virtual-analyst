"""
Text-to-SQL Module
Converts natural language questions to executable SQL using LangChain + LLM.
Module 1 implementation.
"""

from langchain_openai import ChatOpenAI
from langchain.chains import create_sql_query_chain
from langchain_community.utilities import SQLDatabase
from typing import Optional
import re


class TextToSQLAgent:
    """
    Converts natural language business questions to SQL queries.

    Features (Module 1):
    - Schema context injection
    - Multi-table join support
    - Self-correcting retry loop (max 3 attempts)
    - Accuracy tracking
    """

    MAX_RETRIES = 3

    def __init__(self, db_uri: str, model: str = "gpt-4o", temperature: float = 0.0):
        self.llm = ChatOpenAI(model=model, temperature=temperature)
        self.db = SQLDatabase.from_uri(db_uri)
        self.chain = create_sql_query_chain(self.llm, self.db)

    def generate_sql(self, question: str) -> dict:
        """
        Generate and execute SQL for a natural language question.
        Returns the SQL, results, and number of retries used.
        """
        last_error = None

        for attempt in range(self.MAX_RETRIES):
            try:
                sql = self.chain.invoke({"question": question})
                sql = self._clean_sql(sql)
                result = self.db.run(sql)
                return {
                    "sql": sql,
                    "result": result,
                    "attempts": attempt + 1,
                    "success": True,
                }
            except Exception as e:
                last_error = str(e)
                question = self._build_correction_prompt(question, sql if 'sql' in dir() else "", last_error)

        return {
            "sql": None,
            "result": None,
            "attempts": self.MAX_RETRIES,
            "success": False,
            "error": last_error,
        }

    def _clean_sql(self, raw: str) -> str:
        """Strip markdown code fences and whitespace."""
        raw = re.sub(r"```sql\n?", "", raw)
        raw = re.sub(r"```\n?", "", raw)
        return raw.strip()

    def _build_correction_prompt(self, original_question: str, failed_sql: str, error: str) -> str:
        return (
            f"{original_question}\n\n"
            f"Previous attempt failed with SQL:\n{failed_sql}\n"
            f"Error: {error}\n"
            f"Please fix the SQL and try again."
        )


# --- Accuracy evaluation helpers ---

def evaluate_accuracy(agent: TextToSQLAgent, test_cases: list[dict]) -> dict:
    """
    Evaluate agent accuracy on a labelled test set.
    Each test case: {"question": str, "expected_sql": str, "expected_result": any}
    """
    correct = 0
    results = []

    for case in test_cases:
        output = agent.generate_sql(case["question"])
        match = output["success"] and _results_match(output["result"], case["expected_result"])
        if match:
            correct += 1
        results.append({**case, "output": output, "correct": match})

    return {
        "accuracy": correct / len(test_cases) if test_cases else 0,
        "total": len(test_cases),
        "correct": correct,
        "details": results,
    }


def _results_match(actual, expected) -> bool:
    """Simple string-based result comparison — extend for production."""
    return str(actual).strip() == str(expected).strip()
