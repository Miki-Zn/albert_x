from aiogram import Bot, Dispatcher
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import TG_BOT_TOKEN, TG_ADMIN_ID

bot = Bot(token=TG_BOT_TOKEN)
dp = Dispatcher()

async def send_financial_alert(user_handle: str, text: str, analysis: str, action_id: str):
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text="Approve Request", callback_data=f"approve_{action_id}"),
            InlineKeyboardButton(text="Ignore", callback_data=f"deny_{action_id}")
        ]
    ])
    msg = f"🚨 Financial request from @{user_handle}\n\nOriginal Text: {text}\n\nAI Analysis: {analysis}"
    await bot.send_message(TG_ADMIN_ID, msg, reply_markup=keyboard)

async def send_alpha_alert(project_handle: str, analysis: str):
    msg = f"💎 Alpha project detected: {project_handle}\n\nAI Breakdown:\n{analysis}"
    await bot.send_message(TG_ADMIN_ID, msg)