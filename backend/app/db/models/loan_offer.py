from datetime import datetime

from sqlalchemy import Boolean, DateTime, ForeignKey, Integer, Numeric, String, Text, func
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    pass


class LoanOffer(Base):
    __tablename__ = "loan_offers"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(160))
    description: Mapped[str] = mapped_column(Text)
    logo_url: Mapped[str | None] = mapped_column(String(1000), nullable=True)
    max_amount: Mapped[int] = mapped_column(Integer)
    max_term_days: Mapped[int] = mapped_column(Integer)
    rate_from: Mapped[float] = mapped_column(Numeric(7, 3))
    apr_from: Mapped[float] = mapped_column(Numeric(7, 2))
    apr_to: Mapped[float] = mapped_column(Numeric(7, 2))
    popularity: Mapped[int] = mapped_column(Integer, default=0)
    features: Mapped[list[str]] = mapped_column(JSONB, default=list)
    external_url: Mapped[str] = mapped_column(String(1000))
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    is_advertising: Mapped[bool] = mapped_column(Boolean, default=True)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now(), onupdate=func.now()
    )


class OfferClick(Base):
    __tablename__ = "offer_clicks"

    id: Mapped[int] = mapped_column(primary_key=True)
    offer_id: Mapped[int] = mapped_column(ForeignKey("loan_offers.id", ondelete="CASCADE"))
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())
