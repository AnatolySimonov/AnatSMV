import telebot
import configure
from random import sample

client = telebot.TeleBot(configure.config['token'])


def shuffle(text):
    target = text.split(" ")
    return " ".join(sample(target, len(target)))


@client.message_handler(content_types=['text'])
def repeat_all_messages(message):
    a = client.send_message(message.chat.id, shuffle(message.text))


client.infinity_polling()
