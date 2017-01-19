"""add fmt_phone column

Revision ID: aab96e170ead
Revises: aec53809b9ee
Create Date: 2017-01-19 17:12:47.108349

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'aab96e170ead'
down_revision = 'aec53809b9ee'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('orders', sa.Column('fmt_phone', sa.String(100)))


def downgrade():
    op.drop_column('orders', 'fmt_phone')
