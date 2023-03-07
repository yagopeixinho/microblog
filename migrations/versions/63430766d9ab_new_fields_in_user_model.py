"""new fields in user model

Revision ID: 63430766d9ab
Revises: c90334fa91f4
Create Date: 2023-03-07 16:28:20.771329

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '63430766d9ab'
down_revision = 'c90334fa91f4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('about_me', sa.String(length=140), nullable=True))
        batch_op.add_column(sa.Column('last_seen', sa.DateTime(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_column('last_seen')
        batch_op.drop_column('about_me')

    # ### end Alembic commands ###
