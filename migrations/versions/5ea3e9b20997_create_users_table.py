"""Create User table

Revision ID: 5ea3e9b20997
Revises: 
Create Date: 2023-11-16 13:32:25.178389

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = '5ea3e9b20997'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
                    sa.Column('id', sa.Integer(), autoincrement=True,
                              nullable=False),
                    sa.Column('username', sa.String(length=255),
                              nullable=False),
                    sa.Column('fullname', sa.String(length=255), nullable=True),
                    sa.Column('password', sa.String(length=255),
                              nullable=False),
                    sa.Column('is_active', sa.Boolean(), nullable=True),
                    sa.Column('created_at', sa.DateTime(), nullable=True),
                    sa.Column('updated_at', sa.DateTime(), nullable=True),
                    sa.Column('data', sa.Text(), nullable=True),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('username')
                    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')
    # ### end Alembic commands ###
