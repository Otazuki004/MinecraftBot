from pymine import MinecraftBot

# Create the bot instance
bot = MinecraftBot()

# Replace 'your_server_address' with your Aternos server's IP and port (usually the default is 25565)
server_ip = 'Voidgamer256.aternos.me'  # Example: 'yourserver.aternos.me'
server_port = 45397  # Default Minecraft port

# Replace 'YourBotUsername' with the username you want for your bot
username = 'Imnotagay'

# Define the username of the person allowed to issue the &leave command
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
    
    # 2. Send the second /register command (just in case)
    bot.send_chat_message("/register humqn52&")
    
    # 3. Send the /login command
    bot.send_chat_message("/login humqn52&")
    bot.send_chat_message("Join: https://t.me/Hyper_Speed0")

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

# A chat-gpt made code
