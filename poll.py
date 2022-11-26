import asyncio
import nextcord
from nextcord import SlashOption
from nextcord.ext import commands
from typing import Optional
from bot import bot
from secrets import GUILDS

emojis = {1: '1️⃣', 2: '2️⃣', 3: '3️⃣', 4: '4️⃣', 5: '5️⃣', 6: '6️⃣', 7: '7️⃣', 8: '8️⃣', 9: '9️⃣', 10: '🔟'}

@bot.slash_command(guild_ids=GUILDS)
async def poll(
	interaction: nextcord.Interaction,
	message: str,
	option1: str,
	option2: str,
	option3: Optional[str] = SlashOption(required=False),
	option4: Optional[str] = SlashOption(required=False),
	option5: Optional[str] = SlashOption(required=False),
	option6: Optional[str] = SlashOption(required=False),
	option7: Optional[str] = SlashOption(required=False),
	option8: Optional[str] = SlashOption(required=False),
	option9: Optional[str] = SlashOption(required=False),
	option10: Optional[str] = SlashOption(required=False)
	):
	
	options = [option1, option2, option3, option4, option5, option6, option7, option8, option9, option10]

	i = 1	
	message = f'{message}'
	print(f'poll created by: "{interaction.user}"\nmessage: "{message}"')
	for option in options:
		if option != None:
			print(f'{emojis[i]}  {option}')
			message += f'\n{emojis[i]} {option}'
			
			i += 1	
	await interaction.send(message)
	poll = await interaction.original_message()
	j = 1
	while j != i:
		emoji = emojis[j]
		await poll.add_reaction(emoji)
		j += 1
