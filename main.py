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

@bot.command()
async def case2(ctx):
    await ctx.reply(mention_author=False)
    await ctx.reply(f'Кручу кейс, посмотрим, что-же выпадет?!')

    chances = {
        'HistoryDragon': 0.1,
        'M9': 0.2,
        'shirp': 0.5,
        'shirp2': 0.4
    }

    array = os.listdir('case')  # Получаем массив с названиями картинок
    array_chances = [chances.get(name, 1) for name in array]  # Задаем вероятности для каждой картинки, если нет значения - ставим по умолчанию 1

    chosen_picture = random.choices(array, weights=array_chances, k=1)[0]  # Выбираем картинку с учетом заданных вероятностей

    with open(f'case/{chosen_picture}', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)

@bot.command('duck')
async def duck(ctx):
    '''По команде duck вызывает функцию get_duck_image_url'''
    image_url = get_duck_image_url()
    await ctx.send(image_url)



#@bot.command()
#@commands.has_permissions(administrator = True)# команду сможет использовать роль в которой включена привилегия Администратор.
#@commands.has_any_role('Админчик типа да')# все у кого есть роль с именем Администратор могут использовать эту команду
#@commands.has_role(1216448687832567898)#надо вставить id роли которая сможет использовать эту команду
#async def warn(ctx, member: discord.Member, *, about: str):
    #if member:
        #embed = discord.Embed(color = 0x537cda, description = f'Участник **{member.name}** получил предупреждение от **{ctx.message.author.name}** по причине:\n**```\n{about}\n```**')
        #await ctx.send(embed = embed)
    #else:
       # embed = discord.Embed(color = 0x537cda, description = 'Ошибка в аргументах команды\nили участник не найден.', title = 'Ошибка')
        #await ctx.send(embed = embed)

@bot.command()
async def helping(ctx):
    await ctx.reply(mention_author=False)
    await ctx.reply(f'Команды бота \n 1.!spam - позволяет поспамить определённое кол-во сообщений. \n 2. !heh посмеяться вместе с ботом. \n 3. !hello - поздороваться с ботом. \n 4. !add - сложить 2 числа / или 2 текста в едино.')

bot.run("MTIxMjQ0NjMxMjA0MjA3MDE2Nw.G2BOQc.kw6ejZ6qZBK39FBRc8g1P_zHJM2iQt1vpoitCM")