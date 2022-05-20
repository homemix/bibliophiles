"""Initial migration.

Revision ID: 12290f04bd38
Revises: 
Create Date: 2022-05-19 11:09:45.313461

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '12290f04bd38'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('genres',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('description', sa.String(length=100), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user_types',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('description', sa.String(length=100), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('books',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=100), nullable=False),
    sa.Column('author', sa.String(length=100), nullable=False),
    sa.Column('published_date', sa.Date(), nullable=False),
    sa.Column('publisher', sa.String(length=100), nullable=False),
    sa.Column('genre_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['genre_id'], ['genres.id'], onupdate='CASCADE', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_books_genre_id'), 'books', ['genre_id'], unique=False)
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=100), nullable=False),
    sa.Column('password', sa.String(length=100), nullable=False),
    sa.Column('email', sa.String(length=45), nullable=False),
    sa.Column('reset_password', sa.Integer(), nullable=False),
    sa.Column('usertype_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['usertype_id'], ['user_types.id'], onupdate='CASCADE', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_users_usertype_id'), 'users', ['usertype_id'], unique=False)
    op.create_table('reviews',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('rating', sa.Integer(), nullable=False),
    sa.Column('review', sa.Text(), nullable=False),
    sa.Column('users_id', sa.Integer(), nullable=True),
    sa.Column('books_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['books_id'], ['books.id'], onupdate='CASCADE', ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['users_id'], ['users.id'], onupdate='CASCADE', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_reviews_books_id'), 'reviews', ['books_id'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_reviews_books_id'), table_name='reviews')
    op.drop_table('reviews')
    op.drop_index(op.f('ix_users_usertype_id'), table_name='users')
    op.drop_table('users')
    op.drop_index(op.f('ix_books_genre_id'), table_name='books')
    op.drop_table('books')
    op.drop_table('user_types')
    op.drop_table('genres')
    # ### end Alembic commands ###