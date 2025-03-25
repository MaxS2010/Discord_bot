import discord


# Встановлює дозволів, зокрема до відстежування повідомлень
intents = discord.Intents.default()
intents.message_content = True

# Створюємо клієнтаь та передаємо йому дозволи
bot = discord.Client(intents= intents)

# 
@bot.event
async def on_ready():
    print("Bot is ready")

# 
@bot.event
# 
async def on_message(message):
    # 
    content = message.content
    # 
    if message.author != bot.user:
        # 
        if content:
            # 
            await message.channel.send(content)