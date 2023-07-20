import logging
import datetime
import pytz

from aiogram import Bot, Dispatcher, executor, types
from reply_btn import reply_btn_func

API_TOKEN = '6193917375:AAHjg5NyAYRd4slWPp-XOYDRTVssb8N4ITg'

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    btn = await reply_btn_func()
    await message.answer('Здравствуйте! Выберите город в котором хотите узнать время', reply_markup=btn)



@dp.message_handler()
async def echo(message: types.Message):
    text = message.text
    if text == 'Tashkent':
        tz = pytz.timezone('Asia/Tashkent')
    elif text == 'Portugal':
        tz = pytz.timezone('Portugal')
    elif text == 'Brazil':
        tz = pytz.timezone('Brazil/West')
    elif text == 'Los Angeles':
        tz = pytz.timezone('America/Los_Angeles')
    elif text == 'Detroit':
        tz = pytz.timezone('America/Detroit')
    elif text == 'Shanghai':
        tz = pytz.timezone('Asia/Shanghai')
    elif text == 'Tokyo':
        tz = pytz.timezone('Asia/Tokyo')
    elif text == 'Moscow':
        tz = pytz.timezone('Europe/Moscow')
    elif text == 'London':
        tz = pytz.timezone('Europe/London')
    elif text == 'New York':
        tz = pytz.timezone('America/New_York')
    
    now_date = datetime.datetime.now(tz)
    await message.answer(now_date.strftime('%B %d %H:%M'))


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)