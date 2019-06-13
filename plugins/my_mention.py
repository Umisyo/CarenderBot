from slackbot.bot import listen_to, default_reply


@default_reply
def default_message(message):
    message.reply('デフォルトのリプライです')


@listen_to('help-calender')
def help_calender(message):
    message.reply('カレンダーのヘルプです')