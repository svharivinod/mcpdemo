import asyncio
import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from mcp_use import MCPAgent, MCPClient


async def run_memory_chat():
    load_dotenv()
    os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
    config_file = "browser_mcp.json"
    print("Initializing Chat...")

    client = MCPClient("browser_mcp.json")
    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

    agent = MCPAgent(
        llm=llm,
        client=client,
        max_steps=15,
        memory_enabled=True,
    )

    print("\n======== Interactive MCP Chat ========")
    print("Type 'exit' to end the chat.")
    print("Type 'clear' to clear the memory.")
    print("=================================\n")

    try:
        while True:
            user_input = input("You: ")
            if user_input.lower() == "exit":
                print("Exiting...")
                break

            if user_input.lower() == "clear":
                agent.clear_memory()
                print("Memory cleared.")
                continue

            print("\nAssistant: ", end="", flush=True)

            try:
                response = await agent.run(user_input)
                print(response)

            except Exception as e:
                print(f"\nError: {e}")

    finally:
        if client and client.sessions:
            await client.close_all_sessions()


if __name__ == "__main__":
    import asyncio
    asyncio.run(run_memory_chat())
        
