import telebot
import sqlite3
from pyexpat.errors import messages
from telebot.apihelper import ApiTelegramException
from telebot.util import content_type_media
from telebot import types

bot = telebot.TeleBot('7951477708:AAHna6k34mKZNaLm3Yh4Nxk-3kKftSX2Hhw', skip_pending=True)
admin = ['1389316365' , 'mops' , '379313116', 'Aleksandr']
name_of_user=None
city_user=None
car_name=None
year_auto=None
capacity_engine_auto=None
fuel_type_auto=None
drive_type_auto=None
mileage_auto=None
color_auto=None
allowed_car_auto=None
budget_auto=None
data_contact_auto=None
questionn=None

@bot.message_handler(commands=['start'])
def start(message):
    conn = sqlite3.connect('carmax3.sql')
    cur = conn.cursor()

    cur.execute('''CREATE TABLE IF NOT EXISTS tickets (id INTEGER PRIMARY KEY AUTOINCREMENT, nameuser VARCHAR(50), cityuser VARCHAR(50), carname VARCHAR(50), yearp VARCHAR(10), capacity VARCHAR(40), fuel VARCHAR(50), drive VARCHAR(50), mileage VARCHAR(50), color VARCHAR(50), allowedcar VARCHAR(50),budget VARCHAR(50), datacontact VARCHAR(50), questions VARCHAR(200) DEFAULT NULL)''')
    conn.commit()
    cur.close()
    conn.close()

    bot.send_message(message.chat.id, f'👋 Приветствую, {message.from_user.first_name}!\nЯ 🤖— онлайн-помощник экспортной компании CarMax. Чтобы ускорить процесс, ответьте на несколько вопросов ниже — это займет всего 2 минуты.\n🔹 Жмите "Создать заявку"👇\n\nЕсли вы уже выбрали автомобили на Encar.com, отправьте ссылки для бесплатного расчёта стоимости.\n🔹 Жмите "Задать вопрос"👇')
    menu(message)
    return


