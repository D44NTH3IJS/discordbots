import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio


TOKEN = 'TOKEN HERE!!'

bot = commands.Bot(command_prefix = '#')


@bot.event
async def on_ready():
    print ('Your are using version PROTOTYPE')
    print ('You are using the ' + bot.user.name)
    print ('With the ID:' + bot.user.id)
    
#Help command
@bot.command(pass_context=True)
async def showhelp(ctx):
    await bot.say("#showhelp - help command")
    await bot.say("#ping - funny command")
    await bot.say("#info - shows your player info")
    await bot.say("#kick @player - kicks the player")
    print ("User used command help")

#PingPong Command

@bot.command(pass_context=True)
async def ping(ctx):
    await bot.say(":ping_pong: pong!")
    print ("user has pinged")

#info command

@bot.command(pass_context=True)
async def info(ctx, user: discord.Member):
    await bot.say("The users name is: {}".format(user.name))
    await bot.say("The users ID is: {}".format(user.id))
    await bot.say("The users status is: {}".format(user.status))
    await bot.say("The users highest role is: {}".format(user.top_role))
    await bot.say("The user joined at: {}".format(user.joined_at))

#kick command 

@bot.command(pass_context=True)
async def kick(ctx, user: discord.Member):
    await bot.say(":boot: Cya, {}. Ya loser!".format(user.name))
    await bot.kick(user)


bot.run(TOKEN)
