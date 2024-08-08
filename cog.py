"""The cog for bf2042 portal"""
import discord
from discord.ext import commands
from discord import app_commands
from . import server_list, player_list


class Bf1Marne(commands.Cog, name="marne"):
    """Battlefield 1 Marne"""

    def __init__(self, bot: commands.AutoShardedBot):
        self.bot = bot
        super().__init__()

    group = app_commands.Group(name="marne", description="Battlefield 1 Marne cog")
    group.allowed_installs = app_commands.AppInstallationType(guild=True, user=True)
    
    @group.command(
        name="serverlist",
        description="List all the servers based on a searchterm for Battlefield 1 marne.",
    )
    @app_commands.user_install()
    async def serverlist(
        self, interaction: discord.Interaction, servername: str
    ) -> None:
        """marne servers"""
        await interaction.response.defer()
        await server_list.main(interaction, servername)

    @serverlist.error
    async def serverlist_error(self, interaction: discord.Interaction, _error) -> None:
        """Error handling"""
        embed = discord.Embed(
            color=0xE74C3C, description="Failed to get serverlist for marne"
        )
        await interaction.followup.send(embed=embed)

    @group.command(
        name="playerlist",
        description="Get playerlist of the server in Battlefield 1 marne.",
    )
    @app_commands.user_install()
    async def playerlist(
        self, interaction: discord.Interaction, servername: str
    ) -> None:
        """marne playerlist"""
        await interaction.response.defer()
        await player_list.main(interaction, servername)

    @playerlist.error
    async def playerlist_error(self, interaction: discord.Interaction, _error) -> None:
        """Error handling"""
        embed = discord.Embed(
            color=0xE74C3C, description="Failed to get playerlist for a server on marne"
        )
        await interaction.followup.send(embed=embed)
