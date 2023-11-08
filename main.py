import telebot
import random
import requests
from telebot import types

bot = telebot.TeleBot('6989305776:AAF01qeMPe9SL1mabxV5RWnqwGPgn74daoU')

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('поддержка разроботчика')
    markup.row(btn1)
    btn2 = types.KeyboardButton('оценю фото')
    btn3 = types.KeyboardButton('могу послать нахуй')
    markup.row(btn2, btn3)
    bot.send_message(message.chat.id, 'привет пупс :)', reply_markup=markup)
    bot.send_message(message.chat.id, 'что хотел?')
    bot.register_next_step_handler(message, on_click)

@bot.message_handler()
def info(message):
    if message.text.lower() == 'Привет':
        bot.send_message(message.chat.id, f'Привет жаба (@{message.from_user.username})')
    elif message.text.lower() == 'id':
        bot.reply_to(message, f'ID: {message.from_user.id}')
def random_number(message):
    rand_number = random.randint(1, 10)
    response = ""
    if rand_number == 10:
        response = f"я бы выебала, {rand_number}"
    elif rand_number == 9:
        response = f"по сути вкусно, {rand_number}"
    elif rand_number == 8:
        response = f"по сути вкусно, {rand_number}"
    elif rand_number == 7:
        response = f"на пол шишечки пойдет, {rand_number}"
    elif rand_number == 6:
        response = f"ну таке, {rand_number}"
    elif rand_number == 5:
        response = f"пакет на голову и норм, {rand_number}"
    elif rand_number == 4:
        response = f"тут и пакет на голову не поможет, {rand_number}"
    elif rand_number == 3:
        response = f"если от большой любви рождаются красивые дети, то твои родители ненавидели друг друга, {rand_number}"
    elif rand_number == 2:
        response = f"вау, кто тебе на голову надристал, {rand_number}"
    elif rand_number == 1:
        response = f"это пиздец, {rand_number}"

    return response

def on_click(message):
    if message.text == 'поддержка разроботчика':
        markup = types.InlineKeyboardMarkup()
        button = types.InlineKeyboardButton("поддержать разраба", url="https://send.monobank.ua/jar/6MeQrQ6N6R")
        markup.row(button)
        bot.send_message(message.chat.id, "для поддержки разработчика перейдите по ссылке:", reply_markup=markup)
    elif message.text == 'оценю фото':
        bot.send_message(message.chat.id, 'ну показывай')
        bot.register_next_step_handler(message, get_photo)
    elif message.text == 'могу послать нахуй':
        bot.send_message(message.chat.id, 'иди нахуй <3')
        bot.register_next_step_handler(message, on_click)


@bot.message_handler(content_types=['photo'])
def get_photo(message):
    response = random_number(message)
    bot.reply_to(message, response)
    bot.register_next_step_handler(message, on_click)

@bot.message_handler(commands=['evielinks'])
def links(message):
    markup = types.InlineKeyboardMarkup()
    button1 = types.InlineKeyboardButton('Instagram', url='https://www.instagram.com/carter.eevie/')
    markup.row(button1)
    button2 = types.InlineKeyboardButton('Telegram Channel', url='https://t.me/cartereevie')
    button3 = types.InlineKeyboardButton('Telegram Chat', url='https://t.me/+IG_URjvuXh4zYWRi')
    markup.row(button2, button3)
    button4 = types.InlineKeyboardButton('Discord Server', url='https://discord.gg/V4SvY9PvRX')
    markup.row(button4)
    bot.reply_to(message, 'Ссылки, где вы можете увидеть Evie 🥰', reply_markup=markup)


@bot.message_handler(commands=['eviejoke'])
def send_joke(message):
    bot.send_message(message.chat.id, 'пока не работаем 🥲')

@bot.message_handler(commands=['help'])
def main(message):
    bot.send_message(message.chat.id, 'какой те хелп')




bot.polling(none_stop=True)