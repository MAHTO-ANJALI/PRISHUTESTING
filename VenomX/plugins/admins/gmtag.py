from VenomX import app 
import asyncio
import random
from pyrogram import Client, filters
from pyrogram.enums import ChatType, ChatMemberStatus
from pyrogram.errors import UserNotParticipant
from pyrogram.types import ChatPermissions

spam_chats = []

EMOJI = [ "🦋🦋🦋🦋🦋",
          "🧚🌸🧋🍬🫖",
          "🥀🌷🌹🌺💐",
          "🌸🌿💮🌱🌵",
          "❤️💚💙💜🖤",
          "💓💕💞💗💖",
          "🌸💐🌺🌹🦋",
          "🍔🦪🍛🍲🥗",
          "🍎🍓🍒🍑🌶️",
          "🧋🥤🧋🥛🍷",
          "🍬🍭🧁🎂🍡",
          "🍨🧉🍺☕🍻",
          "🥪🥧🍦🍥🍚",
          "🫖☕🍹🍷🥛",
          "☕🧃🍩🍦🍙",
          "🍁🌾💮🍂🌿",
          "🌨️🌥️⛈️🌩️🌧️",
          "🌷🏵️🌸🌺💐",
          "💮🌼🌻🍀🍁",
          "🧟🦸🦹🧙👸",
          "🧅🍠🥕🌽🥦",
          "🐷🐹🐭🐨🐻‍❄️",
          "🦋🐇🐀🐈🐈‍⬛",
          "🌼🌳🌲🌴🌵",
          "🥩🍋🍐🍈🍇",
          "🍴🍽️🔪🍶🥃",
          "🕌🏰🏩⛩️🏩",
          "🎉🎊🎈🎂🎀",
          "🪴🌵🌴🌳🌲",
          "🎄🎋🎍🎑🎎",
          "🦅🦜🕊️🦤🦢",
          "🦤🦩🦚🦃🦆",
          "🐬🦭🦈🐋🐳",
          "🐔🐟🐠🐡🦐",
          "🦩🦀🦑🐙🦪",
          "🐦🦂🕷️🕸️🐚",
          "🥪🍰🥧🍨🍨",
          " 🥬🍉🧁🧇",
        ]

