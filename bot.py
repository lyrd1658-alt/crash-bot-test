from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

# 🔑 توکن رباتت
TOKEN = "8591455186:AAEsQQMeWX389CGf1t-TSnRqzcDRYVvwnfo"

# 📩 دستور /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("سلام! ربات فعال شد ✅")

# 🎰 وقتی کسی پیام می‌فرسته
async def check_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    # 🔍 بررسی متن پیام برای کلمات مورد نظر
    if any(word in text for word in ["ست777", "انگور", "لیمو"]):
        reply_text = "🎉 تبریک! شما برنده شده‌اید!\n\n👉 [چنل ایرونی گیفت](https://t.me/ironi_gift)"
        await update.message.reply_text(reply_text, disable_web_page_preview=True)

# ⚙️ ساخت و اجرای ربات
app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, check_message))

app.run_polling()
