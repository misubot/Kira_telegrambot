import telebot

API_TOKEN = "8197234018:AAHQ67FSfD_rRQg_SKuKHgMSSXJxZ0bVgzs"
bot = telebot.TeleBot(API_TOKEN)

# /start command
@bot.message_handler(commands=['start'])
def send_welcome(message):
    text = (
        "📢 Welcome to Kira PAY Bot 💎\n"
        "Before continuing, you must accept our **Terms & Policy**.\n\n"
        "👉 [✅ Accept]"
    )
    bot.send_message(message.chat.id, text, parse_mode="Markdown")

@bot.message_handler(func=lambda msg: msg.text and "Accept" in msg.text)
def subscription_plans(message):
    text = (
        "🎉 Thanks for accepting!\n"
        "Now choose your subscription plan 👇\n\n"
        "1️⃣ Basic Plan – $5/month\n"
        "   🔓 Access to VIP Channel\n"
        "   📅 Monthly renewal\n\n"
        "2️⃣ Pro Plan – $10/month\n"
        "   🚀 Access to VIP Channel\n"
        "   📞 Personal WhatsApp Support\n"
        "   🎁 Extra Premium Content\n\n"
        "3️⃣ One-Time VIP – $50\n"
        "   🔥 Lifetime VIP Access\n"
        "   📞 Direct WhatsApp number access\n"
        "   🎬 All Exclusive Content\n\n"
        "👉 [Choose Plan]"
    )
    bot.send_message(message.chat.id, text)

@bot.message_handler(func=lambda msg: msg.text and "Pro" in msg.text)
def pro_plan(message):
    text = (
        "✨ You selected **Pro Plan ($10/month)**\n\n"
        "With this plan you’ll get:\n"
        "🚀 VIP Channel Access\n"
        "📞 Direct WhatsApp Support\n"
        "🎁 Exclusive Premium Content\n\n"
        "👉 [Proceed to Payment]\n\n"
        "Please choose your payment method 👇\n"
        "- 💳 PayPal\n"
        "- 🌍 Wise\n"
        "- 🪙 Crypto\n\n"
        "💳 To complete your payment, please send the amount to:\n"
        f"📩 { 'paypal.me/kirapayment10' }\n\n"
        "After payment, send **screenshot + Transaction ID** here ✅"
    )
    bot.send_message(message.chat.id, text, parse_mode="Markdown")

print("🤖 Bot is running...")
bot.infinity_polling()
