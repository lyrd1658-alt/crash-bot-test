from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes

TOKEN = "8591455186:AAEsQQMeWX389CGf1t-TSnRqzcDRYVvwnfo"

async def check_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    if text and any(word in text for word in ["777", "انگور", "لیمو"]):
        await update.message.reply_text(
            "🎉 تبریک! شما برنده شده‌اید!\nبرای دیدن جوایز وارد چنل شوید 👇\n👉 @ironi_gift"
        )

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(MessageHandler(filters.TEXT, check_message))
app.run_polling()
