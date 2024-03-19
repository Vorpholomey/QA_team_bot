from __future__ import annotations

from dataclasses import dataclass
from environs import Env


@dataclass
class TgBot:
    tg_token: str
@dataclass
class TgChat:
    tg_chat_id: str
@dataclass
class TgMainChat:
    tg_main_chat_id: str


@dataclass
class Config:
    tg_bot: TgBot
    tg_chat: TgChat
    tg_main_chat: TgMainChat



def load_config(path: str | None = None) -> Config:

    env: Env = Env()
    env.read_env(path)

    return Config(
        tg_bot=TgBot(
            tg_token=env('BOT_TOKEN')
                    ),
        tg_chat=TgChat(
            tg_chat_id=env('CHAT_ID')
        ),
        tg_main_chat=TgMainChat(
            tg_main_chat_id=env('MAIN_CHAT_ID')
        )
            )
