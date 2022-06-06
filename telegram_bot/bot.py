import base64
import json
from urllib.request import urlopen

import requests
import telebot
from dotenv import dotenv_values
from telebot import types

config = dotenv_values('.env')

bot = telebot.TeleBot(config['TOKEN'])


class ChatSession:
    file = 'session.json'
    _session = {}

    def __init__(self):
        self._read()

    def add(self, key, value):
        self._session[str(key)] = str(value)
        self._save()

    def get(self, key):
        self._read()
        return self._session.get(str(key))

    def _save(self):
        with open(self.file, 'w') as f:
            json.dump(self._session, f)

    def _read(self):
        with open(self.file, 'r') as f:
            self._session = json.load(f)


chat_session = ChatSession()


@bot.message_handler(commands=['filters'])
def get_filters(message):
    if message.text == '/filters':
        keyboard = types.InlineKeyboardMarkup()
        response = requests.get('https://fish-eye.ml/api/nodes/filter/available/')
        data = response.json()
        for item in data:
            text = f"{item['name']} ({', '.join([node['name'] for node in item['nodes']])})"
            callback_data = f"filter_{item['id']}"
            keyboard.add(types.InlineKeyboardButton(text=text, callback_data=callback_data))
        bot.send_message(message.from_user.id, text='Please select the filter:', reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: True)
def display_selection(call):
    if 'filter_' in call.data:
        filter_id = call.data[len('filter_'):]
        chat_session.add(call.message.chat.id, filter_id)
        bot.send_message(call.message.chat.id, 'Please upload an image!')


@bot.message_handler(content_types=['photo'])
def execute_filter(message):
    chat_id = str(message.chat.id)
    filter_id = chat_session.get(chat_id)
    if not filter_id:
        bot.send_message(chat_id, 'Please select the filter from /filters command.')
        return

    filter_res = requests.get(f'https://fish-eye.ml/api/nodes/filter/{filter_id}/')
    filter_json = filter_res.json()
    benchmark_sec = filter_json.get('last_benchmark', {}).get('seconds')
    bot.send_message(chat_id, f'Please wait, last execution took {benchmark_sec}s...')

    image_file_id = message.photo[-1].file_id
    image_url = bot.get_file_url(image_file_id)
    image_base64 = base64.b64encode(urlopen(image_url).read())
    image_base64 = 'data:image/png;base64,' + str(image_base64)[2:-1] if image_base64 else None

    response = requests.post(
        url=f'https://fish-eye.ml/api/nodes/filter/{filter_id}/execute/',
        data=json.dumps({'image_base64': image_base64}),
        headers={'Content-Type': 'application/json'},
    )

    json_res = response.json()
    data = json_res.get('data')

    res_image_base64 = data.get('image_base64')

    if not res_image_base64:
        bot.send_message(chat_id, 'Oops! Couldn\'t read your image.')
        return

    with open('images_cache/' + image_file_id, 'wb') as f:
        split = res_image_base64.split(',')
        split.reverse()
        f.write(base64.b64decode(split[0]))

    bot.send_photo(chat_id, open('images_cache/' + image_file_id, 'rb'))


if __name__ == '__main__':
    print('Staring pooling...')
    bot.polling(none_stop=True, interval=0)
    print('Pooling end.')
