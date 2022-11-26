import nextcord
from nextcord.ext import commands

description = 'YOmit'
intents = nextcord.Intents.default()
intents.members = True
intents.message_content = True


bot = commands.Bot(command_prefix='|', description=description, intents=intents)

