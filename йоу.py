import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://dropstab.com/ru/insights/vesting"
headers = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

vesting_rows = soup.find_all("tr")

# Сюда будем сохранять строки таблицы
all_data = []

for row in vesting_rows:
    cols = row.find_all("td")
    data = [col.get_text(strip=True) for col in cols]
    if data:
        all_data.append(data)

# Создаём DataFrame
df = pd.DataFrame(all_data)

print(df)
