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

if client.user in message.mentions:
    reply = f'{message.author.mention} https://tenor.com/view/honda-keisuke-keisuke-honda-thumbs-up-thumbs-gif-5622287'
    await message.channel.send(reply)
    
    
bot.run(token)


