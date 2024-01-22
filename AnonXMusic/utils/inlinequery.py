from pyrogram.types import InlineQueryResultArticle, InputTextMessageContent

answer = []

answer.extend(
    [
        InlineQueryResultArticle(
            title="Pᴀᴜsᴇ",
            description=f"ᴅᴀʜ ɢᴡ ᴊᴇᴅᴀ ʏᴀ ᴍᴇᴋ sᴛʀᴇᴀᴍ ɴʏᴀ.",
            thumb_url="https://telegra.ph//file/184d77a1d89187d6c9444.jpg",
            input_message_content=InputTextMessageContent("/pause"),
        ),
        InlineQueryResultArticle(
            title="Rᴇsᴜᴍᴇ",
            description=f"ᴅᴀʜ ɢᴡ ʀᴇsᴜᴍᴇ ʏᴀ ᴍᴇᴋ sᴛʀᴇᴀᴍ ɴʏᴀ.",
            thumb_url="https://telegra.ph//file/184d77a1d89187d6c9444.jpg",
            input_message_content=InputTextMessageContent("/resume"),
        ),
        InlineQueryResultArticle(
            title="Sᴋɪᴩ",
            description=f"ᴅᴀʜ ɢᴡ sᴋɪᴘ ʏᴀ ᴍᴇᴋ sᴛʀᴇᴀᴍ ɴʏᴀ.",
            thumb_url="https://telegra.ph//file/184d77a1d89187d6c9444.jpg",
            input_message_content=InputTextMessageContent("/skip"),
        ),
        InlineQueryResultArticle(
            title="Eɴᴅ",
            description="ᴅᴀʜ ɢᴡ ᴇɴᴅ ʏᴀ ᴍᴇᴋ sᴛʀᴇᴀᴍ ɴʏᴀ.",
            thumb_url="https://telegra.ph//file/184d77a1d89187d6c9444.jpg",
            input_message_content=InputTextMessageContent("/end"),
        ),
        InlineQueryResultArticle(
            title="Sʜᴜғғʟᴇ",
            description="ᴅᴀʜ ɢᴡ sᴜғғʟᴇ ʏᴀ ᴍᴇᴋ sᴛʀᴇᴀᴍ ɴʏᴀ.",
            thumb_url="https://telegra.ph//file/184d77a1d89187d6c9444.jpg",
            input_message_content=InputTextMessageContent("/shuffle"),
        ),
        InlineQueryResultArticle(
            title="Lᴏᴏᴩ",
            description="ᴅᴀʜ ɢᴡ ʟᴏᴏᴘ ʏᴀ ᴍᴇᴋ sᴛʀᴇᴀᴍ ɴʏᴀ.",
            thumb_url="https://telegra.ph//file/184d77a1d89187d6c9444.jpg",
            input_message_content=InputTextMessageContent("/loop 3"),
        ),
    ]
)
