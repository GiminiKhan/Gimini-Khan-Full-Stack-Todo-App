import asyncio
from sqlalchemy import text
from sqlalchemy.ext.asyncio import create_async_engine
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

async def test_connection():
    """
    Test the database connection with SQLAlchemy and asyncpg directly.
    """
    database_url = os.getenv("DATABASE_URL")

    if not database_url:
        print("DATABASE_URL not found in environment")
        return

    print(f"Attempting to connect to: {database_url}")

    try:
        # Create engine with the URL (SQLAlchemy should handle the asyncpg part correctly)
        engine = create_async_engine(
            database_url,
            echo=True,  # Set to True for debugging SQL queries
            pool_pre_ping=True,  # Verify connections before use
            pool_size=5,  # Number of connection objects to maintain
            max_overflow=10,  # Additional connections beyond pool_size
            pool_recycle=3600,  # Recycle connections after 1 hour
        )

        # Test the connection
        async with engine.connect() as conn:
            result = await conn.execute(text("SELECT 1"))
            row = result.fetchone()

            # Dispose of the engine
            await engine.dispose()

            if row and row[0] == 1:
                print("Database Connection Successful!")
            else:
                print("Database Connection Failed!")

    except Exception as e:
        print(f"Database Connection Error: {str(e)}")


if __name__ == "__main__":
    asyncio.run(test_connection())