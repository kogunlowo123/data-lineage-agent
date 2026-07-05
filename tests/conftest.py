"""Test configuration for Data Lineage Agent."""

import pytest


@pytest.fixture
def agent_config():
    return {"name": "data-lineage-agent", "category": "Data Engineering"}
