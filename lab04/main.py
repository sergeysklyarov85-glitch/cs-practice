import sys
from stats import average_by_city, read_valid, warmest_city

def main():
lines = sys.stdin.read().splitlines()
records = read_valid(lines)
print(len(records))
print(0)
print(0.0)

if __name__ == "__main__":
main()