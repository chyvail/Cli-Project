"""Added Employee Model

Revision ID: d2075b80b966
Revises: 5ac5485d78bd
Create Date: 2023-12-14 16:06:56.214484

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd2075b80b966'
down_revision = '5ac5485d78bd'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('employees',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('employee_firstname', sa.String(length=50), nullable=False),
    sa.Column('employee_lastname', sa.String(length=50), nullable=False),
    sa.Column('employee_email', sa.String(length=50), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('employees')
    # ### end Alembic commands ###
