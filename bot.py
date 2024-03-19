import asyncio
import logging
from aiogram import Bot, Dispatcher
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from background import keep_alive
from Handlers import other_handlers
from time_message import send_message_time, send_message_window, send_message_bye
from datetime import datetime
from config_date.config import *


logger = logging.getLogger(__name__)


async def main() -> None:
    # Логирование

    logging.basicConfig(
        level=logging.INFO,
        format='%(filename)s:%(lineno)d #%(levelname)-8s'
        '[%(asctime)s] - %(name)s - %(message)s'
    )
    logger.info('Start bot work')
    config: Config = load_config()

    bot: Bot = Bot(token=config.tg_bot.token)
    dp: Dispatcher = Dispatcher()

    scheduler = AsyncIOScheduler(timezone="Asia/Tomsk")

    scheduler.add_job(send_message_time, trigger='cron', day_of_week='mon-fri', hour=11, minute=1,
                      start_date=datetime.now(), kwargs={'bot': bot})
    scheduler.add_job(send_message_window, trigger='cron', day_of_week='mon-fri', hour=9, minute=59,
                      start_date=datetime.now(), kwargs={'bot': bot})
    scheduler.add_job(send_message_window, trigger='cron', day_of_week='mon-fri', hour=10, minute=59,
                      start_date=datetime.now(), kwargs={'bot': bot})
    # scheduler.add_job(send_message_window, trigger='cron', day_of_week='mon-fri', hour=12, minute=30,
    #                     start_date=datetime.now(), kwargs={'bot': bot})
    scheduler.add_job(send_message_notification, trigger='cron', day_of_week='mon-fri', hour=19, minute=10,
                      start_date=datetime.now(), kwargs={'bot': bot})
    scheduler.add_job(send_message_window, trigger='cron', day_of_week='mon-fri', hour=16, minute=59,
                      start_date=datetime.now(), kwargs={'bot': bot})
    scheduler.add_job(send_message_bye, trigger='cron', day_of_week='fri', hour=19, minute=00,
                      start_date=datetime.now(), kwargs={'bot': bot})
    scheduler.start()

    dp.include_router(other_handlers.router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

keep_alive()


if __name__ == '__main__':
    asyncio.run(main())