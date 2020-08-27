import os
import discord
import random
import asyncio
import time
import requests
import json
from datetime import datetime
from datetime import date
from dotenv import load_dotenv
from discord.ext import commands
from discord import FFmpegPCMAudio
from discord.utils import get
from discord.ext.commands import CommandNotFound


load_dotenv()
token = os.getenv('DISCORD_TOKEN')
acc_username = os.getenv('IMGFLIP_USERNAME')
acc_password = os.getenv('IMGFLIP_PASSWORD')

bot = commands.Bot(command_prefix='pot')
votemsgid = 123  # placeholder
defaultrng = 80
commandListHelp = 'Available commands:\n\n>>> ("pot" prefix) \n\n(pot)ion, spit, invite, \nispala, acim, lazke, moca, moki, \nispalaadd, acimadd, lazkeadd, mocaadd \nroll default 100, deathroll number gold name1 name2, \nplay songname, playhelp, leave, playcrusader, \ntimer, \ndrakememe "firstframe" "secondframe"\nmovie, movieadd "moviename", movievote, mocierandom'


@bot.command(name='spit')
async def spit(ctx, at):
    response = 'You spit at ' + at
    await ctx.send(response)


@bot.command(name='ion')
async def ion(ctx):
    lines = open('./other/potion_quotes.txt').read().splitlines()
    myline = random.choice(lines)
    response = myline
    await ctx.send(response)

bot.remove_command("help")
@bot.command(name='help')
async def help(ctx):
    response = commandListHelp
    await ctx.send(response)


@bot.command(name='invite')
async def invite(ctx):
    response = 'To invite bot to your server use this link:\nhttps://discordapp.com/api/oauth2/authorize?client_id=663812740594401317&permissions=8&scope=bot'
    await ctx.send(response)

# Provale
@bot.command(name='acim')
async def acim(ctx):
    lines = open('./provale/acim.txt').read().splitlines()
    myline = random.choice(lines)
    response = '```' + myline + '```'
    await ctx.send(response)


@bot.command(name='acimadd')
async def acimadd(ctx, text):
    f = open('./provale/acim.txt', "a+")
    f.write("\n" + str(date.today().strftime("%d.%m.%Y")) + " -- " + text)
    f.close
    await ctx.send("Nice!")


@bot.command(name='lazke')
async def lazke(ctx):
    lines = open('./provale/lazke.txt').read().splitlines()
    myline = random.choice(lines)
    response = '```' + myline + '```'
    await ctx.send(response)


@bot.command(name='lazkeadd')
async def lazkeadd(ctx, text):
    f = open('./provale/lazke.txt', "a+")
    f.write("\n" + str(date.today().strftime("%d.%m.%Y")) + " -- " + text)
    f.close
    await ctx.send("Nice!")


@bot.command(name='ispala')
async def ispala(ctx):
    lines = open('./provale/ispala.txt').read().splitlines()
    myline = random.choice(lines)
    response = '```' + myline + '```'
    await ctx.send(response)


@bot.command(name='ispalaadd')
async def ispalaadd(ctx, text):
    f = open('./provale/ispala.txt', "a+")
    f.write("\n" + str(date.today().strftime("%d.%m.%Y")) + " -- " + text)
    f.close
    await ctx.send("Nice!")


@bot.command(name='moca')
async def moca(ctx):
    lines = open('./provale/moca.txt').read().splitlines()
    myline = random.choice(lines)
    response = '```' + myline + '```'
    await ctx.send(response)


@bot.command(name='mocaadd')
async def mocaadd(ctx, text):
    f = open('./provale/moca.txt', "a+")
    f.write("\n" + str(date.today().strftime("%d.%m.%Y")) + " -- " + text)
    f.close
    await ctx.send("Nice!")


@bot.command(name='moki')
async def moki(ctx):
    response = "https://gamepedia.cursecdn.com/terraria_gamepedia/1/1e/Propeller_Gato_%28animated%29.gif?version=ffbee9042204d124e5bd44f8721b9a00"
    await ctx.send(response)

