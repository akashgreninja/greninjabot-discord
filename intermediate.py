import discord
from discord.ext import commands
from discord.ext.commands.core import has_guild_permissions
import json
import asyncio

class intermediate(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	@commands.command()
	async def poll(self,ctx,*,message):
		emb=discord.Embed(title="POLL",description=f"{message}",colour=discord.Colour.red())
		msg=await ctx.channel.send(embed=emb)
		await msg.add_reaction('👍')
		await msg.add_reaction('👎')
	
	@commands.command(help='REMOVES SPECIFIC NUMBER OF MESSAGES USE &clear<no of messages>')
	@commands.has_permissions(manage_messages=True)
	async def clear(self,ctx,amount=int()):
		await ctx.channel.purge(limit=amount+1)
		await ctx.send('Messages has been removed!',delete_after=5)

	





	def get_yomamma():
		response = requests.get("https://api.yomomma.info/")
		json_data = json.loads(response.text)
		picture = json_data
		return (picture)


	@commands.command()
	async def yomamma(self,ctx,member:discord.Member): 
		yomamma = get_yomamma()
		await ctx.send(member.mention + format (str(yomamma)))




	@commands.command(brief="Random picture of a woof")
	async def dogpic(self, ctx):
		async with ctx.channel.typing():
				async with aiohttp.ClientSession() as cs:
					async with cs.get("https://random.dog/woof.json") as r:
						data = await r.json()

						embed = discord.Embed(title="Woof")
						embed.set_image(url=data['url'])
						embed.set_footer(text="http://random.dog/")
						await ctx.send(embed=embed)		