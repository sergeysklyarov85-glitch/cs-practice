def parse_record(line: str) -> dict:
"""
Разбирает строку «город;температура;дата» в словарь.
Если строка негодная — возбуждает ValueError.
"""
parts = line.split(";")

# 1. Проверяем количество полей
if len(parts) != 3:
raise ValueError(f"Неверное количество полей (ожидалось 3, получено {len(parts)}): '{line}'")

city, temp_str, date = parts

# 2. Проверяем, что город или дата не пустые
if not city.strip() or not date.strip():
raise ValueError(f"Город или дата не могут быть пустыми: '{line}'")

# 3. Проверяем корректность температуры
try:
temp = float(temp_str)
except ValueError:
raise ValueError(f"Некорректный формат температуры '{temp_str}': '{line}'")

return {
"city": city.strip(),
"temp": temp,
"date": date.strip()
}


def read_valid(lines: list[str]) -> list[dict]:
"""
Разбирает строки журнала, пропуская пустые и негодные.
Записывает количество ошибок в атрибут функции.
"""
valid_records = []
error_count = 0

for line in lines:
if not line.strip():
continue # Пустые строки пропускаются молча

try:
record = parse_record(line)
valid_records.append(record)
except ValueError:
error_count += 1

# Сохраняем счётчик ошибок в атрибут функции, чтобы main.py мог его прочитать
read_valid.error_count = error_count
return valid_records


def average_by_city(records: list[dict]) -> dict:
"""
Считает среднюю температуру по каждому городу, округлённую до десятых.
"""
totals = {}
counts = {}

for record in records:
city = record["city"]
totals[city] = totals.get(city, 0.0) + record["temp"]
counts[city] = counts.get(city, 0) + 1

averages = {}
for city in totals:
averages[city] = round(totals[city] / counts[city], 1)

return averages


def warmest_city(records: list[dict]) -> str:
"""
Находит город с наибольшей средней температурой.
При равенстве температур возвращает первый по алфавиту город.
"""
if not records:
return ""

averages = average_by_city(records)

# Сортируем: сначала по убыванию средней температуры (-averages[city]),
# а при совпадении — по алфавиту самого названия города (city)
return min(averages.keys(), key=lambda city: (-averages[city], city))