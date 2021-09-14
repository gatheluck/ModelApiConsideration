import logging
from typing import Final

import fastapi
from src.config.configurations import APIConfigurations

logger = logging.getLogger(__name__)

def main() -> fastapi.FastAPI:
    app: Final = fastapi.FastAPI(
        title=APIConfigurations.title,
        description=APIConfigurations.description,
        version=APIConfigurations.version,
    )

    return app