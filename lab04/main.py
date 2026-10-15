import sys
from stats import average_by_city, read_valid, warmest_city


def main():
    lines = sys.stdin.read().splitlines()
    records = read_valid(lines)

    error_lines_count = getattr(read_valid, "error_count", 0)
    correct_lines_count = len(records)

    best_city = warmest_city(records)
    if best_city:
        averages = average_by_city(records)
        max_avg_temp = averages[best_city]
    else:
        max_avg_temp = 0.0

    print(correct_lines_count)
    print(error_lines_count)
    print(f"{max_avg_temp:.1f}")


if __name__ == "__main__":
    main()