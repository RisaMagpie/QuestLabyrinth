from flask import Flask, request
import re
import telegram
from telebot.credentials import bot_token, bot_user_name, URL
import re

global bot
global TOKEN
TOKEN = bot_token
bot = telegram.Bot(token=TOKEN)

app = Flask(__name__)


#for routes read here: https://flask.palletsprojects.com/en/1.0.x/quickstart/
@app.route('/{}'.format(TOKEN), methods=['POST'])
def respond():
    # retrieve the message in JSON and then transform it to Telegram object
    update = telegram.Update.de_json(request.get_json(force=True), bot)
    chat_id = update.message.chat.id
    msg_id = update.message.message_id

    # Telegram understands UTF-8, so encode text for unicode compatibility
    text = update.message.text.encode('utf-8').decode()
    # for debugging purposes only
    print("got text message :", text)
    # the first time you chat with the bot AKA the welcoming message

    if text == "/start":
        bot_welcome = """
        Этот бот является текстовым квестом. Ваша задача выбраться из лабиринта, не попавшись монстрам в лапы. Пока что это просто бот, который принимает сообщения и возвращает это же собщение без символов.
        """
        # send the welcoming message
        bot.sendMessage(chat_id=chat_id, text=bot_welcome, reply_to_message_id=msg_id)
    else:
        try:
            # clear the message we got from any non alphabets
            text = re.sub(r"\W", "_", text)          
            bot.sendMessage(chat_id=chat_id, text=text, reply_to_message_id=msg_id)
        except Exception:
            # if things went wrong
            bot.sendMessage(chat_id=chat_id, text="Упс, что-то пошло не так. Попробуйте перезапустить бота.", reply_to_message_id=msg_id)

    return 'ok'

# for messagies arriving:
@app.route('/setwebhook', methods=['GET', 'POST'])
def set_webhook():
    # we use the bot object to link the bot to our app which live
    # in the link provided by URL
    s = bot.setWebhook('{URL}{HOOK}'.format(URL=URL, HOOK=TOKEN))
    # something to let us know things work
    if s:
        return "webhook setup ok"
    else:
        return "webhook setup failed"
    
@app.route('/')
def index():
    return ' Hello! Bot is running now. You can write in telegram @QuestLabyrinthBot'
if __name__ == '__main__':
    # note the threaded arg which allow
    # your app to have more than one thread
    app.run(threaded=True)
