from datetime import timedelta

import nextcord
import ai

from nextcord.ext import commands, tasks
from constants import TOKEN, PREFIX
from text_moudle import remove_punct, text_analyzer, if_severe_sentence

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

    # considered offensive
    if if_severe_sentence(percent):
        response = ai.generate_ai_check_message(content)

        # Timeout user
        if response == "offensive":
            duration = nextcord.utils.utcnow() + timedelta(minutes=1)
            try:
                await message.author.edit(timeout=duration, reason="offensive words")
                await message.channel.send(f"**{message.author.mention} has been timed out for offensive words.**")
                await message.delete()

            except:
                print("I don't have permissions to time out the user.")

    await bot.process_commands(message)

bot.run(TOKEN)
