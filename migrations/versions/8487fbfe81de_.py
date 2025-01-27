"""empty message

Revision ID: 8487fbfe81de
Revises: e71b2098d1dd
Create Date: 2022-03-02 10:38:56.679300

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8487fbfe81de'
down_revision = 'e71b2098d1dd'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user_profiles', sa.Column('password', sa.String(length=255), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user_profiles', 'password')
    # ### end Alembic commands ###
