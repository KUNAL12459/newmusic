from pyrogram import Client, filters
from pyrogram.types import CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton
from config import (
    BOT_USERNAME,
    OWNER_USERNAME,   
)


@Client.on_callback_query(filters.regex("cb_start"))
async def start_op(_, query: CallbackQuery):
    await query.answer("Bot Started")
    await query.edit_message_text(
              f"""**Hello, Welcome {message.from_user.mention()}\n
I am powerful easy to use TeleGram Super Bot. I can play high quality and unbreakable music in your group voice chat. Just add me and promote with needed powers.\n
Use Inline buttons for more !!
For Help : @HEARTBROKENPERSON1**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("✚ 𝐀𝐃𝐃 𝐌𝐄 𝐓𝐎 𝐘𝐎𝐔𝐑 𝐆𝐑𝐎𝐔𝐏", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")
                ],[
                    InlineKeyboardButton("👤 𝐁𝐎𝐓 𝐎𝐖𝐍𝐄𝐑", url=f"https://t.me/{OWNER_USERNAME}"),
                ],[
                    InlineKeyboardButton("🔍 How To Use? Commands", callback_data="cb_cmd")
                ],
            ]
        ),
    )


@Client.on_callback_query(filters.regex("cb_cmd"))
async def cbcmd(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""**🤖 Normal Bot Commands :-

» /play - (song name) 
» /skip - Skip the Song
» /end - Stop Playing Music
» /pause - Pause the track
» /resume - Resumes the Track
» /mute - Mute the Assistant 
» /search - (song name)



⚙ Some Extra Commands :-

» /ping - Shows the Ping Status
» /id - Get the ID
» /rmd - Clean all the downloads
» /clean - Clean the Storage


🌀 Powered By : @technobotsupport**""",
    )

