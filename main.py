import telebot
from telebot import custom_filters
from telebot import StateMemoryStorage
from telebot.handler_backends import StatesGroup, State
state_storage = StateMemoryStorage()
# Вставить свой токет или оставить как есть, тогда мы создадим его сами
bot = telebot.TeleBot("6149812584:AAGTA_73oLnMgACPxHp55jUtTvIwj4wTRQI",
                      state_storage=state_storage, parse_mode='Markdown')
class PollState(StatesGroup):
    name = State()
    card_num = State()
class HelpState(StatesGroup):
    wait_text = State()
text_poll = "вопросы"  # Можно менять текст
text_button_1 = "Сайт"  # Можно менять текст
text_button_2 = "Общая инфа"  # Можно менять текст
text_button_3 = "Первый код на C"  # Можно менять текст
menu_keyboard = telebot.types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
menu_keyboard.add(
    telebot.types.KeyboardButton(
        text_poll,
    )
)
menu_keyboard.add(
    telebot.types.KeyboardButton(
        text_button_1,
    )
)
menu_keyboard.add(
    telebot.types.KeyboardButton(
        text_button_2,
    ),
    telebot.types.KeyboardButton(
        text_button_3,
    )
)
@bot.message_handler(state="*", commands=['start'])
def start_ex(message):
    bot.send_message(
        message.chat.id,
        'Привет! Что будем делать?',  # Можно менять текст
        reply_markup=menu_keyboard)
@bot.message_handler(func=lambda message: text_poll == message.text)
def first(message):
    bot.send_message(message.chat.id, 'Супер! *Ваше* _имя_?')  # Можно менять текст
    bot.set_state(message.from_user.id, PollState.name, message.chat.id)
@bot.message_handler(state=PollState.name)
def name(message):
    with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
        data['name'] = message.text
    bot.send_message(message.chat.id, 'Супер! Ваш номер карты?')  # Можно менять текст
    bot.set_state(message.from_user.id, PollState.card_num, message.chat.id)
@bot.message_handler(state=PollState.card_num)
def age(message):
    with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
        data['card_num'] = message.text
    bot.send_message(message.chat.id, 'Спасибо за регистрацию!', reply_markup=menu_keyboard)  # Можно менять текст
    bot.delete_state(message.from_user.id, message.chat.id)
@bot.message_handler(func=lambda message: text_button_1 == message.text)
def help_command(message):
    bot.send_message(message.chat.id, '[Официальный сайт ВКИ НГУ](https://ci.nsu.ru/).', reply_markup=menu_keyboard)  # Можно менять текст
@bot.message_handler(func=lambda message: text_button_2 == message.text)
def help_command(message):
    bot.send_message(message.chat.id, "Привет!\nМеня зовут Андрей. Мне 17 лет и я учусь в Высшем колледже информатики "
                                      "Новосибирского государственного университета. Мне всегда нравилось что-то создавать "
                                      "на компьютере, и я решил начать программировать", reply_markup=menu_keyboard)  # Можно менять текст
@bot.message_handler(func=lambda message: text_button_3 == message.text)
def help_command(message):
    bot.send_message(message.chat.id, "Сейчас я уже на 2 курсе. И мы пишем лабораторные работы\n"
                                      "Я бы хотел вам показать свой первый код на языке C++\n"
                                      "#include <iostream>\n"
                                      "using namespace std;\n"
                                      "void main()\n"
                                      "{\n"
                                      "    int N;\n"
                                      "    cin >> N;\n"
                                      "    int k = 0;\n"
                                      "    for (int i = 1; i <= N; i++)\n"
                                      "        if (N % i == 0)\n"
                                      "            k++;\n"
                                      "    if (k == 2);\n"
                                      '        cout << "YES";\n'
                                      "    else\n"
                                      '        cout << "NO";\n'
                                      "}\n"
                                      "Это проверка введённого числа на простоту.\n", reply_markup=menu_keyboard)  # Можно менять текст
bot.add_custom_filter(custom_filters.StateFilter(bot))
bot.add_custom_filter(custom_filters.TextMatchFilter())
bot.infinity_polling()

