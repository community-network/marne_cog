import json
import aiohttp
import discord
import urllib.parse
from global_mapping import marne as MARNE
from . import find_server


async def main(interaction: discord.Interaction, searchterm: str):
    servers = await find_server.main(servername=searchterm, limit=10)
    embed = discord.Embed(
        color=0xFFA500,
        title=f"{searchterm} - Battlefield 1 Marne Servers",
    )
    for server in servers:
        server_description = f"on **{MARNE.MAPS.get(server.get('mapName', '').split('/')[-1], server.get('mapName', ''))}** with **{server.get('currentPlayers', 0)}/{server.get('maxPlayers', 0)}** players, **{MARNE.MODES.get(server.get('gameMode', ''), server.get('gameMode', ''))}**\n"
        server_description += f"[More info](https://gametools.network/servers/bf1marne/gameid/{server.get('id')}/pc)"
        embed.add_field(
            name=server.get("name"),
            value=server_description,
            inline=False,
        )
    # footer
    embed.add_field(
        name="\u2063",
        value=f"[Open serverlist](https://gametools.network/servers?search={urllib.parse.quote(searchterm)}&game=bf1marne)",
        inline=False,
    )
    await interaction.followup.send(embed=embed)
