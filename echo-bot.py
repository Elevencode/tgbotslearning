# -*- coding: utf-8 -*-
#!/usr/bin/env python

import config_echo
import telebot

bot = telebot.TeleBot(config_echo.token)

@bot.message_handler(content_types=["text"])
def repeat_messages(message):
	bot.send_message(message.chat.id, message.text)