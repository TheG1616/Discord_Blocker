import nextcord

from nextcord.ext import commands, tasks
from constants import TOKEN, PREFIX

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

    # TODO: call function here
    await bot.process_commands(message)

bot.run(TOKEN)
