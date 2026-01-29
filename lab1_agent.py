import time
from spade.agent import Agent

class BasicAgent(Agent):
    async def setup(self):
        print("Agent starting . . .")
        print(f"Hello World! I am an agent named {self.name}")
        print("Agent setup complete!")

async def main():
    jid = "dcit403-labs@jabbim.com"
    password = "dcit403"

    agent = BasicAgent(jid, password)
    
    # Start the agent
    await agent.start()
    print("Agent is running...")
    
    # Keep alive for a moment to ensure setup finishes
    time.sleep(3)
    
    # Stop the agent
    await agent.stop()
    print("Agent stopped.")

if __name__ == "__main__":
    import spade
    spade.run(main())