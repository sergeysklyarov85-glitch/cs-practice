def parse_record(line: str) -> dict:
"""
Разбирает строку «город;температура;дата» в словарь.
Если строка негодная — возбуждает ValueError.
"""
parts = line.split(";")
if len(parts) != 3:
raise ValueError(f"Неверное количество полей (ожидалось 3, получено {len(parts)}): '{line}'")

city, temp_str, date = parts
if not city.strip() or not date.strip():
raise ValueError(f"Город или дата не могут быть пустыми: '{line}'")

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

# Сохраняем счётчик ошибок в атрибут функции
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
# Заглушка, её допишем на последнем шаге
if not records:
return ""
return records[0]["city"]