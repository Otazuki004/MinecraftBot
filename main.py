from minecraft import *
import random
import time

# Bot details
server_ip = 'Voidgamer256.aternos.me'
server_port = 45397
username = 'Imnotagay'
password = None  # Leave as None if using an offline-mode server
allowed_user = "OtazukiHS"

# Connect to Minecraft server
bot = MinecraftBot(server_ip, server_port, username, password)

# Function to handle the event when the bot joins the server
def on_join():
    print("Bot has joined the server. Sending registration and login commands...")

    # Send the /register and /login commands automatically after joining
    bot.send_message("/register humqn52& humqn52&")
    bot.send_message("/register humqn52&")
    bot.send_message("/login humqn52&")

    # Send custom join message
    bot.send_message("Join: https://t.me/Hyper_Speed0")

    # Start random movement and jumping to prevent inactivity kick
    start_movement()

# Function to move and jump randomly
def start_movement():
    print("Starting movement to avoid inactivity kick...")

    while True:
        # Random movement and jumping
        move = random.choice(['forward', 'backward', 'left', 'right'])
        jump = random.choice([True, False])

        # Simulate movement (Note: Actual implementation requires server-side support)
        if move == 'forward':
            bot.send_message("Moving forward")
        elif move == 'backward':
            bot.send_message("Moving backward")
        elif move == 'left':
            bot.send_message("Moving left")
        elif move == 'right':
            bot.send_message("Moving right")

        if jump:
            bot.send_message("Jumping")

        # Wait a random time between actions
        time.sleep(random.randint(1, 5))

# Function to handle chat messages
def on_chat_message(sender, message):
    if message == "&leave":
        if sender == allowed_user:
            bot.send_message(f"{sender}, I'm leaving the server. Goodbye!")
            bot.disconnect()
            print("Bot has disconnected from the server.")
        else:
            bot.send_message(f"Sorry {sender}, only {allowed_user} can tell me to leave!")
            print(f"{sender} tried to make the bot leave, but they are not {allowed_user}.")

# Register event handlers
bot.on('join', on_join)
bot.on('chat', on_chat_message)

# Start the bot's connection
bot.connect()

# Keep the bot running
try:
    while True:
        bot.tick()  # Process events
except KeyboardInterrupt:
    bot.disconnect()
