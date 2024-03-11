import discord
from discord.ext import commands
import os 
import random
import requests

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')


@bot.command()
async def mem(ctx):

    with open(f'images/{random.choice(os.listdir('images'))}', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)

def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    print(data)
    return data['url']

@bot.command()
async def case(ctx):
    await ctx.reply(f'Кручу кейс, посмотрим, что-же выпадет?!', mention_author=False)

    n = random.randint(1,100)
    print(n)
    p = ''
    if n < 51:
        p = 'shirp'
    elif n < 81:
        p = 'Epic'
    elif n < 91:
        p = "Lega" 
    else:
        p = "HistoryDragon"

    skins1 = os.listdir('case')
    skins2 = []
    for x in skins1:
        if p in x:
            skins2.append(x)

    with open(f'case/{random.choice(skins2)}','rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)


@bot.command('duck')
async def duck(ctx):
    '''По команде duck вызывает функцию get_duck_image_url'''
    await ctx.send(get_duck_image_url())


@bot.command()
async def eco(ctx):
    embed=discord.Embed(title="Экология(Кликабельно)", url="https://www.products.pcc.eu/ru/blog/%D1%87%D1%82%D0%BE-%D1%82%D0%B0%D0%BA%D0%BE%D0%B5-%D1%8D%D0%BA%D0%BE%D0%BB%D0%BE%D0%B3%D0%B8%D1%8F-%D0%B3%D0%BB%D0%B0%D0%B2%D0%BD%D0%BE%D0%B5-%D0%BE%D0%B1-%D1%8D%D1%82%D0%BE%D0%BC-%D0%BF/", description="Не мусори на природе, не порти экологию!", color=0x3ee133)
    embed.set_author(name="Ответ на запрос!")
    embed.add_field(name="Зачем?", value="Она помогает нам сохранять природу!", inline=True)
    embed.add_field(name="Что сделать?", value="Ознакомьтесь с информацией по ссылке!", inline=True)
    await ctx.send(embed=embed)

    



@bot.command()
async def helping(ctx):
    await ctx.reply(mention_author=False)
    await ctx.reply(f'Команды бота \n 1.!spam - позволяет поспамить определённое кол-во сообщений. \n 2. !heh посмеяться вместе с ботом. \n 3. !hello - поздороваться с ботом. \n 4. !add - сложить 2 числа / или 2 текста в едино.')

bot.run("MTIxMjQ0NjMxMjA0MjA3MDE2Nw.G2BOQc.kw6ejZ6qZBK39FBRc8g1P_zHJM2iQt1vpoitCM")