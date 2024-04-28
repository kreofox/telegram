import telebot
import random

bot = telebot.TeleBot("TOKEN", parse_mode=None)
secret_number = random.randint(1, 100)

@bot.message_handler(commands=["start"])
def send_welcome(message):
    bot.reply_to(message,"Hello")
@bot.message_handler(commands=["user"])
def user(message):
    first_name = message.from_user.first_name
    bot.reply_to(message,f"You firts name is:{first_name}")
@bot.message_handler(commands=["info"])
def info(message):
    bot.reply_to(message, "Create:Kreofox\n GitHub:https://github.com/kreofox\nDiscord:470313155478814722")
@bot.message_handler(commands=["play-pin"])
def ping(message):
    bot.reply_to(message,"pong")
@bot.message_handler(commands=["play-numbers"])
def numbers(message):
    bot.reply_to(message,"Hi! I made a number from 1 to 100. Try to guess!")
def handled_message(message):
    try:
        guess = int(message.text)
        if guess==secret_number:
            bot.reply_to(message,"“Congratulations! You guessed the number!”")
            secret_number = random.randint(1,100)
        elif guess < secret_number:
            bot.reply_to(message,"My number is higher.")
        else:
            bot.reply_to(message,"My number is lower.")
    except ValueError:
        bot.reply_to(message,"Please enter a number.")   
bot.polling()

