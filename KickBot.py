import aiogram
from aiogram import Bot, Dispatcher, types
from aiogram.utils.exceptions import BadRequest
from aiogram.dispatcher import filters
from aiogram.types import ParseMode
from aiogram.utils import executor
import logging
import json

with open('config.json', 'r') as file:
    config = json.load(file)

TOKEN = config['TOKEN']
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

logging.basicConfig(level=logging.INFO)

#/start-----
@dp.message_handler(commands=['start'])
async def send_message(message: types.Message):
    await message.reply("🫡 Привіт. Я допоможу тобі позбутися ноунеймів і окремих індивідуумів у чаті. Не забудь дати мені права адміністратора\nЩе вивчай /help")

#/help-----
@dp.message_handler(commands=['help'])
async def send_message(message: types.Message):
    await message.reply("⚙️ *Список команд:*"+
    "\n\n*/start* — _запустити бота_"+
    "\n*/help* — _це повідомлення_"+
    "\n*/id* — _Показує твій ID, якщо відповідь на користувача, то його. Допиши_ `chat`_, і покаже ID чату_"+
    "\n*/bluetext* — _синій текст, кожна команда кикає юзера_"+
    "\n*/roulet* — _список розіграшів, теж кикає юзера_", parse_mode="Markdown")

#/id-----
@dp.message_handler(commands=['id'])
async def command_id(message: types.Message):
    if message.reply_to_message:
        user_id = message.reply_to_message.from_user.id
        await message.reply(f"ID користувача: `{user_id}`", parse_mode="Markdown")
    elif "chat" in message.text:
        chat_id = message.chat.id
        await message.reply(f"ID чату: `{chat_id}`", parse_mode="Markdown")
    else:
        user_id = message.from_user.id
        await message.reply(f"Твій ID: `{user_id}`", parse_mode="Markdown")

#/kickme-----
@dp.message_handler(commands=['kickme'])
async def send_message(message: types.Message):
    await message.reply("Rose, твоя черга😁")

#/roulet-----
@dp.message_handler(commands=['roulet'])
async def send_message(message: types.Message):
    await message.reply("🚀 *Про розіграші:*"+
    "\n_Введи команду та отримай шанс виграти приз. У кожної команди свій приз і свої шанси. Не забудь додати мене в груповий чат (розіграші працюють тільки там) і видати права адміністратора, інакше я не зможу працювати😢_"+
    "\n\n🥳️ *Список розіграшів:*"+
    "\n*/yadebil*"+
    "\n*Приз:* _можливість закріплювати повідомлення_"+
    "\n*Шанс:* _10%_"+
    "\n*/yagandone*"+
    "\n*Приз:* _можливість отримати адміністратора_"+
    "\n*Шанс:* _5%_"+
    "\n*/yapedarasik*"+
    "\n*Приз:* _можливість отримати творця_"+
    "\n*Шанс:* _1%_", parse_mode="Markdown")

async def kick_roulet_words(message: types.Message) -> bool:
    roulet_word = ["/yadebil","/yagandone", "/yapedarasik"]
    return any(keyword in message.text.lower() for keyword in roulet_word)

@dp.message_handler(kick_roulet_words)
async def kick_user(message: types.Message):
    user_id = message.from_user.id
    chat_id = message.chat.id

    try:
        await bot.kick_chat_member(chat_id, user_id)
        await bot.unban_chat_member(chat_id, user_id)
        await message.reply("😢 *На жаль, ти не виграв*\n_Спробуй ще раз_", parse_mode="Markdown")
    except aiogram.exceptions.BadRequest as e:

        if 'not enough rights to restrict/unrestrict chat member' in str(e).lower():
            await message.reply("🚫 *У мене немає прав адміністратора*", parse_mode="Markdown")
        else:
            await message.reply("🚀 *Ти вже отримав цей приз!*", parse_mode="Markdown")

#/kicktext-----
@dp.message_handler(commands=['bluetext'])
async def send_message(message: types.Message):
    await message.reply("/BLUE /TEXT\n/MUST /CLICK\n/I /AM /A /STUPID /ANIMAL /THAT /ISS /ATTRACTED /TO /COLORS")

async def kick_words(message: types.Message) -> bool:
    words = ["слава россии", "/kekmi","/blue", "/text", "/must", "/click", "/i", "/am", "/stupid", "/animal", "/that", "/iss", "/attracted", "/to", "/colors"]
    return any(keyword in message.text.lower() for keyword in words)

@dp.message_handler(kick_words)
async def kick_user(message: types.Message):
    user_id = message.from_user.id
    chat_id = message.chat.id

    try:
        await bot.kick_chat_member(chat_id, user_id)
        await bot.unban_chat_member(chat_id, user_id)
        await message.reply("🫵😂")
    except aiogram.exceptions.BadRequest:
        return

if __name__ == '__main__':
    executor.start_polling(dp)