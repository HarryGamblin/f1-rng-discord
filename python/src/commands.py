from google_sheets import user_in_sheet
from discord import Message

async def register_user(message: Message) -> None:
    if user_in_sheet(user=message.author):
        await message.channel.send(f"You are already a registered user in the sheet (Name: {message.author})")
        return

async def help(message: Message) -> None:
    channel = message.channel
    user = message.author
    help_message = f"""COMMANDS:\n
    register: Add yourself to the sheet if you are not already on it. Will retroactively generate results for past races.\n
    leaderboard: Get the current rankings for the season.
    help: Show all available commands."""
    await channel.send(help_message)
    return
