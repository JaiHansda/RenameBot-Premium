from pyrogram.types import (InlineKeyboardButton, InlineKeyboardMarkup,ForceReply)
from pyrogram import Client , filters

@Client.on_callback_query(filters.regex('upgrade'))
async def upgrade(bot,update):
	text = """**Free Plan User**
	Daily  Upload limit 1GB
	Price 0
	
	**VIP 1 ** 
	Daily  Upload  limit 10GB
	Price Rs 55  🇮🇳/🌎 0.67$  per Month
	
	**VIP 2 **
	Daily Upload limit 50GB
	Price Rs 80  🇮🇳/🌎 0.97$  per Month
	
	Pay Using Upi I'd ```7070784055@fam```
	
	After Payment Send Screenshots Of 
        Payment To Admin"""
	keybord = InlineKeyboardMarkup([[ 
        			InlineKeyboardButton("ADMIN 🛂",url = "https://t.me/TSP_PAID_PROMOTION_BOT)], 
        			[InlineKeyboardButton("PayPal 🌎",url = "https://t.me/TSP_PAID_PROMOTION_BOT"),
        			InlineKeyboardButton("UPI ",url = "https://t.me/TSP_PAID_PROMOTION_BOT")],[InlineKeyboardButton("Cancel",callback_data = "cancel")  ]])
	await update.message.edit(text = text,reply_markup = keybord)
	

@Client.on_message(filters.private & filters.command(["upgrade"]))
async def upgradecm(bot,message):
	text = """**Free Plan User**
	Daily  Upload limit 1GB
	Price 0
	
	**VIP 1 ** 
	Daily  Upload  limit 10GB
	Price Rs 55  🇮🇳/🌎 0.67$  per Month
	
	**VIP 2 **
	Daily Upload limit 50GB
	Price Rs 80  🇮🇳/🌎 0.97$  per Month
	
	
	Pay Using Upi I'd ```7070784055@fam```
	
	After Payment Send Screenshots Of 
        Payment To Admin"""
	keybord = InlineKeyboardMarkup([[ 
        			InlineKeyboardButton("ADMIN 🛂",url = "https://t.me/TSP_PAID_PROMOTION_BOT")], 
        			[InlineKeyboardButton("PayPal 🌎",url = "https://t.me/TSP_PAID_PROMOTION_BOT"),
        			InlineKeyboardButton("Paytm",url = "https://t.me/TSP_PAID_PROMOTION_BOT")],[InlineKeyboardButton("Cancel",callback_data = "cancel")  ]])
	await message.reply_text(text = text,reply_markup = keybord)
