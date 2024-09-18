import random
import time
from pymine import MinecraftBot

# Create the bot instance
bot = MinecraftBot()

# Server details
server_ip = 'Voidgamer256.aternos.me'  # Aternos server address
server_port = 45397  # Server port

# Bot's Minecraft username
username = 'Imnotagay'

# Allowed user for the &leave command
allowed_user = "OtazukiHS"

# Connect the bot to the Aternos server
bot.connect(server_ip, port=server_port, username=username)

# Function to handle the event when the bot joins the server
@bot.on('join')
def on_join():
    # Send the /register and /login commands automatically after joining
    print("Bot has joined the server. Sending registration and login commands...")
    
    # 1. Send the first /register command
    bot.send_chat_message("/register humqn52& humqn52&")
    
    # 2. Send the second /register command
    bot.send_chat_message("/register humqn52&")
    
    # 3. Send the /login command
    bot.send_chat_message("/login humqn52&")
    
    # 4. Send custom join message
    bot.send_chat_message("Join: https://t.me/Hyper_Speed0")
    
    # Start moving and jumping randomly to avoid inactivity kick
    start_movement()

# Function to move and jump randomly to avoid inactivity
def start_movement():
    print("Starting movement to avoid inactivity kick...")
    
    while True:
        # Randomly choose a movement direction and action
        movement = random.choice(['forward', 'backward', 'left', 'right'])
        jump = random.choice([True, False])
        
        # Move the bot
        if movement == 'forward':
            bot.move_forward()
        elif movement == 'backward':
            bot.move_backward()
        elif movement == 'left':
            bot.move_left()
        elif movement == 'right':
            bot.move_right()
        
        # Optionally jump
        if jump:
            bot.jump()
        
        # Wait a random time between movements (1 to 5 seconds)
        time.sleep(random.randint(1, 5))
        
        # Stop moving after a short random time (to simulate natural movement)
        time.sleep(random.uniform(0.5, 1.5))
        bot.stop()

# Function to handle chat messages
@bot.on('chat')
def handle_chat(sender, message):
    # Print incoming chat messages (for debugging or logging)
    print(f"[CHAT] {sender}: {message}")
    
    # Check if the message is the command '&leave'
    if message == "&leave":
        # Check if the sender is the allowed user (OtazukiHS)
        if sender == allowed_user:
            # Send a message to let everyone know the bot is leaving
            bot.send_chat_message(f"{sender}, I'm leaving the server. Goodbye!")
            
            # Disconnect the bot from the server
            bot.disconnect()
            print("Bot has disconnected from the server.")
        else:
            # If someone else tries to issue the command, ignore it or send a message
            bot.send_chat_message(f"Sorry {sender}, only {allowed_user} can tell me to leave!")
            print(f"{sender} tried to make the bot leave, but they are not {allowed_user}.")

# Start the bot's event loop
bot.start()
