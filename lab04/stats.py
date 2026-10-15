def parse_record(line: str) -> dict:
    """
    Разбирает строку «город;температура;дата» в словарь.
    Если строка негодная — возбуждает ValueError.
    """
    parts = line.split(";")

    if len(parts) != 3:
        raise ValueError(f"Неверное количество полей: '{line}'")

    city, temp_str, date = parts

    if not city.strip() or not date.strip():
        raise ValueError(f"Город или дата пусты: '{line}'")

    try:
        temp = float(temp_str)
    except ValueError:
        raise ValueError(f"Некорректная температура: '{line}'")

    return {
        "city": city.strip(),
        "temperature": temp,
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
            continue

        try:
            record = parse_record(line)
            valid_records.append(record)
        except ValueError:
            error_count += 1

    read_valid.error_count = error_count
    return valid_records


def average_by_city(records: list[dict]) -> dict:
    """
    Счет средних температур по каждому городу, округленный до десятых.
    """
    totals = {}
    counts = {}

    for record in records:
        city = record["city"]
        # Используем ключ 'temperature', который ожидает тестер
        totals[city] = totals.get(city, 0.0) + record["temperature"]
        counts[city] = counts.get(city, 0) + 1

    averages = {}
    for city in totals:
        averages[city] = round(totals[city] / counts[city], 1)

    return averages


def warmest_city(records: list[dict]) -> str:
    """
    Город с наибольшей средней температурой. При равенстве — первый по алфавиту.
    """
    if not records:
        return ""

    averages = average_by_city(records)

    best_city = None
    max_temp = float('-inf')

    for city in sorted(averages.keys()):
        if averages[city] > max_temp:
            max_temp = averages[city]
            best_city = city

    return best_city if best_city is not None else ""