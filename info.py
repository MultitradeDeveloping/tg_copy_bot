from _libs import *


# Замените эти значения на свои
api_id = '15944941'
api_hash = '272f6b2104875189e6ba63915e887065'
bot_api = "7745895532:AAHlBR8tyr9SPAEU8qnIYNDFHCQLnowiX78"
channel_toread_username = ["test_lize090", "bybit_tokensplash", "kormushka_mexc", "mexcTracker", "DCATrack", "infinityhedge","invest_zonaa","WatcherGuru","test_lize090"] #NOT USING @
channel_tosend_username = ["-1002512059520","-1002512059520","-1002512059520","-1002512059520","-1002512059520","-1002512059520","-1002512059520","-1002512059520","-1002512059520"] #USING @
topic_tosend_username = ["3", "26", "5", "3", "9", "2161", "2161","2161","3"]

# Создаем клиент
client = TelegramClient('session_name', api_id, api_hash)
# translator = Translator()