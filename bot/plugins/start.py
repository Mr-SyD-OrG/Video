from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from ..screenshotbot import ScreenShotBot


@ScreenShotBot.on_message(filters.private & filters.command("start"))
async def start(c, m):

    await m.reply_text(
        text=f"Hɪ ᴛʜᴇʀᴇ {m.from_user.mention}.\n\nɪ'ᴍ ꜱᴄʀᴇᴇɴꜱʜᴏᴛ Generator Bot. I can provide screenshots from "
        "your video files without downloading the entire file (almost instantly). For more details check /help.",
        quote=True,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Bᴏᴛꜱ", url="https://t.me/bot_cracker/17"
                    ),
                    InlineKeyboardButton("Uᴩᴅᴀᴛᴇꜱ", url="https://t.me/bot_cracker"),
                ],
                [InlineKeyboardButton("Oᴡɴᴇʀ", url="https://t.me/syd_xyz")],
            ]
        ),
    )
