from discord import (
    client,
    Member,
    Message,
    User,
)

def user_in_sheet(
        client: client,
        user: Message.author) -> bool:
    for user_type in (Member, User):
        if isinstance(user, user_type):
            name = user.name
            break
        print(f"ERROR: Could not determine user type.")
    pass