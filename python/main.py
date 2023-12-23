import discord
from google_sheets import user_in_sheet
from constants import MESSAGE_PREFIX

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f"Logged in as {client.user}")

@client.event
async def on_message(message: discord.Message) -> None:
    if not message.content.startswith(MESSAGE_PREFIX):
        pass
    if not user_in_sheet(client=client, user=message.author):
        print("User not found in sheet. Adding now.")
