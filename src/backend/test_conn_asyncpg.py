import asyncio
import asyncpg
from urllib.parse import urlparse, parse_qs
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

async def test_connection():
    """
    Test the database connection directly with asyncpg using proper parameters.
    """
    database_url = os.getenv("DATABASE_URL")

    if not database_url:
        print("DATABASE_URL not found in environment")
        return

    print(f"Attempting to connect to: {database_url}")

    try:
        # Parse the URL to extract components
        parsed = urlparse(database_url)

        # Extract components
        user = parsed.username
        password = parsed.password
        host = parsed.hostname
        port = parsed.port or 5432  # Default PostgreSQL port
        database = parsed.path[1:] if parsed.path.startswith('/') else parsed.path

        # Parse query parameters for SSL
        query_params = parse_qs(parsed.query)
        ssl_mode = query_params.get('sslmode', [None])[0]

        # Prepare connection parameters
        conn_params = {
            'user': user,
            'password': password,
            'host': host,
            'port': port,
            'database': database,
        }

        # Handle SSL parameters appropriately for asyncpg
        if ssl_mode:
            if ssl_mode == 'require':
                conn_params['ssl'] = 'require'
            elif ssl_mode == 'disable':
                pass  # Don't set SSL
            # Add other SSL modes as needed

        # Connect using asyncpg
        conn = await asyncpg.connect(**conn_params)

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