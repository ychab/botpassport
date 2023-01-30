"""Initial

Revision ID: 7ad72b2d7909
Revises:
Create Date: 2023-01-30 22:11:25.137748

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7ad72b2d7909'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('email_history',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('bot', sa.String(), nullable=True),
    sa.Column('created', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('email_history')
    # ### end Alembic commands ###
