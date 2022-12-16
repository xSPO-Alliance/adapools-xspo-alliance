#!/usr/bin/env python

import discord
from discord.ext import commands, tasks
import random
import sys

_user = sys.argv[1]
_token = sys.argv[2]

ver_code = ''.join((random.choice('xSPOAdisc') for i in range(9)))
print(ver_code)

bot = commands.Bot(
    intents=discord.Intents.all() ,
    command_prefix='/' ,
    description='Registration verification code'
    )

@bot.command()
async def code(ctx):
    
    ver_author=str(ctx.author)
    if ver_author == _user:
        try:
            ver_code_from_author=str(ctx.message.content).split(" ")[1]
            if ver_code == ver_code_from_author:
                await ctx.send(ver_author)
                await ctx.send("Code verified successfully")
                exit()
            else:
                await ctx.send(ver_author)
                await ctx.send("Wrong code: " + ver_code_from_author)
                exit(-1)

        except Exception:
            exit(-1)

bot.run(_token)
