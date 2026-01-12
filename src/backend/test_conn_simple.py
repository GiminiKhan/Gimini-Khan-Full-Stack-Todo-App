import asyncio
import asyncpg
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

async def test_connection():
    """
    Test the database connection directly with asyncpg.
    """
    database_url = os.getenv("DATABASE_URL")

    if not database_url:
        print("DATABASE_URL not found in environment")
        return

    print(f"Attempting to connect to: {database_url}")

    try:
        # Parse the connection parameters from the URL
        # For Neon, we'll use the URL directly with asyncpg.connect()
        conn = await asyncpg.connect(dsn=database_url)

        # Execute a simple query
        result = await conn.fetchval("SELECT 1")

        # Close the connection
        await conn.close()

        if result == 1:
            print("Database Connection Successful!")
        else:
            print("Database Connection Failed!")

    except Exception as e:
        print(f"Database Connection Error: {str(e)}")


if __name__ == "__main__":
    asyncio.run(test_connection())