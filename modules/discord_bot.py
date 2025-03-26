import discord, dotenv, os

# Отримання змінної середовища
dotenv.load_dotenv()
# Отримання токену змінної середовища
TOKEN = os.getenv("TOKEN")

# Встановлює дозволів, зокрема до відстежування повідомлень
intents = discord.Intents.default()
intents.message_content = True

# Створюємо клієнтаь та передаємо йому дозволи
bot = discord.Client(intents= intents)

# Створення події, яка відбувається при запуску бота
@bot.event
async def on_ready():
    print("Bot is ready")

@bot.event
# Створення події, яка відбувається при отриманні повідомлення
async def on_message(message):
    # Отримання контенту повідомлення
    content = message.content
    # Якщо автор повідомлення не бот
    if message.author != bot.user:
        # Якщо повідомлення не пусте
        if content:
            # Відправляємо повідомлення с таким самим контентом
            await message.channel.send(content)