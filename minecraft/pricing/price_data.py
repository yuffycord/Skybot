import json
from minecraft.pricing.values.catacombs import catacombs
from minecraft.pricing.values.networth import networth
from minecraft.pricing.values.hotm import hotm
from minecraft.pricing.values.skills import skills
from minecraft.pricing.values.slayers import slayers
from minecraft.pricing.values.crimson import crimson


with open("config.json") as conf:
    config = json.load(conf)


async def pricer(dict, username):
    priced_dict = {}
    priced_dict = {username: {
        "total": 0,
        "cata": {
            "level": 0
        },
        "total_hotm": 0,
        "hotm": {
            "level": 0,
            "mithril_powder": 0,
            "gemstone_powder": 0,
            "glacite_powder": 0
        },
        "total_nw": 0,
        "networth": {
            "unsoulbound": 0,
            "soulbound": 0
        },
        "total_skills": 0,
        "skills": {
            "average": 0,
            "combat": 0,
            "fishing": 0,
            "foraging": 0,
            "mining": 0,
            "farming": 0
        },
        "total_slayers": 0,
        "slayers": {
            "zombie": 0,
            "spider": 0,
            "wolf": 0,
            "enderman": 0,
            "vampire": 0,
            "blaze": 0
        },
        "total_crimson": 0,
        "crimson": {
            "mage": 0,
            "barbarian": 0
        }
    }}

    dict, priced_dict, username = await catacombs(dict, priced_dict, username)
    dict, priced_dict, username = await networth(dict, priced_dict, username)
    dict, priced_dict, username = await hotm(dict, priced_dict, username)
    dict, priced_dict, username = await skills(dict, priced_dict, username)
    dict, priced_dict, username = await slayers(dict, priced_dict, username)
    priced_dict = await crimson(dict, priced_dict, username)

    priced_dict[username]['total'] = round(priced_dict[username]['cata']['level'] + priced_dict[username]['total_hotm'] + priced_dict[username]['total_nw'] + priced_dict[username]['total_skills'] + priced_dict[username]['total_slayers'] + priced_dict[username]['total_crimson'], 2)

    a = 's'
    return priced_dict, a