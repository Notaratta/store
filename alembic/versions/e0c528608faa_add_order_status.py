"""add order status

Revision ID: e0c528608faa
Revises: 56391851aa49
Create Date: 2025-07-10 19:19:04.447979

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e0c528608faa'
down_revision: Union[str, Sequence[str], None] = '56391851aa49'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('orders', sa.Column('status', sa.Enum('PENDING', 'PROCESSING', 'COMPLETED', 'CANCELLED', name='orderstatus'), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('orders', 'status')
    # ### end Alembic commands ###
