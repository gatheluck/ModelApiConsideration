import logging

from fastapi import FastAPI
from src.config.configurations import APIConfigurations

logger = logging.getLogger(__name__)

app = FastAPI(
    title=APIConfigurations.title,
    description=APIConfigurations.description,
    version=APIConfigurations.version,
)