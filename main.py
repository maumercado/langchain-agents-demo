from langchain_openai import ChatOpenAI  # Updated import
from langchain.prompts import (
    HumanMessagePromptTemplate,
    ChatPromptTemplate,
    MessagesPlaceholder,
    SystemMessagePromptTemplate
)
from langchain.agents.agent import AgentExecutor
from langchain.agents.openai_functions_agent.base import create_openai_functions_agent
from langchain.memory import ConversationBufferMemory
from dotenv import load_dotenv

from tools.sql import sql_tool, describe_tables_tool
from tools.report import write_report_tool
from tools.sql import list_tables, connect_to_db
from handlers.chat_model_start_handler import ChatModelStartHandler

load_dotenv()

handlers = [ChatModelStartHandler()]
chat = ChatOpenAI(model="gpt-4o", temperature=0, callbacks=handlers)  # Ensure this is the correct usage

tables = list_tables(connect_to_db("db.sqlite"))

prompt = ChatPromptTemplate.from_messages(
    [
        SystemMessagePromptTemplate.from_template(
            "You are an AI that has access to a SQLite database.\n"
            f"Tables in the database: {tables}\n"
            "Do not make up any information about what tables or columns exist. Instead use the describe_tables tool to get information about the tables."
        ),
        MessagesPlaceholder(variable_name="chat_history"),
        HumanMessagePromptTemplate.from_template("{input}"),
        MessagesPlaceholder(variable_name="agent_scratchpad"),
    ]
)

history = ConversationBufferMemory(memory_key="chat_history", return_messages=True)

tools = [sql_tool, describe_tables_tool, write_report_tool]

# Use the new method to create the agent
agent = create_openai_functions_agent(
    llm=chat,
    tools=tools,
    prompt=prompt,
)

executor = AgentExecutor(
    agent=agent,
    memory=history,  # Ensure this is the correct type
    verbose=False,
    tools=tools
)

def main():
    while True:
        user_input = input("Enter your query (or type 'exit' to quit): ")
        if user_input.lower() == 'exit':
            break
        executor.invoke({
            "input": user_input
        })

# Run the main function
if __name__ == "__main__":
    main()

