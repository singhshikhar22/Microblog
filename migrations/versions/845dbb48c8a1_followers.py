"""followers

Revision ID: 845dbb48c8a1
Revises: 4f3d3268a15e
Create Date: 2020-04-13 02:06:56.483393

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '845dbb48c8a1'
down_revision = '4f3d3268a15e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('followers',
    sa.Column('follower_id', sa.Integer(), nullable=True),
    sa.Column('followed_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['followed_id'], ['user.id'], ),
    sa.ForeignKeyConstraint(['follower_id'], ['user.id'], )
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('followers')
    # ### end Alembic commands ###
