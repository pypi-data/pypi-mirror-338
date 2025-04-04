from typing import Callable
from universal_mcp.applications import app_from_name
from loguru import logger

import pytest

@pytest.mark.parametrize("app_name", [
    "github",
    "zenquotes", 
    "tavily",
    "google-calendar",
    "google-mail",
    "resend",
    "reddit"
])
def test_application(app_name):
    app = app_from_name(app_name)(integration=None)
    assert app is not None
    tools = app.list_tools()
    logger.info(f"Tools for {app_name}: {tools}")
    assert len(tools) > 0
    assert isinstance(tools[0], Callable)
    for tool in tools:
        assert tool.__name__ is not None
        assert tool.__doc__ is not None
