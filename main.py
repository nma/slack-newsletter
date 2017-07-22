import logging
import re
from slackbot.bot import Bot, respond_to, default_reply

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


description = '''
I am a newsletter aggregator bot. My job is just to lurk on channels and accept url links and notices to add
to next month's newsletter.

You can ask me to add events by typing
@lettucebot add <text>|<url>

You can also ask me to keep ideas in a side bin
@lettucebot save <text>|<url>

I can give you a breakdown of the current links here
@lettucebot show

I can give you an inline showcase of what I have collected
@lettucebot stats
'''


@default_reply
def my_default_handler(message):
    message.reply(description)


@respond_to('hi', re.IGNORECASE)
def hi(message):
    message.reply('hi')


@respond_to('add (.*)', re.IGNORECASE)
def add(message, content):
    pass


@respond_to('draft (.*)', re.IGNORECASE)
def draft(message, content):
    pass


@respond_to('show', re.IGNORECASE)
def show(message):
    pass


@respond_to('stats', re.IGNORECASE)
def stats(message):
    pass


def main():
    logger.info('bot:pre_initialize')
    bot = Bot()
    logger.info('bot:post_initialize')
    logger.info('bot:pre_run')
    bot.run()
    logger.info('bot:post_run')

if __name__ == "__main__":
    main()
