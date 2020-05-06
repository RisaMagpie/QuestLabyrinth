from flask import Flask, request, render_template
import re
import telegram
from telebot import user_register
import os


bot_user_name = "QuestLabyrinthBot"
URL = "https://quest-labyrinth.herokuapp.com/"
bot_token = os.environ['bot_token']

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
    chat_id:int = update.message.chat.id
    msg_id:int = update.message.message_id

    # Telegram understands UTF-8, so encode text for unicode compatibility
    text:str = update.message.text.encode('utf-8').decode()
    # for debugging purposes only
    print("got text message :", text)
    # the first time you chat with the bot AKA the welcoming message

    if text == "/start" or text == "Начать сначала":
        bot_welcome = """
        Этот бот является текстовым квестом. Ваша задача выбраться из лабиринта, не попавшись монстрам в лапы. Пока что это просто бот, который принимает сообщения и возвращает это же собщение без символов.
        """
        # send the welcoming message
        bot.sendMessage(chat_id=chat_id, text=bot_welcome)

        # registration:
        user_id:int = update.message.from_user.id

        is_registered : bool
        answer_text : str
        possible_actions : list
        is_registered, answer_text, possible_actions = user_register.registration(user_id)        
        if is_registered:
            print("User was successfull registered and his state set to init values")
            possible_actions.append(['Начать сначала'])
            key_board = telegram.ReplyKeyboardMarkup(possible_actions)
            bot.sendMessage(chat_id=chat_id, text=answer_text, reply_markup = key_board)
        else:
            text = "Registration went wrong"
            bot.sendMessage(chat_id=chat_id, text=text, reply_to_message_id=msg_id)
            
    else:          
        # В будущем надо вынести это в отдельный скрипт
        try:
            # clear the message we got from any non alphabets
            text = re.sub(r"\W", "_", text)          
            bot.sendMessage(chat_id=chat_id, text=text)
        except Exception:
            # if things went wrong
            bot.sendMessage(chat_id=chat_id, text="Упс, что-то пошло не так. Попробуйте перезапустить бота.")

    return 'ok'

# for messagies arriving:
@app.route('/setwebhook', methods=['GET', 'POST'])
def set_webhook():
    bot.deleteWebhook()
    s = bot.setWebhook('{URL}{HOOK}'.format(URL=URL, HOOK=TOKEN))
    # something to let us know things work
    if s:
        return "webhook setup ok"
    else:
        return "webhook setup failed"
  
@app.route('/')
def index():
    return render_template('index.html')
if __name__ == '__main__':
    app.run(threaded=True)
    set_webhook()
