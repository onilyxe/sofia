from sqlite3 import Row

from aiosqlite import Connection


class ChatUserRepository:
    def __init__(self, connection: Connection):
        self.connection = connection

    async def get_chat_user(self, chat_id: int, user_id: int) -> list | None:
        data = await self.connection.execute("SELECT * FROM chat_users WHERE chat_id = ? AND user_id = ?",
                                             (chat_id, user_id,))
        return await data.fetchone()

    async def add_chat_user(self, chat_id: int, user_id: int) -> Row | None:
        data = await self.connection.execute_insert("INSERT OR IGNORE INTO chat_users (chat_id, user_id) "
                                                    "VALUES (?, ?)", (chat_id, user_id))
        await self.connection.commit()
        return data

    async def update_user_russophobia(self, chat_id: int, user_id: int, russophobia: int) -> None:
        data = await self.connection.execute("UPDATE chat_users SET russophobia = ? WHERE chat_id = ? AND user_id = ?",
                                      (russophobia, chat_id, user_id))
        await self.connection.commit()