import discord
from google_sheets import user_in_sheet
from constants import (
    BOT_NAME,
    DISCORD_TOKEN,
    MESSAGE_PREFIX,
    CommandNames,
)
from datetime import datetime
from commands import help

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready() -> None:
    print(f"Logged in as {client.user}")

@client.event
async def on_message(message: discord.Message) -> None:
    if message.author.name == BOT_NAME or message.content.startswith(MESSAGE_PREFIX) is False: return
    raw_message = message.content.removeprefix(MESSAGE_PREFIX).lstrip()
    if raw_message == "help":
        await help(message)
    if raw_message in CommandNames:
        await message.channel.send("Could not recognise command. Use 'f1-rng help' to get all available commands.")
        return

client.run(DISCORD_TOKEN)