"""changed steamID from int to text

Revision ID: 9fb2158e80da
Revises: 7a2d982b16e3
Create Date: 2017-05-30 12:07:33.273651

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9fb2158e80da'
down_revision = '7a2d982b16e3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('img_url', sa.Text(), nullable=True))
    op.create_unique_constraint(None, 'users', ['img_url'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'users', type_='unique')
    op.drop_column('users', 'img_url')
    # ### end Alembic commands ###
