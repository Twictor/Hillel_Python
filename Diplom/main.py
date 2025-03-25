import telebot
from data_manager import DataManager
from person import Person

TOKEN = "8037728324:AAG4pET61SMptKMEG68Z4TJCWImTdGMpMaw"

bot = telebot.TeleBot(TOKEN)
db = DataManager()


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.send_message(message.chat.id, "Привіт! Я бот для управління даними про людей.\n\n"
                                      "Доступні команди:\n"
                                      "/add - Додати запис\n"
                                      "/search - Пошук запису\n"
                                      "/list - Переглянути всі записи\n"
                                      "/help - Довідка")



@bot.message_handler(commands=['add'])
def add_person(message):
    bot.send_message(message.chat.id, "Введіть дані в одному рядку, розділяючи їх комами:\n"
                                      "ПІБ, дата народження, дата смерті (або -), стать (m/f/ч/ж/...)\n"
                                      "Приклад: Іван Іваненко, 10.10.1990, -, m")
    bot.register_next_step_handler(message, process_add)


def process_add(message):
    chat_id = message.chat.id
    try:
        data = message.text.split(',')
        if len(data) < 4:
            raise ValueError(
                "Недостатньо даних. Потрібно мінімум 4 параметри (ПІБ, дата народження, дата смерті, стать).")


        name_parts = data[0].strip().split()
        if not name_parts:
            raise ValueError("ПІБ не може бути пустим.")
        first_name = name_parts[0]
        last_name = name_parts[1] if len(name_parts) > 1 else None
        patronymic = name_parts[2] if len(name_parts) > 2 else None

        birth_date = data[1].strip()
        if birth_date == "-":
            birth_date = None

        death_date = data[2].strip()
        if death_date == "-":
            death_date = None

        gender = data[3].strip()
        if gender == "-":
            gender = None

        person = Person(first_name, last_name, patronymic, birth_date, death_date, gender)
        db.add_person(person)
        bot.send_message(chat_id, f"Запис додано:\n{person}")


    except ValueError as e:
        bot.send_message(chat_id, f"Помилка: {e}.  Спробуйте ще раз /add.")
    except Exception as e:
        bot.send_message(chat_id, f"Сталася невідома помилка: {e}. Спробуйте ще раз /add")


@bot.message_handler(commands=['list'])
def list_all(message):
    chat_id = message.chat.id
    people = db.get_all_people()
    if not people:
        bot.send_message(chat_id, "Записів не знайдено.")
        return

    for person in people:
        bot.send_message(chat_id, str(person))


@bot.message_handler(commands=['search'])
def search(message):
    chat_id = message.chat.id
    bot.send_message(chat_id, "Введіть пошуковий запит (частина імені, прізвища, тощо):")
    bot.register_next_step_handler(message, process_search)


def process_search(message):
    chat_id = message.chat.id
    query = message.text
    results = db.search(query)
    if results:
        for person in results:
            bot.send_message(chat_id, str(person))
    else:
        bot.send_message(chat_id, "Нічого не знайдено.")


print("Бот запущено....")
bot.polling()
