import logging
import os

from dataclasses import dataclass

logger = logging.getLogger(__name__)

@dataclass
class APIConfigurations:
    title: str = os.getenv("API_TITLE", "API Test")
    description: str = os.getenv("API_DESCRIPTION", "simple test api to deploy model")
    version: str = os.getenv("API_VERSION", "0.1")


logger.info(f"{APIConfigurations.__name__}: {APIConfigurations.__dict__}")