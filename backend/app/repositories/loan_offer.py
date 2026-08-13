from sqlalchemy import Select, select
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.models.loan_offer import LoanOffer, OfferClick
from app.schemas.loan_offer import LoanOfferQueryParams


class LoanOfferRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def list_active(self, params: LoanOfferQueryParams) -> list[LoanOffer]:
        query: Select[tuple[LoanOffer]] = select(LoanOffer).where(LoanOffer.is_active.is_(True))
        if params.min_amount:
            query = query.where(LoanOffer.max_amount >= params.min_amount)
        if params.max_amount:
            query = query.where(LoanOffer.max_amount <= params.max_amount)
        if params.max_term_days:
            query = query.where(LoanOffer.max_term_days <= params.max_term_days)
        ordering = {
            "popularity": LoanOffer.popularity.desc(),
            "max_amount": LoanOffer.max_amount.desc(),
            "max_term": LoanOffer.max_term_days.desc(),
        }[params.sort]
        result = await self.session.scalars(query.order_by(ordering, LoanOffer.id))
        return list(result)

    async def get_active(self, offer_id: int) -> LoanOffer | None:
        return await self.session.scalar(
            select(LoanOffer).where(LoanOffer.id == offer_id, LoanOffer.is_active.is_(True))
        )

    async def add_click(self, offer_id: int) -> None:
        self.session.add(OfferClick(offer_id=offer_id))
        await self.session.commit()
