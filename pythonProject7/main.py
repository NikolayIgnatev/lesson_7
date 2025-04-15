import os
import ptbot
from dotenv import load_dotenv
from pytimeparse import parse


def reply(chat_id, text):
    time = parse(text)
    message_id = bot.send_message(chat_id, f"Осталось {time} секунд!")
    bot.create_countdown(time, notify, chat_id=chat_id, message_id=message_id, total=time)
    bot.create_timer(time + 1, seconds_left, chat_id=chat_id)


def notify(time, chat_id, message_id, total):
    bot.update_message(chat_id, message_id, f"{render_progressbar(total, time)}\nОсталось {time} секунд!")


def seconds_left(chat_id):
    bot.send_message(chat_id, "время вышло")


def render_progressbar(total, iteration, prefix='', suffix='', length=30, fill='█', zfill='░'):
    iteration = min(total, iteration)
    percent = "{0:.1f}".format(100 * (iteration / float(total)))
    filled_length = int(length * iteration // total)
    pbar = fill * filled_length + zfill * (length - filled_length)
    return f'{prefix} |{pbar}| {percent}% {suffix}'


def main():

    bot.send_message(tg_chat_id, "Бот запущен")
    bot.reply_on_message(reply)
    bot.run_bot()


if __name__ == "__main__":
    load_dotenv()

    tg_token = os.environ['TELEGRAM_TOKEN']
    tg_chat_id = os.environ['TG_CHAT_ID']
    bot = ptbot.Bot(tg_token)

    main()
