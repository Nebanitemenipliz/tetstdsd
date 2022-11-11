from .. import loader
from telethon.tl.types import Message


@loader.tds
class photo(loader.Module):
    """Подпишись на мой канал @userbotik"""

    strings = {"name": "photo"}

    async def photocmd(self, message: Message):
        """Скидывает photo)"""
        if message.out:
            await message.delete()

        await message.respond(
            f'<a href="https://t.me/userbotik/77">­</a>',
        )
