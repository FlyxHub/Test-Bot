# Import required libraries
import discord
from discord.ext import commands
import random

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
    await ctx.send(f":ping_pong: *Pong!* Bot ping: {int(bot.latency*1000)} MS")
    return


# Rock Paper Scissors game
@bot.command()
async def rps(ctx, choice: str) -> None:
    choice = choice.lower()
    options = ["rock", "paper", "scissors"]

    botPick = random.choice(options)

    if choice not in options:
        await ctx.send("You must pick either rock, paper, or scissors.")
        return

    if choice == botPick:
        await ctx.send(f"**{botPick.title()}!** It's a tie!")
        return

    winConditions = {"rock": "scissors", "paper": "rock", "scissors": "paper"}

    if winConditions[choice] == botPick:
        await ctx.send(f"**{botPick.title()}!** You win!")
        return
    else:
        await ctx.send(f"**{botPick.title()}!** You lose!")
        return


# Error handler for rps command
@rps.error
async def rpsError(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("You must pick either rock, paper, or scissors.")
        return
    else:
        await ctx.send(f"An error occurred. Try again later.")
        return


# Run the bot after defining commands and listeners
bot.run(token=token)
