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
    line = rng(594)
    file = open("Animals.txt", "r")
    await client.say(context.message.author.mention + " " + file.readlines()[line])
    file.close()


@client.command(name='bestiary',
                description="Gives a random entry from the bestiary.",
                brief="Random creature?",
                aliases=['b'])
async def bestiary():
    line = rng(131)
    file = open("Bestiary.txt", "r")
    await client.say(file.readlines()[line])
    file.close()


@client.command(name='pickup',
                description="Best way to tell someone you like them!.",
                brief="Cheesy pick up lines.",
                aliases=['p'])
async def pickup(member: Member):
    line = rng(120)
    file = open("Pickup.txt", "r")
    await client.say(member.mention + " " + file.readlines()[line])
    file.close()

    
@client.command(name='dead',
                description="Depressed? Use this to get more depressed!",
                brief="Use at your own risk",
                aliases=['rip', 'die', 'kys', 'kms'])
async def dead():
    line = rng(53)
    file = open("Demotivational.txt", "r")
    await client.say(file.readlines()[line])
    file.close()


@client.command(name='fact',
                description="Fun Facts.",
                brief="Fun Facts",
                aliases=['f'])
async def fact():
    line = rng(206)
    file = open("Facts.txt", "r")
    await client.say(file.readlines()[line])
    file.close()


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.channel.is_private:
        msg = message.author.mention + " - " + message.content
        me = await client.get_user_info('442014182767067150')
        await client.send_message(me, msg)
    await client.process_commands(message)


client.run(TOKEN)
