import random
from discord.ext.commands import Bot
from discord import Game
from random import randint
from discord import Member
import os


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


@client.command(name='rng',
                description="Get a random number.",
                brief="Random Number Generator?",
                aliases=['random'],
                pass_context=False)
async def random_number(ctx: int):
        await client.say(rng(ctx))


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
    line = rng(593)
    file = open("Animals.txt", "r")
    await client.say(context.message.author.mention + " " + file.readlines()[line])
    if line == 593:
        await client.say("<@442014182767067150>")
    file.close()


client.run(TOKEN)
