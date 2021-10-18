from telebot import *
from configure import config
from random_game import get_data

client = telebot.TeleBot(config['token'])


@client.message_handler(commands=['game'])
def start_command(message):
    game = get_data()
    client.send_message(message.chat.id, f"{game['Ссылка']}")
    client.send_message(message.chat.id, f"{game['Название']}\n{game['Тэги']}")


client.polling(none_stop=True, interval=0)
