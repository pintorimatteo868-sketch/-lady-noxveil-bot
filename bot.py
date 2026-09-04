import os
from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters,
)

TOKEN = os.environ["TELEGRAM_BOT_TOKEN"]
OWNER_CHAT_ID = int(os.environ["OWNER_CHAT_ID"])


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🖤 Welcome to Lady Noxveil's private world. 🎭\n\n"
        "Discover exclusive content and private experiences.\n\n"
        "Use /menu to view the Private Menu.\n"
        "Use /custom for a custom request.\n"
        "Use /vip for private access.\n"
        "Use /contact to contact Lady Noxveil."
    )


async def menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🖤 LADY NOXVEIL — PRIVATE MENU 🎭\n\n"
        "📸 Private Photo — €10\n"
        "🖤 Secret Set | 5–7 photos — €25\n"
        "🎥 Private Video — from €25\n"
        "🎭 Behind the Veil Tease — €25\n"
        "✨ Custom Photo — from €25\n"
        "🎬 Custom Video — from €50\n\n"
        "🗝 The First Secret — €19\n"
        "🌙 Behind the Veil — €39\n"
        "👑 Noxveil Private Ritual — from €69\n\n"
        "Use /custom for a private request. 🎭"
    )


async def custom(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "✨ CUSTOM REQUEST\n\n"
        "Send your idea here in one message.\n"
        "Lady Noxveil will review your request and confirm the final price before payment. 🖤"
    )


async def vip(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🗝 PRIVATE EXPERIENCES\n\n"
        "The First Secret — €19\n"
        "Behind the Veil — €39\n"
        "Noxveil Private Ritual — from €69\n\n"
        "Use /contact if you want more information. 🎭"
    )


async def contact(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "💌 Send your message here.\n\n"
        "Your request will be passed to Lady Noxveil. 🖤"
    )


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "/menu — Private Menu\n"
        "/custom — Custom Request\n"
        "/vip — Private Access\n"
        "/contact — Contact Lady Noxveil\n"
        "/help — Assistance"
    )


async def auto_reply(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.lower()

    if any(word in text for word in ["ciao", "hello", "hi", "hey"]):
        reply = (
            "🖤 Welcome to Lady Noxveil's private world. 🎭\n\n"
            "You can ask about the menu, custom content, VIP access or contact."
        )
    elif any(word in text for word in ["prezzo", "prezzi", "price", "menu"]):
        reply = "🖤 You can view the full Private Menu with /menu."
    elif any(word in text for word in ["custom", "personalizzato", "richiesta"]):
        reply = (
            "✨ For a custom request, send your idea in one message "
            "or use /custom."
        )
    elif any(word in text for word in ["vip", "private", "access"]):
        reply = "🗝 For private experiences and VIP access, use /vip."
    elif any(word in text for word in ["pagamento", "payment", "pay"]):
        reply = "💳 Payment details are confirmed privately before delivery."
    else:
        reply = (
            "🖤 I’m Lady Noxveil’s private assistant. 🎭\n\n"
            "You can ask about the menu, custom requests, VIP access "
            "or contact Lady Noxveil."
        )

    await update.message.reply_text(reply)


def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("menu", menu))
    app.add_handler(CommandHandler("custom", custom))
    app.add_handler(CommandHandler("vip", vip))
    app.add_handler(CommandHandler("contact", contact))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, auto_reply))

    print("Lady Noxveil bot is running...")
    app.run_polling()


if __name__ == "__main__":
    main()
