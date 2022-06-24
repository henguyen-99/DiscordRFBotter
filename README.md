# DiscordRFBotter

Personal general use Discord bot.

## General features:

This bot includes a few commands that provide some convenient uses and other fun features. All commands begin with an exclamation point (!) followed by the command itself.

### Parrot (!parrot):

First command created to test out bot functionality. This command makes the bot repeat any phrase (string) it is given and then follows up on the repeat by reacting to the original command with an emote.

### YouTube Video Search (!yt):

This command takes in a search query (string) and uses this to search for and return a link to the most relevant YouTube video related to the query. This is done via an HTTP request to YouTube, passing in the search query in the request. A regular expression is then used in order to find unique video IDs which all follow a format of 11 characters. This forms a list of videos that can be shown, and the first video ID in the list tends to belong to the most relevant video, so the ID of the video is used to form the final link that is sent back to the server by the bot.

### Minecraft Server Status (!mcstatus):

This command checks the status of a Minecraft server. In this case, it is directed to my own server. Running the command returns important information regarding the server such as number of players online, the latency of the server, and, if there are any players online, the list of players that are currently in the server.

### Roblox Random Game Finder (!randblox):

This command searches for a random game to join on Roblox. Each game on Roblox contains a 10-digit integer ID, so a random 10-digit ID is created and then passed into an HTTP request to Roblox. The result of the HTTP request may either return a status code of 200 indicating that the ID is valid and there exists a game with this generated ID, or a status code of 404 is returned, meaning the generated ID is not valid. In the case that the ID is not valid, a new ID is continuously generated and tested until a status code 200 is returned, where a link to the game is finally sent back to the server by the bot.

# Cogs

Extensions that implement further commands that are more in common.

## Toontown Rewritten (TTR)

This cog implements some commands that are relevant to Toontown Rewritten, or TTR.

### Population Check (!ttrpop):

This command checks the current population of Toontown Rewritten, or in other words, the number of players online in the game. This command is performed by making an HTTP request to TTR's [population API](https://www.toontownrewritten.com/api/population) and then parsing the returned JSON for the bot to display information such as the total population as well as population by district. This command may take in district names in order to display the populations of just the specified districts.


### Invasion Check (!ttrinvasions):

This command checks on the current invasions in progress in Toontown Rewritten, which are limited-time events where specific enemies are roaming the world of Toontown. This command is performed by making an HTTP request to TTR's [invasion API](https://www.toontownrewritten.com/api/invasions) and then parsing the returned JSON for the bot to display information such as the district being invaded, what cog is invading that district, and the current progress of the invasion.