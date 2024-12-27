from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message

bot_token = '7551580728:AAHnZ1AI0cildkTXibM1PGmkt-hgbh204YI'

bot = Bot(token=bot_token)
db = Dispatcher()

@db.message(Command(commands=['start']))
async def process_start_command(message: Message):
    await message.answer('''
                        Здарова баклан еба..й!
                         Меня зовут Эхо-бот!
                         Напиши мне что-нибудь
                         ''')

@db.message(Command(commands=['help']))
async def process_help_command(message: Message):
    await message.answer('''
                        Напиши мне что-нибудь в ответ
                         я пришлю тебе твое сообщение
                         ''')

@db.message()
async def send_echo(message: Message):
    await message.reply(text=message.text)


if __name__ == '__main__':
    db.run_polling(bot)