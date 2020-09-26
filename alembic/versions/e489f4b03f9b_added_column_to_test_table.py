"""added column to Test table

Revision ID: e489f4b03f9b
Revises: 8f1e448b7ecd
Create Date: 2020-09-26 15:28:11.154806

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e489f4b03f9b'
down_revision = '8f1e448b7ecd'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('test', sa.Column('numbers', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('test', 'numbers')
    # ### end Alembic commands ###
