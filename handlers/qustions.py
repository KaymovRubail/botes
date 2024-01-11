from aiogram import types, Dispatcher
from config import bot
from keyboardbuttons import buttons

async def ask(call: types.CallbackQuery):
    await bot.send_message(
        chat_id=call.from_user.id,
        text="Type of transport u prefer:",
        reply_markup= await buttons.var()
    )

async def answer_air(call: types.CallbackQuery):
    await bot.send_message(
        chat_id=call.from_user.id,
        text="Wich plane do like most:",
        reply_markup= await buttons.var2()
    )
async def answer_car(call: types.CallbackQuery):
    await bot.send_message(
        chat_id=call.from_user.id,
        text="Wich car do like most:",
        reply_markup= await buttons.var3()
    )
async def answer_Bus(call: types.CallbackQuery):
    await bot.send_message(
        chat_id=call.from_user.id,
        text="Wich bus do like most:",
        reply_markup= await buttons.var5()
    )
async def answer_train(call: types.CallbackQuery):
    await bot.send_message(
        chat_id=call.from_user.id,
        text="Wich train do like most:",
        reply_markup= await buttons.var4()
    )
async def answerfor2(call: types.CallbackQuery):
    await bot.send_message(
        chat_id=call.from_user.id,
        text="Have u ever been on it:",
        reply_markup= await buttons.yes_no()
    )
async def thanks(call: types.CallbackQuery):
    await bot.send_message(
        chat_id=call.from_user.id,
        text="Thank you for answering"
    )
t=[str(i) for i in range(1,9)]
def register_ask(dp: Dispatcher):
    dp.register_callback_query_handler(ask, lambda call: call.data == "question_base")
    dp.register_callback_query_handler(answer_air, lambda call:call.data == "air")
    dp.register_callback_query_handler(answer_car, lambda call:call.data == "car")
    dp.register_callback_query_handler(answer_train, lambda call:call.data == "train")
    dp.register_callback_query_handler(answer_Bus, lambda call:call.data == "bus")
    dp.register_callback_query_handler(answerfor2, lambda call:call.data in t)
    dp.register_callback_query_handler(thanks, lambda call:call.data in ("yes","no"))

