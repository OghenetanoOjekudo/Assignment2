from collections import Counter
import string

def get_clean_tokens(filename):
    # I reused the same cleaning rules from Q1
    cleanedTokens = []

    with open(filename, "r", encoding="utf-8") as file:
        text = file.read()

    rawTokens = text.split()

    for token in rawTokens:
        token = token.lower()
        token = token.strip(string.punctuation)

        alphaCount = sum(1 for ch in token if ch.isalpha())
        if alphaCount >= 2:
            cleanedTokens.append(token)

    return cleanedTokens


def main():
    filename = "sample-file.txt"
    tokens = get_clean_tokens(filename)

    # I built bigrams by pairing each word with the next one
    bigrams = []
    for i in range(len(tokens) - 1):
        bigrams.append((tokens[i], tokens[i + 1]))

    bigramCounts = Counter(bigrams)

    # I got the 5 most common bigrams in descending order
    top5 = bigramCounts.most_common(5)

    for (w1, w2), count in top5:
        print(f"{w1} {w2} -> {count}")


if __name__ == "__main__":
    main()
