import string

def normalize_line(line):
    # I normalized by lowercasing and removing whitespace + punctuation
    line = line.lower()

    normalizedChars = []
    for ch in line:
        # I removed punctuation characters
        if ch in string.punctuation:
            continue
        # I removed any whitespace (spaces, tabs, newlines)
        if ch.isspace():
            continue

        normalizedChars.append(ch)

    return "".join(normalizedChars)


def main():
    filename = "sample-file.txt"

    # I used a dictionary where:
    # key = normalized line
    # value = list of (line_number, original_line)
    groups = {}

    with open(filename, "r", encoding="utf-8") as file:
        for idx, line in enumerate(file, start=1):
            originalLine = line.rstrip("\n")
            key = normalize_line(originalLine)

            if key not in groups:
                groups[key] = []
            groups[key].append((idx, originalLine))

    # I kept only groups that have 2 or more lines (near-duplicate sets)
    duplicateSets = [group for group in groups.values() if len(group) >= 2]

    print("Number of near-duplicate sets:", len(duplicateSets))

    # I printed the first two sets found (if they exist)
    setsToShow = duplicateSets[:2]

    for setIndex, group in enumerate(setsToShow, start=1):
        print(f"\nSet {setIndex}:")
        for lineNumber, originalLine in group:
            print(f"{lineNumber}: {originalLine}")


if __name__ == "__main__":
    main()
