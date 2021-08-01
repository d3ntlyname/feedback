from os import system as terminal
terminal('pip3 install pyrogram tgcrypto')
from pyrogram import Client, filters, idle
from asyncio import sleep
from random import randint, choice
from time import sleep
import os, io, requests, sys
from datetime import datetime as date

app = Client('1')

@app.on_message(~filters.me)
def message(client, message):
	if message.from_user.is_bot == True:
		return
	try:
		if randint(1, 5) == 3:
			client.send_chat_action(message.chat.id, 'typing')
			text = client.get_inline_bot_results('DotaGosuBot', 'Дентли топ')['results'][1]['send_message']['message']
			message.reply_text(text)
			try:
				client.join_chat(message.text)
			except:
				pass
	except:
		pass
		
app.run()
