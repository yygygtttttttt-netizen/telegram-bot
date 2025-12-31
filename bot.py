from telegram.ext import ApplicationBuilder, CommandHandler

TOKEN = "8552534161:AAGbeGKz7QQ5boYrtRTTDJBojxYs4HlbBzw"
ADMIN_ID = @Abir0019850

async def start(update, context):
    await update.message.reply_text("Bot Live ✅")

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.run_polling()
