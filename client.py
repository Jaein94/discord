import numpy as np
import discord
from discord.ext import commands
import datetime
import os
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
from urllib.parse import quote
import re # Regex for youtube link

client = discord.Client() # Create Instance of Client. This Client is discord server's connection to Discord Room

f = open("config.txt", 'r')
key = f.readline().split(':')[-1].split("'")[1]
print(key)
f.close()
bot = commands.Bot(command_prefix='!')

def crawl(Id):
    url = "https://lostark.game.onstove.com/Profile/Character/" + quote(Id)
    html = urlopen(url)
    bsObject = BeautifulSoup(html, "html.parser")
    list_char = []
    tmp = bsObject.select_one('div.profile-character-list').select('ul>li>span>button>span')

    for n in tmp:
        name = n.text
        url = "https://lostark.game.onstove.com/Profile/Character/" + quote(name)
        html = urlopen(url)
        bsObject = BeautifulSoup(html, "html.parser")
        serv = bsObject.find_all(attrs={"class": "profile-character-info__server"})
        job = bsObject.find('img', "profile-character-info__img")
        itemlv = bsObject.find_all("div", {"class": "level-info2__item"})[0].find_all("span")[1]
        list_char.append([str(serv[0].get_text())[1:], name, job.attrs['alt'], float(itemlv.get_text()[3:].replace(',', '')), job.attrs['src']])
    list_char = sorted(list_char, key = lambda x : -1*x[3])
    
    return list_char

@client.event # Use these decorator to register an event.
async def on_ready(): # on_ready() event : when the bot has finised logging in and setting things up
    await client.change_presence(status=discord.Status.online, activity=discord.Game("amlab 기능 봇"))
    print("New log in as {0.user}".format(client))


@bot.command()
async def test(ctx,arg):
    await ctx.send(arg)

