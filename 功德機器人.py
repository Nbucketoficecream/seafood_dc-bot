# coding: utf-8

from discord.ext import commands
import discord
import json
import asyncio
intents = discord.Intents.default()
intents.message_content = True
intents.voice_states = True
bot = commands.Bot(command_prefix='!',
                   intents=discord.Intents.all())

with open('json1.json', "r", encoding="utf8") as file:
    data = json.load(file)
seafood=data["monk"]
@bot.event
async def on_ready():
    print("Bot is ready")
    game = discord.Game(data["now"])  
    await bot.change_presence(status=discord.Status.idle, activity=game)
@bot.command()
async def pray(ctx):
    await ctx.send(data['pray'])
@bot.command()
async def monk(ctx):
      await ctx.send(f"<@{447739348473872384}> %s"%seafood)
@bot.command()
async def image(ctx):
    await ctx.send(file=discord.File(data['image']))
@bot.command()
async def play(ctx):
    if ctx.author.voice and ctx.author.voice.channel:
        voice_channel = ctx.author.voice.channel
        voice_client = await voice_channel.connect()    
        voice_client.play(discord.FFmpegPCMAudio(data["wood.mp3"]))
        while voice_client.is_playing():
            await asyncio.sleep(1)
        await voice_client.disconnect()
        await ctx.send(data["gon"])
    else:
        await ctx.send(data["gon2"])


bot.run(data['token'])
