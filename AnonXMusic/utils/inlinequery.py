from pyrogram.types import InlineQueryResultArticle, InputTextMessageContent

answer = []

answer.extend(
    [
        InlineQueryResultArticle(
            title="Pᴀᴜsᴇ",
            description=f"ᴅᴀʜ ɢᴡ ᴊᴇᴅᴀ ʏᴀ ᴍᴇᴋ sᴛʀᴇᴀᴍ ɴʏᴀ.",
            thumb_url="https://telegra.ph//file/cc3e25abe2c92af4e784c.jpg",
            input_message_content=InputTextMessageContent("/pause"),
        ),
        InlineQueryResultArticle(
            title="Rᴇsᴜᴍᴇ",
            description=f"ᴅᴀʜ ɢᴡ ʀᴇsᴜᴍᴇ ʏᴀ ᴍᴇᴋ sᴛʀᴇᴀᴍ ɴʏᴀ.",
            thumb_url="https://telegra.ph//file/cc3e25abe2c92af4e784c.jpg",
            input_message_content=InputTextMessageContent("/resume"),
        ),
        InlineQueryResultArticle(
            title="Sᴋɪᴩ",
            description=f"ᴅᴀʜ ɢᴡ sᴋɪᴘ ʏᴀ ᴍᴇᴋ sᴛʀᴇᴀᴍ ɴʏᴀ.",
            thumb_url="https://telegra.ph//file/cc3e25abe2c92af4e784c.jpg",
            input_message_content=InputTextMessageContent("/skip"),
        ),
        InlineQueryResultArticle(
            title="Eɴᴅ",
            description="ᴅᴀʜ ɢᴡ ᴇɴᴅ ʏᴀ ᴍᴇᴋ sᴛʀᴇᴀᴍ ɴʏᴀ.",
            thumb_url="https://telegra.ph//file/cc3e25abe2c92af4e784c.jpg",
            input_message_content=InputTextMessageContent("/end"),
        ),
        InlineQueryResultArticle(
            title="Sʜᴜғғʟᴇ",
            description="ᴅᴀʜ ɢᴡ sᴜғғʟᴇ ʏᴀ ᴍᴇᴋ sᴛʀᴇᴀᴍ ɴʏᴀ.",
            thumb_url="https://telegra.ph//file/cc3e25abe2c92af4e784c.jpg",
            input_message_content=InputTextMessageContent("/shuffle"),
        ),
        InlineQueryResultArticle(
            title="Lᴏᴏᴩ",
            description="ᴅᴀʜ ɢᴡ ʟᴏᴏᴘ ʏᴀ ᴍᴇᴋ sᴛʀᴇᴀᴍ ɴʏᴀ.",
            thumb_url="https://telegra.ph//file/ce83f87bc1ea1c3510ae2.jpg",
            input_message_content=InputTextMessageContent("/loop 3"),
        ),
    ]
)
