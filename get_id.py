
import requests

TOKEN = "7745895532:AAHlBR8tyr9SPAEU8qnIYNDFHCQLnowiX78"  # вставь сюда токен бота
URL = f"https://api.telegram.org/bot{TOKEN}/getUpdates"

response = requests.get(URL)
data = response.json()

print("Топики, в которые писали сообщения:\n")

used_threads = set()

for update in data.get("result", []):
    msg = update.get("message")
    if msg:
        chat = msg["chat"]
        thread_id = msg.get("message_thread_id")
        if thread_id:
            title = chat.get("title", "Без названия")
            print(f"- Группа: {title} | chat_id: {chat['id']} | message_thread_id: {thread_id}")
            used_threads.add(thread_id)

if not used_threads:
    print("Сообщения в топиках пока не найдены. Напиши что-нибудь в нужный топик.")