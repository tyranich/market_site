import logging

from fastapi import HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.repositories.loan_offer import LoanOfferRepository
from app.schemas.loan_offer import LoanOfferListResponse, LoanOfferQueryParams

logger = logging.getLogger(__name__)


class LoanOfferService:
    def __init__(self, session: AsyncSession):
        self.repository = LoanOfferRepository(session)

    async def list_offers(self, params: LoanOfferQueryParams) -> LoanOfferListResponse:
        offers = await self.repository.list_active(params)
        return LoanOfferListResponse(items=offers, total=len(offers))

    async def track_click(self, offer_id: int) -> None:
        if not await self.repository.get_active(offer_id):
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Предложение не найдено")
        await self.repository.add_click(offer_id)
        logger.info("Offer click recorded: offer_id=%s", offer_id)
