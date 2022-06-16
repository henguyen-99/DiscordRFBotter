import discord
import json
from discord.ext import commands
from urllib import request

class TTR(commands.Cog):

    # Constructor for class of commands related to Toontown Rewritten
    def __init__(self, client):
        self.client = client
    
    # Uses TTR's population API to get the current amount of TTR players online
    @commands.command()
    async def ttrpop(self, ctx):
        ttrResp = request.urlopen("https://www.toontownrewritten.com/api/population")
        ttrPop = ttrResp.read().decode()
        ttrPop = json.loads(ttrPop)
        await ctx.message.channel.send(f'Current TTR population: **{ttrPop["totalPopulation"]}**')

    # Uses TTR's invasion API to get current invasion data, specifically what cogs are invading and invasion progress
    @commands.command()
    async def ttrinvasions(self, ctx):
        ttrResp = request.urlopen("https://www.toontownrewritten.com/api/invasions")
        ttrInv = ttrResp.read().decode()
        ttrInv = json.loads(ttrInv)
        if ttrInv["error"] is None:
            invasionData = ""
            invasionList = ttrInv["invasions"]
            for key in ttrInv["invasions"].keys():
                invaded = f"**{invasionList[key]['type']}** at progress **{invasionList[key]['progress']}**\n"
                invasionData += invaded
            
            await ctx.message.channel.send(f'Current invasions:\n{invasionData}')
        
        else:
            await ctx.message.channel.send(f'TTR invasion API responded with an error: {ttrInv["error"]}')

    
def setup(client):
    client.add_cog(TTR(client))