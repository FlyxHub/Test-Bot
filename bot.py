# Import required libraries
import discord
from discord.ext import commands

# Read token from ./token.txt
with open("token.txt", "r") as tokenFile:
    token = tokenFile.read()
tokenFile.close()

# Initialize bot
bot = commands.Bot(command_prefix=".", intents=discord.Intents.all())


# Print to console when bot successfully logs in
@bot.event
async def on_ready() -> None:
    print(f"Bot ready! Logged in as {bot.user}")
    return


# Simple "Hello world" command
@bot.command()
async def hello(ctx) -> None:
    await ctx.send("Hello world!")
    return


# Command to tell the user who they are
@bot.command()
async def whoami(ctx) -> None:
    await ctx.send(f"You are {ctx.author.mention}")
    return


# Command to display bot latency
@bot.command()
async def ping(ctx) -> None:
    await ctx.send(f":ping_pong: *Pong!* Bot ping: {bot.latency*1000} MS")
    return


# Run the bot after defining commands and listeners
bot.run(token=token)
