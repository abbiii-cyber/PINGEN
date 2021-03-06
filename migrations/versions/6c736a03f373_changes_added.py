"""changes added

Revision ID: 6c736a03f373
Revises: fe3db72990ae
Create Date: 2020-02-04 13:57:36.288521

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6c736a03f373'
down_revision = 'fe3db72990ae'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('generate',
    sa.Column('s_n', sa.Integer(), nullable=False),
    sa.Column('pin', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('s_n'),
    sa.UniqueConstraint('pin')
    )
    op.drop_index('ix_register_request_time', table_name='register')
    op.drop_table('register')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('register',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('s_n', sa.INTEGER(), nullable=False),
    sa.Column('pin', sa.VARCHAR(length=140), nullable=False),
    sa.Column('request_time', sa.DATETIME(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('pin'),
    sa.UniqueConstraint('s_n')
    )
    op.create_index('ix_register_request_time', 'register', ['request_time'], unique=False)
    op.drop_table('generate')
    # ### end Alembic commands ###
