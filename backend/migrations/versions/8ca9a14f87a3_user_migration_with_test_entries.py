"""user migration with test entries.

Revision ID: 8ca9a14f87a3
Revises: 
Create Date: 2020-03-18 18:15:15.383487

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8ca9a14f87a3'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.BigInteger(), nullable=False),
    sa.Column('first_name', sa.String(length=75), nullable=False),
    sa.Column('last_name', sa.String(length=75), nullable=False),
    sa.Column('username', sa.String(length=50), nullable=False),
    sa.Column('email', sa.String(length=100), nullable=False),
    sa.Column('password', sa.Text(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username')
    )
    op.create_table('entry',
    sa.Column('id', sa.BigInteger(), nullable=False),
    sa.Column('title', sa.String(length=30), nullable=True),
    sa.Column('content', sa.Text(), nullable=False),
    sa.Column('entryDate', sa.DateTime(), nullable=False),
    sa.Column('userId', sa.BigInteger(), nullable=False),
    sa.ForeignKeyConstraint(['userId'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('entry')
    op.drop_table('user')
    # ### end Alembic commands ###
