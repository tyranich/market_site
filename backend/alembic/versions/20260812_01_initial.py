"""initial loan offers tables

Revision ID: 20260812_01
Revises:
Create Date: 2026-08-12
"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

revision = "20260812_01"
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "loan_offers",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("name", sa.String(160), nullable=False),
        sa.Column("description", sa.Text(), nullable=False),
        sa.Column("logo_url", sa.String(1000), nullable=True),
        sa.Column("max_amount", sa.Integer(), nullable=False),
        sa.Column("max_term_days", sa.Integer(), nullable=False),
        sa.Column("rate_from", sa.Numeric(7, 3), nullable=False),
        sa.Column("apr_from", sa.Numeric(7, 2), nullable=False),
        sa.Column("apr_to", sa.Numeric(7, 2), nullable=False),
        sa.Column("popularity", sa.Integer(), nullable=False, server_default="0"),
        sa.Column("features", postgresql.JSONB(astext_type=sa.Text()), nullable=False),
        sa.Column("external_url", sa.String(1000), nullable=False),
        sa.Column("is_active", sa.Boolean(), nullable=False, server_default=sa.true()),
        sa.Column("is_advertising", sa.Boolean(), nullable=False, server_default=sa.true()),
        sa.Column("created_at", sa.DateTime(timezone=True), server_default=sa.text("now()"), nullable=False),
        sa.Column("updated_at", sa.DateTime(timezone=True), server_default=sa.text("now()"), nullable=False),
    )
    op.create_table(
        "offer_clicks",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("offer_id", sa.Integer(), sa.ForeignKey("loan_offers.id", ondelete="CASCADE"), nullable=False),
        sa.Column("created_at", sa.DateTime(timezone=True), server_default=sa.text("now()"), nullable=False),
    )


def downgrade() -> None:
    op.drop_table("offer_clicks")
    op.drop_table("loan_offers")
