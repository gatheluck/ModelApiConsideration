import logging
import fastapi
from typing import Dict

logger = logging.getLogger(__name__)
router = fastapi.APIRouter()

@router.get("/health")
def healt() -> Dict[str, str]:
    """endpoint for health check"""
    return {"health": "ok"}


