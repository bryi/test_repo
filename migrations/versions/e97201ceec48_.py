"""empty message

Revision ID: e97201ceec48
Revises: 
Create Date: 2020-02-19 07:45:40.711222

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e97201ceec48'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=128), nullable=False),
    sa.Column('email', sa.String(length=128), nullable=False),
    sa.Column('password', sa.String(length=128), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('modified_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('blogposts',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=128), nullable=False),
    sa.Column('contents', sa.Text(), nullable=False),
    sa.Column('owner_id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('modified_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['owner_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('blogposts')
    op.drop_table('users')
    # ### end Alembic commands ###