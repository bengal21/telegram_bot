from aiogram import Bot, Dispatcher, executor, types
import asyncio


bot = Bot(token='Put here your token')
dp = Dispatcher(bot)


button_language = [
    types.InlineKeyboardButton(text='Русский', callback_data='Русский'),
    types.InlineKeyboardButton(text='English', callback_data='English')
                   ]
button_dice_rus = [types.InlineKeyboardButton(text='Кинуть кубик', callback_data='Кинуть кубик')]
button_dice_eng = [types.InlineKeyboardButton(text='Roll the dice', callback_data='Roll the dice')]


keyboard_language = types.InlineKeyboardMarkup()
keyboard_language.add(*button_language)
keyboard_dice_rus = types.InlineKeyboardMarkup()
keyboard_dice_rus.add(*button_dice_rus)
keyboard_dice_eng = types.InlineKeyboardMarkup()
keyboard_dice_eng.add(*button_dice_eng)

@dp.message_handler(commands='start')
async def answer(message: types.Message):
    await message.answer('Привет, выберите язык.\nHello, choose the language', reply_markup=keyboard_language)

@dp.callback_query_handler(lambda x: x.data == 'Русский')
async def lang(call: types.CallbackQuery):
    await call.message.answer('Хороший выбор, в любой момент вы можете поменять язык, просто отправьте /start', reply_markup=keyboard_dice_rus)
    await call.answer()
@dp.callback_query_handler(lambda x: x.data == 'Кинуть кубик')
async def answer(message: types.Message):
    user_dice = await bot.send_dice(message.from_user.id)
    await asyncio.sleep(4)
    await bot.send_message(message.from_user.id, 'А теперь кидаю я!')
    await asyncio.sleep(0.5)
    bot_dice = await bot.send_dice(message.from_user.id)
    await asyncio.sleep(4)
    if user_dice['dice']['value'] > bot_dice['dice']['value']:
        await bot.send_message(message.from_user.id, 'Вы выиграли!', reply_markup=keyboard_dice_rus)
    elif user_dice['dice']['value'] < bot_dice['dice']['value']:
        await bot.send_message(message.from_user.id, 'Вы проиграли!', reply_markup=keyboard_dice_rus)
    else:
        await bot.send_message(message.from_user.id, 'Ничья!', reply_markup=keyboard_dice_rus)


@dp.callback_query_handler(lambda x: x.data == 'English')
async def lang(call: types.CallbackQuery):
    await call.message.answer('Good choice, if you want to change the language just send /start', reply_markup=keyboard_dice_eng)
    await call.answer()
@dp.callback_query_handler(lambda x: x.data == 'Roll the dice')
async def b(message: types.Message):
    user_dice = await bot.send_dice(message.from_user.id)
    await asyncio.sleep(4)
    await bot.send_message(message.from_user.id, 'Now my turn!')
    await asyncio.sleep(0.5)
    bot_dice = await bot.send_dice(message.from_user.id)
    await asyncio.sleep(4)
    if user_dice['dice']['value'] > bot_dice['dice']['value']:
        await bot.send_message(message.from_user.id, 'You won!', reply_markup=keyboard_dice_eng)
    elif user_dice['dice']['value'] < bot_dice['dice']['value']:
        await bot.send_message(message.from_user.id, 'You lost!', reply_markup=keyboard_dice_eng)
    else:
        await bot.send_message(message.from_user.id, 'Draw!', reply_markup=keyboard_dice_eng)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)