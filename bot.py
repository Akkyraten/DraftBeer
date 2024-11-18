# from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
# from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler


# async def get_chat_id(update: Update, context):
#     chat_id = update.message.chat.id
#     await update.message.reply_text(f"Ваш chat_id: {chat_id}")

# # Функция для команды /start
# async def start(update: Update, context):
#     keyboard = [
#         [InlineKeyboardButton("Напитки, лист №1", url="https://business.untappd.com/app/boards/59126")],
#         [InlineKeyboardButton("Напитки, лист №2", url="https://business.untappd.com/app/boards/59127")]
#     ]
#     reply_markup = InlineKeyboardMarkup(keyboard)
#     await update.message.reply_text('Привет! Выбери одну из страниц нашего меню:', reply_markup=reply_markup)

# # Главная функция для запуска бота
# if __name__ == '__main__':
#     # Вставь свой токен сюда
#     TOKEN = "7203418316:AAH04gl8TjnNtb2d3iYZDmzxKk5Ch23g0zo"
#     app = ApplicationBuilder().token(TOKEN).build()

#     app.add_handler(CommandHandler("start", start))
#     app.add_handler(CommandHandler("chatid", get_chat_id))

#     print("Бот запущен!")
#     app.run_polling()



from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, MessageHandler, filters


MY_CHAT_ID = 893646369

# Команды /start
async def start(update: Update, context):
    photo_url = "https://i.pinimg.com/736x/44/2e/36/442e360757ea56fdb16e756588739f2a.jpg"
    keyboard = [
        [InlineKeyboardButton("🦞 Раки и икра", callback_data="seafood_catalog"), InlineKeyboardButton("🎉 Вечеринки", callback_data="events")],
        [InlineKeyboardButton("🚚 Доставка", callback_data="delivery"), InlineKeyboardButton("📞 Связаться", callback_data="contact")],
        [InlineKeyboardButton("Напитки, лист №1", url="https://business.untappd.com/app/boards/59126")],
        [InlineKeyboardButton("Напитки, лист №2", url="https://business.untappd.com/app/boards/59127")],
        [InlineKeyboardButton("🤝 Сотрудничество", callback_data='cooperation'), InlineKeyboardButton("🤖 Нравится бот", callback_data='robot')],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_photo(photo=photo_url, caption="Если ты ищешь уютное место, чтобы скоротать вечерок в приятной компании - ты на верном пути!🍺", reply_markup=reply_markup)

# Жмак на кнопки
async def button_handler(update: Update, context):
    query = update.callback_query
    data = query.data

    if data == "seafood_catalog":
        await query.message.reply_text("🦞 Раки и икра:\n1. Живые раки\n40-60 — 2100 руб/кг\n60-80 — 2400 руб/кг\n80+ — 2800 руб/кг\n2. Икра\nГорбуша — 3600 руб/банка\nКета — 3800 руб/банка")
    elif data == "events":
        await query.message.reply_text("🎉 Предстоящие вечеринки:\n- Мафия в пятницу\n- Пивная вечеринка в субботу.")
    elif data == "delivery":
        await query.message.reply_text("🚚 Для доставки укажите адрес и время и необходимый товар. Оплата производится при получени.")
    elif data == "contact":
        await query.message.reply_text("📞 Свяжитесь с нами по телефону +7 977 436 36 20 или напишите в чат.")
    elif data == "cooperation":
        await query.message.reply_text("🫵 Если ты активный и амбициозный - мы с тобой сейчас тут таких дел наворотим! Звони, будем рады знакомстсву +7 977 436 36 20")
    elif data == "robot":
        await query.message.reply_text("🫡 Спасибо что оценил! Если хочешь себе такой же - звони +7 916 070 75 62, пиши - @www051995")

# Пересылаем сообщения
async def text_handler(update: Update, context):
    # Пересылка сообщения на chat_id
    await context.bot.forward_message(chat_id=MY_CHAT_ID, from_chat_id=update.message.chat_id, message_id=update.message.message_id)
    await update.message.reply_text("Ваше сообщение было получено. Мы скоро с вами свяжемся!")

# Главная функция для запуска бота
if __name__ == '__main__':
    # Вставьте ваш токен сюда
    TOKEN = "7203418316:AAH04gl8TjnNtb2d3iYZDmzxKk5Ch23g0zo"
    app = ApplicationBuilder().token(TOKEN).build()

    # Команда /start
    app.add_handler(CommandHandler("start", start))
    # Обработка нажатий на кнопки
    app.add_handler(CallbackQueryHandler(button_handler))
    # Обработка текстовых сообщений
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, text_handler))

    print("Бот запущен!")
    app.run_polling()
