import os
import telebot
from flask import Flask
from threading import Thread

# Получаем токен из переменной окружения (добавь в Render)
TOKEN = os.getenv("TOKEN")

bot = telebot.TeleBot(TOKEN)  # Создаём объект бота

app = Flask(__name__)

@app.route('/')
def home():
    return "I'm alive!"

def run():
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", 5000)))  # Используем порт из Render

Thread(target=run).start()  # Запускаем Flask-сервер в фоне

# Обработчик команды /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message,    f"Привет, {message.from_user.first_name}!\n"
        "❗ Это Единственный ОФИЦИАЛЬНЫЙ канал-переходник\n\n"
        "⚡ Остальные каналы, которые представлены в поиске - МОШЕННИКИ!\n\n"
        "📝 Ниже Ссылка на наш закрытый канал.\n\n"
        "✅ Заявки в канал принимаются автоматически!\n\n"
        "https://t.me/+quQ4ll6cNPQ1YWVi\n"
        "https://t.me/+quQ4ll6cNPQ1YWVi\n"
        "https://t.me/+quQ4ll6cNPQ1YWVi\n")

# Запускаем бота
bot.polling(none_stop=True)
