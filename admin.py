import discord
from discord.ext import commands
from discord.ext.commands.core import has_guild_permissions


class admin(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	

	@commands.command(help="Mutes the specified user.")
	@commands.has_permissions(manage_messages=True)
	async def mute(self,ctx, member: discord.Member, *, reason=None):
		guild = ctx.guild
		mutedRole = discord.utils.get(guild.roles, name="Muted")

		if not mutedRole:
			mutedRole = await guild.create_role(name="Muted")

			for channel in guild.channels:
				await channel.set_permissions(mutedRole, speak=False, send_messages=False, read_message_history=True, read_messages=False)

		await member.add_roles(mutedRole, reason=reason)
		await ctx.send(f"Muted {member.mention} for reason {reason}")
		await member.send(f"You were muted in the server {guild.name} for {reason}")

	@commands.command(help="Unmutes a specified user.")
	@commands.has_permissions(manage_messages=True)
	async def unmute(self,ctx, member: discord.Member):
		mutedRole = discord.utils.get(ctx.guild.roles, name="Muted")

		await member.remove_roles(mutedRole)
		await ctx.send(f"Unmuted {member.mention}")
		await member.send(f"You were unmuted in the server {ctx.guild.name}")

	@commands.command(help="Bans a member")
	@commands.has_permissions(ban_members=True)
	async def ban(self,ctx, member: discord.Member, *, reason=None):
		await member.ban(reason=reason)
		await ctx.send(f"{member} was banned!")	

	@commands.command(help="Unbans a member")
	@commands.has_permissions(ban_members=True)
	async def unban(self,ctx, *, member):
		bannedUsers = await ctx.guild.bans()
		name, discriminator = member.split("#")

		for ban in bannedUsers:
				user = ban.user

				if(user.name, user.discriminator) == (name, discriminator):
						await ctx.guild.unban(user)
						await ctx.send(f"{user.mention} was unbanned.")
						return	


		

		