# Movies


@bot.command(name='movie')
async def movie(ctx):
    response = 'Movie commands:\n>>> **movielist** to see the list of added movies \n**movieadd** to suggest a movie \n**movieremove** to remove the movie that you\'ve added \n**movievote** to call a movie vote\n**movierandom** to get a random movie from the suggested list'
    await ctx.send(response)


@bot.command(name='movielist')
async def movielist(ctx):

    f = open('./other/movies.txt')
    lines = f.read().splitlines()
    response = '**Movie list:**\n'
    for i in lines:
        response += ''.join(['> ', i.strip(), '\n'])
    await ctx.send(response)


@bot.command(name='movieremove')
async def movieremove(ctx):

    with open("./other/movies.txt", "r") as f:
        lines = f.readlines()
    with open("./other/movies.txt", "w") as f:
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
    f = open('./other/movies.txt')
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
    # lines = open('./other/movies.txt').read().splitlines()

    msg = await ctx.send(response + "\n**React** to add a vote !\nTime remaining to vote: **~ " + str(delayseconds) + " seconds.**")
    msgid = msg.id
    global votemsgid
    votemsgid = msgid
    for i in reactions:
        await msg.add_reaction(i)

    offset = 12  # offset the number by a couple of seconds
    randomoffset = random.randint(0, offset) - int(offset/2)
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
        lines = open('./other/movies.txt').read().splitlines()
        myline = lines[emoteid]
        response = '```First place determined randomly: ' + myline + '```'
        await ctx.send(response)

        with open("./other/movies.txt", "r") as f:
            lines = f.readlines()
        with open("./other/movies.txt", "w") as f:
            for line in lines:
                if line.strip("\n") != myline:
                    f.write(line)

    elif firstplaced == 1:
        emoteid = 0
        for emotecode, mostvotes in counts.items():
            if maxvote == mostvotes:
                lines = open('./other/movies.txt').read().splitlines()
                myline = lines[emoteid]
                response = '```' + myline + '```'
                await ctx.send(response)

                with open("./other/movies.txt", "r") as f:
                    lines = f.readlines()
                with open("./other/movies.txt", "w") as f:
                    for line in lines:
                        if line.strip("\n") != myline:
                            f.write(line)

            emoteid += 1


@bot.command(name='movieadd')
async def movieadd(ctx, text):

    with open('./other/movies.txt') as f:
        if str(ctx.message.author) in f.read():
            await ctx.send("You have already suggested a movie!")
            f.close()
            return

    f = open('./other/movies.txt', "a+")

    f.write(str(ctx.message.author) + " -- " + text + "\n")
    f.close
    await ctx.send("Nice!")


@bot.command(name='movierandom')
async def movierandom(ctx):
    lines = open('./other/movies.txt').read().splitlines()
    myline = random.choice(lines)
    response = '```' + myline + '```'
    await ctx.send(response)

    with open("./other/movies.txt", "r") as f:
        lines = f.readlines()
    with open("./other/movies.txt", "w") as f:
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
    await ctx.send("Invalid arguments. The correct arguments are: \n`potdeathroll NUMBER GOLD NAME1 NAME2`")

# Sounds


@bot.command(
    name='play',
    pass_context=True,
)
async def play(ctx, filename):

    channel = ctx.message.author.voice.channel
    voice = get(bot.voice_clients, guild=ctx.guild)

    filepath = './mp3/' + filename + '.mp3'
    filepath2 = './mp3/' + filename + '.wav'

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
    voice.play(FFmpegPCMAudio('./mp3/lol.mp3'))
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
    voice.play(FFmpegPCMAudio('./mp3/lol.mp3'))
    await asyncio.sleep(3)

    guild = ctx.message.guild.voice_client
    await guild.disconnect()

bot.remove_command("playhelp")
@bot.command(name='playhelp')
async def playhelp(ctx):
    response = os.listdir("E:/Python/PZ/mp3/")
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
    voice.play(FFmpegPCMAudio('./mp3/lol.mp3'))
    await asyncio.sleep(3)
    guild = ctx.message.guild.voice_client
    await guild.disconnect()
    await ctx.send("Bot left the voice channel.")

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

