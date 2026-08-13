from fastapi import APIRouter

router = APIRouter(tags=["service"])


@router.get("/health", summary="Проверка доступности API")
async def health() -> dict[str, str]:
    return {"status": "ok"}
