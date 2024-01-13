from aiogram import types, Dispatcher
from aiogram.types import Update
from config import bot,chat1_id
from keyboardbuttons import buttons
from database import ddbb
from profanity_check import predict_prob

async def group_filter_message(m: types.Message):
    datab=ddbb.Database()
    if m.chat.id==int(chat1_id):
        bad_word=predict_prob([m.text])
        if bad_word>0.7:
            datab.inseert_ban(tg_id=m.from_user.id)
            datab.update_count_bun_table(tg_id=m.from_user.id)
            countt=datab.select_count_bun_table(tg_id=m.from_user.id)
            count=countt[0]
            await m.delete()
            if count<3:
                await bot.send_message(
                    chat_id=m.chat.id,
                    text=f'user: {m.from_user.first_name}\n'
                         f'U have written bad word\n'
                         f'It was {count}th time\n'
                         f'If u do it 3rd time\n'
                         f'U will be banned!!'

                )
            else:
                await bot.send_message(
                    chat_id=m.chat.id,
                    text= f'user: {m.from_user.first_name}\n'
                          f'U wrote bad word 3rd time '
                          f'I must ban u!'

                )
                await bot.ban_chat_member(
                    chat_id=m.chat.id,
                    user_id=m.from_user.id
                )
                datab.delete_user(tg_id=m.from_user.id)
def register_group_filter( dp: Dispatcher):
    dp.register_message_handler(group_filter_message)