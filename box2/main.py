import discord
from discord.ext import commands
from config import token
from logic import Pokemon, Wizard, Fighter
import random

intents = discord.Intents.default()
intents.messages = True
intents.message_content = True
intents.guilds = True
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

@bot.command()
async def go(ctx):
    author = ctx.author.name
    if author not in Pokemon.pokemons:
        chance = random.randint(1, 3)
        print(chance)
        if chance == 1:
            pokemon = Pokemon(author)
        elif chance == 2:
            pokemon = Wizard(author)
        elif chance == 3:
            pokemon = Fighter(author)
        await ctx.send(await pokemon.info())
        image_url = await pokemon.show_img()
        if image_url:
            embed = discord.Embed()
            embed.set_image(url=image_url)
            await ctx.send(embed=embed)
        else:
            await ctx.send("Tidak dapat memuat gambar pokemon.")
    else:
        await ctx.send("Anda sudah memiliki pokemon.")

@bot.command()
async def attack(ctx):
    target = ctx.message.mentions[0] if ctx.message.mentions else None
    if target:
        if target.name in Pokemon.pokemons and ctx.author.name in Pokemon.pokemons:
            enemy = Pokemon.pokemons[target.name]
            attacker = Pokemon.pokemons[ctx.author.name]
            result = await attacker.attack(enemy)
            await ctx.send(result)
        else:
            await ctx.send("Kedua pihak harus memiliki pokemon untuk pertempuran!")
    else:
        await ctx.send("Tentukan pengguna yang ingin Anda menyerang, menyebutnya.")

@bot.command()
async def info(ctx):
    author = ctx.author.name
    if author in Pokemon.pokemons:
        pokemon = Pokemon.pokemons[author]
        await ctx.send(await pokemon.info())
    else:
        await ctx.send("Anda tidak memiliki pokemon!")

@bot.command()
async def feed(ctx):
    author = ctx.author.name
    if author in Pokemon.pokemons:
        pokemon = Pokemon.pokemons[author]
        response = await pokemon.feed()
        await ctx.send(response)
    else:
        await ctx.send("Anda tidak memiliki pokemon!")


bot.run(token)
