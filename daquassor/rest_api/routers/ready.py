from fastapi import APIRouter

router = APIRouter(prefix="/ready", tags=["Ready"])

@router.get("/ready")
async def ready():
    return True

