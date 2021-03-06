"""empty message

Revision ID: 83fd966f85c2
Revises: None
Create Date: 2016-07-03 09:35:00.428953

"""

# revision identifiers, used by Alembic.
revision = '83fd966f85c2'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('append',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('time_created', sa.DateTime(), nullable=True),
    sa.Column('content', sa.Text(), nullable=True),
    sa.Column('content_rendered', sa.Text(), nullable=True),
    sa.Column('deleted', sa.Boolean(), nullable=True),
    sa.Column('topic_id', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('comment',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('content', sa.Text(), nullable=True),
    sa.Column('content_rendered', sa.Text(), nullable=True),
    sa.Column('deleted', sa.Boolean(), nullable=True),
    sa.Column('time_created', sa.DateTime(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('topic_id', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('node',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=64), nullable=True),
    sa.Column('description', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('notify',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('content', sa.Text(), nullable=True),
    sa.Column('is_read', sa.Boolean(), nullable=True),
    sa.Column('time_created', sa.DateTime(), nullable=True),
    sa.Column('sender_id', sa.Integer(), nullable=True),
    sa.Column('receiver_id', sa.Integer(), nullable=True),
    sa.Column('comment_id', sa.Integer(), nullable=True),
    sa.Column('topic_id', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('topic',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=128), nullable=True),
    sa.Column('content', sa.Text(), nullable=True),
    sa.Column('content_rendered', sa.Text(), nullable=True),
    sa.Column('click', sa.Integer(), nullable=True),
    sa.Column('reply_count', sa.Integer(), nullable=True),
    sa.Column('deleted', sa.Boolean(), nullable=True),
    sa.Column('time_created', sa.DateTime(), nullable=True),
    sa.Column('last_replied', sa.DateTime(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('node_id', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=64), nullable=True),
    sa.Column('password_hash', sa.String(length=128), nullable=True),
    sa.Column('email', sa.String(length=64), nullable=True),
    sa.Column('is_superuser', sa.Boolean(), nullable=True),
    sa.Column('nickname', sa.String(length=64), nullable=True),
    sa.Column('use_avatar', sa.Boolean(), nullable=True),
    sa.Column('avatar_url', sa.String(length=64), nullable=True),
    sa.Column('website', sa.String(length=64), nullable=True),
    sa.Column('last_login', sa.DateTime(), nullable=True),
    sa.Column('date_joined', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_users_email'), 'users', ['email'], unique=True)
    op.create_index(op.f('ix_users_username'), 'users', ['username'], unique=True)
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_users_username'), table_name='users')
    op.drop_index(op.f('ix_users_email'), table_name='users')
    op.drop_table('users')
    op.drop_table('topic')
    op.drop_table('notify')
    op.drop_table('node')
    op.drop_table('comment')
    op.drop_table('append')
    ### end Alembic commands ###
