import random
import asyncio
from spade.agent import Agent
from spade.behaviour import CyclicBehaviour

# 1. Simulate the Disaster Environment
# We simulate random "percepts" (sensor readings)
def get_sensor_readings():
    disaster_types = ["None", "Flood", "Fire", "Earthquake"]
    severity_levels = ["Low", "Medium", "High", "Critical"]
    
    current_event = random.choice(disaster_types)
    current_severity = random.choice(severity_levels) if current_event != "None" else "None"
    
    return current_event, current_severity

# 2. Define the Agent
class SensorAgent(Agent):
    class SensingBehaviour(CyclicBehaviour):
        async def run(self):
            print("--- Sensing Environment ---")
            
            # "Perceive" the environment
            event, severity = get_sensor_readings()
            
            # Log the event 
            if event != "None":
                print(f"[ALERT] Detected: {event} | Severity: {severity}")
            else:
                print("[INFO] Status Normal. No disasters detected.")
            
            # Wait for 5 seconds before next sensing cycle
            await asyncio.sleep(5)

    async def setup(self):
        print("SensorAgent starting...")
        # Add the behavior to the agent
        self.add_behaviour(self.SensingBehaviour())

async def main():
    jid = "dcit403-labs@jabbim.com" 
    password = "dcit403"

    sensor = SensorAgent(jid, password)
    await sensor.start()
    
    print("SensorAgent is running. Press Ctrl+C to stop.")
    
    # Keep the script running so the agent can cycle
    try:
        while True:
            await asyncio.sleep(1)
    except KeyboardInterrupt:
        print("Stopping agent...")
        await sensor.stop()

if __name__ == "__main__":
    import spade
    spade.run(main())