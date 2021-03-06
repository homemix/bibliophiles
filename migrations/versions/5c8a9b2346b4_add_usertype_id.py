"""add usertype id

Revision ID: 5c8a9b2346b4
Revises: 4b337a3700a3
Create Date: 2022-05-19 11:23:39.539413

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5c8a9b2346b4'
down_revision = '4b337a3700a3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user_types', sa.Column('user_id', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user_types', 'user_id')
    # ### end Alembic commands ###
