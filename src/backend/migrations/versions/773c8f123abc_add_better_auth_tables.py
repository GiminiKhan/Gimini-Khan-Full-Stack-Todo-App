"""Add Better Auth managed tables for authentication

Revision ID: 773c8f123abc
Revises: 662b861772f7
Create Date: 2026-01-10 19:30:00.000000

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = '773c8f123abc'
down_revision: Union[str, Sequence[str], None] = '662b861772f7'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema to add Better Auth managed tables."""

    # Create Better Auth managed tables (these are typically managed by Better Auth)
    # but we'll create them for reference

    # Better Auth Users table (reference table for our application to connect to Better Auth users)
    op.create_table('better_auth_users',
        sa.Column('id', sa.UUID(), nullable=False),
        sa.Column('email', sa.String(length=255), nullable=False),
        sa.Column('email_verified', sa.Boolean(), nullable=False, default=False),
        sa.Column('name', sa.String(length=255), nullable=True),
        sa.Column('username', sa.String(length=50), nullable=True),
        sa.Column('locale', sa.String(length=10), nullable=True),
        sa.Column('image', sa.Text(), nullable=True),
        sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
        sa.Column('updated_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('email'),
        sa.UniqueConstraint('username')
    )

    # For the actual Better Auth managed tables (sessions, accounts, verification),
    # these would typically be managed by Better Auth itself.
    # We'll create placeholder tables for reference purposes.

    # Better Auth Sessions table
    op.create_table('better_auth_sessions',
        sa.Column('id', sa.UUID(), nullable=False),
        sa.Column('user_id', sa.UUID(), nullable=False),
        sa.Column('expires_at', sa.DateTime(timezone=True), nullable=False),
        sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
        sa.Column('updated_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
        sa.ForeignKeyConstraint(['user_id'], ['better_auth_users.id'], ondelete='CASCADE'),
        sa.PrimaryKeyConstraint('id')
    )

    op.create_index('idx_sessions_user_id', 'better_auth_sessions', ['user_id'])
    op.create_index('idx_sessions_expires_at', 'better_auth_sessions', ['expires_at'])

    # Better Auth Accounts table
    op.create_table('better_auth_accounts',
        sa.Column('id', sa.UUID(), nullable=False),
        sa.Column('user_id', sa.UUID(), nullable=False),
        sa.Column('account_type', sa.String(length=50), nullable=False),
        sa.Column('provider_id', sa.String(length=100), nullable=False),
        sa.Column('provider_account_id', sa.String(length=255), nullable=False),
        sa.Column('refresh_token', sa.Text(), nullable=True),
        sa.Column('access_token', sa.Text(), nullable=True),
        sa.Column('expires_at', sa.Integer(), nullable=True),
        sa.Column('token_type', sa.String(length=50), nullable=True),
        sa.Column('scope', sa.String(length=255), nullable=True),
        sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
        sa.Column('updated_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
        sa.ForeignKeyConstraint(['user_id'], ['better_auth_users.id'], ondelete='CASCADE'),
        sa.PrimaryKeyConstraint('id')
    )

    op.create_index('idx_accounts_user_id', 'better_auth_accounts', ['user_id'])
    op.create_index('idx_accounts_provider', 'better_auth_accounts', ['provider_id', 'provider_account_id'])

    # Better Auth Verification table
    op.create_table('better_auth_verification',
        sa.Column('id', sa.UUID(), nullable=False),
        sa.Column('identifier', sa.String(length=255), nullable=False),
        sa.Column('value', sa.String(length=255), nullable=False),
        sa.Column('expires_at', sa.DateTime(timezone=True), nullable=False),
        sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
        sa.PrimaryKeyConstraint('id')
    )

    op.create_index('idx_verification_identifier_value', 'better_auth_verification', ['identifier', 'value'])
    op.create_index('idx_verification_expires_at', 'better_auth_verification', ['expires_at'])

    # Update projects table to reference better_auth_users
    op.add_column('projects', sa.Column('better_auth_owner_id', sa.UUID(), nullable=True))

    # Update todos table to reference better_auth_users
    op.add_column('todos', sa.Column('better_auth_owner_id', sa.UUID(), nullable=True))

    # Add foreign key constraints to the new columns
    op.create_foreign_key(
        'fk_projects_better_auth_owner_id',
        'projects', 'better_auth_users',
        ['better_auth_owner_id'], ['id'],
        ondelete='CASCADE'
    )

    op.create_foreign_key(
        'fk_todos_better_auth_owner_id',
        'todos', 'better_auth_users',
        ['better_auth_owner_id'], ['id'],
        ondelete='CASCADE'
    )

    # The original 'users' table and its relationships remain for backward compatibility
    # During the transition period, applications can work with both systems


def downgrade() -> None:
    """Downgrade schema to remove Better Auth tables."""

    # Remove foreign key constraints
    op.drop_constraint('fk_todos_better_auth_owner_id', 'todos', type_='foreignkey')
    op.drop_constraint('fk_projects_better_auth_owner_id', 'projects', type_='foreignkey')

    # Remove the new columns
    op.drop_column('todos', 'better_auth_owner_id')
    op.drop_column('projects', 'better_auth_owner_id')

    # Drop Better Auth tables
    op.drop_index('idx_verification_expires_at', table_name='better_auth_verification')
    op.drop_index('idx_verification_identifier_value', table_name='better_auth_verification')
    op.drop_table('better_auth_verification')

    op.drop_index('idx_accounts_provider', table_name='better_auth_accounts')
    op.drop_index('idx_accounts_user_id', table_name='better_auth_accounts')
    op.drop_table('better_auth_accounts')

    op.drop_index('idx_sessions_expires_at', table_name='better_auth_sessions')
    op.drop_index('idx_sessions_user_id', table_name='better_auth_sessions')
    op.drop_table('better_auth_sessions')

    op.drop_table('better_auth_users')