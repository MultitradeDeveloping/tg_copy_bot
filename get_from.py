from _libs import *
from info import *
from send import *



@client.on(events.NewMessage(chats=channel_toread_username))
async def handler(event):
    text = event.message.message

    # Определяем канал, откуда пришло сообщение
    src = event.chat.username  
    print(f"📩 Новое сообщение в канале {src}: {text}")

    messages = await client.get_messages(src, limit=1)
    text_ = messages[0].text

    text_ = await format(text_, src)
    
    print(text_)

    # Ищем индекс источника, чтобы отправить в соответствующий канал
    if src in channel_toread_username:
        idx = channel_toread_username.index(src)
        send_via_bot(text_, topic_tosend_username[idx])
# Старт клиента
async def main():
    await client.start()
    print("🚀 Бот запущен и слушает канал...")
    await client.run_until_disconnected()

client.loop.run_until_complete(main())
