from ast import match_case
import os
from tokenize import String
import discord
import random
import asyncio
import time
import requests
import json
from datetime import datetime
from datetime import timedelta
from datetime import date
from dotenv import load_dotenv
from discord.ext import commands
from discord import FFmpegPCMAudio
from discord.utils import get
from discord.ext.commands import CommandNotFound
import logging

load_dotenv()
token = os.getenv('DISCORD_TOKEN')
acc_username = os.getenv('IMGFLIP_USERNAME')
acc_password = os.getenv('IMGFLIP_PASSWORD')

bot = commands.Bot(command_prefix='pot')
votemsgid = 123  # placeholder
defaultrng = 80
lastmessage = "placeholder message"
leaveChance = 70

loopCounter = 0

logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(
    filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter(
    '%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)


@bot.command(name='spit')
async def spit(ctx, at):
    response = 'You spit at ' + at
    await ctx.send(response)


@spit.error
async def spit_on_error(ctx, error):
    await ctx.send("Invalid arguments. The correct arguments are: \n`potspit NAME`")


@bot.command(name='ion')
async def ion(ctx):
    lines = open('./resources/other/potion_quotes.txt').read().splitlines()
    myline = random.choice(lines)
    response = myline
    await ctx.send(response)


bot.remove_command("help")


@bot.command(name='help')
async def help(ctx):
    commandListHelp = open('./resources/other/help.txt').read()
    response = commandListHelp
    await ctx.send(response)


@bot.command(name='invite')
async def invite(ctx):
    response = 'To invite bot to your server use this link:\nhttps://discordapp.com/api/oauth2/authorize?client_id=663812740594401317&permissions=8&scope=bot'
    await ctx.send(response)


# Provale


@bot.command(name='acim')
async def acim(ctx):
    lines = open('./resources/provale/acim.txt').read().splitlines()
    myline = random.choice(lines)
    response = '```' + myline + '```'
    await ctx.send(response)


@bot.command(name='acimadd')
async def acimadd(ctx, text):
    f = open('./resources/provale/acim.txt', "a+")
    f.write("\n" + str(date.today().strftime("%d.%m.%Y")) + " -- " + text)
    f.close
    await ctx.send("Nice!")


@bot.command(name='lazke')
async def lazke(ctx):
    lines = open('./resources/provale/lazke.txt').read().splitlines()
    myline = random.choice(lines)
    response = '```' + myline + '```'
    await ctx.send(response)


@bot.command(name='lazkeadd')
async def lazkeadd(ctx, text):
    f = open('./resources/provale/lazke.txt', "a+")
    f.write("\n" + str(date.today().strftime("%d.%m.%Y")) + " -- " + text)
    f.close
    await ctx.send("Nice!")


@bot.command(name='ispala')
async def ispala(ctx):
    lines = open('./resources/provale/ispala.txt').read().splitlines()
    myline = random.choice(lines)
    response = '```' + myline + '```'
    await ctx.send(response)


@bot.command(name='ispalaadd')
async def ispalaadd(ctx, text):
    f = open('./resources/provale/ispala.txt', "a+")
    f.write("\n" + str(date.today().strftime("%d.%m.%Y")) + " -- " + text)
    f.close
    await ctx.send("Nice!")


@bot.command(name='moca')
async def moca(ctx):
    lines = open('./resources/provale/moca.txt').read().splitlines()
    myline = random.choice(lines)
    response = '```' + myline + '```'
    await ctx.send(response)


@bot.command(name='mocaadd')
async def mocaadd(ctx, text):
    f = open('./resources/provale/moca.txt', "a+")
    f.write("\n" + str(date.today().strftime("%d.%m.%Y")) + " -- " + text)
    f.close
    await ctx.send("Nice!")


@bot.command(name='moki')
async def moki(ctx):
    lines = open('./resources/provale/moki.txt').read().splitlines()
    myline = random.choice(lines)
    response = myline
    await ctx.send(response)


@bot.command(name='ogi')
async def ogi(ctx):
    lines = open('./resources/provale/ogi.txt').read().splitlines()
    myline = random.choice(lines)
    response = myline
    await ctx.send(response)


@bot.command(name='zalba')
async def zalba(ctx):
    if str(ctx.message.author) == "mokipls#3810":
        await ctx.send("I bow to your will")
    elif str(ctx.message.author) == "harrowr#8165":
        await ctx.send("...")
    elif str(ctx.message.author) == "lazke#2166":
        await ctx.send("Nemoj samo ti molim te smucio si nam se vise sa te fore")
    elif str(ctx.message.author) == "Durion#4219":
        await ctx.send("Nikako")
    elif str(ctx.message.author) == "Aweron#8635":
        await ctx.send("De si be Awerone")
    else:
        await ctx.send("Nemoj molim te, nemoj molim te, nemoj molim te.")


@bot.command(name='vote')
async def vote(ctx):
    defaultTimeout = 30.0
    msgauthor = ctx.message.author
    answers = []

    def isSameUser(m):
        # print(str(m.content))
        # if m.content == "done":
        #     return False
        print("Same author: " + str(m.author == msgauthor))
        return m.author == msgauthor

    # await message.channel.send('Type out a question:')
    # msg = await bot.wait_for('message', check=isSameUser, timeout=5.0)
    # await message.channel.send("test")

    await ctx.channel.send('Type out a question:')
    question = await bot.wait_for('message', check=isSameUser, timeout=5.0)

    while True:
        await ctx.channel.send('Type out an answer:')
        await bot.wait_for('', check=isSameUser, timeout=5.0)
        answers.append(ctx.message.content)
        print("proso: " + str(len(answers)))
        print("currmsg: " + ctx.message.content)
        print("currList: ")
        print(answers)
        if ctx.message.content == "done":
            return False
        # if 'done' in message.content.lower():
        #     return
    print("final done")


# Movies


@bot.command(name='movie')
async def movie(ctx):
    response = 'Movie commands:\n>>> **movielist** to see the list of added movies \n**movieadd** to suggest a movie \n**movieremove** to remove the movie that you\'ve added \n**movievote** to call a movie vote\n**movierandom** to get a random movie from the suggested list'
    await ctx.send(response)


@bot.command(name='movielist')
async def movielist(ctx):
    f = open('./resources/movies/' + str(ctx.guild) + '.txt')
    lines = f.read().splitlines()
    response = '**Movie list:**\n'
    for i in lines:
        response += ''.join(['> ', i.strip(), '\n'])
    await ctx.send(response)


@movielist.error
async def movielist_on_error(ctx, error):
    await ctx.send("No movies added to the list yet. Plese add some movies using the movielist command.")


@bot.command(name='movieremove')
async def movieremove(ctx):
    with open('./resources/movies/' + str(ctx.guild) + '.txt', "r") as f:
        lines = f.readlines()
    with open('./resources/movies/' + str(ctx.guild) + '.txt', "w") as f:
        for line in lines:
            if str(ctx.message.author) in line.strip("\n"):
                await ctx.send(line.strip("\n") + " removed!")
            else:
                f.write(line)


@bot.command(name='movievote')
async def movievote(ctx):
    delayseconds = 30

    global uservotelist
    uservotelist = []
    f = open('./resources/movies/' + str(ctx.guild) + '.txt')
    lines = f.read().splitlines()  # linenum
    linenum = 0
    response = "**Movie list:** \n\n"
    for i in lines:
        linenum += 1
        response += ''.join(['> ', str(linenum), '. ', i.strip(), '\n'])

    f.close()
    reactions = ['1️⃣', '2️⃣', '3️⃣', '4️⃣', '5️⃣',
                 '6️⃣', '7️⃣', '8️⃣', '9️⃣', '🔟',
                 '🕚', '🕛', '🕐', '🕑', '🕒', '🕓',
                 '🕔', '🕕', '🕖', '🕗', '🕘', '🕙'][:linenum]
    # lines = open('./resources/other/movies.txt').read().splitlines()

    msg = await ctx.send(
        response + "\n**React** to add a vote !\nTime remaining to vote: **~ " + str(delayseconds) + " seconds.**")
    msgid = msg.id
    global votemsgid
    votemsgid = msgid
    for i in reactions:
        await msg.add_reaction(i)

    offset = 12  # offset the number by a couple of seconds
    randomoffset = random.randint(0, offset) - int(offset / 2)
    print(randomoffset)
    if randomoffset > 0:
        # delay before getting the votes
        await asyncio.sleep(delayseconds + randomoffset)
    else:
        await asyncio.sleep(delayseconds - randomoffset)

    newmsg = await ctx.fetch_message(msgid)

    counts = {react.emoji: react.count for react in newmsg.reactions}
    print(counts)

    maxvote = 0
    maxemote = "NotAvailable"
    for emotecode, mostvotes in counts.items():  # check for max
        if mostvotes > maxvote:
            maxvote = mostvotes
            maxemote = emotecode

    if maxvote == 1:
        await ctx.send("Nobody voted :(")
        return

    firstplaced = 0
    for emotecode, mostvotes in counts.items():  # check if multiple max
        if mostvotes == maxvote:
            firstplaced += 1

    if firstplaced > 1:  # check if more than 1 max
        firstplacelist = []
        firstplacelistindex = 0
        for emotecode, mostvotes in counts.items():
            if mostvotes == maxvote:
                firstplacelist.append(firstplacelistindex)
            firstplacelistindex += 1

        emoteid = random.choice(firstplacelist)
        lines = open('./resources/movies/' + str(ctx.guild) +
                     '.txt').read().splitlines()
        myline = lines[emoteid]
        response = '```First place determined randomly: ' + myline + '```'
        await ctx.send(response)

        with open('./resources/movies/' + str(ctx.guild) + '.txt', "r") as f:
            lines = f.readlines()
        with open('./resources/movies/' + str(ctx.guild) + '.txt', "w") as f:
            for line in lines:
                if line.strip("\n") != myline:
                    f.write(line)

    elif firstplaced == 1:
        emoteid = 0
        for emotecode, mostvotes in counts.items():
            if maxvote == mostvotes:
                lines = open(
                    './resources/movies/' + str(ctx.guild) + '.txt').read().splitlines()
                myline = lines[emoteid]
                response = 'The winner is:\n```' + myline + '```'
                await ctx.send(response)

                with open('./resources/movies/' + str(ctx.guild) + '.txt', "r") as f:
                    lines = f.readlines()
                with open('./resources/movies/' + str(ctx.guild) + '.txt', "w") as f:
                    for line in lines:
                        if line.strip("\n") != myline:
                            f.write(line)

            emoteid += 1


@bot.command(name='movieadd')
async def movieadd(ctx, text):
    with open('./resources/movies/' + str(ctx.guild) + '.txt') as f:
        print("passed 1")
        if str(ctx.message.author) in f.read():
            print("passed 2")

            await ctx.send("You have already suggested a movie!")
            f.close()
            return

    f = open('./resources/movies/' + str(ctx.guild) + '.txt', "a+")

    f.write(str(ctx.message.author) + " -- " + text + "\n")
    f.close
    await ctx.send("Nice!")


@bot.command(name='movierandom')
async def movierandom(ctx):
    lines = open('./resources/movies/' + str(ctx.guild) +
                 '.txt').read().splitlines()
    myline = random.choice(lines)
    response = '```' + myline + '```'
    await ctx.send(response)

    with open('./resources/movies/' + str(ctx.guild) + '.txt', "r") as f:
        lines = f.readlines()
    with open('./resources/movies/' + str(ctx.guild) + '.txt', "w") as f:
        for line in lines:
            if line.strip("\n") != myline:
                f.write(line)


# Casino

@bot.command(name='roll')
async def roll(ctx, max=100):
    max = int(max)
    response = random.randint(1, max)
    await ctx.send(response)


@roll.error
async def roll_on_error(ctx, error):
    await ctx.send("Invalid arguments. The correct arguments are: \n`potroll NUMBER/NULL`")


@bot.command(name='deathroll')
async def deathroll(ctx, num, gold, name1, name2):
    num = int(num)
    names = [name1, name2]
    iter = 0

    while num > 1:
        numholder = random.randint(1, num)
        currname = names[iter % 2]
        response = (currname + ' rolled ' + str(numholder) +
                    ' (1 to ' + str(num) + ')' + '\n')
        await ctx.send(response)
        num = numholder
        iter = iter + 1
        await asyncio.sleep(2)
        # time.sleep(2)
    currname = names[iter % 2]
    response = (currname + ' wins ' + str(gold) + ' gold')
    await ctx.send(response)


@deathroll.error
async def deathroll_on_error(ctx, error):
    await ctx.send(
        "Invalid arguments. The correct arguments are: \n`potdeathroll ROLL_NUMBER GOLD_AMOUNT NAME_1 NAME_2`")


# Sounds


@bot.command(
    name='play',
    pass_context=True,
)
async def play(ctx, filename):
    channel = ctx.message.author.voice.channel
    voice = get(bot.voice_clients, guild=ctx.guild)

    filepath = './resources/sounds/mp3/' + filename + '.mp3'
    filepath2 = './resources/sounds/mp3/' + filename + '.wav'

    if os.path.exists(filepath) or os.path.exists(filepath2):

        if voice and voice.is_connected():
            await voice.move_to(channel)
        else:
            voice = await channel.connect()

        if os.path.exists(filepath):
            source = FFmpegPCMAudio(filepath)
            voice.play(source)

        if os.path.exists(filepath2):
            source = FFmpegPCMAudio(filepath2)
            voice.play(source)

        msg = await ctx.send("Playing " + filename)

        await asyncio.sleep(20)
        await ctx.message.delete(delay=5)
        await msg.delete(delay=5)

    else:
        await ctx.send("File doesn't exist")

    await asyncio.sleep(600)
    voice.play(FFmpegPCMAudio('./resources/sounds/mp3/lol.mp3'))
    await asyncio.sleep(3)

    guild = ctx.message.guild.voice_client
    await guild.disconnect()


# @play.error
# async def play_error(ctx, error):
#     # await ctx.send(error)
#     await ctx.send("You are not connected to a voice channel.")


@bot.command(
    name='playcrusader',
    pass_context=True,
)
async def playcrusader(ctx):
    channel = ctx.message.author.voice.channel
    voice = get(bot.voice_clients, guild=ctx.guild)

    filepath = 'D:/Program Files/Steam/steamapps/common/Stronghold Crusader Extreme/fx/speech/'

    if voice and voice.is_connected():
        await voice.move_to(channel)
    else:
        voice = await channel.connect()

    voice.play(FFmpegPCMAudio(filepath + random.choice(os.listdir(filepath))))

    msg = await ctx.send("Playing ")

    await asyncio.sleep(20)
    await ctx.message.delete(delay=5)
    await msg.delete(delay=5)

    await asyncio.sleep(600)
    voice.play(FFmpegPCMAudio('./resources/sounds/mp3/lol.mp3'))
    await asyncio.sleep(3)

    guild = ctx.message.guild.voice_client
    await guild.disconnect()


bot.remove_command("playhelp")


@bot.command(name='playhelp')
async def playhelp(ctx):
    response = os.listdir("./resources/sounds/mp3/")
    responseString = ""
    currChar = response[0][0]
    for i in response:
        # print ("I: " + i)
        # print ("currChar: " + currChar + "\n" )
        if currChar == i[0]:
            responseString = responseString + i + "  "
        else:
            responseString = responseString + "\n" + i + "  "
            currChar = i[0]

    await ctx.send('```' + responseString + '```')


@bot.command(pass_context=True)
async def leave(ctx):
    voice = get(bot.voice_clients, guild=ctx.guild)
    voice.play(FFmpegPCMAudio('./resources/sounds/mp3/lol.mp3'))
    await asyncio.sleep(3)
    guild = ctx.message.guild.voice_client
    await guild.disconnect()
    msg = await ctx.send("Bot left the voice channel.")

    await asyncio.sleep(20)
    await ctx.message.delete(delay=5)
    await msg.delete(delay=5)


##################################################


@bot.command(name='timer')
async def timer(ctx, min):
    await ctx.send("Timer set for " + min + " minute/s.")
    sec = int(min) * 60
    if sec > 0:
        await asyncio.sleep(sec)
        await ctx.send("Time's up, let's do this <@" + str(ctx.author.id) + "> " + "!")


@timer.error
async def timer_on_error(ctx, error):
    await ctx.send("Invalid arguments. The correct arguments are: \n`pottimer NUMBER(minutes)`")

    print("\n\nTimestamp: " + str(datetime.now().strftime("%Y-%m-%d %H-%M-%S")) +
          "\nMeme: " + str(data['data']['url']))

    await ctx.send(data['data']['url'])


@bot.command(name='lazarmeme')
async def lazarmeme(ctx, caption1: str):
    url = 'https://api.imgflip.com/caption_image'
    boxes = '{"text":caption1}'

    params = dict(template_id=102156234, username=acc_username,
                  password=acc_password, boxes=boxes)

    res = requests.get(url, params=params)

    data = res.json()

    print("\n\nTimestamp: " + str(datetime.now().strftime("%Y-%m-%d %H-%M-%S")) +
          "\nMeme: " + str(data['data']['url']))

    await ctx.send(data['data']['url'])


##################################################

finalists = ['🇨🇿', '🇷🇴', '🇵🇹', '🇫🇮', '🇨🇭', '🇫🇷', '🇳🇴', '🇦🇲', '🇮🇹', '🇪🇸', '🇳🇱', '🇺🇦',
             '🇩🇪', '🇱🇹', '🇦🇿', '🇧🇪', '🇬🇷', '🇮🇸', '🇲🇩', '🇸🇪', '🇦🇺', '🇬🇧', '🇵🇱', '🇷🇸',
             '🇪🇪']

@bot.event
async def on_message(message):
    global finalists

    if message.author == bot.user:
        return
    msg = str(message.clean_content.lower())  # string holder

    if isinstance(message.channel, discord.DMChannel):
        if message.clean_content.lower() == "eurovote":

            await message.channel.send(file=discord.File('./resources/eurovision/contestants.jpg'))

            author = message.author

            allowed_reactions = set(finalists)
            voting_start_time = datetime.now()

            voting_messages = []
            voting_options = [12, 10, 8, 7, 6, 5, 4, 3, 2, 1]
            for i in voting_options:
                await message.author.send('⠀\nWho would you like to give ' + str(i) + 'points?')

                first_msg = await message.author.send('⠀')
                for flag in finalists[:13]:
                    await first_msg.add_reaction(flag)

                second_msg = await message.author.send('⠀')
                for flag in finalists[13:]:
                    await second_msg.add_reaction(flag)

                voting_messages.append({
                    "points": i,
                    "messages": [first_msg.id, second_msg.id]
                })
                await asyncio.sleep(2)

            votes = {}
            votes_to_submit = {}

            done_msg = None
            while True:
                while voting_start_time < voting_start_time + timedelta(minutes=25):
                    votes = {}
                    for vote_msgs in voting_messages:
                        points = vote_msgs.get("points")
                        first_group, second_group = vote_msgs.get("messages")
                        first_group = await message.channel.fetch_message(first_group)
                        second_group = await message.channel.fetch_message(second_group)

                        first_group_votes = list(filter(lambda x: x.count > 1, first_group.reactions))
                        second_group_votes = list(filter(lambda x: x.count > 1, second_group.reactions))

                        if not first_group_votes and not second_group_votes:
                            continue

                        if len(first_group_votes) + len(second_group_votes) > 1:
                            await message.author.send(f'Please select only one option for {points} points')
                            await asyncio.sleep(1)
                            continue

                        voted_for = [*first_group_votes, *second_group_votes][0]

                        if str(voted_for) not in allowed_reactions:
                            await message.author.send(f'You cannot vote for {voted_for}...')
                            await asyncio.sleep(1)
                            continue

                        if votes.get(voted_for):
                            await message.author.send(f'You can only give one point to a country: {voted_for}')
                            await asyncio.sleep(1)
                            continue

                        votes[str(voted_for)] = points

                    if len(votes) == len(voting_options):
                        votes_to_submit = votes
                        break

                if not done_msg:
                    done_msg = await message.author.send('Done?')
                    await done_msg.add_reaction('✅')
                    await asyncio.sleep(1)

                is_done_msg = await message.channel.fetch_message(done_msg.id)
                is_done = is_done_msg.reactions and is_done_msg.reactions[0].count > 1

                if len(votes_to_submit) != len(voting_options):
                    await message.author.send('Please correct your choices')
                    continue

                if is_done:
                    break

            if len(votes_to_submit) == len(voting_options):
                print(f"{author.name} voted: {votes}")
                votes = votes_to_submit
                await author.send('Voting finished, calculating and submitting votes...')

                msg_str = "\n"
                for voted_for, points in votes.items():
                    msg_str += f"{voted_for}: {points}\n"

                await author.send(f'Your votes: {msg_str}')
                with open(f'./resources/eurovision/votes/{author.name}.json', 'w+') as votes_file:
                    votes_file.write(json.dumps(votes))
                await author.send("Successfully submitted")

            return

    # if bot.dev and not await bot.is_owner(message.author): #always returns for any user
    #     return

    if bot.user.mentioned_in(message) and message.mention_everyone is False:
        if 'help' in message.content.lower():
            commandListHelp = open('./resources/other/help.txt').read()
            await message.channel.send(commandListHelp)
        else:
            await message.add_reaction('👀')  # :eyes:
    if 'i?' in message.clean_content.lower():  # I sta i
        if msg.find('i?', 0, 2) >= 0:
            await message.channel.send("Sta i?")
    if 'moca' in message.clean_content.lower():  # Moca
        await message.add_reaction('💩')  # :poop:
        emoji = discord.utils.get(message.guild.emojis, name='momcilo')
        if emoji:
            await message.add_reaction(emoji)
    if 'potkodjen' in message.clean_content.lower():  # Kodjen
        emoji = discord.utils.get(message.guild.emojis, name='astor')
        if emoji:
            await message.add_reaction(emoji)
    if 'lazar' in message.clean_content.lower():
        emoji = discord.utils.get(message.guild.emojis, name='lazar')
        if emoji:
            await message.add_reaction(emoji)
    if str(message.author) == "Faust#5371":  # Lazar
        messageholder = ""
        i = True
        randroll = random.randint(1, 100)
        if (randroll > 90):
            for char in message.content:
                if i:
                    messageholder += char.upper()
                else:
                    messageholder += char.lower()
                if char != ' ':
                    i = not i
            # print (messageholder)
            # await message.edit(content=messageholder)
            await message.channel.send(messageholder)

    # Test
    # if str(message.author) == "Mokipls#3810":

    if str(message.author) == "Schmeiser#3016":
        await message.add_reaction('🍁')

    if str(message.author) == "harrowr#8165":  # rename user to his sent message by random
        global defaultrng

        global lastmessage  # spam protection
        if (lastmessage == message.clean_content):
            return
        lastmessage = message.clean_content

        randroll = random.randint(1, 100)
        if (randroll > defaultrng):
            # print ("Moca rolao: " + str(randroll) + str(message.content))
            if message.content:
                if "<" not in message.content:  # User id on discord
                    if "http" not in message.content:  # Link
                        defaultrng = defaultrng + random.randint(30, 70)
                        # change nickname
                        await message.author.edit(nick=message.content)
                        emoji = discord.utils.get(
                            message.guild.emojis, name='momcilo')
                        if emoji:
                            await message.add_reaction(emoji)
        else:
            # print ("Moca nije rolao: " + str(randroll) + str(message.content))
            randminiroll = random.randint(3, 10)
            defaultrng = defaultrng - randminiroll

    # if any(message.guild.emojis in message.clean_content.lower()):
    #     print ("ima")
    # emokilist = list(message.guild.emojis())

    # if emokilist[emojis] in message.clean_content.lower():
    #     emoji = discord.utils.get(message.guild.emojis, name=emojis)
    #     if emoji:
    #         await message.add_reaction(emoji)

    # await bot.process_commands(message)

    if str(message.author) == "highlander#5120":
        # if str(message.author) == "Mokipls#3810":
        if message.content:
            # change nickname
            await message.author.edit(nick="Acim rollao: " + (str)(random.randint(0, 100)))

    # processing commands, should be at the end?
    await bot.process_commands(message)

    if message.content.startswith('potgreet'):
        channel = message.channel
        author = str(message.author)

        # await channel.send('Say hello!')  #wait for message
        # msg = await bot.wait_for('message')

        await channel.send('Hello ' + author[:-5] + '!')

    if message.content.startswith('potcreateevent'):  # event creating command
        channel = message.channel
        author = message.author
        await channel.send('Input the event name')
        eventName = await bot.wait_for('message')

        await channel.send("Input the number of minutes until the event is starting ")
        eventTimeStr = await bot.wait_for('message')
        eventTime = int(eventTimeStr.content)
        eventTime = eventTime * 60  # sec to min
        # eventName = await bot.wait_for('message')
        await channel.send("Event created: " + eventName.content + " by: " + author.name + " starting in: " + str(
            eventTime / 60) + " minutes...")
        await asyncio.sleep(eventTime)
        await channel.send("Event created: " + eventName.content + " by: " + author.name + " is starting now!")


@bot.command(name='createevent')
async def createevent(ctx):
    return


# Voice leave


@bot.event
async def on_voice_state_update(member, before, after):
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")

    if (before.channel is None and after.channel is not None):
        print('Server: ' + str(member.guild) + ' Joined the voice: ' + str(member) +
              " Current Time =", current_time)
        if (str(member) == 'kole16#4134'):

            # User Joins a voice channel
            voice = get(bot.voice_clients, guild=member.guild)
            await asyncio.sleep(5)
            if member == bot.user:  # check for self
                return
            if member.bot:  # check for other bots
                return
            if voice and voice.is_connected():
                await voice.move_to(after.channel)
            else:
                voice = await after.channel.connect()
            await asyncio.sleep(1)

            voice.play(FFmpegPCMAudio('./resources/sounds/calljoiner/kodjen.mp3'))
            await asyncio.sleep(7)
            guild = member.guild.voice_client
            await guild.disconnect()

        if (str(member) == 'BABLIBOYBBB#3809'):

            # User Joins a voice channel
            voice = get(bot.voice_clients, guild=member.guild)
            await asyncio.sleep(1)
            if member == bot.user:  # check for self
                return
            if member.bot:  # check for other bots
                return
            if voice and voice.is_connected():
                await voice.move_to(after.channel)
            else:
                voice = await after.channel.connect()
            await asyncio.sleep(1)
            voice.play(FFmpegPCMAudio('./resources/sounds/calljoiner/bubbly.mp3'))
            await asyncio.sleep(10)
            guild = member.guild.voice_client
            await guild.disconnect()


    elif (after.channel is None):
        # print('left')
        if before.channel.members:  # check if list members is empty
            # print('empty channel')
            randroll = random.randint(1, 100)
            print('Server: ' + str(member.guild) + ' Left the voice:   ' + str(member) +
                  " Current Time = " + str(current_time) + " " + str(randroll))
            voice = get(bot.voice_clients, guild=member.guild)
            if (randroll > leaveChance):
                await asyncio.sleep(1)
                if member == bot.user:  # check for self
                    return
                if member.bot:  # check for other bots
                    return
                if voice and voice.is_connected():
                    await voice.move_to(before.channel)
                else:
                    voice = await before.channel.connect()
                await asyncio.sleep(1)
                voice.play(FFmpegPCMAudio('./resources/sounds/callleaver/' +
                                          random.choice(os.listdir('./resources/sounds/callleaver/'))))
                await asyncio.sleep(10)
                guild = member.guild.voice_client
                await guild.disconnect()


# @bot.event
# async def on_raw_reaction_add(payload):
#     if payload.member != None:
#         return
#     # print(payload)
#     author = await bot.fetch_user(payload.user_id)
#     if author.bot:
#         return
#
#     channel = await bot.fetch_channel(payload.channel_id)
#     message = await channel.fetch_message(payload.message_id)
#
#     for reaction in message.reactions:
#         if reaction.count > 1:
#             print("found", reaction)
#             await message.remove_reaction(reaction, author)
#
#     emoji_to_add = payload.emoji.name
#     await message.add_reaction(emoji_to_add)
#     print(author, type(author))
#     # currmsg = discord.utils.get(await currchannel.history(limit=100).flatten(), name=author)


@bot.event
async def on_reaction_add(reaction, user):
    global votemsgid
    global uservotelist
    maxvotes = 1
    if reaction.message.id == votemsgid:
        if user == bot.user:  # check for self
            return
        elif uservotelist.count(user) > maxvotes - 1:
            await reaction.message.remove_reaction(reaction, user)
            await reaction.message.channel.send("<@" + str(user.id) + "> " + "you have already voted! Stop spamming!")
        else:
            uservotelist.append(user)


# @bot.command(name='meme')
# async def meme(ctx, template_id: int, caption0: str, caption1: str):
#     url = 'https://api.imgflip.com/caption_image'
#     params = dict(template_id=template_id, username=acc_username,
#                   password=acc_password, text0=caption0, text1=caption1)
#     res = requests.get(url, params=params)

#     data = res.json()

#     print("\n\nTimestamp: " + str(datetime.now().strftime("%Y-%m-%d %H-%M-%S")) +
#           "\nMeme: " + str(data['data']['url']))

#     await ctx.send(data['data']['url'])

# @bot.command(name='meme_templates')
# async def meme(ctx):
#     await ctx.send('https://api.imgflip.com/popular_meme_ids')

@bot.command(name='insteadofwow')
async def timecalculator(ctx):
    await ctx.send(
        "Wondering what else to spend time on instead of WoW?\nChoose an expansion: \n1. Classic\n2. TBC\n3. Shadowlands")
    msg = await bot.wait_for('message')
    await ctx.send(
        ">>> With that amount of time it would take you to level 1 character to max level, you can play:\n" + expansioncalculator(
            int(msg.content)))


def expansioncalculator(i):
    match i:
        # classic
        case 1:
            i = 170
        # tbc
        case 2:
            i = 200
        # shadowlands
        case 3:
            i = 30

        # error
        case _:
            return "nothing, you inputed a wrong value ._."

    # avg game time in hours
    rocketLeagueTime = 0.166667
    fortniteTime = 0.333
    dotaTime = 1
    lolTime = 0.5

    calculatedString = "```json\n" + str(int(i / rocketLeagueTime)) + " Rocket League games or\n" + str(
        int(i / fortniteTime)) + " Fortnite games or\n" + str(int(i / lolTime)) + " LoL games or\n" + str(
        int(i / dotaTime)) + " DotA games\n" + "```"

    return calculatedString


@bot.command(name='imgtest')
async def imgtest(ctx):
    imgNumber = 1
    for filename in os.listdir('./resources/eurovision/'):
        if filename.endswith(".png") or filename.endswith(".jpg"):
            msg = await ctx.channel.send(
                file=discord.File('./resources/eurovision/' + "Screenshot_" + str(imgNumber) + ".png"))
            imgNumber = imgNumber + 1
            reactions = ['1️⃣', '2️⃣', '3️⃣', '4️⃣', '5️⃣',
                         '6️⃣', '7️⃣', '8️⃣', '9️⃣', '🔟']

            for i in reactions:
                await msg.add_reaction(i)
                continue
        else:
            continue


@bot.command(name='eurovote')
async def eurovote(ctx):
    await ctx.author.create_dm()
    await ctx.author.dm_channel.send('To vote, type "eurovote" here in my DMs')


@bot.command(name='eurovision')
async def eurovision(ctx):
    votes = {f: 0 for f in finalists}
    for filename in os.listdir('./resources/eurovision/votes'):
        if filename.endswith(".json"):
            with open(f'./resources/eurovision/votes/{filename}') as f:
                content = "".join(f.readlines())
                votes_json = json.loads(content)
                for country, points in votes_json.items():
                    votes[country] = votes[country] + points

    sorted_votes = dict(sorted(votes.items(), key=lambda item: item[1], reverse=True))
    msg_str = "\n"
    for voted_for, points in sorted_votes.items():
        msg_str += f"{voted_for}: {points}\n"
    await ctx.send(f'Current standings: {msg_str}')

    #
    #     msg = await ctx.channel.send(
    #         file=discord.File('./resources/eurovision/' + "Screenshot_" + str(imgNumber) + ".png"))
    #     imgNumber = imgNumber + 1
    #     reactions = ['1️⃣', '2️⃣', '3️⃣', '4️⃣', '5️⃣',
    #                  '6️⃣', '7️⃣', '8️⃣', '9️⃣', '🔟']
    #
    #     for i in reactions:
    #         await msg.add_reaction(i)
    #         continue
    # else:
    #     continue


bot.run(token)
