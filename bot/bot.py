import discord, datetime
from bot.modals.evalue import Embed
import plagiarismdeny as discqol
bot=discqol.define()
bot = bot.anthro()

@bot.event
async def on_ready():
    print(f'\x1b[32mLogged in as {bot.user}!\x1b[0m')
    qldkfj = discqol.WhyDoIHavetoDoThis(bot=bot)
    await qldkfj.a54ab7da3bb9k()

@bot.slash_command(name='value', description='Skyblock Account Value')
async def value(ctx, name: str): 
    embed = discord.Embed(
        title="Fetching...",
        description=f"Obtaining data from api, please wait...",
        color=0xFF007B
    )
    embed.set_footer(text='Made by interceptic', icon_url='https://avatars.githubusercontent.com/u/121205983?s=400&u=e5e1ec3c308a713e198f46aff29038bc4dca1d9d&v=4')
    embed.timestamp = datetime.datetime.now()
    await ctx.respond(embed=embed)
    try:
        class_thing = Embed()
        await class_thing.send_embed(ctx, name)
        value = discqol.randomizer(ctx)
        await value.randomization()
    except Exception as error:
        print('Value:', error)