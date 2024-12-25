import asyncio
import aiohttp
import tls_client
from minecraft.info.username import user_data
from bot.build_embed import build



async def shiyu_data(ctx, username):
    user = await user_data(ctx, username)
    
    session = tls_client.Session(
        client_identifier="chrome112",
        random_tls_extension_order=True
    )
        
    try:    
        response = session.get(f"https://sky.shiiyu.moe/api/v2/profile/{user['id']}")
        if response.status_code != 200:
                embed = await build(f"Caught Exception: {response.status}", f"**From Shiyu API: {response.reason}**", 0xFF0000)
                await ctx.edit(embed=embed)
                return
        else:
            username = response.json()
            return username
    except Exception as error:
        print(f'Exception triggered: {error}')      
        return error 