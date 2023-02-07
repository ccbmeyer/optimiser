import requests
from bs4 import BeautifulSoup

search_term = "software testing"
url = f"https://www.google.com/search?q={search_term}"

response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

results = soup.find_all("div", class_="r")

for i, result in enumerate(results[:5]):
    link = result.find("a").get("href")
    if "wikipedia" in link:
        print(f"Wikipedia link found in result {i + 1}")
        break
else:
    print("Wikipedia link not found in first 5 results")

