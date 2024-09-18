import random
import time
from minecraft.networking.connection import Connection
from minecraft.networking.packets import clientbound, serverbound

# Bot details
server_ip = 'Voidgamer256.aternos.me'
server_port = 45397
username = 'Imnotagay'
password = None  # Leave as None if you are using an offline-mode server
allowed_user = "OtazukiHS"

# Connect to the Minecraft server
connection = Connection(server_ip, server_port, username=username, auth_token=password)

# Function to handle the event when the bot joins the server
def on_join_game(join_game_packet):
    print("Bot has joined the server. Sending registration and login commands...")
    
    # Send the /register and /login commands automatically after joining
    connection.write_packet(serverbound.play.ChatPacket("/register humqn52& humqn52&"))
    connection.write_packet(serverbound.play.ChatPacket("/register humqn52&"))
    connection.write_packet(serverbound.play.ChatPacket("/login humqn52&"))
    
    # Send custom join message
    connection.write_packet(serverbound.play.ChatPacket("Join: https://t.me/Hyper_Speed0"))
    
    # Start random movement and jumping to prevent inactivity kick
    start_movement()

# Function to move and jump randomly
def start_movement():
    print("Starting movement to avoid inactivity kick...")
    
    while True:
        # Random movement and jumping
        move = random.choice(['forward', 'backward', 'left', 'right'])
        jump = random.choice([True, False])
        
        if move == 'forward':
            connection.write_packet(serverbound.play.PositionAndLookPacket(position=(1, 0, 0), on_ground=True))
        elif move == 'backward':
            connection.write_packet(serverbound.play.PositionAndLookPacket(position=(-1, 0, 0), on_ground=True))
        elif move == 'left':
            connection.write_packet(serverbound.play.PositionAndLookPacket(position=(0, 1, 0), on_ground=True))
        elif move == 'right':
            connection.write_packet(serverbound.play.PositionAndLookPacket(position=(0, -1, 0), on_ground=True))
        
        if jump:
            connection.write_packet(serverbound.play.PositionAndLookPacket(position=(0, 0, 1), on_ground=False))
        
        time.sleep(random.randint(1, 5))  # Random delay

# Function to handle chat messages
def on_chat_message(chat_packet):
    sender = chat_packet.json_data['with'][0]['text']
    message = chat_packet.json_data['with'][1]['text']
    
    if message == "&leave":
        if sender == allowed_user:
            connection.write_packet(serverbound.play.ChatPacket(f"{sender}, I'm leaving the server. Goodbye!"))
            connection.disconnect()
            print("Bot has disconnected from the server.")
        else:
            connection.write_packet(serverbound.play.ChatPacket(f"Sorry {sender}, only {allowed_user} can tell me to leave!"))
            print(f"{sender} tried to make the bot leave, but they are not {allowed_user}.")

# Register event handlers
connection.register_packet_listener(on_join_game, clientbound.play.JoinGamePacket)
connection.register_packet_listener(on_chat_message, clientbound.play.ChatMessagePacket)

# Start the bot's connection
connection.connect()

# Keep the bot running
try:
    while True:
        connection.network_tick()
except KeyboardInterrupt:
    connection.disconnect()
