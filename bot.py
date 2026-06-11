import os
from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    ContextTypes,
    MessageHandler,
    filters,
)

TOKEN = os.getenv("8794448818:AAEWO8oAxTWhnkBZK_d0LiaJO9QwnD4GpMw")
ADMIN_ID = int(os.getenv("8978814040"))

user_map = {}

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):

    message = update.message

    if message.chat.id == ADMIN_ID:

        if message.reply_to_message:

            try:
                target_user = int(
                    message.reply_to_message.text.split("\n")[0]
                )

                await context.bot.send_message(
                    chat_id=target_user,
                    text=message.text
                )

            except:
                pass

        return

    user_id = message.from_user.id

    text = message.text or ""

    sent = await context.bot.send_message(
        chat_id=ADMIN_ID,
        text=f"{user_id}\n\n{text}"
    )

    user_map[sent.message_id] = user_id


app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(
    MessageHandler(filters.ALL, handle_message)
)

app.run_polling()
