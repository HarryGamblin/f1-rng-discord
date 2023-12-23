import pytest
import discord
import main


class MockMessage(discord.Message):
    def __init__(self) -> None:
        pass


def test_not_in_sheet(mocker):
    mocker.patch("discord.Message")
    mocker.patch("discord.Client")

    main.on_message(message=MockMessage())
