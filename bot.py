import os
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

load_dotenv()

MESSAGE = """
╔══════════════════════════╗
🔥 FULL MAIN ID SAFE PANEL 🔥
╚══════════════════════════╝

🛡️ Full Main ID Safe Panel — 300৳
⚡ Teleport — 300৳
🚀 Speed Hack — 250৳

━━━━━━━━━━━━━━━━━━━━

📲 Root & Non-Root Panel
আরও বিভিন্ন Root / Non-Root Panel-এর জন্য যোগাযোগ করুন:

📱 WhatsApp: 01775838578

━━━━━━━━━━━━━━━━━━━━

🙏 আমাদের সাথে থাকার জন্য
অনেক অনেক ধন্যবাদ ❤️

✦ — Sani ✦
━━━━━━━━━━━━━━━━━━━━
"""


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(MESSAGE)


async def price(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(MESSAGE)


TOKEN = os.getenv("BOT_TOKEN")

app = Application.builder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("price", price))

print("Bot is running...")
app.run_polling()
