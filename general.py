import discord
from discord.ext import commands
import datetime
import time
import random

today = datetime.datetime.now()
date_time = today.strftime("%m/%d/%Y, %H:%M:%S")

class general(commands.Cog):
	def __init__(self, bot):
		self.bot = bot




	@commands.command(help = 'the bot code')
	async def code(self,ctx):
		await ctx.send('**GUYS FEEL FREE TO USE MY CODE WOULD APPRICIATE IF YOU DONT DELETE THE &creator COMMAND ** https://github.com/akashgreninja/DISCORD')

	@commands.command(help = 'want a bot for yourself?')
	async def free(self,ctx):
		await ctx.send('** WANT A CUSTOM BOT FOR FREE WITH YOUR SERVER NAME DM ME OR John Wick#9788 ON DISCORD** ')	

	
	@commands.command(help = ' time')
	async def time(self,ctx):
		await ctx.send(date_time)


	@commands.command(help = ' date')
	async def date(self,ctx):
		await ctx.send(date_time)

	@commands.command(help = 'are you sus')	
	async def sus(self,ctx,*,member:discord.Member):
		responses=[' was a imposter',
          ' was not a imposter',
					' was ejected']
		await ctx.send(f'{member.mention} {random.choice(responses)}')				





	@commands.command(help = 'want to become a tester')
	async def tester(self,ctx):
  		await ctx.send('WANT TO TEST THIS BOT DM John Wick#9788 ON DISCORD HE WILL ADD YOU')	



	@commands.command(help = 'greets you')
	async def heybot(self,ctx):
  		await ctx.send('**hey human nice to have you here**')	
        

	
	@commands.command(help = 'tells whats new')
	async def new(self,ctx):
  		await ctx.send('  &clear use &help to see what they do ')



	@commands.command(help = 'who made me')
	async def creator(self,ctx):
  		await ctx.send(' Made by akash uday  \n Still improving it  \n made  using python,replit.com  \n')	



	@commands.command(help = 'WANT TO INVITE ME TO YOUR SERVER??')
	async def invite(self,ctx):
		await ctx.send('https://discord.com/api/oauth2/authorize?client_id=846282882716663820&permissions=4294441975&scope=bot  ')
		await ctx.send( 'IF YOU WANT 100% ACCESS TO ALL THE COMMANDS THEN USE THE BELOW LINK ⏬⏬')
		await ctx.send('https://discord.com/api/oauth2/authorize?client_id=846282882716663820&permissions=8&scope=bot')

	
	@commands.command(help= 'sends the bot display picture')
	async def dp(self,ctx):
		await ctx.send(file=discord.File('GRENINJA BOT ori.jpg'))



	@commands.command(help = 'website still under development')
	async def website(self,ctx):
		await ctx.send('https://sites.google.com/view/greninjabot/home')	




