from pyrogram import Client
from datetime import datetime
import time

# Configuration and constants
API_ID = "your_api_id"  # Replace with your actual API_ID
API_HASH = "your_api_hash"  # Replace with your actual API_HASH
BOT_TOKEN = "your_bot_token"  # Replace with your actual BOT_TOKEN
SUDO_USERS = []  # Define your SUDO_USERS
OWNER_ID = "your_owner_id"  # Replace with your actual OWNER_ID

# Assume STRING_SESSION1 to STRING_SESSION10 are defined somewhere
STRING_SESSION1 = None  # Example, replace with actual session strings
STRING_SESSION2 = None
STRING_SESSION3 = None
STRING_SESSION4 = None
STRING_SESSION5 = None
STRING_SESSION6 = None
STRING_SESSION7 = None
STRING_SESSION8 = None
STRING_SESSION9 = None
STRING_SESSION10 = None

StartTime = time.time()
CMD_HELP = {}
clients = []

SUDO_USERS.append(OWNER_ID)

def validate_config():
    global API_ID, API_HASH
    if not API_ID:
        print("WARNING: API ID NOT FOUND USING UTTAM API ⚡")
        API_ID = "27079591"
    if not API_HASH:
        print("WARNING: API HASH NOT FOUND USING UTTAM API ⚡")
        API_HASH = "c81ae4c3dc026ea4bf49842a8ce4a5f9"
    if not BOT_TOKEN:
        raise ValueError("WARNING: BOT TOKEN NOT FOUND. PLEASE ADD ⚡")

validate_config()

# Main bot client
app = Client(
    name="app",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
    plugins=dict(root="UTTAM/plugins"),
    in_memory=True,
)

def create_clients():
    for i in range(1, 11):
        session_var = globals().get(f'STRING_SESSION{i}')
        if session_var:
            print(f"Client{i}: Found.. Starting.. 📳")
            client = Client(
                name=f"client{i}",
                api_id=API_ID,
                api_hash=API_HASH,
                session_string=session_var,
                plugins=dict(root="UTTAM/plugins")
            )
            clients.append(client)

create_clients()

# Start all clients
for client in clients:
    try:
        client.start()
        print(f"{client.name} started successfully.")
    except Exception as e:
        print(f"Failed to start {client.name}: {e}")

# Add your bot logic here...

# Don't forget to run the main app if needed
if __name__ == "__main__":
    app.run()
