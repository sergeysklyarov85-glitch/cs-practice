from logstats import parse_event, count_levels, top_errors, format_report


def main():
    path = input().strip()

    total = 0
    errors = 0
    broken = 0
    with open(path, encoding="utf-8") as log:
        for line in log:
            if not line.strip():
                continue
            total += 1
            try:
                event = parse_event(line)
            except ValueError:
                broken += 1
                continue
            if event["level"] == "ERROR":
                errors += 1

    print(total)
    print(errors)
    print(broken)

    with open(path, encoding="utf-8") as log:
        counts = count_levels(log)
    with open(path, encoding="utf-8") as log:
        errors_top = top_errors(log, 3)

    report = format_report(counts, errors_top)
    with open("report.txt", "w", encoding="utf-8") as f:
        f.write(report)


if __name__ == "__main__":
    main()
