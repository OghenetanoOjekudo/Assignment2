from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import csv

# I used the Machine learning Wikipedia page for this question
url = "https://en.wikipedia.org/wiki/Machine_learning"

# I added a User-Agent so the request doesn't get blocked
request = Request(url, headers={"User-Agent": "Mozilla/5.0"})

# I fetched and parsed the HTML
html = urlopen(request).read()
soup = BeautifulSoup(html, "html.parser")

# I found the main content area
content = soup.find("div", id="mw-content-text")

# I located the first table (inside mw-content-text) that has at least 3 data rows
chosenTable = None
for table in content.find_all("table"):
    rows = table.find_all("tr")

    # I counted rows that contain at least one <td> (data cell)
    dataRowCount = 0
    for r in rows:
        if r.find("td") is not None:
            dataRowCount += 1

    if dataRowCount >= 3:
        chosenTable = table
        break

if chosenTable is None:
    print("No table with at least 3 data rows was found.")
else:
    # I extracted rows from the chosen table
    tableRows = chosenTable.find_all("tr")

    extractedRows = []
    maxCols = 0

    # I extracted text from each row's td/th cells
    for r in tableRows:
        cells = r.find_all(["th", "td"])
        rowData = [c.get_text(" ", strip=True) for c in cells]

        # I skipped completely empty rows
        if all(item == "" for item in rowData):
            continue

        extractedRows.append(rowData)
        if len(rowData) > maxCols:
            maxCols = len(rowData)

    # I tried to build headers from <th> cells if present; otherwise I created col1, col2, ...
    header = None

    # I looked for a header row (a row that has <th> and no <td>)
    for r in tableRows:
        ths = r.find_all("th")
        tds = r.find_all("td")
        if len(ths) > 0 and len(tds) == 0:
            header = [th.get_text(" ", strip=True) for th in ths]
            break

    if header is None or len(header) == 0:
        header = [f"col{i}" for i in range(1, maxCols + 1)]

    # I padded the header if it's shorter than the widest row
    if len(header) < maxCols:
        header = header + [""] * (maxCols - len(header))

    # I padded each row so they all have the same number of columns
    paddedRows = []
    for row in extractedRows:
        if len(row) < maxCols:
            row = row + [""] * (maxCols - len(row))
        paddedRows.append(row)

    # I wrote everything to wiki_table.csv
    with open("wiki_table.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(header)
        writer.writerows(paddedRows)

    print("Saved table to wiki_table.csv")
