"""Added an 'admin' field into the user table.

Revision ID: 36f649b10fd0
Revises: e6785c68b318
Create Date: 2016-09-21 19:51:52.483536

"""

# revision identifiers, used by Alembic.
revision = '36f649b10fd0'
down_revision = 'e6785c68b318'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('admin', sa.Boolean(), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'admin')
    ### end Alembic commands ###
