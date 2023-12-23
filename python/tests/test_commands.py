import pytest
import discord
import src.commands as commands


class MockMessage(discord.Message):
    def __init__(self) -> None:
        self.author = "test_author"


def test_register_not_in_sheet(mocker):
    mocker.patch("discord.Message")

    commands.register_user(message=MockMessage())
