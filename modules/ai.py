import openai, dotenv, os

# Отримаємо змінну середовища з ключем
dotenv.load_dotenv()
KEY = os.getenv("KEY")

# Створення клієнта для взаємодії з OpenAI
client_openai = openai.AsyncOpenAI(api_key = KEY)

# Функція, яка отримує запит та повертає відповідь
async def get_response(request: str):
    # Задаємо запит
    response = await client_openai.chat.completions.create(
        model="gpt-4o-mini", # Вказуємо модель
        messages=[{
            "role": "user", # Вказуємо роль користувач
            "content": request, # Вказуємо питання до бота
        }]
    )
    # Повертаємо тільки контент відповіді
    return response.choices[0].message.content

