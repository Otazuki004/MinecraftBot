from minecraft.protocol import NetworkClient
from minecraft.protocol.packet import Packet
import random
import time

# Bot details
server_ip = 'Voidgamer256.aternos.me'
server_port = 45397
username = 'Imnotagay'
password = None  # Leave as None if using an offline-mode server
allowed_user = "OtazukiHS"

# Connect to the Minecraft server
client = NetworkClient(server_ip, server_port, username=username, password=password)

# Send a chat message to the server
def send_chat_message(message):
    client.write_packet(Packet('chat', {'message': message}))

# Function to handle the event when the bot joins the server
def on_join():
    print("Bot has joined the server. Sending registration and login commands...")
    
    # Send the /register and /login commands automatically after joining
    send_chat_message("/register humqn52& humqn52&")
    send_chat_message("/register humqn52&")
    send_chat_message("/login humqn52&")
    
    # Send custom join message
    send_chat_message("Join: https://t.me/Hyper_Speed0")
    
    # Start random movement and jumping to prevent inactivity kick
    start_movement()

# Function to move and jump randomly
def start_movement():
    print("Starting movement to avoid inactivity kick...")
    
    while True:
        # Random movement and jumping
        move = random.choice(['forward', 'backward', 'left', 'right'])
        jump = random.choice([True, False])
        
        # Example movement (this won't actually move the player in `minecraft-protocol`, just sends a message)
        if move == 'forward':
            send_chat_message("Moving forward")
        elif move == 'backward':
            send_chat_message("Moving backward")
        elif move == 'left':
            send_chat_message("Moving left")
        elif move == 'right':
            send_chat_message("Moving right")
        
        if jump:
            send_chat_message("Jumping")

        # Wait a random time between actions
        time.sleep(random.randint(1, 5))

# Function to handle chat messages
def on_chat_message(packet):
    message = packet['message']
    sender = packet['sender']  # Placeholder, actual extraction depends on packet structure

    if message == "&leave":
        if sender == allowed_user:
            send_chat_message(f"{sender}, I'm leaving the server. Goodbye!")
            client.close()
            print("Bot has disconnected from the server.")
        else:
            send_chat_message(f"Sorry {sender}, only {allowed_user} can tell me to leave!")
            print(f"{sender} tried to make the bot leave, but they are not {allowed_user}.")

# Register event handlers
client.on('join_game', on_join)
client.on('chat_message', on_chat_message)

# Start the bot's connection
client.connect()

# Keep the bot running
try:
    while True:
        client.tick()  # Process events
except KeyboardInterrupt:
    client.close()
