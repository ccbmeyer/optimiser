import requests
from bs4 import BeautifulSoup

search_term = "software testing"
url = f"https://www.google.com/search?q={search_term}"

response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

# results = soup.find_all("div", class_="r")
results = soup.find_all("a")


for i, result in enumerate(results[:25]):
    # link = result.find("a").get("href")
    print(f"The Ruslt is:{result}")
    if "/url" in result:
        print(result)

    #if "wikipedia" in link:
    #   print(f"Wikipedia link found in result {i + 1}")
    #    break
else:
    print("Wikipedia link not found in first 5 results")

