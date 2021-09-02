from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn
from config import BOT_USERNAME as bu
from helpers.filters import other_filters2


@Client.on_message(other_filters2)
async def start(_, message: Message):
    await message.reply_sticker("CAACAgQAAx0CTv65QgABBfJlYF6VCrGMm6OJ23AxHmD6qUSWESsAAhoQAAKm8XEeD5nrjz5IJFYeBA")
    await message.reply_text(
        f"""**Tao là {bn} 🎵

Tao có thể phát nhạc trong cuộc gọi thoại của nhóm bạn. Được phát triển bởi [owogram](https://t.me/owogram).

Thêm tôi vào nhóm của bạn và chơi nhạc tự do!**
        """,
        reply_markup=InlineKeyboardMarkup(
            [
               [
                    InlineKeyboardButton(
                        "💬 Group", url="https://t.me/owohub"
                    ),
                    InlineKeyboardButton(
                        "🔊 Channel", url="https://t.me/owogram"
                    )
                ]
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_message(filters.command("start") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""**Bố mày con thức ✅**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🔊 Updates", url="https://t.me/owogram")
                ]
            ]
        )
   )


