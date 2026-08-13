from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field


class LoanOfferResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    name: str
    description: str
    logo_url: str | None
    max_amount: int
    max_term_days: int
    rate_from: float
    apr_from: float
    apr_to: float
    popularity: int
    features: list[str]
    external_url: str
    is_advertising: bool
    created_at: datetime
    updated_at: datetime


class LoanOfferListResponse(BaseModel):
    items: list[LoanOfferResponse]
    total: int


class LoanOfferQueryParams(BaseModel):
    min_amount: int | None = Field(default=None, ge=1)
    max_amount: int | None = Field(default=None, ge=1)
    max_term_days: int | None = Field(default=None, ge=1)
    sort: str = Field(default="popularity", pattern="^(popularity|max_amount|max_term)$")
