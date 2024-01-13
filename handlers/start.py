from aiogram import types, Dispatcher
from database import ddbb
from config import bot,mediaa
from const import FirstCaption
from keyboardbuttons import buttons
async def start_button(message:types.Message):
    data=ddbb.Database()
    data.insert_user(
        telegram_id=message.from_user.id,
        username=message.from_user.username,
        first_name=message.from_user.first_name,
        last_name=message.from_user.last_name
    )
    with open(mediaa+"ani.gif",'rb') as gif:
        await bot.send_animation(
            chat_id=message.from_user.id,
            animation=gif,
            caption=FirstCaption.format(name=message.from_user.first_name),
            reply_markup=await buttons.quest_button(),
        )
def register_start_handler(dp:Dispatcher):
    dp.register_message_handler(start_button, commands="start")
