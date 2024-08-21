"""empty message

Revision ID: ca78d279cbc1
Revises: 72b6886bd311
Create Date: 2024-08-20 19:36:23.775175

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

import sqlmodel



# revision identifiers, used by Alembic.
revision: str = 'ca78d279cbc1'
down_revision: Union[str, None] = '72b6886bd311'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('messages',
    sa.Column('create_date', sa.DateTime(), nullable=False),
    sa.Column('update_date', sa.DateTime(), nullable=False),
    sa.Column('delete_yn', sa.Boolean(), nullable=False),
    sa.Column('id', sqlmodel.sql.sqltypes.GUID(), nullable=False),
    sa.Column('chat_id', sqlmodel.sql.sqltypes.GUID(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('name', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('content', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('is_user', sa.Boolean(), nullable=False),
    sa.ForeignKeyConstraint(['chat_id'], ['chats.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('messages')
    # ### end Alembic commands ###
