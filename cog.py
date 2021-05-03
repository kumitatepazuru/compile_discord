import os
import subprocess

from discord.ext import commands

from lib import new_dir, process_output


class Cog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=["cep"])
    async def compile_python(self, ctx, *, args):
        d = new_dir()
        with open(d + "/main.py", "w") as f:
            f.write(args)
        cmd = ["timeout","-k","2","10","docker", "run", "--rm", "-v", os.getcwd() + "/" + d + ":" + "/usr/src/myapp", "-w", "/usr/src/myapp",
               "python:3.6.4", "python",
               "main.py"]
        p = subprocess.Popen(cmd,
                             stdout=subprocess.PIPE,
                             stderr=subprocess.STDOUT)
        m = await ctx.send("compiler")
        _ = await process_output(p, m, "", ctx)


def setup(bot):
    bot.add_cog(Cog(bot))
