"""empty message

Revision ID: 7d54a4c857d4
Revises: 44f162714301
Create Date: 2023-07-22 16:44:32.994785

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7d54a4c857d4'
down_revision = '44f162714301'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('first_name', sa.String(length=25), nullable=False),
    sa.Column('last_name', sa.String(length=25), nullable=False),
    sa.Column('email', sa.String(length=80), nullable=False),
    sa.Column('password', sa.Text(), nullable=False),
    sa.Column('gender', sa.String(), nullable=False),
    sa.Column('job_role', sa.String(), nullable=False),
    sa.Column('department', sa.String(), nullable=False),
    sa.Column('address', sa.String(), nullable=False),
    sa.Column('is_admin', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.drop_table('recipe')
    op.drop_table('user')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('first_name', sa.VARCHAR(length=25), autoincrement=False, nullable=False),
    sa.Column('last_name', sa.VARCHAR(length=25), autoincrement=False, nullable=False),
    sa.Column('email', sa.VARCHAR(length=80), autoincrement=False, nullable=False),
    sa.Column('department', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('address', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('is_admin', sa.BOOLEAN(), autoincrement=False, nullable=True),
    sa.Column('password', sa.TEXT(), autoincrement=False, nullable=False),
    sa.Column('gender', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('job_role', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='user_pkey'),
    sa.UniqueConstraint('email', name='user_email_key')
    )
    op.create_table('recipe',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('title', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('description', sa.TEXT(), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='recipe_pkey')
    )
    op.drop_table('users')
    # ### end Alembic commands ###
