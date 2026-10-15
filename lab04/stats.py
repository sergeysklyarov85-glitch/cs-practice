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
return [parse_record(line) for line in lines if line.strip()]

def average_by_city(records: list[dict]) -> dict:
return {}

def warmest_city(records: list[dict]) -> str:
return ""