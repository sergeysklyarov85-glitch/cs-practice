def parse_record(line: str) -> dict:
# Базовая заглушка
parts = line.split(";")
return {"city": parts[0], "temp": float(parts[1]), "date": parts[2]}

def read_valid(lines: list[str]) -> list[dict]:
# Просто преобразуем все строки без проверок
return [parse_record(line) for line in lines if line.strip()]

def average_by_city(records: list[dict]) -> dict:
return {}

def warmest_city(records: list[dict]) -> str:
return ""
