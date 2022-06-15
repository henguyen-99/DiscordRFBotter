import discord
import json
from discord.ext import commands
from urllib import request

class TTR(commands.Cog):

    def __init__(self, client):
        self.client = client
    
    @commands.command()
    async def ttrpop(self, ctx):
        ttrResp = request.urlopen("https://www.toontownrewritten.com/api/population")
        ttrPop = ttrResp.read().decode()
        ttrPop = json.loads(ttrPop)
        await ctx.message.channel.send(f'Current TTR population: {ttrPop["totalPopulation"]}')
    
def setup(client):
    client.add_cog(TTR(client))