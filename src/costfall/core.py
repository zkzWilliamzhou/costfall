"""Core module for costfall"""

from dataclasses import dataclass
from typing import Any


@dataclass
class Config:
    name: str
    version: str = "0.1.0"


class Core:
    def __init__(self, config: Config):
        self.config = config

    def execute(self, input_data: str) -> str:
        return f"Executed: {input_data}"


def create_core(config: Config) -> Core:
    return Core(config)
