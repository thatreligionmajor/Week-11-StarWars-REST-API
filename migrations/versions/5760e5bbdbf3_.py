"""empty message

Revision ID: 5760e5bbdbf3
Revises: 161b311b67b9
Create Date: 2023-09-02 00:35:41.225713

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5760e5bbdbf3'
down_revision = '161b311b67b9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('people',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('persons_name', sa.String(length=50), nullable=False),
    sa.Column('height', sa.String(length=50), nullable=True),
    sa.Column('mass', sa.String(length=50), nullable=True),
    sa.Column('hair_color', sa.String(length=50), nullable=True),
    sa.Column('skin_color', sa.String(length=50), nullable=True),
    sa.Column('eye_color', sa.String(length=50), nullable=True),
    sa.Column('gender', sa.String(length=50), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('planets',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('diameter', sa.String(length=30), nullable=False),
    sa.Column('rotation_period', sa.String(length=30), nullable=False),
    sa.Column('orbital_period', sa.String(length=30), nullable=False),
    sa.Column('gravity', sa.String(length=30), nullable=False),
    sa.Column('population', sa.String(length=30), nullable=False),
    sa.Column('climate', sa.String(length=30), nullable=False),
    sa.Column('terrain', sa.String(length=30), nullable=True),
    sa.Column('description', sa.String(length=30), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('vehicles',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('model', sa.String(length=50), nullable=False),
    sa.Column('vehicle_class', sa.String(length=50), nullable=True),
    sa.Column('manufacturer', sa.String(length=50), nullable=True),
    sa.Column('cost_in_credits', sa.String(length=50), nullable=True),
    sa.Column('length', sa.String(length=50), nullable=True),
    sa.Column('crew', sa.String(length=50), nullable=True),
    sa.Column('passengers', sa.String(length=50), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('user')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('email', sa.VARCHAR(length=120), autoincrement=False, nullable=False),
    sa.Column('password', sa.VARCHAR(length=80), autoincrement=False, nullable=False),
    sa.Column('is_active', sa.BOOLEAN(), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='user_pkey'),
    sa.UniqueConstraint('email', name='user_email_key')
    )
    op.drop_table('vehicles')
    op.drop_table('planets')
    op.drop_table('people')
    # ### end Alembic commands ###