def menu(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    if str(message.from_user.id) or str(call.message.from_user.id) in admin and message.from_user.first_name or call.message.from_user.first_name in admin:
        btn1 = types.KeyboardButton('📑Создать заявку📑')
        btn2 = types.KeyboardButton('❓Задать вопрос❓')
        btn3 = types.KeyboardButton('🔄Процесс покупки🔄')
        btn4 = types.KeyboardButton('📩Заявки📩')
        btn5 = types.KeyboardButton('⁉️Вопросы⁉️')
        btn6 = types.KeyboardButton('📢НАШ TELEGRAM📢')
        markup.row(btn1, btn2)
        markup.row(btn3, btn6)
        markup.row(btn4, btn5)
    else:
        btn1 = types.KeyboardButton('📑Создать заявку📑')
        btn2 = types.KeyboardButton('❓Задать вопрос❓')
        btn3 = types.KeyboardButton('🔄Процесс покупки🔄')
        btn6 = types.KeyboardButton('📢НАШ TELEGRAM📢')
        markup.row(btn1, btn2)
        markup.row(btn3, btn6)
    bot.send_message(message.chat.id, 'Выберите действие:', reply_markup=markup)
    bot.register_next_step_handler(message, on_click)
    return


def on_click(message):
    if message.text == '📑Создать заявку📑':
        ticket_create(message)
    elif message.text == '❓Задать вопрос❓':
        make_question(message)
    elif message.text == '📩Заявки📩':
        tickets(message)
    elif message.text == '🔄Процесс покупки🔄':
        buy_process(message)
    elif message.text == '⁉️Вопросы⁉️':
        questions(message)
    elif message.text == '📢НАШ TELEGRAM📢':
        transition(message)

def notification_ticket(message):
    chat_id = 1389316365
    chat_id2 = 379313116# Сюда помещаем id пользователя кому будет отправлено сообщение
    bot.send_message(chat_id, 'Новая заявка!')
    bot.send_message(chat_id2, 'Новая заявка!')

def notification_question(message):
    chat_id = 1389316365
    chat_id2 = 379313116 # Сюда помещаем id пользователя кому будет отправлено сообщение
    bot.send_message(chat_id, f'Новый вопрос: {message.text}')
    bot.send_message(chat_id2, f'Новый вопрос: {message.text}')

def transition(message):
    markup = types.InlineKeyboardMarkup(row_width=1)
    markup.add(types.InlineKeyboardButton('Перейти', url = 'https://t.me/+035XTmuA4kY1ZGRl'))
    markup.add(types.InlineKeyboardButton('Назад', callback_data = 'cancel'))
    bot.send_message(message.chat.id, 'Вы уверены что хотите перейти в наш телеграм канал?', reply_markup=markup)

def buy_process(message):
    bot.send_message(message.chat.id, 'Процесс покупки авто из Кореи:\n\n'
                                      '1. Связываемся, обсуждаем автомобиль, просматриваем Encar.com, аукционных площадки и другие сайты, выбираем подходящие варианты, определяемся со стоимостью. Вы можете самостоятельно выбрать 2-3 варианта и отправить ссылки для уточнения информации и прозвона.\n'
                                      '2. Если автомобиль нас устраивает, вы вносите задаток в размере 50 000 руб. (этой суммой мы делаем бронь за автомобиль) на карту Сбербанка или Тинькофф. Затем мы проводим осмотр автомобиля (до 3 вариантов),  проверяем его на юридическую чистоту и страховые случаи. Если из 3 вариантов нам не подходят, продолжаем поиск по договорённости. Отправляем вам фото- и видеоотчёты для согласования. Если всё в порядке, мы резервируем автомобиль. \n'
                                      '3. Сделка: заключаем договор, я отправляю вам инвойс. Вы оплачиваете его через Солид банк или другой банк, который осуществляет транзакции в Южную Корею в долларах США. В течение 3-5 дней получаем денежные средства и выкупаем автомобиль. \n'
                                      '4. Подготавливаем автомобиль к отправке во Владивосток (снятие с учёта, подготовка всех необходимых документов для экспорта и таможни, снятие тонировки и т.д.). При необходимости, за дополнительную плату, можно установить дополнительное оборудование, заменить шины, выполнить русификацию и т.д. \n'
                                      '5. После прибытия во Владивосток мы связываем вас с нашим представителем. Он будет курировать процесс растаможки, получения СБКТС и ПТС на ваше имя, а также отправку автомобиля в ваш город на автовозе. Стоимость доставки из Владивостока до вашего города составляет до 250 000 руб., в зависимости от расстояния и габаритов автомобиля. Доставка возможна автовозом или по железной дороге. Весь процесс ориентировочно занимает 1-1,5 месяца с момента оплаты в Корею. \n\n'
                                      'Оплата производится в три этапа после заключения договора: \n\n'
                                      '1) Вносите задаток в размере 50 000 руб. на карту. \n'
                                      '2) Оплата инвойса в долларах США (стоимость автомобиля + расходы по Корее) Расходы по Корее составляют 2млн. корейских вон, примерно 1400$ (комиссия дилера, перегон авто, подготовка документов, паром/стивидорные работы)\n'
                                      '3) Оплата расходов во Владивостоке (таможенная пошлина, таможенный сбор, утилизационный сбор и т.д.).  ')
    menu(message)


def make_question(message):

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    markup.row(types.KeyboardButton('🚫Отмена🚫'))

    conn = sqlite3.connect('carmax3.sql')
    cur = conn.cursor()

    cur.execute('''CREATE TABLE IF NOT EXISTS tickets (id INTEGER PRIMARY KEY AUTOINCREMENT, nameuser VARCHAR(50), cityuser VARCHAR(50), carname VARCHAR(50), yearp VARCHAR(10), capacity VARCHAR(40), fuel VARCHAR(50), drive VARCHAR(50), mileage VARCHAR(50), color VARCHAR(50), allowedcar VARCHAR(50),budget VARCHAR(50), datacontact VARCHAR(50), questions VARCHAR(200) DEFAULT NULL)''')
    conn.commit()
    cur.close()
    conn.close()

    bot.send_message(message.chat.id, 'Оставляйте ссылки на интересующие автомобили с Encar.com 🚗 или задавайте любые вопросы ❓ — мы с радостью всё посчитаем и ответим в течение дня ⏰. Пожалуйста, укажите ваш номер телефона 📱 и удобный способ связи (Telegram, WhatsApp, Viber) 💬. Спасибо за обращение! 🙏', reply_markup=markup)
    bot.register_next_step_handler(message, question_taker)


def question_taker(message):
    if message.text == '🚫Отмена🚫':
        menu(message)
        return

    global questionn
    questionn = message.text.strip()

    conn = sqlite3.connect('carmax3.sql')
    cur = conn.cursor()

    cur.execute("INSERT INTO tickets (questions) VALUES (?)",(questionn,))
    conn.commit()
    cur.close()
    conn.close()

    bot.send_message(message.chat.id,'🤝 Спасибо за ваш вопрос! В ближайшее время мы свяжемся с вами для уточнения деталей. \n\n☀️Хорошего вам дня!')
    notification_question(message)
    menu(message)

@bot.message_handler(commands=['questions'])
def questions(message):
    if str(message.from_user.id) in admin and message.from_user.first_name in admin:
        markup = telebot.types.InlineKeyboardMarkup()
        btn1 = telebot.types.InlineKeyboardButton('Да', callback_data='questions')
        btn2 = telebot.types.InlineKeyboardButton('Нет', callback_data='cancel')
        markup.row(btn1, btn2)

        bot.send_message(message.chat.id,'Вы уверены, что хотите открыть список вопросов?',reply_markup=markup)
    else:
        bot.send_message(message.chat.id, 'У вас нет прав на использование этой команды!')
        menu(message)


def ticket_create(message):

    conn = sqlite3.connect('carmax3.sql')
    cur = conn.cursor()

    cur.execute('''CREATE TABLE IF NOT EXISTS tickets (id INTEGER PRIMARY KEY AUTOINCREMENT, nameuser VARCHAR(50), cityuser VARCHAR(50), carname VARCHAR(50), yearp VARCHAR(10), capacity VARCHAR(40), fuel VARCHAR(50), drive VARCHAR(50), mileage VARCHAR(50), color VARCHAR(50), allowedcar VARCHAR(50),budget VARCHAR(50), datacontact VARCHAR(50), questions VARCHAR(200))''')
    conn.commit()
    cur.close()
    conn.close()

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    markup.row(types.KeyboardButton('🚫Отмена🚫'))

    bot.send_message(message.chat.id, 'Как к вам обращаться?',reply_markup=markup)
    bot.register_next_step_handler(message, nameuser)

@bot.message_handler(commands=['tickets'])
def tickets(message):
    if str(message.from_user.id) in admin and message.from_user.first_name in admin:
        markup = telebot.types.InlineKeyboardMarkup()
        btn1 = telebot.types.InlineKeyboardButton('Да', callback_data='tickets')
        btn2 = telebot.types.InlineKeyboardButton('Нет', callback_data='cancel')
        markup.row(btn1, btn2)

        bot.send_message(message.chat.id,'Вы уверены, что хотите открыть список заявок?',reply_markup=markup)
    else:
        bot.send_message(message.chat.id, 'У вас нет прав на использование этой команды!')
        menu(message)

def clear_check(message):
    if str(message.from_user.id) in admin and message.from_user.first_name in admin:
        markup = telebot.types.InlineKeyboardMarkup()
        btn1 = telebot.types.InlineKeyboardButton('Да', callback_data='clear_list')
        btn2 = telebot.types.InlineKeyboardButton('Нет', callback_data='cancel')
        markup.row(btn1, btn2)

        bot.send_message(message.chat.id,'Вы уверены, что хотите очистить список заявок?',reply_markup=markup)
    else:
        bot.send_message(message.chat.id, 'У вас нет прав на использование этой команды!')
        menu(message)

def clear_list(message):
    try:
        if message.text == '🚫Очистить🚫':
            clear_check(message)
        elif message.text == '🔴Меню🔴':
            menu(message)
    except sqlite3.OperationalError:
        bot.send_message(message.chat.id, 'Таблицы не существует')
        menu(message)


def cityuser(message):
    if message.text == '🚫Отмена🚫':
        menu(message)
        return
#    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
#    btn1 = types.KeyboardButton('🚫Отмена🚫')
#    markup.row(btn1)
    global city_user
    city_user = message.text.strip()
    bot.send_message(message.chat.id, 'Какой автомобиль вас интересует?(марка, модель)')
    bot.register_next_step_handler(message, carname)

def nameuser(message):
    if message.text == '🚫Отмена🚫':
        menu(message)
        return
#    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
#    btn1 = types.KeyboardButton('🚫Отмена🚫')
#    markup.row(btn1)
    global name_of_user
    name_of_user = message.text.strip()
    bot.send_message(message.chat.id, 'Из какого вы города?')
    bot.register_next_step_handler(message, cityuser)

def carname(message):
    if message.text == '🚫Отмена🚫':
        menu(message)
        return
#    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
#    btn1 = types.KeyboardButton('🚫Отмена🚫')
#    markup.row(btn1)

    global car_name
    car_name = message.text.strip()
    bot.send_message(message.chat.id, 'Какого года выпуска?')
    bot.register_next_step_handler(message, year)

def year(message):
    if message.text == '🚫Отмена🚫':
        menu(message)
        return
#    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
#    btn1 = types.KeyboardButton('🚫Отмена🚫')
#    markup.row(btn1)

    global year_auto
    year_auto = message.text.strip()
    bot.send_message(message.chat.id, 'Какой объём двигателя?')
    bot.register_next_step_handler(message, capacity)

def capacity(message):
    if message.text == '🚫Отмена🚫':
        menu(message)
        return
#    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
#    btn1 = types.KeyboardButton('🚫Отмена🚫')
#    markup.row(btn1)

    global capacity_engine_auto
    capacity_engine_auto = message.text.strip()
    bot.send_message(message.chat.id, 'Какой тип топлива предпочитаете?')
    bot.register_next_step_handler(message, fuel_type)

def fuel_type(message):
    if message.text == '🚫Отмена🚫':
        menu(message)
        return
#    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
#    btn1 = types.KeyboardButton('🚫Отмена🚫')
#    markup.row(btn1)

    global fuel_type_auto
    fuel_type_auto = message.text.strip()
    bot.send_message(message.chat.id, 'Какой привод нужен? (2WD / 4WD / Задний / Передний)')
    bot.register_next_step_handler(message, drive_type)

def drive_type(message):
    if message.text == '🚫Отмена🚫':
        menu(message)
        return
#    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
#    btn1 = types.KeyboardButton('🚫Отмена🚫')
#    markup.row(btn1)

    global drive_type_auto
    drive_type_auto = message.text.strip()
    bot.send_message(message.chat.id, 'Какой допустимый пробег?')
    bot.register_next_step_handler(message, mileage)

def mileage(message):
    if message.text == '🚫Отмена🚫':
        menu(message)
        return
#    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
#    btn1 = types.KeyboardButton('🚫Отмена🚫')
#    markup.row(btn1)

    global mileage_auto
    mileage_auto = message.text.strip()
    bot.send_message(message.chat.id, 'Какой цвет салона и кузова предпочитаете?')
    bot.register_next_step_handler(message, color)

def color(message):
    if message.text == '🚫Отмена🚫':
        menu(message)
        return
#    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
#    btn1 = types.KeyboardButton('🚫Отмена🚫')
#    markup.row(btn1)

    global color_auto
    color_auto = message.text.strip()
    bot.send_message(message.chat.id, 'Допустимы ли окрашенные детали или заменённые элементы?')
    bot.register_next_step_handler(message, allowed_car)

def allowed_car(message):
    if message.text == '🚫Отмена🚫':
        menu(message)
        return
#    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
#    btn1 = types.KeyboardButton('🚫Отмена🚫')
#    markup.row(btn1)

    global allowed_car_auto
    allowed_car_auto = message.text.strip()
    bot.send_message(message.chat.id, 'Какой бюджет планируете?')
    bot.register_next_step_handler(message, budget)

def budget(message):
    if message.text == '🚫Отмена🚫':
        menu(message)
        return
#    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
#    btn1 = types.KeyboardButton('🚫Отмена🚫')
#    markup.row(btn1)

    global budget_auto
    budget_auto = message.text.strip()
    bot.send_message(message.chat.id, 'Оставьте ваш контактный номер и укажите удобный способ связи (Telegram, WhatsApp, Viber)')
    bot.register_next_step_handler(message, data_contact)

def data_contact(message):
    global data_contact_auto
    data_contact_auto = message.text.strip()

    conn = sqlite3.connect('carmax3.sql')
    cur = conn.cursor()

    cur.execute("INSERT INTO tickets (nameuser, cityuser, carname, yearp, capacity, fuel, drive, mileage, color, allowedcar, budget,datacontact) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",(name_of_user, city_user, car_name, year_auto, capacity_engine_auto, fuel_type_auto, drive_type_auto, mileage_auto, color_auto, allowed_car_auto, budget_auto, data_contact_auto))
    conn.commit()
    cur.close()
    conn.close()

    bot.send_message(message.chat.id,'🤝 Спасибо, что ответили на все вопросы! Это поможет нам быстрее и точнее подобрать нужный автомобиль. В ближайшее время мы свяжемся с вами для уточнения деталей. \n\n☀️Хорошего вам дня!')
    notification_ticket(message)
    menu(message)


@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    global admin
    if call.data == 'tickets':
        try:
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
            btn1 = types.KeyboardButton('🚫Очистить🚫')
            btn2 = types.KeyboardButton('🔴Меню🔴')
            markup.row(btn1, btn2)

            conn = sqlite3.connect('carmax3.sql')
            cur = conn.cursor()

            cur.execute('SELECT * FROM tickets')
            tickets = cur.fetchall()

            info = ''
            for el in tickets:
                if el[1] != None:
                    info += f'#️⃣Номер заявки: {el[0]}\n 😀Имя клиента: {el[1]}\n 🌁Город клиента: {el[2]}\n 🚗Название машины: {el[3]}\n ⌛Год машины: {el[4]}\n ⚙️Объём двигателя: {el[5]}\n ⛽Тип топлива: {el[6]}\n 🔧Привод: {el[7]}\n 🛣️Пробег: {el[8]}\n 🎨Цвет кузова/салона: {el[9]}\n 🛠️Допустимые косяки: {el[10]}\n 💸Бюджет: {el[11]}\n ☎️Контакты клиента: {el[12]}\n\n'

            cur.close()
            conn.close()

            bot.send_message(call.message.chat.id, info , reply_markup=markup)
            bot.register_next_step_handler(call.message, clear_list)
        except (sqlite3.OperationalError, telebot.apihelper.ApiTelegramException):
            bot.send_message(call.message.chat.id, 'Таблицы не существует')
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
            btn1 = types.KeyboardButton('📑Создать заявку📑')
            btn2 = types.KeyboardButton('❓Задать вопрос❓')
            btn3 = types.KeyboardButton('🔄Процесс покупки🔄')
            btn4 = types.KeyboardButton('📩Заявки📩')
            btn5 = types.KeyboardButton('⁉️Вопросы⁉️')
            btn6 = types.KeyboardButton('📢НАШ TELEGRAM📢')
            markup.row(btn1, btn2)
            markup.row(btn3. btn4)
            markup.row(btn5, btn6)
            bot.send_message(call.message.chat.id, 'Выберите действие:', reply_markup=markup)
            bot.register_next_step_handler(call.message, on_click)
    elif call.data == 'cancel':
        menu(call.message)
        return
    elif call.data == 'questions':
        try:
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
            btn1 = types.KeyboardButton('🚫Очистить🚫')
            btn2 = types.KeyboardButton('🔴Меню🔴')
            markup.row(btn1, btn2)

            conn = sqlite3.connect('carmax3.sql')
            cur = conn.cursor()

            cur.execute('SELECT * FROM tickets')
            tickets = cur.fetchall()

            info = ''
            for el in tickets:
                if el[13] != None:
                    info += f'Вопрос №{el[0]}: {el[13]}\n\n'

            cur.close()
            conn.close()

            bot.send_message(call.message.chat.id, info, reply_markup=markup)
            bot.register_next_step_handler(call.message, clear_list)
        except (sqlite3.OperationalError, telebot.apihelper.ApiTelegramException):
            bot.send_message(call.message.chat.id, 'Вопросов сейчас нет')
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)

            btn1 = types.KeyboardButton('📑Создать заявку📑')
            btn2 = types.KeyboardButton('❓Задать вопрос❓')
            btn3 = types.KeyboardButton('🔄Процесс покупки🔄')
            btn4 = types.KeyboardButton('📩Заявки📩')
            btn5 = types.KeyboardButton('⁉️Вопросы⁉️')
            btn6 = types.KeyboardButton('📢НАШ TELEGRAM📢')
            markup.row(btn1, btn2)
            markup.row(btn3, btn4)
            markup.row(btn5, btn6)
            bot.send_message(call.message.chat.id, 'Выберите действие:', reply_markup=markup)
            bot.register_next_step_handler(call.message, on_click)
            return
    elif call.data == 'clear_list':
        try:
            conn = sqlite3.connect('carmax3.sql')
            cur = conn.cursor()

            cur.execute('DROP TABLE IF EXISTS tickets')
            conn.commit()
            cur.close()
            conn.close()
            bot.send_message(call.message.chat.id, 'Таблица очищена')
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
            btn1 = types.KeyboardButton('📑Создать заявку📑')
            btn2 = types.KeyboardButton('❓Задать вопрос❓')
            btn3 = types.KeyboardButton('🔄Процесс покупки🔄')
            btn4 = types.KeyboardButton('📩Заявки📩')
            btn5 = types.KeyboardButton('⁉️Вопросы⁉️')
            btn6 = types.KeyboardButton('📢НАШ TELEGRAM📢')
            markup.row(btn1, btn2)
            markup.row(btn3, btn4)
            markup.row(btn5, btn6)
            bot.send_message(call.message.chat.id, 'Выберите действие:', reply_markup=markup)
            bot.register_next_step_handler(call.message, on_click)
            return
        except sqlite3.OperationalError:
            bot.send_message(call.message.chat.id, 'Таблицы не существует')
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
            btn1 = types.KeyboardButton('📑Создать заявку📑')
            btn2 = types.KeyboardButton('❓Задать вопрос❓')
            btn3 = types.KeyboardButton('🔄Процесс покупки🔄')
            btn4 = types.KeyboardButton('📩Заявки📩')
            btn5 = types.KeyboardButton('⁉️Вопросы⁉️')
            btn6 = types.KeyboardButton('📢НАШ TELEGRAM📢')
            markup.row(btn1, btn2)
            markup.row(btn3, btn4)
            markup.row(btn5, btn6)
            bot.send_message(call.message.chat.id, 'Выберите действие:', reply_markup=markup)
            bot.register_next_step_handler(call.message, on_click)
            return


bot.infinity_polling(skip_pending=True)
