"""Перевод между форматами: CSV, простой YAML, JSON-справочник."""

import json


def csv_to_records(text: str) -> list[dict]:
    lines = [line for line in text.splitlines() if line.strip()]
    if not lines:
        return []

    names = lines[0].split(",")
    rows = []
    for line in lines[1:]:
        parts = line.split(",")
        row = {}
        for i in range(len(names)):
            if i < len(parts):
                row[names[i]] = parts[i]
            else:
                row[names[i]] = ""
        rows.append(row)
    return rows


def parse_settings(lines: list[str]) -> dict:
    data = {}
    list_key = None

    for line in lines:
        line = line.split("#", 1)[0].strip()
        if line == "":
            continue

        if line.startswith("-"):
            if list_key is not None:
                data[list_key].append(to_type(line[1:].strip()))
            continue

        key, _, value = line.partition(":")
        key = key.strip()
        value = value.strip()

        if value == "":
            list_key = key
            data[key] = []
        else:
            list_key = None
            data[key] = to_type(value)

    return data


def to_type(text: str):
    small = text.lower()
    if small == "true" or small == "yes":
        return True
    if small == "false" or small == "no":
        return False
    try:
        return int(text)
    except ValueError:
        pass
    try:
        return float(text)
    except ValueError:
        pass
    return text


def merge_by_key(rows: list[dict], extra: dict, key: str = "id") -> list[dict]:
    result = []
    for row in rows:
        new_row = dict(row)
        val = row.get(key)
        if val in extra and isinstance(extra[val], dict):
            for k, v in extra[val].items():
                if k not in new_row:
                    new_row[k] = v
        result.append(new_row)
    return result


def records_to_json(records: list[dict]) -> str:
    return json.dumps(records, ensure_ascii=False, indent=2, sort_keys=True)