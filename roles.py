# This example requires the 'members' privileged intents
import nextcord
from nextcord.ext import commands
from bot import bot
from secrets import TOKEN


class Bot(commands.Bot):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.role_message_id = 1038546208869847100  # ID of the message that can be reacted to to add/remove a role.
        self.emoji_to_role = {
            nextcord.PartialEmoji(name=":em:"): [
                1038033881133228051, # ne
                1038034018882555954, # en
                1038034492281073684, # ma
                1038034521452458004, # ckv
                1038034921446461511, # lo
                1038034266883358750, # gd
                1038032205328433253  # gs
            ],
            nextcord.PartialEmoji(name="cm"): [
                1038033881133228051, # ne
                1038034018882555954, # en
                1038034492281073684, # ma
                1038034521452458004, # ckv
                1038034921446461511, # lo
                1038034266883358750, # gd
                1038032205328433253, # gs
                1038034389587734558  # ec
            ],
            nextcord.PartialEmoji(name="ng"): [
                1038033881133228051, # ne
                1038034018882555954, # en
                1038034492281073684, # ma
                1038034521452458004, # ckv
                1038034921446461511, # lo
                1038034266883358750, # gd
                1038032127746392146, # bi
                1038032049879121970  # sk
            ],
            nextcord.PartialEmoji(name="nt"): [
                1038033881133228051, # ne
                1038034018882555954, # en
                1038034492281073684, # ma
                1038034521452458004, # ckv
                1038034921446461511, # lo
                1038034266883358750, # gd
                1038034087757234216, # wb
                1038032049879121970, # sk
                1038031766641967125  # na
            ]
        }

    async def on_raw_reaction_add(self, payload: nextcord.RawReactionActionEvent):
        """Gives a role based on a reaction emoji."""
        # Make sure that the message the user is reacting to is the one we care about.
        if payload.message_id != self.role_message_id:
            return

        guild = self.get_guild(payload.guild_id)
        if guild is None:
            # Check if we're still in the guild and it's cached.
            return

        try:
            role_ids = self.emoji_to_role[payload.emoji]
        except KeyError:
            # If the emoji isn't the one we care about then exit as well.
            return

        for role_id in role_ids:
            role = guild.get_role(role_id)
            if role is None:
                # Make sure the role still exists and is valid.
                return

            try:
                # Finally, add the role.
                await payload.member.add_roles(role)
            except nextcord.HTTPException:
                # If we want to do something in case of errors we'd do it here.
                pass

    async def on_raw_reaction_remove(self, payload: nextcord.RawReactionActionEvent):
        """Removes a role based on a reaction emoji."""
        # Make sure that the message the user is reacting to is the one we care about.
        if payload.message_id != self.role_message_id:
            return

        guild = self.get_guild(payload.guild_id)
        if guild is None:
            # Check if we're still in the guild and it's cached.
            return

        try:
            role_ids = self.emoji_to_role[payload.emoji]
        except KeyError:
            # If the emoji isn't the one we care about then exit as well.
            return

        for role_id in role_ids:
            role = guild.get_role(role_id)
            if role is None:
                # Make sure the role still exists and is valid.
                return

            # The payload for `on_raw_reaction_remove` does not provide `.member`
            # so we must get the member ourselves from the payload's `.user_id`.
            member = guild.get_member(payload.user_id)
            if member is None:
                # Make sure the member still exists and is valid.
                return

            try:
                # Finally, remove the role.
                await member.remove_roles(role)
            except nextcord.HTTPException:
                # If we want to do something in case of errors we'd do it here.
                pass


@Bot.event
async def on_ready():
    print(f"Logged in as {bot.user} (ID: {bot.user.id})")


if __name__ == '__main__':
	bot.run(TOKEN)
