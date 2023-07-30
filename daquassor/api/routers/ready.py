from fastapi import APIRouter

router = APIRouter(prefix="/ready", tags=["App Status"])


@router.get("", response_model=bool)
async def ready():
    return True
