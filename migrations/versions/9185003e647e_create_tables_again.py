"""create_tables_again

Revision ID: 9185003e647e
Revises: 
Create Date: 2024-10-29 17:30:02.822314

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '9185003e647e'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('likes',
    sa.Column('id', sa.BigInteger(), autoincrement=True, nullable=False),
    sa.Column('user_id', sa.BigInteger(), nullable=False),
    sa.Column('post_id', sa.BigInteger(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('posts',
    sa.Column('post_id', sa.BigInteger(), autoincrement=True, nullable=False),
    sa.Column('post_from_user', sa.BigInteger(), nullable=False),
    sa.Column('media', sa.String(), nullable=False),
    sa.Column('description', sa.String(), nullable=False),
    sa.Column('tags', sa.String(), nullable=True),
    sa.Column('likes', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text("timezone('UTC', now())"), nullable=False),
    sa.PrimaryKeyConstraint('post_id')
    )
    op.create_table('social_network',
    sa.Column('user_id', sa.BigInteger(), autoincrement=True, nullable=False),
    sa.Column('full_name', sa.String(), nullable=False),
    sa.Column('age', sa.SmallInteger(), nullable=False),
    sa.Column('media', sa.String(), nullable=False),
    sa.Column('likes', sa.Integer(), nullable=False),
    sa.Column('city', sa.String(), nullable=False),
    sa.Column('description', sa.String(), nullable=False),
    sa.Column('subscribes', sa.Integer(), nullable=False),
    sa.Column('grade', sa.Float(), nullable=False),
    sa.Column('count_posts', sa.SmallInteger(), nullable=False),
    sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text("timezone('UTC', now())"), nullable=False),
    sa.PrimaryKeyConstraint('user_id')
    )
    op.create_table('sport_foods',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('description', sa.String(), nullable=False),
    sa.Column('manual_use', sa.String(), nullable=False),
    sa.Column('photo', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('sportsman',
    sa.Column('sportsmen_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('surname', sa.String(), nullable=False),
    sa.Column('full_name', sa.String(), nullable=False),
    sa.Column('description', sa.String(), nullable=False),
    sa.Column('photo', sa.String(), nullable=False),
    sa.Column('nickname', sa.String(), nullable=True),
    sa.Column('exercises', sa.String(), nullable=True),
    sa.Column('food', sa.String(), nullable=True),
    sa.Column('music', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('sportsmen_id')
    )
    op.create_table('strength_indicator',
    sa.Column('id', sa.BigInteger(), autoincrement=True, nullable=False),
    sa.Column('user_id', sa.BigInteger(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('core', sa.String(), nullable=False),
    sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text("timezone('UTC', now())"), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('users',
    sa.Column('user_id', sa.BigInteger(), nullable=False),
    sa.Column('user_photo', sa.String(), nullable=True),
    sa.Column('username', sa.String(), nullable=True),
    sa.Column('premium', sa.Boolean(), nullable=False),
    sa.Column('select_sportsman', sa.Boolean(), nullable=False),
    sa.Column('role', sa.String(), server_default='user', nullable=False),
    sa.Column('created', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
    sa.Column('current_sportsman', sa.Integer(), nullable=True),
    sa.Column('current_sport_food', sa.Integer(), nullable=True),
    sa.Column('current_post', sa.Integer(), nullable=True),
    sa.Column('notifications', sa.Boolean(), nullable=True),
    sa.Column('notifications_category', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('user_id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('users')
    op.drop_table('strength_indicator')
    op.drop_table('sportsman')
    op.drop_table('sport_foods')
    op.drop_table('social_network')
    op.drop_table('posts')
    op.drop_table('likes')
    # ### end Alembic commands ###
