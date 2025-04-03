import asyncio
from .client import KaioAgentClient

def main():
    try:
        client = KaioAgentClient()
        asyncio.run(client.start_session())
    except KeyboardInterrupt:
        print("\nScript terminated by user.")
    except Exception as e:
        print(f"\nAn error occurred: {str(e)}")

if __name__ == "__main__":
    main()