from discord.ext import commands
import os
import traceback

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']


@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)


@bot.command()
async def ping(ctx):
    await ctx.send('pong')
    
@bot.command()
async def おはよう(ctx):
    await ctx.send('おっはー！')         

bot.run(token)

global voich
# 接続
if message.content.startswith('/connect'):
    voich = await discord.VoiceChannel.connect(message.author.voice.channel)
# 切断
if message.content.startswith('/discon'):
    await voich.disconnect()
    
    