##################################################
# command template
# @bot.command(name='')
# async def (ctx):
#     response = ''
#     await ctx.send(response)

##################################################


@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')
    await bot.change_presence(status=discord.Status.online, activity=discord.Game("Brewing potions...  Type \"pothelp\" to see the available commands"))
    print('bot id:' + str(bot.user.id))
    if bot.user.id == 663812740594401317:
        bot.dev = True
    else:
        bot.dev = False


@bot.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Well met {member.name}. Welcome to ' + str(member.guild) + '!')

# Memes


@bot.command(name='drakememe')
async def drakememe(ctx, caption0: str, caption1: str):
    url = 'https://api.imgflip.com/caption_image'
    params = dict(template_id=181913649, username=acc_username,
                  password=acc_password, text0=caption0, text1=caption1)
    res = requests.get(url, params=params)

    data = res.json()

    print("\n\nTimestamp: " + str(datetime.now().strftime("%Y-%m-%d %H-%M-%S")) +
          "\nMeme: " + str(data['data']['url']))

    await ctx.send(data['data']['url'])


@bot.command(name='lazarmeme')
async def lazarmeme(ctx, caption1: str):
    url = 'https://api.imgflip.com/caption_image'
    boxes ='{"text":caption1}'
    
    params = dict(template_id=102156234, username=acc_username,
                  password=acc_password, boxes=boxes)

    res = requests.get(url, params=params)

    data = res.json()

    print("\n\nTimestamp: " + str(datetime.now().strftime("%Y-%m-%d %H-%M-%S")) +
          "\nMeme: " + str(data['data']['url']))

    await ctx.send(data['data']['url'])

##################################################


@bot.event
async def on_message(message):
    msg = str(message.clean_content.lower())  # string holder
    if isinstance(message.channel, discord.DMChannel):
        await message.author.send('Don\'t DM me, I\'m brewing potions you donkey!')
        return
    # if bot.dev and not await bot.is_owner(message.author): #always returns for any user
    #     return
    if message.author == bot.user:
        return
    if bot.user.mentioned_in(message) and message.mention_everyone is False:
        if 'help' in message.content.lower():
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

    if str(message.author) == "harrowr#8165":
        global defaultrng
        randroll = random.randint(1, 100)
        if (randroll > defaultrng):
            # print ("Moca rolao: " + str(randroll) + str(message.content))
            if message.content:
                defaultrng = defaultrng + random.randint(30, 70)
                await message.author.edit(nick = message.content)
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

    await bot.process_commands(message)

# Voice leave

@bot.event
async def on_voice_state_update(member, before, after):
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")

    if(before.channel is None and after.channel is not None):
        print('Joined the voice: ' + str(member) +
              " Current Time =", current_time)
        # User Joins a voice channel

    elif(after.channel is None):
        if before.channel.members: # check if list members is empty
            randroll = random.randint(1, 100)
            print('Left the voice:   ' + str(member) + " Current Time = " + str(current_time) + " " + str(randroll))
            voice = get(bot.voice_clients, guild=member.guild)

            if (randroll > 80):
                await asyncio.sleep(1)
                if member == bot.user:  # check for self
                    return
                if member.bot:  # check for other bots
                    return
                if voice and voice.is_connected():
                    await voice.move_to(before.channel)
                else:
                    voice = await before.channel.connect()

                voice.play(FFmpegPCMAudio('./callLeaver/' +
                                        random.choice(os.listdir('./callLeaver/'))))
                await asyncio.sleep(6)
                guild = member.guild.voice_client
                await guild.disconnect()


@bot.event
async def on_reaction_add(reaction, user):
    global votemsgid
    global uservotelist
    maxvotes = 1
    if reaction.message.id == votemsgid:
        if user == bot.user:  # check for self
            return
        elif uservotelist.count(user) > maxvotes-1:
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

bot.run(token)
