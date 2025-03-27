import discord, dotenv, os
from .ai import get_response
# Отримання змінної середовища
dotenv.load_dotenv()
# Отримання токену змінної середовища
TOKEN = os.getenv("TOKEN")

# Встановлює дозволів, зокрема до відстежування повідомлень
intents = discord.Intents.default()
intents.message_content = True

# Створюємо бота та передаємо йому дозволи
bot = discord.Client(intents= intents)

# Створення події, яка відбувається при запуску бота
@bot.event
async def on_ready():
    print("Bot is ready")

@bot.event
# Створення події, яка відбувається при отриманні повідомлення
async def on_message(message):
    # Якщо автор повідомлення не бот
    if message.author != bot.user:
        # Отримання контенту повідомлення
        content = message.content
        # Якщо повідомлення не пусте
        if content:
            # Отримання відповіді від бота
            answer = await get_response(request= content)
            # Отримання повідомлення для відпові з указанням на повідомлення
            message_for_answer = await message.channel.fetch_message(message.id)
            # Відправлення відповіді на повідомлення
            await message_for_answer.reply(answer)