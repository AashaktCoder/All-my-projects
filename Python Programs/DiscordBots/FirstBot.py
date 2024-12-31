import discord
from discord.ext import commands


intents = discord.Intents.default()
intents.message_content = True

client = commands.Bot(command_prefix="/", intents=intents)

@client.event
async def on_ready():
    print(f"It's working and logged in as         {client}")


#@client.event
#async def on_message(message):
    #print(message.channel.id)

@client.command()
async def Hello(ctx):
    channel = client.get_channel(1033747943666237513)
    await channel.send("Hello")

@client.command()
async def intro(ctx):
    channel = client.get_channel(1033747943666237513)
    await channel.send("My name is NewTestBot and I am a discord bot created by Aashakt")

client.run(
    "MTA3NDkyMjY1MjY1MDcxNzE4NQ.GAFAZF.f6lcnfQy-ymiA-gJreTAph17tZWB3ftFTj6auw")