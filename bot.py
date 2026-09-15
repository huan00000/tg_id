from telegram import Update
from telegram.ext import Application, MessageHandler, filters, ContextTypes

TOKEN = "你的BOT_TOKEN"

async def reply_id(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id

    await update.message.reply_text(
        f"你的 Telegram ID：{user_id}"
    )

app = Application.builder().token(TOKEN).build()
app.add_handler(MessageHandler(filters.ALL, reply_id))

app.run_polling()