TAGMES = [ " **➠ 𝐆ᴏᴏᴅ 𝐍ɪɢʜᴛ 🌚** ",
           " **➠ 𝐂ʜᴜᴘ 𝐂ʜᴀᴘ 𝐒ᴏ 𝐉ᴀ 🙊** ",
           " **➠ 𝐏ʜᴏɴᴇ 𝐑ᴀᴋʜ 𝐊ᴀʀ 𝐒ᴏ 𝐉ᴀ, 𝐍ᴀʜɪ 𝐓ᴏ 𝐁ʜᴏᴏᴛ 𝐀ᴀ 𝐉ᴀʏᴇɢᴀ..👻** ",
           " **➠ 𝐀ᴡᴇᴇ 𝐁ᴀʙᴜ 𝐒ᴏɴᴀ 𝐃ɪɴ 𝐌ᴇɪɴ 𝐊ᴀʀ 𝐋ᴇɴᴀ 𝐀ʙʜɪ 𝐒ᴏ 𝐉ᴀᴏ..?? 🥲** ",
           " **➠ 𝐌ᴜᴍᴍʏ 𝐃ᴇᴋʜᴏ 𝐘ᴇ 𝐀ᴘɴᴇ 𝐆ғ 𝐒ᴇ 𝐁ᴀᴀᴛ 𝐊ʀ 𝐑ʜᴀ ʜ 𝐑ᴀᴊᴀɪ 𝐌ᴇ 𝐆ʜᴜs 𝐊ᴀʀ, 𝐒ᴏ 𝐍ᴀʜɪ 𝐑ᴀʜᴀ 😜** ",
           " **➠ 𝐏ᴀᴘᴀ 𝐘ᴇ 𝐃ᴇᴋʜᴏ 𝐀ᴘɴᴇ 𝐁ᴇᴛᴇ 𝐊ᴏ 𝐑ᴀᴀᴛ 𝐁ʜᴀʀ 𝐏ʜᴏɴᴇ 𝐂ʜᴀʟᴀ 𝐑ʜᴀ 𝐇ᴀɪ 🤭** ",
           " **➠ 𝐉ᴀɴᴜ 𝐀ᴀᴊ 𝐑ᴀᴀᴛ 𝐊ᴀ 𝐒ᴄᴇɴᴇ 𝐁ɴᴀ 𝐋ᴇ..?? 🌠** ",
           " **➠ 𝐆ɴ 𝐒ᴅ 𝐓ᴄ.. 🙂** ",
           " **➠ 𝐆ᴏᴏᴅ 𝐍ɪɢʜᴛ 𝐒ᴡᴇᴇᴛ 𝐃ʀᴇᴀᴍ 𝐓ᴀᴋᴇ 𝐂ᴀʀᴇ..?? ✨** ",
           " **➠ 𝐑ᴀᴀᴛ 𝐁ʜᴜᴛ 𝐆ᴏ 𝐆ʏɪ 𝐇ᴀɪ 𝐒ᴏ 𝐉ᴀᴏ, 𝐆ɴ..?? 🌌** ",
           " **➠ 𝐌ᴜᴍᴍʏ 𝐃ᴇᴋʜᴏ 11 𝐁ᴀᴊɴᴇ 𝐖ᴀʟᴇ 𝐇ᴀɪ 𝐘ᴇ 𝐀ʙʜɪ 𝐓ᴀᴋ 𝐏ʜᴏɴᴇ 𝐂ʜᴀʟᴀ 𝐑ʜᴀ 𝐍ᴀʜɪ 𝐒ᴏ 𝐍ᴀʜɪ 𝐑ʜᴀ 🕦** ",
           " **➠ 𝐊ᴀʟ 𝐒ᴜʙʜᴀ 𝐒ᴄʜᴏᴏʟ 𝐍ᴀʜɪ 𝐉ᴀɴᴀ 𝐊ʏᴀ, 𝐉ᴏ 𝐀ʙʜɪ 𝐓ᴀᴋ 𝐉ᴀɢ 𝐑ʜᴇ 𝐇ᴏ 🏫** ",
           " **➠ 𝐁ᴀʙᴜ, 𝐆ᴏᴏᴅ 𝐍ɪɢʜᴛ 𝐒ᴅ 𝐓ᴄ..?? 😊** ",
           " **➠ 𝐀ᴀᴊ 𝐁ʜᴜᴛ 𝐓ʜᴀɴᴅ 𝐇ᴀɪ, 𝐀ᴀʀᴀᴍ 𝐒ᴇ 𝐉ᴀʟᴅɪ 𝐒ᴏ 𝐉ᴀᴛɪ 𝐇ᴏᴏɴ 🌼** ",
           " **➠ 𝐉ᴀɴᴇᴍᴀɴ, 𝐆ᴏᴏᴅ 𝐍ɪɢʜᴛ 🌷** ",
           " **➠ 𝐌ᴇ 𝐉ᴀ 𝐑ᴀʜɪ 𝐒ᴏɴᴇ, 𝐆ɴ 𝐒ᴅ 𝐓ᴄ 🏵️** ",
           " **➠ 𝐇ᴇʟʟᴏ 𝐉ɪ 𝐍ᴀᴍᴀsᴛᴇ, 𝐆ᴏᴏᴅ 𝐍ɪɢʜᴛ 🍃** ",
           " **➠ 𝐇ᴇʏ, 𝐁ᴀʙʏ 𝐊ᴋʀʜ..? 𝐒ᴏɴᴀ 𝐍ᴀʜɪ 𝐇ᴀɪ 𝐊ʏᴀ ☃️** ",
           " **➠ 𝐆ᴏᴏᴅ 𝐍ɪɢʜᴛ 𝐉ɪ, 𝐁ʜᴜᴛ 𝐑ᴀᴀᴛ 𝐇ᴏ 𝐆ʏɪ..? ⛄** ",
           " **➠ 𝐌ᴇ 𝐉ᴀ 𝐑ᴀʜɪ 𝐑ᴏɴᴇ, ɪ 𝐌ᴇᴀɴ 𝐒ᴏɴᴇ 𝐆ᴏᴏᴅ 𝐍ɪɢʜᴛ 𝐉ɪ 😁** ",
           " **➠ 𝐌ᴀᴄʜʜᴀʟɪ 𝐊ᴏ 𝐊ᴇʜᴛᴇ 𝐇ᴀɪ 𝐅ɪsʜ, 𝐆ᴏᴏᴅ ɴɪɢʜᴛ 𝐃ᴇᴀʀ 𝐌ᴀᴛ 𝐊ʀɴᴀ 𝐌ɪss, 𝐉ᴀ 𝐑ʜɪ 𝐒ᴏɴᴇ 🌄** ",
           " **➠ 𝐆ᴏᴏᴅ 𝐍ɪɢʜᴛ 𝐁ʀɪɢʜᴛғᴜʟʟ 𝐍ɪɢʜᴛ 🤭** ",
           " **➠ 𝐓ʜᴇ 𝐍ɪɢʜᴛ 𝐇ᴀs 𝐅ᴀʟʟᴇɴ, 𝐓ʜᴇ 𝐃ᴀʏ 𝐈s 𝐃ᴏɴᴇ,, 𝐓ʜᴇ 𝐌ᴏᴏɴ 𝐇ᴀs 𝐓ᴀᴋᴇɴ 𝐓ʜᴇ 𝐏ʟᴀᴄᴇ 𝐎ғ 𝐓ʜᴇ 𝐒ᴜɴ... 😊** ",
           " **➠ 𝐌ᴀʏ 𝐀ʟʟ 𝐘ᴏᴜʀ 𝐃ʀᴇᴀᴍs 𝐂ᴏᴍᴇ 𝐓ʀᴜᴇ ❤️** ",
           " **➠ 𝐆ᴏᴏᴅ 𝐍ɪɢʜᴛ 𝐒ᴘʀɪɴᴋʟᴇs 𝐒ᴡᴇᴇᴛ 𝐃ʀᴇᴀᴍ 💚** ",
           " **➠ 𝐆ᴏᴏᴅ 𝐍ɪɢʜᴛ, 𝐍ɪɴᴅ 𝐀ᴀ 𝐑ʜɪ 𝐇ᴀɪ 🥱** ",
           " **➠ 𝐌ʏ 𝐃ᴇᴀʀ 𝐅ʀɪᴇɴᴅ 𝐆ᴏᴏᴅ 𝐍ɪɢʜᴛ 💤** ",
           " **➠ 𝐁ᴀʙʏ 𝐀ᴀᴊ 𝐑ᴀᴀᴛ 𝐊ᴀ 𝐒ᴄᴇɴᴇ 𝐁ɴᴀ 𝐋ᴇ 🥰** ",
           " **➠ 𝐈ᴛɴɪ 𝐑ᴀᴀᴛ 𝐌ᴇ 𝐉ᴀɢ 𝐊ᴀʀ 𝐊ʏᴀ 𝐊ᴀʀ 𝐑ʜᴇ 𝐇ᴏ sᴏɴᴀ 𝐍ᴀʜɪ 𝐇ᴀɪ 𝐊ʏᴀ 😜** ",
           " **➠ 𝐂ʟᴏsᴇ ʏᴏᴜʀ 𝐄ʏᴇs 𝐒ɴᴜɢɢʟᴇ 𝐔ᴘ 𝐓ɪɢʜᴛ,, ᴀɴᴅ 𝐑ᴇᴍᴇᴍʙᴇʀ 𝐓ʜᴀᴛ 𝐀ɴɢᴇʟs, 𝐖ɪʟʟ 𝐖ᴀᴛᴄʜ 𝐎ᴠᴇʀ 𝐘ᴏᴜ 𝐓ᴏɴɪɢʜᴛ... 💫** ",
           ]

