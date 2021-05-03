import os
import random

import discord
import string


def randomname(n):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=n))


async def process_output(p, m, msg, ctx):
    embed = discord.Embed()
    embed.add_field(name="compile & run your program", value="loading...")
    await m.edit(embed=embed)
    for line in iter(p.stdout.readline, b''):
        embed.clear_fields()
        msg += line.rstrip().decode("utf-8") + "\n"
        try:
            embed.add_field(name="compile & run your program", value=msg)
            await m.edit(embed=embed)
        except discord.errors.HTTPException:
            msg = msg.splitlines()[-1]
            embed = discord.Embed()
            embed.add_field(name="compile & run your program", value=msg)
            m = await ctx.send(embed=embed)
    p.communicate()
    embed = discord.Embed()
    embed.add_field(name="returncode",value=p.returncode)
    await ctx.send(embed=embed)
    return msg, m


def new_dir():
    name = ""
    ok = False
    while not ok:
        name = randomname(16)
        ok = not os.path.isdir("./env/"+name)
    os.mkdir("env/"+name)
    return "./env/"+name
