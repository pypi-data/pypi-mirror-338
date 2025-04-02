# dbqna.py
import re
from autogen_ext.models.openai import AzureOpenAIChatCompletionClient
from autogen_agentchat.agents import AssistantAgent
from dbqna.db_helper import execute_query, get_database_schema
from autogen_core import CancellationToken
from autogen_agentchat.messages import TextMessage

class AIDBBot:
    def __init__(self, azure_api_key, azure_api_base, azure_api_version, azure_deployment_name, model):
        """Initialize DBQnA with Azure OpenAI credentials"""
        self.model_client = AzureOpenAIChatCompletionClient(
            azure_deployment=azure_deployment_name,
            model=model,
            api_version=azure_api_version,
            azure_endpoint=azure_api_base,
            api_key=azure_api_key,
        )
        self.assistant_agent = AssistantAgent(
            name="sql_assistant",
            model_client=self.model_client,
            reflect_on_tool_use=True,
            system_message="You are a helpful SQL assistant.",
            model_client_stream=True,
        )

    async def generate_sql_query(self, natural_language_query, host, port, database, user, password):
        """Convert natural language query into SQL using AI"""
        schema_info = get_database_schema(host, port, database, user, password)
        prompt = f"""
        You are an AI SQL assistant. Convert the following natural language query into a valid PostgreSQL SQL query.
        Here is the database schema:
        {schema_info}

        Now convert this request: "{natural_language_query}"
        """
        response = await self.assistant_agent.on_messages(
        [TextMessage(content=prompt, source="user")],
        cancellation_token=CancellationToken(),
        )
        sql_query = re.search(r"SELECT.*?;", str(response), re.DOTALL)

        if sql_query:
            return sql_query.group(0)
        return "No valid SQL query generated."

    async def query_database(self, natural_language_query, host, port, database, user, password):
        """Convert natural language to SQL and execute the query"""
        sql_query = await self.generate_sql_query(natural_language_query, host, port, database, user, password)
        return execute_query(sql_query, host, port, database, user, password)
