import os
import aiosqlite
from bot.build_embed import build
import discord
from discord.ui import View, Button, InputText, Modal
from bot.modals.views.button import button_view


async def build(title, description, color):
    embed = discord.Embed(title=title, description=description, color=color)
    return embed

class Setup:
    @staticmethod
    async def check(ctx):
        if not os.path.exists("./database/database.db"):
            embed = await build("Database Not Found", "Please initiate the setup process by clicking the button below \n **Step 1/?**", 0xFF0000)
            view = button_view("Role ID of Sellers", "ID")
            await ctx.respond(embed=embed, view=view)
            
