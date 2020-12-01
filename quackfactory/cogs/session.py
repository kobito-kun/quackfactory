from discord.ext import commands
import discord
import logging

intents = discord.Intents.default()
intents.reactions = True
intents.members = True
client = discord.Client(intents=intents)

class Session(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

@client.event
async def on_voice_state_update(member, before, after):

    guild = member.guild
    role = "Test"
    everyone = "@everyone" 
    channel_id = 756574459556659323
    message = f"Hey! {member} needs a rubber duck!"

    if before.channel is None and after.channel.id == channel_id:
        await after.channel.set_permissions(discord.utils.get(guild.roles, name=role), connect=True)
        await after.channel.set_permissions(discord.utils.get(guild.roles, name=everyone), connect=False)
        await after.channel.edit(user_limit=2)

        for member in guild.members:
            for role in member.roles:
                if role.name == "Test": # Rubberduck role idk why but it doesnt work using a variable ;(
                    await member.send(message)

def setup(bot):
    bot.add_cog(Session(bot))