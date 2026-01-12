from sqlmodel.ext.asyncio.session import AsyncSession
from sqlmodel import create_engine
from sqlalchemy.pool import QueuePool
from ..core.config import settings
import os
from dotenv import load_dotenv
from urllib.parse import urlparse, parse_qs, urlencode

# Load environment variables from .env file - use absolute path to ensure it's found
env_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__)))), '.env')
load_dotenv(env_path)


def get_engine():
    """
    Create and return the async engine for SQLModel, only when needed.
    This handles the asyncpg SSL parameter issue with Neon PostgreSQL.
    """
    # Use the database URL from settings, which should be loaded from .env
    db_url = settings.database_url

    # Fallback to environment variable if settings.database_url is None
    if not db_url:
        db_url = os.getenv("DATABASE_URL")

    # Check if db_url is still None or empty
    if not db_url:
        raise ValueError("DATABASE_URL not set in environment or settings")

    # For Neon PostgreSQL with SQLModel + asyncpg, we need to handle SSL properly
    # The issue is that asyncpg does not support 'sslmode' in the connection string
    # We need to use connect_args to configure SSL for asyncpg
    parsed = urlparse(db_url)

    # Parse query parameters to handle them separately
    query_params = parse_qs(parsed.query)

    # Create connect_args for asyncpg with proper SSL configuration
    connect_args = {"ssl": True}  # Enable SSL for Neon connection

    # Handle other asyncpg-specific parameters if needed (without sslmode)
    if 'sslcert' in query_params:
        connect_args["sslcert"] = query_params['sslcert'][0]
    if 'sslkey' in query_params:
        connect_args["sslkey"] = query_params['sslkey'][0]
    if 'sslrootcert' in query_params:
        connect_args["sslrootcert"] = query_params['sslrootcert'][0]

    # Remove sslmode from the URL since asyncpg doesn't support it in connection string
    # Reconstruct URL without sslmode parameter
    base_url = f"{parsed.scheme}://{parsed.netloc}{parsed.path}"
    filtered_params = {k: v for k, v in query_params.items() if k != 'sslmode'}

    if filtered_params:
        query_string = urlencode({k: v[0] for k, v in filtered_params.items()}, doseq=True)
        final_db_url = f"{base_url}?{query_string}" if query_string else base_url
    else:
        final_db_url = base_url

    # Create the engine with the URL (without sslmode) and connect_args for SSL
    return create_engine(
        final_db_url,
        echo=True,  # Set to True for debugging SQL queries
        poolclass=QueuePool,
        pool_pre_ping=True,  # Verify connections before use
        pool_size=5,  # Number of connection objects to maintain
        max_overflow=10,  # Additional connections beyond pool_size
        pool_recycle=3600,  # Recycle connections after 1 hour
        connect_args=connect_args,  # Pass asyncpg-specific arguments including SSL
    )


async def get_db_session():
    """
    Dependency function that provides a database session for FastAPI endpoints.
    """
    engine = get_engine()
    async with AsyncSession(engine) as session:
        yield session