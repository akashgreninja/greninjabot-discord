import os
import discord
from discord.ext import commands
from discord.ext.commands.core import has_guild_permissions
my_secret = os.environ['discord key']
import requests
import DiscordUtils

from keep_alive import keep_alive
from music import music
from intermediate import intermediate
from advance import advance
from admin import admin
from general import general

intents= discord.Intents.default()
intents.members=True
client = commands.Bot(command_prefix='&',intents=intents)






client.add_cog(music(client))
client.add_cog(general(client))
client.add_cog(intermediate(client))
client.add_cog(advance(client))
client.add_cog(admin(client))

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.idle, activity=discord.Game("TRYING TO FIT IN AMONG HUMANS"))
    print('we have logged in as{0.user}'.format(client))

	


@client.event
async def on_member_join(member):
	if member.guild.id==488038731270455298:

		await client.get_channel(488381691870576642).send(f'welcome to this server hope you enjoy your stay btw im better than the other bots in this server use &help for commands {member.mention} !  :star_struck: ')
		guildname=member.guild.name
		await member.send(f"hey welcome to {guildname} hope you enjoy your stay if you want me in your server reply back to this message or use &invite  {guildname}")

	elif member.guild.id==753868632848859138:
			
		await client.get_channel(753868633322815521).send(f'welcome to this server i am greninjaBot hope you enjoy your stay   {member.mention} ! use &help for available commands   :star_struck: ')
		await member.send(f"hey welcome to {guildname} hope you enjoy your stay if you want me in your server reply back to this message or use &invite  {guildname}")



keep_alive()
client.run(my_secret)



