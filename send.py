from _libs import *
# from get_from import *
from info import *
# Отправка сообщения через Bot API



def convert_utc_to_gmt3(text):
    lines = text.splitlines()
    result_lines = []

    for line in lines:
        if "UTC" in line:
            try:
                # Выцепляем дату и время
                parts = line.split("**")
                date_part = parts[-1].split("UTC")[0].strip()
                dt = datetime.strptime(date_part, "%Y-%m-%d %H:%M")
                dt_gmt3 = dt + timedelta(hours=3)
                dt_gmt3_str = dt_gmt3.strftime("%Y-%m-%d %H:%M")

                # Заменяем дату во всей строке
                new_line = line.replace(date_part + " UTC", dt_gmt3_str)
                result_lines.append(new_line)
            except Exception as e:
                print(f"Ошибка обработки строки: {line}\n{e}")
                result_lines.append(line)
        else:
            result_lines.append(line)
    print("\n".join(result_lines))
    return ("\n".join(result_lines))


async def format(text, src):
    if src == "bybit_tokensplash":
        text = convert_utc_to_gmt3(text)
        text = text.replace("Start", "Старт")
        text = text.replace("End", "Конец")
        text = text.replace("New user deadline", "Дедлайн")
        text = text.replace("New user prize", "Награда*")
        text = text.replace("~$ ", "")
        text = text.replace("Details", "Детали")

        text = convert_utc_to_gmt3(text)
    if src == "kormushka_mexc":
        if "+" in text:
            text = "*Pump \n\n$" + text
        elif "i" in text:
            text = "*Dump \n\n$" + text
        text = text.replace("in", "за")
        text = text.replace("secs", "секунд*")
        text = text.replace("| Limit ~", "\n\n MEXC Limit - *")
        text = text.replace('`', "")
        text = text + "*"
    if src == "mexcTracker":
        # if "support me" in text:
            
        #     text = text.replace("```", "")
        #     text = text.replace("prices have leveled off to", "цены выровнялись до")
        #     text = text.replace("Duration", "*Продолжительность*")
        #     text = text.replace("Open", "*Открытие*")
        #     text = text.replace("Close", "*Закрытие*")
        #     text = text.replace("ATL", "*ATL*")
        #     text = text.replace("ATH", "*ATH*")
        #     text = text.replace("PNL", "*PNL*")

        # elif "difference changed to" in text:
        #     text = text.replace("difference changed to", 'спред изменился до')
            
        
        if "support me" in text:
            
            text = text.replace("source // chat // trackers // support me", "")
            if("Long" in text):
                text = text.replace("| Long", "")
                text = "🟢Long " + text
            if("Short" in text):
                text = text.replace("| Short", "")
                text = "🔴Short " + text
            available = ''.join([char for char in text if char in '✅❌'])
            results = []
            start_index = text.find("Lim/V24")
            text_n = text[start_index:] if start_index != -1 else ""

            for match in re.finditer(r':\s*([^;\n]+)', text_n):
                values = [v.strip().replace('*', '') for v in match.group(1).split('/')]
                results.extend(values)

            print(results)

            text = re.sub(r'```.*?```', '', text, flags=re.DOTALL)
            text = text.replace("*", "")
            
            text = text.replace("Long", "*Long*")
            text = text.replace("Short", "*Short*")
            text = text.replace("Arbitrage", "Арбитраж")
            text = text.replace("with", "")
            text = text.replace("ended", "продлился")
            text = text.replace("Price", "*Цена*")
            
            text = text.replace("CA:", "*Адрес*:")
            text = text.replace("Chain:", "*Блокчейн:*")
            text = re.sub(r'Lim/V24.*?(?=Found)', '', text, flags=re.DOTALL)

            text = re.sub(r'Блокчейн:\s*(.+)', r'*Блокчейн:* \1\nДепозит:\nВывод:\n\nЛиквидность:\nMEXC limit:\nОбьем 1ч/24ч:', text)
            if available.startswith("✅"):
                text = text.replace("Депозит:", "*Депозит: ✅*")
            if available.startswith("❌"):
                text = text.replace("Депозит:", "*Депозит: ❌*")
            if available[1] == "✅":
                text = text.replace("Вывод:", "*Вывод: ✅*")
            if available[1] == "❌":
                text = text.replace("Вывод:", "*Вывод: ✅*")    

            text = text.replace("Ликвидность:", f"*Ликвидность:* {results[0]}")
            text = text.replace("MEXC limit:", f"*MEXC limit:* {results[2]}")
            text = text.replace("Обьем 1ч/24ч:", f"*Обьем 1ч/24ч:* {results[3]}/{results[4]}")
            # text = text.replace("Deposit", "Депозит")
            # text = text.replace("Withdrawal", "Вывод")
            # text = text.replace("Spot", "*спот*")

            text = text.replace("Found", "*Найдено*")
            text =text.replace("15m", "15мин")
            text =text.replace("3h", "3ч")
            text =text.replace("24h", "24ч")

            
            text =text.replace("Avg Duration", "*Средняя продолжительность*")
            lines = text.strip().split('\n')
            text = '\n'.join(lines[:-1])
            

        else:
            text = ""
    if src == "DCATrack":
        text = re.sub(r'```.*?```', '', text, flags=re.DOTALL)
        if ("selling" in text or "buying" in text) and "filled and closed" not in text:
            lines = text.strip().split('\n')

            buy = "🟩" in text
            

            words = text.strip().split(' ')
            val = words[0]
            name = words[2]

            text = '\n'.join(lines[1:])
            
            text = re.sub(r'\(\d+\s+cycles\)', '', text)
            # text = re.sub(r'\(\d+\s+cycles\)', '', text)
            
            lines = text.splitlines()
            userline = next((i for i, line in enumerate(lines) if 'User:' in line), None)
            user = lines[userline].strip().split(' ')
            user = user[1]
            
            # for i in range(5):
            #     del lines[userline-2]
            
            text = '\n'.join(lines[:-1])
            user = user.replace("`", "")

            if buy:
                text = f"🟢 {name} {val}\n"  + text
                text = text.replace('Frequency:', f"[DCA](https://solscan.io/account/{user}) *покупает*")

            else:
                text = f"🔴 {name} {val}\n" + text
                text = text.replace('Frequency:', f"[DCA](https://solscan.io/account/{user}) *продаёт*")
            
            text = text.replace('every', 'каждые')
            text = text.replace('seconds', 'сек')


            lines = text.splitlines()
            quoteline = next((i for i, line in enumerate(lines) if 'Quote' in line), None)
            if quoteline is not None:
                del lines[quoteline]
            
            text = '\n'.join(lines)

            #переназначаем lines
            lines = text.splitlines()
            capline = next((i for i, line in enumerate(lines) if 'MC:' in line), None)
            
            if capline is not None:
                cap = lines[capline].strip().split(' ')
                cap_val = cap[1]
                lq_val = cap[4]

                # только замена нужных строк
                lines[capline] = f"MCap: {cap_val}"
                lines[capline + 1] = f"Ликвидности: {lq_val}"
            
            l = 3
            while l<capline:
                del lines[3]
                l+=1
            
            lines[2] += '\n'

            # заменяем только эти строки в text
            text = '\n'.join(lines)
            
            

            text = text.replace('Price:', 'Цена:')
            text = text.replace('**', '')


     
            # text = '\n'.join(lines)
            user = user.strip('`')

            
            lines = text.splitlines()
            Vline = next((i for i, line in enumerate(lines) if 'V1h' in line), None)
            
            if capline is not None:
                Vwords = lines[Vline].strip().split(' ')
                Vword = Vwords[4]

                lines[Vline] = f"Объём за час: {Vword}"
            
            text = '\n'.join(lines)

            text = text.replace('Period:', f'Период:')
            pattern = r'Период: (\d{2} \w+ \d{4} \d{2}:\d{2}:\d{2}) - (\d{2} \w+ \d{4} \d{2}:\d{2}:\d{2}) GMT'
    
            match = re.search(pattern, text)
            if not match:
                return text  # Если формат не найден — возвращаем оригинал

            dt_format = "%d %b %Y %H:%M:%S"
            try:
                start = datetime.strptime(match.group(1), dt_format)
                end = datetime.strptime(match.group(2), dt_format)
            except ValueError:
                # Если не английские месяцы, пробуем русский
                dt_format = "%d %B %Y %H:%M:%S"
                start = datetime.strptime(match.group(1), dt_format)
                end = datetime.strptime(match.group(2), dt_format)

            start += timedelta(hours=3)
            end += timedelta(hours=3)

            new_period = f"\nПериод: {start.strftime('%d %b %Y %H:%M:%S')} - {end.strftime('%d %b %Y %H:%M:%S')} GMT+3"

            lines = text.splitlines()
            text = '\n'.join(lines[:-2])
            text = text + '\n' + new_period
            
           

            # Найдём строку, где первое слово — Период
            lines = text.strip().splitlines()
            pattern = re.compile(r'^\*?Период\b.*', re.IGNORECASE)

            matching_line = None
            remaining_lines = []

            for line in lines:
                if matching_line is None and pattern.match(line.strip()):
                    matching_line = line
                else:
                    remaining_lines.append(line)

            # Собираем текст обратно, перенося подходящую строку в конец
            if matching_line:
                text = '\n'.join(remaining_lines + [matching_line])
            else:
                text = text.strip()

            monthes_en = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
            monthes_ru = ['Янв', 'Фев', 'Марта', 'Апр','Мая', 'Июня', 'Июля', 'Авг', 'Сен', 'Окт', 'Ноя','Дек']
            text = re.sub(r'(\bЦена\s+)(\w+)', r'\1**\2**', text)

            text = text.replace("MCap","*MCap*")
            text = text.replace("Ликвидности","*Ликвидности*")
            text = text.replace("Объём за час","*Объём за час*")
            text = text.replace("Цена","*Цена*")
            text = text.replace("Futures","*Futures*")
            text = text.replace("CA:","*CA*:")
            text = text.replace("User","*User*")
            text = text.replace("Период","*Период*")

            for i in range(len(monthes_en)):
                text = text.replace(monthes_en[i], monthes_ru[i])

            
        else: 
            text = ''
    
    return(text)



def send_via_bot(text, to):
    print("чёт пришло")
    url = f"https://api.telegram.org/bot{bot_api}/sendMessage"
    data = {
        "chat_id": channel_tosend_username[0],
        "text": text,
        "message_thread_id": to,
        "parse_mode": "Markdown",
        "disable_web_page_preview": True

    }
    try:
        response = requests.post(url, json=data)
        print(f"✅ Отправка через бот: {response.status_code}, {response.text}")
    except Exception as e:
        print(f"❌ Ошибка при отправке через бот: {e}")

# async def get_latest_message():
#     await client.start()
#     # Получаем объект канала
#     channel = await client.get_entity("DCATrack")
#     # Получаем последнее сообщение
#     messages = await client.get_messages(channel, limit=20)
#     text = await format(messages[1].text, "DCATrack")
#     send_via_bot(text, "DCATrack")
    
# with client:
#     client.loop.run_until_complete(get_latest_message())