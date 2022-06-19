import discord
from discord.ext import commands
import os
import re
from urllib import request, parse
from mcstatus import JavaServer

client = commands.Bot(command_prefix = '!')

# Runs when bot is up and running
@client.event
async def on_ready():
  print(f'Successful log in as {client.user}')

# Runs when there is an error caught while executing a command
@client.event
async def on_command_error(ctx, error):

  # If a command is given with insufficient arguments, send message notifying user
  if isinstance(error, commands.MissingRequiredArgument):
    await ctx.send('Missing parameters! Make sure all parameters are given.')
    
  # If the given command is not valid, send message notifying user.
  elif isinstance(error, commands.CommandNotFound):
    await ctx.send('Not a valid command! Please check your input command.')

# Load cogs to activate types of commands
@client.command()
async def load(ctx, extension):
  client.load_extension(f'cogs.{extension}')
  await ctx.send(f'Loaded cog extension {extension}!')

# Unloads cogs to deactivate types of commands
@client.command()
async def unload(ctx, extension):
  client.unload_extension(f'cogs.{extension}')
  await ctx.send(f'Unloaded cog extension {extension}!')

@client.command()
async def reload(ctx, extension):
  client.unload_extension(f'cogs.{extension}')
  client.load_extension(f'cogs.{extension}')
  await ctx.send(f'Reloaded cog extension {extension}!')

# "Parrots" back whatever arguments were given as well as reacting to the original command with an emoji.
@client.command()
async def parrot(ctx, *, phrase):
  await ctx.send(phrase)
  emoji = "\U0001f60e"
  await ctx.message.add_reaction(emoji)

# Search for YouTube videos
# Link to first YouTube video is returned
@client.command()
async def yt(ctx, *, search):
  query = parse.quote_plus(search)
  YTSearch = request.urlopen(f'https://www.youtube.com/results?search_query={query}')
  await ctx.send(f'Finding a YouTube video of {search}...')
  vidIDs = re.findall(r"watch\?v=(\S{11})", YTSearch.read().decode())
  video_link = f'https://www.youtube.com/watch?v={vidIDs[0]}'
  await ctx.send(video_link)

# Check local Minecraft server status
# Detects whether the server is online
# and provides basic server information
# including player count, latency, and player list.
@client.command()
async def mcstatus(ctx):
  try:
    server = JavaServer.lookup('localhost')
    status = server.status()

  except Exception as e:
    print("Exception caught:")
    print(e)
    await ctx.send("Unable to connect to MC server! Server is offline or otherwise unable to be reached.")
    return

  await ctx.send(f'Server has {status.players.online} players and replied in {status.latency} ms.')
  if status.players.online > 0:
    usersConnected = [ user['name'] for user in status.raw['players']['sample'] ]
    await ctx.send(f"Players online: {usersConnected}")

# Function runs upon any message being sent to the server
@client.event
async def on_message(message):
  if message.author == client.user:
    return
  
  else:
    print(f'Message received from {message.author}')

  await client.process_commands(message)

if __name__ == '__main__':
  for f in os.listdir('./cogs'):
    if f.endswith('.py'):
      client.load_extension(f'cogs.{f[:-3]}')

  client.run(os.getenv('TOKEN'))