VC_TAG = [ "**➠ 𝐆ᴏᴏᴅ 𝐌ᴏʀɴɪɴɢ, 𝐊ᴇsᴇ 𝐇ᴏ 🐱**",
         "**➠ 𝐆ᴍ, 𝐒ᴜʙʜᴀ 𝐇ᴏ 𝐆ʏɪ 𝐔ᴛʜɴᴀ 𝐍ᴀʜɪ 𝐇ᴀɪ 𝐊ʏᴀ 🌤️**",
         "**➠ 𝐆ᴍ 𝐁ᴀʙʏ, 𝐂ʜᴀɪ 𝐏ɪ 𝐋ᴏ ☕**",
         "**➠ 𝐉ᴀʟᴅɪ 𝐔ᴛʜᴏ, 𝐒ᴄʜᴏᴏʟ 𝐍ᴀʜɪ 𝐉ᴀɴᴀ 𝐊ʏᴀ 🏫**",
         "**➠ 𝐆ᴍ, 𝐂ʜᴜᴘ 𝐂ʜᴀᴘ 𝐁ɪsᴛᴇʀ 𝐒ᴇ 𝐔ᴛʜᴏ 𝐕ʀɴᴀ 𝐏ᴀɴɪ 𝐃ᴀʟ 𝐃ᴜɴɢɪ 🧊**",
         "**➠ 𝐁ᴀʙʏ 𝐔ᴛʜᴏ 𝐀ᴜʀ 𝐉ᴀʟᴅɪ 𝐅ʀᴇsʜ 𝐇ᴏ 𝐉ᴀᴏ, 𝐍ᴀsᴛᴀ 𝐑ᴇᴀᴅʏ 𝐇ᴀɪ 🫕**",
         "**➠ 𝐎ғғɪᴄᴇ 𝐍ᴀʜɪ 𝐉ᴀɴᴀ 𝐊ʏᴀ 𝐉ɪ 𝐀ᴀᴊ, ᴀʙʜɪ ᴛᴀᴋ ᴜᴛʜᴇ ɴᴀʜɪ 🏣**",
         "**➠ 𝐆ᴍ 𝐃ᴏsᴛ, 𝐂ᴏғғᴇᴇ/𝐓ᴇᴀ 𝐊ʏᴀ 𝐋ᴏɢᴇ ☕🍵**",
         "**➠ 𝐁ᴀʙʏ 8 𝐁ᴀᴊɴᴇ 𝐖ᴀʟᴇ 𝐇ᴀɪ, 𝐀ᴜʀ 𝐓ᴜᴍ 𝐀ʙʜɪ 𝐓ᴋ 𝐔ᴛʜᴇ 𝐍ᴀʜɪ 🕖**",
         "**➠ 𝐊ʜᴜᴍʙʜᴋᴀʀᴀɴ 𝐊ɪ 𝐀ᴜʟᴀᴅ 𝐔ᴛʜ 𝐉ᴀᴀ... ☃️**",
         "**➠ 𝐆ᴏᴏᴅ 𝐌ᴏʀɴɪɴɢ 𝐇ᴀᴠᴇ ᴀ 𝐍ɪᴄᴇ 𝐃ᴀʏ... 🌄**",
         "**➠ 𝐆ᴏᴏᴅ 𝐌ᴏʀɴɪɴɢ, 𝐇ᴀᴠᴇ ᴀ 𝐆ᴏᴏᴅ 𝐃ᴀʏ... 🪴**",
         "**➠ 𝐆ᴏᴏᴅ 𝐌ᴏʀɴɪɴɢ, 𝐇ᴏᴡ 𝐀ʀᴇ 𝐘ᴏᴜ 𝐁ᴀʙʏ 😇**",
         "**➠ 𝐌ᴜᴍᴍʏ 𝐃ᴇᴋʜᴏ 𝐘ᴇ 𝐍ᴀʟᴀʏᴋ 𝐀ʙʜɪ 𝐓ᴀᴋ 𝐒ᴏ 𝐑ʜᴀ 𝐇ᴀɪ... 😵‍💫**",
         "**➠ 𝐑ᴀᴀᴛ 𝐁ʜᴀʀ 𝐁ᴀʙᴜ 𝐒ᴏɴᴀ 𝐊ʀ 𝐑ʜᴇ 𝐓ʜᴇ 𝐊ʏᴀ, 𝐉ᴏ 𝐀ʙʜɪ 𝐓ᴋ 𝐒ᴏ 𝐑ʜᴇ 𝐇ᴏ 𝐔ᴛʜɴᴀ 𝐍ᴀʜɪ 𝐇ᴀɪ 𝐊ʏᴀ... 😏**",
         "**➠ 𝐁ᴀʙᴜ 𝐆ᴏᴏᴅ 𝐌ᴏʀɴɪɴɢ 𝐔ᴛʜ 𝐉ᴀᴏ 𝐀ᴜʀ 𝐆ʀᴏᴜᴘ 𝐌ᴇ 𝐒ᴀʙ 𝐅ʀɪᴇɴᴅs 𝐊ᴏ 𝐆ᴍ 𝐖ɪsʜ 𝐊ʀᴏ... 🌟**",
         "**➠ 𝐏ᴀᴘᴀ 𝐘ᴇ 𝐀ʙʜɪ 𝐓ᴀᴋ 𝐔ᴛʜ 𝐍ᴀʜɪ, 𝐒ᴄʜᴏᴏʟ ᴋᴀ 𝐓ɪᴍᴇ 𝐍ɪᴋᴀʟᴛᴀ 𝐉ᴀ 𝐑ʜᴀ 𝐇ᴀɪ... 🥲**",
         "**➠ 𝐉ᴀɴᴇᴍᴀɴ 𝐆ᴏᴏᴅ 𝐌ᴏʀɴɪɴɢ, 𝐊ʏᴀ 𝐊ʀ 𝐑ʜᴇ 𝐇ᴏ ... 😅**",
         "**➠ 𝐆ᴍ 𝐁ᴇᴀsᴛɪᴇ, 𝐁ʀᴇᴀᴋғᴀsᴛ 𝐇ᴜᴀ 𝐊ʏᴀ... 🍳**",
        ]


