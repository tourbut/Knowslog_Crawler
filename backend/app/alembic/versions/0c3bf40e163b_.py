"""empty message

Revision ID: 0c3bf40e163b
Revises: 9f59aa9eafb1
Create Date: 2024-07-29 17:30:37.705590

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

import sqlmodel

from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = '0c3bf40e163b'
down_revision: Union[str, None] = '9f59aa9eafb1'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('userdetail')
    op.add_column('user', sa.Column('name', sqlmodel.sql.sqltypes.AutoString(), nullable=False))
    op.add_column('user', sa.Column('age', sa.Integer(), nullable=False))
    op.add_column('user', sa.Column('discord_yn', sa.Boolean(), nullable=False))
    op.add_column('user', sa.Column('email_yn', sa.Boolean(), nullable=False))
    op.add_column('user', sa.Column('interests', sqlmodel.sql.sqltypes.AutoString(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'interests')
    op.drop_column('user', 'email_yn')
    op.drop_column('user', 'discord_yn')
    op.drop_column('user', 'age')
    op.drop_column('user', 'name')
    op.create_table('userdetail',
    sa.Column('create_date', postgresql.TIMESTAMP(), autoincrement=False, nullable=False),
    sa.Column('update_date', postgresql.TIMESTAMP(), autoincrement=False, nullable=False),
    sa.Column('delete_yn', sa.BOOLEAN(), autoincrement=False, nullable=False),
    sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('name', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('age', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('discord_yn', sa.BOOLEAN(), autoincrement=False, nullable=False),
    sa.Column('email_yn', sa.BOOLEAN(), autoincrement=False, nullable=False),
    sa.Column('interests', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], name='userdetail_user_id_fkey'),
    sa.PrimaryKeyConstraint('user_id', name='userdetail_pkey')
    )
    # ### end Alembic commands ###