import asyncio

from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError

from userbot import CMD_HELP, bot
from userbot import CMD_HANDLER as cmd
from userbot.utils import skyzu_cmd


@skyzu_cmd(pattern="tm(?: |$)(.*)")
async def _(event):
    chat = "@TempMailBot"
    geez = await event.edit("Sedang Memprosess...")
    async with bot.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=220112646)
            )
            await conv.send_message("/start")
            await asyncio.sleep(1)
            await conv.send_message("Generate New")
            response = await response
            geezuserbot = (response).reply_markup.rows[2].buttons[0].url
            await event.client.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            await geez.edit(
                "`Mohon Maaf, Silahkan Buka` @TempMailBot `Lalu Tekan Start dan Coba Lagi.`"
            )
            return
        await event.edit(
            f"**SKY TEMPMAIL** ~ `{response.message.message}`\n\n[KLIK DISINI UNTUK VERIFIKASI]({geezuserbot})"
        )


CMD_HELP.update(
    {"tempmail": "𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.tm`" "\n•: Mendapatkan Email Gratis Dari Temp Mail"}
)
