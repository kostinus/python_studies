from gtts import gTTS  # Импортируем библиотеку для работы с текстом в речь
import random
import os
import telebot  # Если вы используете pyTelegramBotAPI
from your_ai_module import get_ai_response  # Импорт функции для генерации ответа ИИ

# Создаем экземпляр бота (замените 'YOUR_BOT_TOKEN' на ваш токен бота)
bot = telebot.TeleBot('8162476786:AAEWhLQYdB64Y4EJsDgxF4Tz7veikPTrn-U')


### Часть 2: Команда `/game` для игры "Камень-ножницы-бумага"

@bot.message_handler(commands=['game'])
def play_game(message):
    bot.reply_to(
        message,
        "Давайте сыграем в Камень-ножницы-бумага! Напишите ваш выбор: Камень, Ножницы или Бумага."
    )

@bot.message_handler(func=lambda message: message.text.lower() in ['камень', 'ножницы', 'бумага'])
def game_response(message):
    user_choice = message.text.lower()
    options = ['камень', 'ножницы', 'бумага']
    bot_choice = random.choice(options)

    if user_choice == bot_choice:
        result = "Ничья!"
    elif (user_choice == 'камень' and bot_choice == 'ножницы') or \
         (user_choice == 'ножницы' and bot_choice == 'бумага') or \
         (user_choice == 'бумага' and bot_choice == 'камень'):
        result = "Вы выиграли!"
    else:
        result = "Вы проиграли!"

    bot.reply_to(
        message,
        f"Вы выбрали: {user_choice.capitalize()}\n"
        f"Я выбрал: {bot_choice.capitalize()}\n"
        f"{result}"
    )


### Часть 3: Обработка обычных сообщений с озвучкой ответа

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    user_message = message.text
    bot.send_chat_action(message.chat.id, 'typing')  # Показываем статус "печатает..."

    # Отправляем сообщение "Думаю над ответом..."
    thinking_message = bot.reply_to(message, "Думаю над ответом...")
    try:
        ai_response = get_ai_response(user_message)  # Получаем ответ от нейросети
        bot.edit_message_text(chat_id=thinking_message.chat.id, message_id=thinking_message.message_id, text=ai_response)

        # Создаем голосовой файл с помощью gTTS
        tts = gTTS(ai_response, lang='ru')  # Устанавливаем язык на русский
        audio_file = f"response_{random.randint(1000, 9999)}.mp3"  # Генерируем уникальное имя файла
        tts.save(audio_file)  # Сохраняем аудио

        # Отправляем голосовое сообщение
        with open(audio_file, 'rb') as audio:
            bot.send_voice(chat_id=message.chat.id, voice=audio)

        # Удаляем временный файл после отправки
        os.remove(audio_file)

    except Exception as e:
        bot.edit_message_text(chat_id=thinking_message.chat.id, message_id=thinking_message.message_id, text="Произошла ошибка. Попробуйте позже!")
        print(f"Ошибка: {e}")


### Часть 4: Запуск бота
# Запуск бота
print("Бот запущен и работает...")
bot.infinity_polling()