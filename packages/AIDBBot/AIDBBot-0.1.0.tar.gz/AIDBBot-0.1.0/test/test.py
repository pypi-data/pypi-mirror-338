import asyncio
from dbqna import AIDBBot


host="localhost",
port=5432,
database="cmms",
user="postgres",
password="postgres"


# Set up AI Connection
dbqna = AIDBBot(
    azure_api_key="aaaaa",
    azure_api_base="bbbbb",
    azure_api_version="cccccc",
    azure_deployment_name="ddddd",
    model="eeeee"
)

# Define a function to test the query
async def test_query():
    query = "how many users are there for tenant 1289"
    result = await dbqna.query_database(query, host, port, database, user, password)
    print("Result:", result)

# Run the test query
if __name__ == "__main__":
    asyncio.run(test_query())
