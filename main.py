import os
import discord
from discord.ext import commands


token = os.environ['token']
client = commands.Bot(command_prefix=".",  status=discord.Status.idle, activity = discord.Activity(type=discord.ActivityType.watching, name=";)"), intents=discord.Intents.all())

@client.event
async def on_ready():
  print(f'Logged in as {client.user} (ID: {client.user.id})')

@client.command()
async def l(ctx):
  await ctx.send('Someone you know has requested for this bot to raid your server, have fun')
  await ctx.send('Raided')
  await ctx.send('Raided')
  await ctx.send('Raided')
  await ctx.send('Raided')
  await ctx.send('Raided')
  await ctx.send('Raided')
  await ctx.send('Raided')
  await ctx.send('Raided')
  await ctx.send('Raided')
  await ctx.send('Raided')
  await ctx.send('Raided')
  await ctx.send('Raided')
  await ctx.send('Raided')
  await ctx.send('Raided')
  await ctx.send('Raided')
  await ctx.send('Raided')
  await ctx.send('Raided')
  await ctx.send('Raided')
  await ctx.send('Raided')
  await ctx.send('Raided')
  await ctx.send('Raided')
  await ctx.send('Raided')
  await ctx.send('Raided')
  await ctx.send('Raided')
  await ctx.send('Raided')
  await ctx.send('Raided')
  await ctx.send('Raided')
  await ctx.send('Raided')
  await ctx.send('Raided')
  await ctx.send('Raided')
  await ctx.send('Raided')
  await ctx.send('Raided')
  await ctx.send('Raided')
  await ctx.send('Raided')
  await ctx.send('Raided')
  await ctx.send('Raided')
  await ctx.send('Raided')
  await ctx.send('Raided')
  await ctx.send('Raided')
  await ctx.send('Raided')
  await ctx.send('Raided')
  await ctx.send('Raided')
  await ctx.send('Raided')
  await ctx.send('Raided')
  await ctx.send('Raided')
  await ctx.send('Raided')
  await ctx.send('Raided')
  await ctx.send('Raided')
  await ctx.send('Raided')
  await ctx.send('Raided')
  print('raid completed')
  
client.run(token)
