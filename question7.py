from urllib.request import Request, urlopen
from bs4 import BeautifulSoup

# URL of the Wikipedia page
url = "https://en.wikipedia.org/wiki/Data_science"

# I added a User-Agent so Wikipedia does not block the request
request = Request(url, headers={"User-Agent": "Mozilla/5.0"})

# I fetched the HTML content of the page
html = urlopen(request).read()

# I parsed the HTML using BeautifulSoup
soup = BeautifulSoup(html, "html.parser")

# I printed the page title
print("Page title:")
print(soup.title.text)
print()

# I found the main content div
content = soup.find("div", id="mw-content-text")

# I looped through paragraphs and printed the first one with at least 50 characters
for p in content.find_all("p"):
    text = p.get_text(strip=True)
    if len(text) >= 50:
        print("First paragraph (at least 50 characters):")
        print(text)
        break
