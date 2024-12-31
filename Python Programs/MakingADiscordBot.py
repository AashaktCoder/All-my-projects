import discord
from discord.ext import commands

client = discord.Client(intents=discord.Intents.default())

intents = discord.Intents.default()
intents.message_content = True
bot= commands.Bot(command_prefix="--",case_insensitive=True,intents=intents)
bot.remove_command("help")

@client.event
async def on_ready():
    print(f"It's working and logged in as         {client}")


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith("/Hello"):
        await message.channel.send("Hello, How are you")


client.run(
    "MTAzMzc0ODkwNzM4NzI3NzM3Mg.GDC52g.xXjjAx_vVs-5xMmA35O13Hh2rNacKa7vR36S00")