from urllib.request import Request, urlopen
from bs4 import BeautifulSoup

# I used the Data science Wikipedia page for this question
url = "https://en.wikipedia.org/wiki/Data_science"

# I added a User-Agent so the request doesn't get blocked
request = Request(url, headers={"User-Agent": "Mozilla/5.0"})

# I fetched the HTML and parsed it with BeautifulSoup
html = urlopen(request).read()
soup = BeautifulSoup(html, "html.parser")

# I found the main content area
content = soup.find("div", id="mw-content-text")

# These are headings I was told not to include
bannedWords = ["References", "External links", "See also", "Notes"]

headings = []

# I looped through all h2 headings in the main content
for h2 in content.find_all("h2"):
    # I got the visible heading text and stripped extra spaces
    headingText = h2.get_text(" ", strip=True)

    # I removed any [edit] text that Wikipedia includes
    headingText = headingText.replace("[edit]", "").strip()

    # I skipped headings that contain banned words
    if any(banned in headingText for banned in bannedWords):
        continue

    # I kept non-empty headings only
    if headingText != "":
        headings.append(headingText)

# I saved headings to headings.txt, one per line, in order
with open("headings.txt", "w", encoding="utf-8") as f:
    for heading in headings:
        f.write(heading + "\n")

print(f"Saved {len(headings)} headings to headings.txt")
