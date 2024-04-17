import discord
import responses
import opkeys
from discord.ext import commands
import time

dick = {
'Q': 0x10,
'W': 0x11,
'E': 0x12,
'R': 0x13,
'T': 0x14,
'Y': 0x15,
'U': 0x16,
'I': 0x17,
'O': 0x18,
'P': 0x19,
'A': 0x1E,
'S': 0x1F,
'D': 0x20,
'F': 0x21,
'G': 0x22,
'H': 0x23,
'J': 0x24,
'K': 0x25,
'L': 0x26,
'Z': 0x2C,
'X': 0x2D,
'C': 0x2E,
'V': 0x2F,
'B': 0x30,
'N': 0x31,
'M': 0x32,
'Й': 0x10,
'Ц': 0x11,
'У': 0x12,
'К': 0x13,
'Е': 0x14,
'Н': 0x15,
'Г': 0x16,
'Ш': 0x17,
'Щ': 0x18,
'З': 0x19,
'Х': 0xDB,
'Ф': 0x1E,
'Ы': 0x1F,
'В': 0x20,
'А': 0x21,
'П': 0x22,
'Р': 0x23,
'О': 0x24,
'Л': 0x25,
'Д': 0x26,
'Ж': 0xBA,
'Э': 0x28,
'Я': 0x2C,
'Ч': 0x2D,
'С': 0x2E,
'М': 0x2F,
'И': 0x30,
'Т': 0x31,
'Ь': 0x32,
'Б': 0X33,
'Ю': 0x34,
'Х': 0x1A,
' ': 0x39,
}

async def send_message(message, user_message, is_private):
    try:
        response = responses.handle_response(user_message)
        await message.author.send(response) if is_private else await message.channel.send(response)

    except Exception as e:
        print(e)


def run_discord_bot():
    TOKEN = # Вставить свой токен
    client = discord.Client(intents = discord.Intents().all())

    @client.event
    async def on_ready():
        print(f'{client.user} is now running!')

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return

        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)

        print(f"{user_message}")
        time.sleep(5)
        for i in user_message:
            opkeys.HoldAndReleaseKey(dick[i.upper()],.0001)

    client.run(TOKEN)