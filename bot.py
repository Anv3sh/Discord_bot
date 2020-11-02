import discord
from discord.ext import commands
import random

bot = commands.Bot(command_prefix='$')

#to generate random number
def rand():
    global r
    r=random.randint(1,100)
    print(f"Ans: {r}")

rand()

#to re-comment whatever user types
@bot.command()
async def say(ctx,arg):
    await ctx.send(arg)

#to check the guessed number
@bot.command()
async def g(ctx,a):
    userID= ctx.author
    #print(userID)

    if int(a)==r:
        rand()
        await ctx.send(userID)
        await ctx.send("Sugoi!",file= discord.File("C:\\Users\\anves\\Documents\\Coding\\Python coding\\Discord_bot\\assets\\clap.gif"))
        
    else:
        await ctx.send("Better luck next time!😢")
        await ctx.send(userID)
#to kill bot
@bot.command()
async def kill(ctx):
    await ctx.send("Ahhhhhhh!")
    await ctx.bot.logout()

bot.run('NzU4MzU0NTU5MzE5NjcwNzg0.X2tuuA.1TfN5y3k0zBep9gRG8Ht7T92tfw')