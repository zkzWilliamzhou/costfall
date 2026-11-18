"""Tests for costfall"""

import pytest
from costfall.core import Core, create_core, Config


def test_core_creation():
    config = Config(name="test")
    core = create_core(config)
    assert core is not None
    assert core.get_config().name == "test"


def test_core_execute():
    config = Config(name="test")
    core = create_core(config)
    result = core.execute("input")
    assert result == "Executed: input"


def test_config():
    config = Config(name="test", version="1.0.0")
    assert config.name == "test"
    assert config.version == "1.0.0"
