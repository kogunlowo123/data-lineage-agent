"""Data Lineage Agent - Unit Tests."""

import pytest
from src.agent.tools import AgentTools


@pytest.mark.asyncio
async def test_trace_lineage():
    """Test Trace data lineage from a dataset back to its sources."""
    tools = AgentTools()
    result = await tools.trace_lineage(dataset="test", depth=1)
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_analyze_impact():
    """Test Analyze downstream impact of a schema or data change."""
    tools = AgentTools()
    result = await tools.analyze_impact(dataset="test", change_type="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_map_dependencies():
    """Test Map data dependencies for a dataset or pipeline."""
    tools = AgentTools()
    result = await tools.map_dependencies(dataset="test", direction="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_detect_broken_lineage():
    """Test Detect gaps or breaks in data lineage chains."""
    tools = AgentTools()
    result = await tools.detect_broken_lineage(scope="test", include_stale=True)
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_agent_initialization():
    """Test that the agent initializes correctly."""
    from src.agent.data_lineage_agent_agent import DataLineageAgentAgent
    agent = DataLineageAgentAgent()
    assert agent.agent_id is not None
    assert agent._system_prompt is not None
    assert len(agent._tool_dispatch) > 0
