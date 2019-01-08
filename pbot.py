import random
from discord.ext.commands import Bot
from discord import Game
from random import randint
from discord import Member
import os
import asyncio


TOKEN = os.environ['token']
BOT_PREFIX = "^^"
client = Bot(command_prefix = BOT_PREFIX)
animal_pings = 0


# Random Number Generator
def rng(x):
    return randint(0, x)


@client.event
async def on_ready():
    await client.change_presence(game=Game(name="with himself OwO"))
    print("Bot is ready.")


@client.command(name='8ball',
                description="Answers a yes/no question.",
                brief="Answers from the beyond.",
                aliases=['eight_ball', 'eightball', '8-ball'],
                pass_context=True)
async def eight_ball(context):
    possible_responses = ["As I see it, yes", "It is certain", "It is decidedly so", "Most likely", "Outlook good",
                     "Signs point to yes", "Without a doubt", "Yes", "Yes – definitely", "You may rely on it", "Reply hazy, try again",
                     "Ask again later", "Better not tell you now", "Cannot predict now", "Concentrate and ask again",
                     "Don't count on it", "My reply is no", "My sources say no", "Outlook not so good", "Very doubtful"]
    await client.say(random.choice(possible_responses) + ", " + context.message.author.mention)


@client.command(name='animal',
                description="Tells you what animal you are.",
                brief="What animal are you?",
                aliases=['a'],
                pass_context=True)
async def animal(context):
    global animal_pings
    animal_pings = animal_pings + 1
    line = rng(592)
    file = open("Animals.txt", "r")
    await client.say(context.message.author.mention + " " + file.readlines()[line] + "<@442014182767067150>")
    file.close()


client.run(TOKEN)
