from .. import Riz, SUDO_USERS, rizoelversion
from .. import ALIVE_PIC
from telethon import events, version, Button
from telethon.tl.custom import button
from time import time
from datetime import datetime

RIZ_PIC = ALIVE_PIC if ALIVE_PIC else "https://telegra.ph/file/ef6efd684ecddabd3e8f8.jpg"
  

          
rizoel = "✧ твн ѕραмвσт ιѕ αℓινє ✧\n\n"

rizoel += f"┏━━━━━━━━━━━━━━━━━━━\n"

rizoel += f"┣➣ **ᴘʏᴛʜᴏɴ ᴠᴇʀsɪᴏɴ** : `3.9.6`\n"

rizoel += f"┣➣ **ᴛᴇʟᴇᴛʜᴏɴ ᴠᴇʀsɪᴏɴ** : `{version.__version__}`\n"

rizoel += f"┣➣ **𝐓𝐁𝐇 𝐒𝐏𝐀𝐌𝐁𝐎𝐓 𝐕𝐄𝐑𝐒𝐈𝐎𝐍**  : `{𝐓𝐁𝐇 𝐒𝐏𝐀𝐌𝐁𝐎𝐓 𝐕𝐄𝐑𝐒𝐈𝐎𝐍}`\n"

rizoel += f"┗━━━━━━━━━━━━━━━━━━━\n\n"
         
                                    
@Riz.on(events.NewMessage(pattern=".alive"))
async def alive(event):
    if event.sender_id in SUDO_USERS:
     await Riz.send_file(event.chat_id,
                                  RIZ_PIC,
                                  caption=rizoel,
                                  buttons=[
        [
        Button.url("ᴄʜᴀɴɴᴇʟ", "https://t.me/TBH_NETWORK"),
        Button.url("sᴜᴘᴘᴏʀᴛ", "https://t.me/TBH_NETWORK")
        ],
        [
        Button.url("• ʀᴇᴘᴏ •", "www.pornhub.com")
        ]
        ]
        )
    
    #### ABE SUN BHOSDIKE KANG MAT KRNA VRNA TERA DEVICE HACK KRLUNGA
    