@client.event
async def on_message(message): # on_message() event : when the bot has recieved a message
    #To user who sent message
    # await message.author.send(msg)
    print(message.content)
    if message.author == client.user:
        return

    if message.content.startswith("!help") or message.content.startswith("!도움말"):
        embed = discord.Embed(title="명령어 List!", color=0x5CD1E5)
        embed.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/698548508126609409.png?size=96')
        embed.add_field(name = "!김태훈", value = "태훈형 놀리기",inline=False)
        embed.add_field(name = "!디붕전압", value = "디붕 모코코 아바타",inline=False)
        embed.add_field(name = "!예둔효율표", value = "예둔효율맵보기",inline=False)
        embed.add_field(name = "!아브3관", value = "아브렐 3관문 ",inline=False)
        embed.add_field(name = "!비아", value = "비아키스 체력 별 패턴",inline=False)
        embed.add_field(name = "!발탄", value = "발탄 체력 별 패턴",inline=False)
        embed.add_field(name = "!쿠크", value = "쿠크 체력 별 패턴",inline=False)
        embed.add_field(name = "!아브", value = "아브렐슈드 체력 별 패턴",inline=False)
        embed.add_field(name = "!아브6관", value = "아브렐 6 관문",inline=False)
        embed.add_field(name = "!우리가게영업함", value = "영업한대;;",inline=False)
        embed.add_field(name = "!로스런쌀쌀", value = "쌀쌀쌀쌀",inline=False)
        await message.channel.send("도움말!", embed=embed)

    if message.content.startswith("!예둔효율표"):
        embed = discord.Embed(title=f"{message.guild.name}", description="예둔효율표", timestamp=datetime.datetime.utcnow(), color=discord.Color.blue())
        embed.set_image(url='https://cdn.discordapp.com/attachments/820048020728053771/831720557082968114/i14531518113.png')
        await message.channel.send("예둔 효율!", embed=embed)
    
    if message.content.startswith("!디붕전압"):
        embed = discord.Embed(title=f"{message.guild.name}", description="디붕 전압;;;;;", timestamp=datetime.datetime.utcnow(), color=discord.Color.blue())
        embed.set_image(url='https://cdn.discordapp.com/attachments/843444463120154667/923974460703379557/unknown.png')

        await message.channel.send(embed=embed)

    if message.content.startswith("!김태훈"):
        embed = discord.Embed(timestamp=datetime.datetime.utcnow(), color=discord.Color.blue())
        embed.add_field(name = "태훈형", value = "김태훈 바보")
        embed.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/834722904918589450.gif?size=96')
        await message.channel.send(embed=embed)

    if message.content.startswith("!쌀먹"):
        embed = discord.Embed(timestamp=datetime.datetime.utcnow(), color=discord.Color.blue())
        embed.set_image(url = 'https://cdn.discordapp.com/attachments/843444463120154668/924584125325799474/IMG_4989.png')
        await message.channel.send(embed=embed)

    if message.content.startswith("!비아"):
        if message.content == "!비아3관":
            embed = discord.Embed(timestamp=datetime.datetime.utcnow(), color=discord.Color.blue())
            embed.set_image(url = 'https://cdn.discordapp.com/attachments/820049088447905853/831196788601126912/i13565110175.png')
            await message.channel.send(embed=embed)
        elif message.content == "!비아1관":
            embed = discord.Embed(timestamp=datetime.datetime.utcnow(), color=discord.Color.blue())
            embed.set_image(url = 'https://cdn.discordapp.com/attachments/843444463120154667/927179565900656700/i13440150376.png')
            await message.channel.send(embed=embed)
        elif message.content == "!비아":
            embed = discord.Embed(timestamp=datetime.datetime.utcnow(), color=discord.Color.blue())
            embed.set_image(url = 'https://cdn.discordapp.com/attachments/843444463120154668/925980039474991144/unknown.png')
            await message.channel.send(embed=embed)

    if message.content.startswith("!발탄"):
        embed = discord.Embed(timestamp=datetime.datetime.utcnow(), color=discord.Color.blue())
        embed.set_image(url = 'https://cdn.discordapp.com/attachments/843444463120154668/925979894423363645/unknown.png')
        await message.channel.send(embed=embed)

    if message.content.startswith("!쿠크"):
        embed = discord.Embed(timestamp=datetime.datetime.utcnow(), color=discord.Color.blue())
        embed.set_image(url = 'https://cdn.discordapp.com/attachments/843444463120154668/925979894423363645/unknown.png')
        await message.channel.send(embed=embed)

    if message.content.startswith("!아브"):
        if message.content == "!아브3관":
            embed = discord.Embed(timestamp=datetime.datetime.utcnow(), color=discord.Color.blue())
            embed.add_field(name = "3관 별도형",value = '별도형')
            embed.set_image(url = 'https://cdn.discordapp.com/attachments/820049088447905853/893531427197562920/unknown.png')
            await message.channel.send(embed=embed)
        elif message.content == "!아브6관":
            embed = discord.Embed(timestamp=datetime.datetime.utcnow(), color=discord.Color.blue())
            embed.set_image(url = 'https://cdn.discordapp.com/attachments/820049088447905853/890614236559069235/unknown.png')
            await message.channel.send(embed=embed)
        elif message.content == "!아브":
            embed = discord.Embed(timestamp=datetime.datetime.utcnow(), color=discord.Color.blue())
            embed.set_image(url = 'https://cdn.discordapp.com/attachments/843444463120154668/925980078796578876/unknown.png')
            await message.channel.send(embed=embed)

    if message.content.startswith("!우리가게영업함"):
        embed = discord.Embed(timestamp=datetime.datetime.utcnow(), color=discord.Color.blue())
        embed.set_image(url = 'https://cdn.discordapp.com/attachments/843444463120154667/924583977963110400/IMG_2298.jpg')
        await message.channel.send(embed=embed)

    if message.content.startswith("!로스런쌀쌀"):
        embed = discord.Embed(timestamp=datetime.datetime.utcnow(), color=discord.Color.blue())
        embed.set_image(url = 'https://cdn.discordapp.com/attachments/843444463120154667/927112882687197184/unknown.png')
        await message.channel.send(embed=embed)

## 아직 해야 할것
    if client.get_channel(724168494480097280):
        print(client.get_channel(724168494480097280))
        print('?????')
        embed = discord.Embed(timestamp=datetime.datetime.utcnow(), color=discord.Color.blue())
        embed.add_field(name = "코리아 디스코드 알림", value = '떳냐?')
        await message.channel.send(embed=embed)

## 이거 괜찮냐;
    if message.content.startswith("!계정정보_"):
        id = message.content.split('_')[-1]
        # id = '로스런탭탭'
        list_char = crawl(id)
        # val_serv = ""
        val_char_id = ""
        val_job = ""
        val_lv = ""
        # print(list_char)
        embed = discord.Embed(title = id + "님의 계정 정보",timestamp=datetime.datetime.utcnow(), color=discord.Color.blue())
        name,cl,lv,png_url = list_char[0][1:]
        embed.set_thumbnail(url = png_url)
            # embed.set_thumbnail(url = 'https://cdn.discordapp.com/emojis/875782790086529024.png?v=1')
        for idx in range(len(list_char)):
            # val_serv += list_char[idx][0] + "\n"
            val_char_id += list_char[idx][1] + "\n"
            val_job += list_char[idx][2] + "\n"
            val_lv += str(list_char[idx][3]) + "\n"
        # embed.add_field(name = '서버',value = val_serv)
        embed.add_field(name = '캐릭터 아이디',value = val_char_id)
        embed.add_field(name = '직업',value = val_job)
        embed.add_field(name = '레벨',value = val_lv)
        await message.channel.send(embed=embed)


client.run(key)