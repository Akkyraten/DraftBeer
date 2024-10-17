from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler

# Функция для команды /start
async def start(update: Update, context):
    keyboard = [
        [InlineKeyboardButton("Напитки, лист №1", url="https://business.untappd.com/app/boards/59126")],
        [InlineKeyboardButton("Напитки, лист №2", url="https://business.untappd.com/app/boards/59127")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text('Привет! Выбери одну из страниц нашего меню:', reply_markup=reply_markup)

# Главная функция для запуска бота
if __name__ == '__main__':
    # Вставь свой токен сюда
    TOKEN = "7203418316:AAH04gl8TjnNtb2d3iYZDmzxKk5Ch23g0zo"
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))

    print("Бот запущен!")
    app.run_polling()