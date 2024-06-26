"""add video column

Revision ID: 6fe5c4eb3557
Revises: 2ce0866e44f2
Create Date: 2024-03-18 00:01:01.681132

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '6fe5c4eb3557'
down_revision: Union[str, None] = '2ce0866e44f2'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('videos', sa.Column('video_data', sa.LargeBinary(), nullable=True))
    op.drop_column('videos', 'url')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('videos', sa.Column('url', sa.VARCHAR(length=255), autoincrement=False, nullable=False))
    op.drop_column('videos', 'video_data')
    # ### end Alembic commands ###
