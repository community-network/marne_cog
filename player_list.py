import discord
from global_mapping import marne as MARNE
from tabulate import tabulate
from . import find_server


async def main(interaction: discord.Interaction, searchterm: str):
    servers = await find_server.main(servername=searchterm, limit=1)
    if len(servers) == 0:
        await interaction.followup.send("No servers found.")
        return

    current_server = servers[0]
    players = []
    if current_server.get("playerList", "") != "":
        players = current_server.get("playerList", [])

    server_players = {}
    server_players["Team 1"] = []
    server_players["Team 2"] = []
    for player in players:
        server_players[f'Team {player.get("team", "1")}'].append(player.get("name", ""))

    table = tabulate(server_players, headers="keys")
    discord_table = "```ini\n" + table + "```"

    embed = discord.Embed(
        color=0xFFA500,
        title=f'{current_server.get("name", "")} players',
        description=discord_table,
        url=f"https://gametools.network/servers/bf1marne/gameid/{current_server.get('id', '')}/pc",
    )
    embed.set_footer(
        text=f"on {MARNE.MAPS.get(current_server.get('mapName', '').split('/')[-1], current_server.get('mapName', ''))} with {current_server.get('currentPlayers', 0)} players, on {MARNE.MODES.get(current_server.get('gameMode', ''), current_server.get('gameMode', ''))}"
    )
    await interaction.followup.send(embed=embed)