@app.on_message(filters.command(["gntag", "tagmember" ], prefixes=["/", "@", "#"]))
async def mentionall(client, message):
    chat_id = message.chat.id
    if message.chat.type == ChatType.PRIVATE:
        return await message.reply("๏ 𝐈s 𝐂ᴏᴍᴍᴀɴᴅ 𝐊ᴏ 𝐆ʀᴏᴜᴘ 𝐌ᴇ 𝐔sᴇ 𝐊ᴀʀ 𝐘ᴀʜᴀ 𝐆𝐇𝐀𝐍𝐓𝐀 𝐊ɪsɪᴋᴏ 𝐆𝐌 𝐊ᴀʀᴜɴɢɪ 😏")

    is_admin = False
    try:
        participant = await client.get_chat_member(chat_id, message.from_user.id)
    except UserNotParticipant:
        is_admin = False
    else:
        if participant.status in (
            ChatMemberStatus.ADMINISTRATOR,
            ChatMemberStatus.OWNER
        ):
            is_admin = True
    if not is_admin:
        return await message.reply("๏ ʏᴏᴜ ᴀʀᴇ ɴᴏᴛ ᴀᴅᴍɪɴ ʙᴀʙʏ, ᴏɴʟʏ ᴀᴅᴍɪɴs ᴄᴀɴ ᴛᴀɢ ᴍᴇᴍʙᴇʀs. ")

    if message.reply_to_message and message.text:
        return await message.reply("/tagall ɢᴏᴏᴅ ᴍᴏʀɴɪɴɢ ᴛʏᴘᴇ ʟɪᴋᴇ ᴛʜɪs / ʀᴇᴘʟʏ ᴀɴʏ ᴍᴇssᴀɢᴇ ɴᴇxᴛ ᴛɪᴍᴇ ʙᴏᴛ ᴛᴀɢɢɪɴɢ...")
    elif message.text:
        mode = "text_on_cmd"
        msg = message.text
    elif message.reply_to_message:
        mode = "text_on_reply"
        msg = message.reply_to_message
        if not msg:
            return await message.reply("/tagall ɢᴏᴏᴅ ᴍᴏʀɴɪɴɢ ᴛʏᴘᴇ ʟɪᴋᴇ ᴛʜɪs / ʀᴇᴘʟʏ ᴀɴʏ ᴍᴇssᴀɢᴇ ɴᴇxᴛ ᴛɪᴍᴇ ғᴏᴛ ᴛᴀɢɢɪɴɢ...")
    else:
        return await message.reply("/tagall ɢᴏᴏᴅ ᴍᴏʀɴɪɴɢ ᴛʏᴘᴇ ʟɪᴋᴇ ᴛʜɪs / ʀᴇᴘʟʏ ᴀɴʏ ᴍᴇssᴀɢᴇ ɴᴇxᴛ ᴛɪᴍᴇ ʙᴏᴛ ᴛᴀɢɢɪɴɢ...")
    if chat_id in spam_chats:
        return await message.reply("๏ ᴘʟᴇᴀsᴇ ᴀᴛ ғɪʀsᴛ sᴛᴏᴘ ʀᴜɴɴɪɴɢ ᴍᴇɴᴛɪᴏɴ ᴘʀᴏᴄᴇss...")
    spam_chats.append(chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in client.get_chat_members(chat_id):
        if not chat_id in spam_chats:
            break
        if usr.user.is_bot:
            continue
        usrnum += 1
        usrtxt += f"[{usr.user.first_name}](tg://user?id={usr.user.id}) "

        if usrnum == 1:
            if mode == "text_on_cmd":
                txt = f"{usrtxt} {random.choice(TAGMES)}"
                await client.send_message(chat_id, txt)
            elif mode == "text_on_reply":
                await msg.reply(f"[{random.choice(EMOJI)}](tg://user?id={usr.user.id})")
            await asyncio.sleep(4)
            usrnum = 0
            usrtxt = ""
    try:
        spam_chats.remove(chat_id)
    except:
        pass


@app.on_message(filters.command(["gmtag"], prefixes=["/", "@", "#"]))
async def mention_allvc(client, message):
    chat_id = message.chat.id
    if message.chat.type == ChatType.PRIVATE:
        return await message.reply("๏ ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ ᴏɴʟʏ ғᴏʀ ɢʀᴏᴜᴘs.")

    is_admin = False
    try:
        participant = await client.get_chat_member(chat_id, message.from_user.id)
    except UserNotParticipant:
        is_admin = False
    else:
        if participant.status in (
            ChatMemberStatus.ADMINISTRATOR,
            ChatMemberStatus.OWNER
        ):
            is_admin = True
    if not is_admin:
        return await message.reply("๏ ʏᴏᴜ ᴀʀᴇ ɴᴏᴛ ᴀᴅᴍɪɴ ʙᴀʙʏ, ᴏɴʟʏ ᴀᴅᴍɪɴs ᴄᴀɴ ᴛᴀɢ ᴍᴇᴍʙᴇʀs. ")
    if chat_id in spam_chats:
        return await message.reply("๏ ᴘʟᴇᴀsᴇ ᴀᴛ ғɪʀsᴛ sᴛᴏᴘ ʀᴜɴɴɪɴɢ ᴍᴇɴᴛɪᴏɴ ᴘʀᴏᴄᴇss...")
    spam_chats.append(chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in client.get_chat_members(chat_id):
        if not chat_id in spam_chats:
            break
        if usr.user.is_bot:
            continue
        usrnum += 1
        usrtxt += f"[{usr.user.first_name}](tg://user?id={usr.user.id}) "

        if usrnum == 1:
            txt = f"{usrtxt} {random.choice(VC_TAG)}"
            await client.send_message(chat_id, txt)
            await asyncio.sleep(4)
            usrnum = 0
            usrtxt = ""
    try:
        spam_chats.remove(chat_id)
    except:
        pass



@app.on_message(filters.command(["gmstop", "gnstop", "cancle"]))
async def cancel_spam(client, message):
    if not message.chat.id in spam_chats:
        return await message.reply("๏ ᴄᴜʀʀᴇɴᴛʟʏ ɪ'ᴍ ɴᴏᴛ ᴛᴀɢɢɪɴɢ ʙᴀʙʏ.")
    is_admin = False
    try:
        participant = await client.get_chat_member(message.chat.id, message.from_user.id)
    except UserNotParticipant:
        is_admin = False
    else:
        if participant.status in (
            ChatMemberStatus.ADMINISTRATOR,
            ChatMemberStatus.OWNER
        ):
            is_admin = True
    if not is_admin:
        return await message.reply("๏ ʏᴏᴜ ᴀʀᴇ ɴᴏᴛ ᴀᴅᴍɪɴ ʙᴀʙʏ, ᴏɴʟʏ ᴀᴅᴍɪɴs ᴄᴀɴ ᴛᴀɢ ᴍᴇᴍʙᴇʀs.")
    else:
        try:
            spam_chats.remove(message.chat.id)
        except:
            pass
        return await message.reply("๏ ᴍᴇɴᴛɪᴏɴ ᴘʀᴏᴄᴇss sᴛᴏᴘᴘᴇᴅ ๏")


