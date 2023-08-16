from discord.ext import commands
import discord
import json
import asyncio

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!',
                   intents=discord.Intents.all())

with open('json1.json', "r", encoding="utf8") as file:
    data = json.load(file)

@bot.event
async def on_ready():
    print("Bot is ready")

@bot.command()
async def pray(ctx):
    await ctx.send(data['pray'])

@bot.command()
async def image(ctx):
    await ctx.send(file=discord.File(data['image']))

@bot.command(
    name='vuvuzela',
    description='Plays an awful vuvuzela in the voice channel',
    pass_context=True,
)
async def vuvuzela(context):
    user = context.message.author
    voice_channel = user.voice.channel

    if voice_channel is not None:
        vc = await voice_channel.connect()
        vc.play(discord.FFmpegPCMAudio(executable="ffmpeg", source=data['vuvuzela.mp3']))
        while vc.is_playing():
            await asyncio.sleep(1)
        await vc.disconnect()
    else:
        await context.send('User is not in a channel.')

bot.run(data['token'])
