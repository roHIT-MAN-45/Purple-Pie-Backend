"""add name and phone fields to users table

Revision ID: 15aba8ff005f
Revises: 
Create Date: 2022-08-31 13:00:10.276274

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '15aba8ff005f'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # Adding name column
    op.add_column('users', sa.Column("name", sa.String(), nullable=False))

    # Adding phone column
    op.add_column("users", sa.Column("phone", sa.String(), nullable=False))
    pass


def downgrade() -> None:
    # Remove changes
    op.drop_column("users", "name")
    op.drop_column("users", "phone")
    pass
