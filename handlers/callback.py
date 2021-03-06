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
                    InlineKeyboardButton("โ ๐๐๐ ๐๐ ๐๐ ๐๐๐๐ ๐๐๐๐๐", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")
                ],[
                    InlineKeyboardButton("๐ค ๐๐๐ ๐๐๐๐๐", url=f"https://t.me/{OWNER_USERNAME}"),
                ],[
                    InlineKeyboardButton("๐ How To Use? Commands", callback_data="cb_cmd")
                ],
            ]
        ),
    )


@Client.on_callback_query(filters.regex("cb_cmd"))
async def cbcmd(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""**๐ค Normal Bot Commands :-

ยป /play - (song name) 
ยป /skip - Skip the Song
ยป /end - Stop Playing Music
ยป /pause - Pause the track
ยป /resume - Resumes the Track
ยป /mute - Mute the Assistant 
ยป /search - (song name)



โ Some Extra Commands :-

ยป /ping - Shows the Ping Status
ยป /id - Get the ID
ยป /rmd - Clean all the downloads
ยป /clean - Clean the Storage


๐ Powered By : @technobotsupport**""",
    )

