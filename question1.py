from collections import Counter
import string

def get_clean_tokens(filename):
    # I used this list to store the cleaned words
    cleanedTokens = []

    # I read the entire file at once because I only need tokens
    with open(filename, "r", encoding="utf-8") as file:
        text = file.read()

    # I split by whitespace to get rough tokens
    rawTokens = text.split()

    for token in rawTokens:
        # I made everything lowercase so words like Data and data count as the same
        token = token.lower()

        # I removed punctuation only from the start/end (so data-driven stays as data-driven)
        token = token.strip(string.punctuation)

        # I counted alphabetic characters to enforce "at least two letters"
        alphaCount = sum(1 for ch in token if ch.isalpha())

        if alphaCount >= 2:
            cleanedTokens.append(token)

    return cleanedTokens


def main():
    filename = "sample-file.txt"

    tokens = get_clean_tokens(filename)
    wordCounts = Counter(tokens)

    # I used most_common to get the top 10 words in descending order
    top10 = wordCounts.most_common(10)

    for word, count in top10:
        print(f"{word} -> {count}")


if __name__ == "__main__":
    main()
