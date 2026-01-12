import asyncio
import sys
import os
from sqlalchemy import text

# Load environment variables from .env file
from dotenv import load_dotenv
load_dotenv()

# Add the src directory to the path so we can import the backend modules properly
sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

# Change to the backend directory to make imports work properly
os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__))))

from backend.database.session import get_engine


async def test_connection():
    """
    Test the database connection by executing a simple SELECT 1 query.
    """
    try:
        engine = get_engine()
        async with engine.connect() as conn:
            result = await conn.execute(text("SELECT 1"))
            row = result.fetchone()
            if row and row[0] == 1:
                print("Database Connection Successful!")
            else:
                print("Database Connection Failed!")

        # Properly dispose of the engine
        await engine.dispose()
    except Exception as e:
        print(f"Database Connection Error: {str(e)}")


if __name__ == "__main__":
    asyncio.run(test_connection())