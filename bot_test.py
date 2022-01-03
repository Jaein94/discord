import numpy as np
import discord
from discord.ext import commands
import datetime

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print("봇이 시작되었습니다.")

@bot.command()
async def test(ctx,arg):
    await ctx.send(arg)

@bot.event
async def on_message(message): # on_message() event : when the bot has recieved a message
    #To user who sent message
    # await message.author.send(msg)
    print(message.content)
    if message.author == bot.user:
        return
    if message.content.startswith("!help") or message.content.startswith("!도움말"):
        embed = discord.Embed(title="명령어 사용방법!", description="!전적 (소환사 이름 - 띄어쓰기 붙여쓰기 상관없습니다)", color=0x5CD1E5)
        embed.set_footer(text='Service provided by Hoplin.',
                         icon_url='https://avatars2.githubusercontent.com/u/45956041?s=460&u=1caf3b112111cbd9849a2b95a88c3a8f3a15ecfa&v=4')
        await message.channel.send("도움말!", embed=embed)
        
@bot.command()
async def 안녕(ctx):
    await ctx.send('반갑습니다')

@bot.command()
async def 이름(ctx):
    await ctx.send('김태훈 바보 ㅎㅎ ')

@bot.command()
async def 명령어(ctx):
    embed = discord.Embed(title=f"{ctx.guild.name}", description="all commands", timestamp=datetime.datetime.utcnow(), color=discord.Color.blue())
    embed.add_field(name="Commands", value=f"{ctx.bot.all_commands.keys()}")
    # tmp = []
    # for i in ctx.bot.__dict__['all_commands'].keys():
    #     tmp.append(i)
    await ctx.send(embed=embed)


@bot.command()
async def info(ctx):
    embed = discord.Embed(title=f"{ctx.guild.name}", description="Lorem Ipsum asdasd", timestamp=datetime.datetime.utcnow(), color=discord.Color.blue())
    embed.add_field(name="Server created at", value=f"{ctx.guild.created_at}")
    embed.add_field(name="Server Owner", value=f"{ctx.guild.owner}")
    embed.add_field(name="Server Region", value=f"{ctx.guild.region}")
    embed.add_field(name="Server ID", value=f"{ctx.guild.id}")
    # embed.set_thumbnail(url=f"{ctx.guild.icon}")
    embed.set_thumbnail(url="https://pluralsight.imgix.net/paths/python-7be70baaac.png")

    await ctx.send(embed=embed)

@bot.command()
async def 예둔효율표(ctx):
    embed = discord.Embed(title=f"{ctx.guild.name}", description="예둔효율표", timestamp=datetime.datetime.utcnow(), color=discord.Color.blue())
    embed.set_image(url='https://cdn.discordapp.com/attachments/843444463120154667/924559339660931102/i14537745196.png')

    await ctx.send(embed=embed)

@bot.command()
async def 디붕전압(ctx):
    embed = discord.Embed(title=f"{ctx.guild.name}", description="디붕 전압;;;;;", timestamp=datetime.datetime.utcnow(), color=discord.Color.blue())
    embed.set_image(url='https://cdn.discordapp.com/attachments/843444463120154667/923974460703379557/unknown.png')

    await ctx.send(embed=embed)

bot.run('OTI0NTQ4MTc1OTIxMDQxNDA4.YcgKlg.GBF-L1Jpd8RC5aerWH_oPrRCxSY')