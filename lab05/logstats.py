LEVELS = {"DEBUG", "INFO", "WARNING", "ERROR"}


def parse_event(line: str) -> dict:
    parts = line.split(maxsplit=2)
    if len(parts) != 3:
        raise ValueError(f"bad line: {line!r}")
    time, level, message = parts
    if level not in LEVELS:
        raise ValueError(f"unknown level: {level!r}")
    return {"time": time, "level": level, "message": message.rstrip("\n")}


def count_levels(lines) -> dict:
    counts = {}
    for line in lines:
        if not line.strip():
            continue
        try:
            event = parse_event(line)
        except ValueError:
            counts["BROKEN"] = counts.get("BROKEN", 0) + 1
            continue
        counts[event["level"]] = counts.get(event["level"], 0) + 1
    return counts


def top_errors(lines, n: int) -> list:
    counter = {}
    for line in lines:
        if not line.strip():
            continue
        try:
            event = parse_event(line)
        except ValueError:
            continue
        if event["level"] != "ERROR":
            continue
        msg = event["message"]
        counter[msg] = counter.get(msg, 0) + 1
    ordered = sorted(counter.items(), key=lambda kv: (-kv[1], kv[0]))
    return [[msg, cnt] for msg, cnt in ordered[:n]]


def format_report(counts: dict, errors: list) -> str:
    out = ["Отчёт по журналу", ""]
    for level in sorted(counts):
        out.append(f"{level}: {counts[level]}")
    out.append("")
    out.append("Частые ошибки:")
    for message, cnt in errors:
        out.append(f"- {message} — {cnt}")
    return "\n".join(out) + "\n"