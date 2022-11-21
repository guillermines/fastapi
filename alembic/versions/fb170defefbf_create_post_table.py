"""create post table

Revision ID: fb170defefbf
Revises: 
Create Date: 2022-11-21 21:24:30.535539

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "fb170defefbf"
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "posts",
        sa.Column("id", sa.Integer(), nullable=False, primary_key=True),
        sa.Column("title", sa.String(), nullable=False),
    )

    pass


def downgrade() -> None:
    op.drop_table("posts")
    pass
