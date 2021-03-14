import os
import sys
import typing
import discord
from discord.ext import commands
import random
import time
from dotenv import load_dotenv
from textgenrnn import textgenrnn
import asyncio

if len(sys.argv) != 2:
    print("Usage:")
    print("python3 bot.py <TOKEN-NAME>")
    exit()

nn = textgenrnn('./weights/loverboy.hdf5')
load_dotenv('./.env')
TOKEN = str(os.getenv(str(sys.argv[1])))
GUILD = str(os.getenv('DISCORD_GUILD'))

intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix="#", intents=intents)
bot.remove_command("help")

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

class Greetings(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._cd = commands.CooldownMapping.from_cooldown(1, 10, commands.BucketType.member) # Change accordingly
                                                        # rate, per, BucketType

    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = member.guild.system_channel
        if channel is not None:
            await channel.send('forsooth {0.mention}! I bite my thumb at thee >:('.format(member))

    def get_ratelimit(self, message: discord.Message) -> typing.Optional[int]:
        """Returns the ratelimit left"""
        bucket = self._cd.get_bucket(message)
        return bucket.update_rate_limit()

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author != bot.user:
            # Getting the ratelimit left
            ratelimit = self.get_ratelimit(message)
            if ratelimit is None:
                luck = random.randint(0, 10)
                if luck > 9:
                    to_send = ('Forsooth {0.mention}!'.format(message.author))
                    await message.channel.send(str(to_send))
                else:
                    to_gen = random.randint(1, 5)
                    for i in range(0, to_gen):
                        to_send = nn.generate(return_as_list=True, max_gen_length=300)[0]
                        await message.channel.send(str(to_send))
                # to_send = nn.generate(return_as_list=True, max_gen_length=300)[0]
                # await message.channel.send(str(to_send))
                print('not-ratelimited')
            else:
                # The user is ratelimited
                print('ratelimited')
            
bot.add_cog(Greetings(bot))
bot.run(TOKEN)
