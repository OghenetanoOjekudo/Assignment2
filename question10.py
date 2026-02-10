def find_lines_containing(filename, keyword):
    """
    Returns a list of (line_number, line_text) for lines that contain keyword
    (case-insensitive). Line numbers start at 1.
    """
    matches = []

    # I used lowercase to make the search case-insensitive
    keywordLower = keyword.lower()

    with open(filename, "r", encoding="utf-8") as file:
        for lineNumber, line in enumerate(file, start=1):
            lineText = line.rstrip("\n")

            # I compared lowercased versions so "Lorem" matches "lorem"
            if keywordLower in lineText.lower():
                matches.append((lineNumber, lineText))

    return matches


# I tested the function using sample-file.txt with the keyword "lorem"
filename = "sample-file.txt"
keyword = "lorem"

results = find_lines_containing(filename, keyword)

print("Number of matching lines found:", len(results))

# I printed the first 3 matching lines (or fewer if there aren't 3)
for lineNumber, lineText in results[:3]:
    print(f"{lineNumber}: {lineText}")
