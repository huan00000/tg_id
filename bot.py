import os
from telegram import Update
from telegram.ext import Application, MessageHandler, filters, ContextTypes

TOKEN = os.environ["BOT_TOKEN"]

async def reply_id(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user

    await update.message.reply_text(
        f"Telegram ID：{user.id}"
    )

app = Application.builder().token(TOKEN).build()
app.add_handler(MessageHandler(filters.ALL, reply_id))

app.run_polling()
