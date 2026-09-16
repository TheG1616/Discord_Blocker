from datetime import timedelta

import nextcord
import ai

from nextcord.ext import commands, tasks
from constants import TOKEN, PREFIX
from text_moudle import remove_punct, text_analyzer, if_severe_sentence
from image import check_image
from care_json import add_new_event, get_settings, get_count_of_offence

# intents
intents = nextcord.Intents.default()
intents.members = True
intents.message_content = True

# bot's config
bot = commands.Bot(command_prefix=PREFIX, intents=intents)
bot.remove_command("help")


@bot.event
async def on_ready():
    print(f"{bot.user} is ready")
    await bot.change_presence(
        activity=nextcord.Activity(
        type=nextcord.ActivityType.watching,
        name="you!"
        )
    )


@bot.event
async def on_message(message):
    # bot won't reply himself in a endless loop.
    if message.author.bot:
        return
    content = remove_punct(message.content)
    percent = text_analyzer(content)

    if message.attachments:
        if not check_image(message.attachments[0].url):
            return

        else:
            settings = get_settings()
            amount = get_count_of_offence(message.author.name) + 1
            if amount == settings["kick_amount"]:
                await message.author.kick(reason="offensive image")
                await message.channel.send(f"**{message.author.mention} has been kicked for offensive image.**")
                add_new_event(message.author, str(message.created_at), "image", "kick")

            elif amount == settings["ban_amount"]:
                await message.author.ban(reason="offensive image")
                await message.channel.send(f"**{message.author.mention} has been banned for offensive image.**")
                add_new_event(message.author, str(message.created_at), "image", "ban")

            else:
                duration = nextcord.utils.utcnow() + timedelta(minutes=settings["timeout_duration"])
                await message.author.edit(timeout=duration, reason="offensive image")
                await message.channel.send(f"**{message.author.mention} has been timed out for offensive image.**")
                add_new_event(message.author, str(message.created_at), "image", "timeout")

            await message.delete()


    # considered offensive
    if if_severe_sentence(percent):
        response = ai.generate_ai_check_message(content)

        # Timeout user
        if response == "offensive":
            settings = get_settings()
            amount = get_count_of_offence(message.author.name) + 1
            if amount == settings["kick_amount"]:
                await message.author.kick(reason="offensive text")
                await message.channel.send(f"**{message.author.mention} has been kicked for offensive text.**")
                add_new_event(message.author, str(message.created_at), "text", "kick")

            elif amount == settings["ban_amount"]:
                await message.author.ban(reason="offensive text")
                await message.channel.send(f"**{message.author.mention} has been banned for offensive text.**")
                add_new_event(message.author, str(message.created_at), "text", "ban")

            else:
                duration = nextcord.utils.utcnow() + timedelta(minutes=settings["timeout_duration"])
                await message.author.edit(timeout=duration, reason="offensive text")
                await message.channel.send(f"**{message.author.mention} has been timed out for offensive text.**")
                add_new_event(message.author, str(message.created_at), "text", "timeout")

            await message.delete()

    await bot.process_commands(message)


bot.run(TOKEN)
