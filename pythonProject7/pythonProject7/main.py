import ptbot
import os
from dotenv import load_dotenv
from pytimeparse import parse


def reply(chat_id, text):
    time = parse(text)
    message_id = bot.send_message(chat_id, "Осталось {} секунд!".format(time))
    bot.create_countdown(time, notify, chat_id=chat_id,
                         message_id=message_id, total=time)
    bot.create_timer(time + 1, seconds_left, chat_id=chat_id)


def notify(time, chat_id, message_id, total):
    bot.update_message(chat_id, message_id,
                       f"{render_progressbar(total,time)}\nОсталось {time} секунд!")


def seconds_left(chat_id):
    bot.send_message(chat_id, 'время вышло')


def render_progressbar(total, iteration, prefix='',
                       suffix='', length=30, fill='█', zfill='░'):
    iteration = min(total, iteration)
    percent = "{0:.1f}"
    percent = percent.format(100 * (iteration / float(total)))
    filled_length = int(length * iteration // total)
    pbar = fill * filled_length + zfill * (length - filled_length)
    return '{0} |{1}| {2}% {3}'.format(prefix, pbar, percent, suffix)



if __name__ == "__main__":
    load_dotenv()
    TG_TOKEN = os.environ['TELEGRAM_TOKEN']
    TG_CHAT_ID = os.environ['TG_CHAT_ID']
    bot = ptbot.Bot(TG_TOKEN)
    bot.send_message(TG_CHAT_ID, "Бот запущен")

    bot = ptbot.Bot(TG_TOKEN)
    bot.reply_on_message(reply)
    bot.run_bot()
