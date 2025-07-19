import discord
from discord.ext import commands
import os

intents = discord.Intents.default()
intents.guilds = True
intents.guild_messages = True

bot = commands.Bot(command_prefix='!', intents=intents)

OWNER_ID = int(os.environ['OWNER_ID'])

@bot.event
async def on_ready():
    print(f'✅ Bot connesso come {bot.user}')

@bot.command()
async def oscura(ctx, channel: discord.TextChannel):
    if ctx.author.id != OWNER_ID:
        return await ctx.send("❌ Non sei autorizzato.")
    overwrites = {
        ctx.guild.default_role: discord.PermissionOverwrite(view_channel=False),
        ctx.author: discord.PermissionOverwrite(view_channel=True)
    }
    await channel.edit(overwrites=overwrites)
    await ctx.send(f'🔒 {channel.mention} è ora visibile solo a te.')

@bot.command()
async def mostra(ctx, channel: discord.TextChannel):
    if ctx.author.id != OWNER_ID:
        return await ctx.send("❌ Non sei autorizzato.")
    overwrites = {
        ctx.guild.default_role: discord.PermissionOverwrite(view_channel=True),
    }
    await channel.edit(overwrites=overwrites)
    await ctx.send(f'🔓 {channel.mention} è ora visibile a tutti.')

bot.run(os.environ['DISCORD_TOKEN'])
