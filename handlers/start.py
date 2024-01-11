from aiogram import types, Dispatcher
from database import ddbb
from config import bot
from keyboardbuttons import buttons
async def start_button(message:types.Message):
    data=ddbb.Database()
    data.insert_user(
        telegram_id=message.from_user.id,
        username=message.from_user.username,
        first_name=message.from_user.first_name,
        last_name=message.from_user.last_name
    )
    await bot.send_message(
        chat_id=message.from_user.id,
        text=f"Hello {message.from_user.first_name}",
        reply_markup= await buttons.quest_button()
    )
def register_start_handler(dp:Dispatcher):
    dp.register_message_handler(start_button, commands="start")