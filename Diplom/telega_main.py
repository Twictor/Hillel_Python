import telebot
from data_manager import DataManager
from person import Person

TOKEN = "8037728324:AAG4pET61SMptKMEG68Z4TJCWImTdGMpMaw"
bot = telebot.TeleBot(TOKEN)
db = DataManager()

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Привіт!\nВведіть /add для додавання запису або /search для пошуку.")

@bot.message_handler(commands=['add'])
def add_person(message):
    bot.send_message(message.chat.id, "Введіть дані: Ім'я Прізвище По-батькові ДатаНародження ДатаСмерті Стать (m/f)")

    @bot.message_handler(content_types=['text'])
    def process_add(message):
        try:
            parts = message.text.split()
            if len(parts) < 2:
                bot.send_message(message.chat.id, "Недостатньо даних! Повторіть введення.")
                return
            person = Person(*parts)
            db.add_person(person)
            bot.send_message(message.chat.id, f"Запис додано: {person.first_name}")
        except ValueError as e:
            bot.send_message(message.chat.id, f"Помилка: {e}")

@bot.message_handler(commands=['search'])
def search(message):
    bot.send_message(message.chat.id, "Введіть пошуковий запит:")

    @bot.message_handler(content_types=['text'])
    def process_search(message):
        results = db.search(message.text)
        if results:
            response = "\n".join([f"{p.first_name} {p.last_name or ''} {p.patronymic or ''}, {p.calculate_age()} років" for p in results])
        else:
            response = "Нічого не знайдено"
        bot.send_message(message.chat.id, response)


bot.polling()
