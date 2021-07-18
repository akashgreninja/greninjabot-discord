import discord
from discord.ext import commands
import giphy_client
from giphy_client.rest import ApiException
import random
import json

class advance(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	
	@commands.command(help="Gets info about the user")
	async def userinfo(self,ctx):
		user = ctx.author

		embed=discord.Embed(title="USER INFO",description=f"Here is the info we retrieved about {user}", colour=user.colour)
		embed.set_thumbnail(url=user.avatar_url)
		embed.add_field(name="NAME", value=user.name, inline=True)
		embed.add_field(name="NICKNAME", value=user.nick, inline=True)
		embed.add_field(name="ID", value=user.id, inline=True)
		embed.add_field(name="STATUS", value=user.status, inline=True)
		embed.add_field(name="TOP ROLE", value=user.top_role.name, inline=True)
		await ctx.send(embed=embed)

	@commands.command(help="Gets info about the user")
	async def memberinfo(self,ctx, member: discord.Member=None):
		if member == None:
			member =ctx.author
			try:
				embed=discord.Embed(title="USER INFO",description=f"Here is the info we retrieved about {user}", colour=user.colour)
				embed.set_thumbnail(url=user.avatar_url)
				embed.add_field(name="NAME", value=user.name, inline=True)
				embed.add_field(name="NICKNAME", value=user.nick, inline=True)
				embed.add_field(name="ID", value=user.id, inline=True)
				embed.add_field(name="STATUS", value=user.status, inline=True)
				embed.add_field(name="TOP ROLE", value=user.top_role.name, inline=True)
			except:
				await ctx.send(embed=embed)	


	@commands.command(help="gives a funny meme")
	async def gif(self,ctx,*,q="funny meme"):
		api_key="i5LNUs1AAmqop5JWZOYeszAlhP9ODtRI"
		api_instance = giphy_client.DefaultApi()
		try:
			api_response = api_instance.gifs_search_get(api_key,q,limit=5, rating='g')
			lst = list(api_response.data)
			giff = random.choice(lst)
			emb = discord.Embed(title=q)
			emb.set_image(url = f'https://media.giphy.com/media/{giff.id}/giphy.gif')
			await ctx.channel.send(ctx.author)
			await ctx.channel.send(embed=emb)
		except ApiException as e:
			print("Exception when calling DefaultApi->gifs_search_get: %s\n" % e)	
	
	@commands.command(help="GIVES A CUTE DOGGO PIC",aliases=['dog'])
	async def doggif(self,ctx,*,q="random golden retriever"):
		api_key="i5LNUs1AAmqop5JWZOYeszAlhP9ODtRI"
		api_instance = giphy_client.DefaultApi()
		try:
			api_response = api_instance.gifs_search_get(api_key,q,limit=5, rating='g')
			lst = list(api_response.data)
			giff = random.choice(lst)
			emb = discord.Embed(title=q)
			emb.set_image(url = f'https://media.giphy.com/media/{giff.id}/giphy.gif')
		
			await ctx.channel.send(embed=emb)
		except ApiException as e:
			print("Exception when calling DefaultApi->gifs_search_get: %s\n" % e)	

	@commands.command(help="GIVES A RANDOM PIC",aliases=['rand'])
	async def randomgif(self,ctx,*,q="random"):
		api_key="i5LNUs1AAmqop5JWZOYeszAlhP9ODtRI"
		api_instance = giphy_client.DefaultApi()
		try:
			api_response = api_instance.gifs_search_get(api_key,q,limit=10, rating='g')
			lst = list(api_response.data)
			giff = random.choice(lst)
			emb = discord.Embed(title=q)
			emb.set_image(url = f'https://media.giphy.com/media/{giff.id}/giphy.gif')
		
			await ctx.channel.send(embed=emb)
		except ApiException as e:

			
			print("Exception when calling DefaultApi->gifs_search_get: %s\n" % e)				

	@commands.command(help="use it to cheer someone")
	async def cheer(self,ctx,*,member: discord.Member,q="cheer"):
		api_key="i5LNUs1AAmqop5JWZOYeszAlhP9ODtRI"
		api_instance = giphy_client.DefaultApi()
		try:
			api_response = api_instance.gifs_search_get(api_key,q,limit=5, rating='g')
			lst = list(api_response.data)
			giff = random.choice(lst)
			emb = discord.Embed(title=q)
			emb.set_image(url = f'https://media.giphy.com/media/{giff.id}/giphy.gif')
			await ctx.channel.send( member.mention)
			await ctx.channel.send(embed=emb)
		except ApiException as e:
			print("Exception when calling DefaultApi->gifs_search_get: %s\n" % e)		


	@commands.command(help="funny animal pics")
	async def funnygif(self,ctx,*,q="funny animal pictures"):
		api_key="i5LNUs1AAmqop5JWZOYeszAlhP9ODtRI"
		api_instance = giphy_client.DefaultApi()
		try:
			api_response = api_instance.gifs_search_get(api_key,q,limit=5, rating='g')
			lst = list(api_response.data)
			giff = random.choice(lst)
			emb = discord.Embed(title=q)
			emb.set_image(url = f'https://media.giphy.com/media/{giff.id}/giphy.gif')
	
			await ctx.channel.send(embed=emb)
		except ApiException as e:
			print("Exception when calling DefaultApi->gifs_search_get: %s\n" % e)	
	
