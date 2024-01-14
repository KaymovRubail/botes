from aiogram import types, Dispatcher
from database import ddbb
from config import bot,mediaa,admin
from const import FirstCaption
from keyboardbuttons import buttons,menu_buttons

async def foradmin(m:types.Message):
    if m.chat.id==m.from_user.id:
        if m.from_user.id == int(admin):
            await bot.send_message(
                chat_id=m.from_user.id,
                text=f'Welcome to Admins menu {m.from_user.first_name}!',
                reply_markup=await menu_buttons.menu_buttons_for_admin("See all users📃", "See all bad users👿")
            )
        else:
            await bot.send_message(
                chat_id=m.from_user.id,
                text='It is only for admin'
            )




def register_admin(dp:Dispatcher):
    dp.register_message_handler(foradmin, commands="foradmin")
