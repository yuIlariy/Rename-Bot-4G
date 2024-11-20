from pyrogram import Client, idle
from plugins.cb_data import app as Client2
from config import *
import pyromod
import pyrogram.utils
from pyrogram.errors import SessionRevoked, AuthKeyInvalid  # Import necessary exceptions

# Update Pyrogram minimum chat and channel ID values
pyrogram.utils.MIN_CHAT_ID = -999999999999
pyrogram.utils.MIN_CHANNEL_ID = -100999999999999

# Create bot client
bot = Client("Renamer", bot_token=BOT_TOKEN, api_id=API_ID, api_hash=API_HASH, plugins=dict(root='plugins'))

if STRING_SESSION:
    try:
        # Initialize both clients
        apps = [Client2, bot]
        for app in apps:
            app.start()
        print("Bot and additional client started successfully!")

        # Keep the bot idle
        idle()

    except (SessionRevoked, AuthKeyInvalid) as e:
        # Handle session revocation or invalidation errors
        print(f"Error: {e}. The session has been revoked or is invalid.")
        print("Please generate a new session string to continue.")
        
        # Optionally, log the error or notify the owner (e.g., via Telegram)

    finally:
        # Stop all clients gracefully
        for app in apps:
            app.stop()
        print("Clients stopped.")

else:
    # If no STRING_SESSION, only run the bot
    bot.run()
