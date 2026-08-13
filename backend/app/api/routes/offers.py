from fastapi import APIRouter, Depends, Query, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.database import get_session
from app.schemas.loan_offer import LoanOfferListResponse, LoanOfferQueryParams
from app.services.loan_offer import LoanOfferService

router = APIRouter(prefix="/offers", tags=["offers"])


@router.get("", response_model=LoanOfferListResponse, summary="Список активных предложений")
async def list_offers(
    min_amount: int | None = Query(default=None, ge=1),
    max_amount: int | None = Query(default=None, ge=1),
    max_term_days: int | None = Query(default=None, ge=1),
    sort: str = Query(default="popularity", pattern="^(popularity|max_amount|max_term)$"),
    session: AsyncSession = Depends(get_session),
) -> LoanOfferListResponse:
    params = LoanOfferQueryParams(
        min_amount=min_amount, max_amount=max_amount, max_term_days=max_term_days, sort=sort
    )
    return await LoanOfferService(session).list_offers(params)


@router.post("/{offer_id}/click", status_code=status.HTTP_204_NO_CONTENT, summary="Зафиксировать переход")
async def track_offer_click(offer_id: int, session: AsyncSession = Depends(get_session)) -> None:
    await LoanOfferService(session).track_click(offer_id)
