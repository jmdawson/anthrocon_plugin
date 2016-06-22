"""Add badge printing columns.

Revision ID: e5d885afba92
Revises: 
Create Date: 2016-05-16 23:05:11.167811

"""

# revision identifiers, used by Alembic.
revision = 'e5d885afba92'
down_revision = None
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('attendee', sa.Column('print_pending', sa.Boolean(), server_default='False', nullable=False))
    op.add_column('attendee', sa.Column('times_printed', sa.Integer(), server_default='0', nullable=False))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('attendee', 'times_printed')
    op.drop_column('attendee', 'print_pending')
    ### end Alembic commands ###