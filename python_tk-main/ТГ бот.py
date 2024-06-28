import telebot
import random

API_TOKEN='7024818120:AAFmSPU9dBUa9_PbFNoxHM9_BLyhU4HUCJw'

bot = telebot.TeleBot(API_TOKEN, parse_mode='HTML')

@bot.message_handler(commands=["start"])
def send_welсome(message):
    bot.reply_to(message, "Добро пожаловать!")



@bot.message_handler(commands=["info"])
def info(message):
    bot.reply_to(message, "Здесь ты научешся качть самые мощные томатные банки но пока ты просто кетчуп")

@bot.message_handler(commands=["infocommand"])
def send_infocommand(message):
    help_text = (
        "<b>Доступные команды:</b>\n"
        "/start - запуск бота \n"
        ",/info - список команд и функция бота\n"
    )
    bot.reply_to(message, help_text)



@bot.message_handler(commands=['rad'])
def send_help(message):
    try:
        random_index = random.randint(1,7)
        image_path = f"./img/image{random_index}.jpg"
        with open(image_path, 'rb') as image_file:
            bot.send_photo(message.chat.id, image_file)
    except Exception as e:
        bot.reply_to(message, f"ЭЭЭ Ошибка: {e}")

    
@bot.message_handler()
def handle_unknown_command(message):
    response = "<b>я хз что ты написал </b>."
    bot.reply_to(message, response)




bot.polling(none_stop=True)