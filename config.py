from aiogram import Bot, Dispatcher
from decouple import config
token=config('TOKEN')
mediaa=config('MEDIA')
chat1_id=config('CHAT1_ID')
bot=Bot(token=token)
dp=Dispatcher(bot=bot)