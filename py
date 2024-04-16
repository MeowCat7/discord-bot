import discord
import random
from discord.ext import commands

#yetki ayarları
intents = discord.Intents.default()
#message.content mesajın içeriğinin okunabilmesi için gerekli.
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)
copgifler=["https://tenor.com/view/dumpster-trash-can-hide-jump-to-trash-gif-12324630","https://tenor.com/view/dumping-trash-daniel-labelle-frustrated-garbage-trash-gif-27186872"]
@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')

@bot.command()
async def hello(ctx):
    await ctx.send('hi!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def temiz(ctx):
    await ctx.send("Çevreyi Temiz Tutmayı Unutma")

@bot.command()
async def çöp(ctx,a=random.choice(copgifler)): 
    await ctx.send(a)


@bot.command()
async def add(ctx, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send(left + right)

@bot.command()
async def mem(ctx):
    with open('M2L1/images/M2L1-T2-1_tlaheo.png', 'rb') as f:
        # Dönüştürülen Discord kütüphane dosyasını bu değişkende saklayalım!
        picture = discord.File(f)
   # Daha sonra bu dosyayı bir parametre olarak gönderebiliriz!
    await ctx.send("Al sana mem!")
    await ctx.send(file=picture)

bot.run("")
