"""empty message

Revision ID: 648154f58ef9
Revises: 643975434968
Create Date: 2024-09-04 14:13:11.921697

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

import sqlmodel



# revision identifiers, used by Alembic.
revision: str = '648154f58ef9'
down_revision: Union[str, None] = '643975434968'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('userfiles',
    sa.Column('create_date', sa.DateTime(), nullable=False),
    sa.Column('update_date', sa.DateTime(), nullable=False),
    sa.Column('delete_yn', sa.Boolean(), nullable=False),
    sa.Column('id', sqlmodel.sql.sqltypes.GUID(), nullable=False),
    sa.Column('user_id', sqlmodel.sql.sqltypes.GUID(), nullable=False),
    sa.Column('file_name', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('file_path', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('file_size', sa.Integer(), nullable=False),
    sa.Column('file_type', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('file_ext', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('file_desc', sqlmodel.sql.sqltypes.AutoString(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('userfiles')
    # ### end Alembic commands ###
