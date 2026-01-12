from logging.config import fileConfig
import sys
import os
from dotenv import load_dotenv

# Add the backend directory to the Python path to import modules
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))  # Add src/backend to path

# Load environment variables from .env file - use absolute path
env_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), '.env')
load_dotenv(env_path)

from sqlalchemy import create_engine
from alembic import context
from core.config import settings
from models.base import Base

# this is the Alembic Config object, which provides
# access to the values within the .ini file in use.
config = context.config

# Interpret the config file for Python logging.
# This line sets up loggers basically.
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# Get the database URL from settings
if settings.database_url:
    # Convert asyncpg URL to standard postgresql URL for migrations
    database_url = settings.database_url
    if '+asyncpg' in database_url:
        database_url = database_url.replace('+asyncpg', '')
    elif '+psycopg' in database_url:
        database_url = database_url.replace('+psycopg', '')

    config.set_main_option('sqlalchemy.url', database_url)

# Set the target metadata to our Base model's metadata
target_metadata = Base.metadata

def run_migrations_offline() -> None:
    """Run migrations in 'offline' mode.

    This configures the context with just a URL
    and not an Engine, though an Engine is acceptable
    here as well.  By skipping the Engine creation
    we don't even need a DBAPI to be available.

    Calls to context.execute() here emit the given string to the
    script output.

    """
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    """Run migrations in 'online' mode.

    In this scenario we need to create an Engine
    and associate a connection with the context.

    """
    # Get the database URL directly from settings instead of config to bypass issues
    raw_url = settings.database_url

    # Fallback to environment variable if settings.database_url is None
    if not raw_url:
        raw_url = os.getenv("DATABASE_URL")

    # Check if raw_url is still None or empty
    if not raw_url:
        raise ValueError("DATABASE_URL NOT FOUND IN ENV")

    # Clean the URL by removing async driver specifications
    if '+asyncpg' in raw_url:
        cleaned_url = raw_url.replace('+asyncpg', '')
    elif '+psycopg' in raw_url:
        cleaned_url = raw_url.replace('+psycopg', '')
    else:
        cleaned_url = raw_url

    print(f"DEBUG ALEMBIC: Using cleaned URL: {cleaned_url}")

    # Create engine with the cleaned URL directly
    connectable = create_engine(cleaned_url)

    with connectable.connect() as connection:
        context.configure(
            connection=connection, target_metadata=target_metadata
        )

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()