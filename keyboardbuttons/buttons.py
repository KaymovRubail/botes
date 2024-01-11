from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
async def quest_button():
    markup = InlineKeyboardMarkup()
    qb=InlineKeyboardButton('Quastions', callback_data='question_base')
    markup.add(qb)
    return markup
async def var():
    markup = InlineKeyboardMarkup()
    air=InlineKeyboardButton('Airplane', callback_data='air')
    car=InlineKeyboardButton('Car', callback_data='car')
    bus=InlineKeyboardButton('Bus', callback_data='bus')
    train=InlineKeyboardButton('Train', callback_data='train')
    markup.add(air,car,bus,train)
    return markup
async def var2():
    markup = InlineKeyboardMarkup()
    air1=InlineKeyboardButton('Boeing 737', callback_data='1')
    air2=InlineKeyboardButton('Airbus A320', callback_data='2')
    markup.add(air1,air2)
    return markup
async def var3():
    markup = InlineKeyboardMarkup()
    car1=InlineKeyboardButton('BMW', callback_data='3')
    car2=InlineKeyboardButton('Mercedes', callback_data='4')
    markup.add(car1,car2)
    return markup
async def var4():
    markup = InlineKeyboardMarkup()
    train1=InlineKeyboardButton('Shinkansen (Bullet Train) - Japan', callback_data='5')
    train2=InlineKeyboardButton('TGV (Train à Grande Vitesse) - France', callback_data='6')
    markup.add(train1,train2)
    return markup
async def var5():
    markup = InlineKeyboardMarkup()
    bus1=InlineKeyboardButton('London Routemaster (London Bus)', callback_data='7')
    bus2=InlineKeyboardButton('Mercedes-Benz Citaro (Various Cities Worldwide)',callback_data='8')
    markup.add(bus1,bus2)
    return markup
async def yes_no():
    markup = InlineKeyboardMarkup()
    bus1=InlineKeyboardButton('yes', callback_data='yes')
    bus2=InlineKeyboardButton('no', callback_data='no')
    markup.add(bus1,bus2)
    return markup
