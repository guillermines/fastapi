"""add content table to posts table

Revision ID: 0b68aa5d669f
Revises: fb170defefbf
Create Date: 2022-11-21 21:33:14.917044

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "0b68aa5d669f"
down_revision = "fb170defefbf"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column("posts", sa.Column("content", sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column("posts", "content")
    pass
