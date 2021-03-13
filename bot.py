# bot.py
import os
import discord
from dotenv import load_dotenv
# from textgenrnn import textgenrnn
# nn = textgenrnn()

load_dotenv('./.env')
TOKEN = str(os.getenv('DISCORD_TOKEN'))
GUILD = str(os.getenv('DISCORD_GUILD'))

intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')

@client.event
async def on_member_join(member):
    await member.send("forsooth! i bite my thumb at thee >:(")


# <Message id=820288228758257745 channel=<TextChannel id=820275546692517901 name='general' position=0 nsfw=False news=False category_id=820275546692517899> type=<MessageType.default: 0> author=<Member id=622143275796660235 name='HWIW' discriminator='8724' bot=False nick=None guild=<Guild id=820275546692517898 name='Shakespeare Roleplay Bot Test Server' shard_id=None chunked=True member_count=5>> flags=<MessageFlags value=0>>

@client.event
async def on_message(message):
    # print(message.author)
    # to_send = nn.generate()
    if message.author != client.user:
        await message.channel.send("forsooth! i hath taken thy message and i readeth")
        # await message.channel.send(str(to_send))
    

client.run(TOKEN)
