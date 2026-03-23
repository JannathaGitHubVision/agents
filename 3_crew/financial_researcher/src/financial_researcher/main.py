#!/usr/bin/env python
import sys
import warnings
from pathlib import Path

from datetime import datetime
from dotenv import load_dotenv

from financial_researcher.crew import FinancialResearcher

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")


def _load_env_files() -> None:
    """Load .env files from ancestor folders so nested projects can inherit keys."""
    env_paths = [
        parent / ".env"
        for parent in Path(__file__).resolve().parents
        if (parent / ".env").exists()
    ]

    # Load outer .env first, then inner .env to allow local overrides.
    for env_path in reversed(env_paths):
        load_dotenv(env_path, override=True)


_load_env_files()


def run():
    ''''
    Run the financial researcher crew.
    '''

    inputs = {
        'company' : 'Tesla'
    }
    result = FinancialResearcher().crew().kickoff(inputs=inputs)
    print(result.raw)


if __name__ == "__main__":
    run()

    

  