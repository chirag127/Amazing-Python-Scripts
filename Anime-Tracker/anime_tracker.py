import requests
from bs4 import BeautifulSoup
import re

# mainly bs4 lib is used for extracting html from web pages
def details(soup):
    # selecting div with class pure...
    info = soup.find("div", {"class": "pure-1 md-3-5"})
    # now extracting the text for p tag of the div
    print("\nAbout  the Anime : \n", "\t\t", info.find("p").getText(), "\n")

    total_episodes = soup.find("div", {"class": "pure-1 md-1-5"})
    print(
        "\nTotal number of episodes :\t",
        re.sub("[^0-9]", "", total_episodes.find("span").getText()),
    )  # usimg regex for only selecting numbers

    Active_years = soup.find("span", {"class": "iconYear"})
    print("\n Years Active (From-To)\t:\t", Active_years.getText(), "-\n")

    rating = soup.find("div", {"class": "avgRating"})
    print("Rating : ", rating.find("span").getText())

    tags = soup.find("div", {"class": "tags"})
    # print("Tags : ", tags.find('ul').getText())

    list = [tags.find("ul").getText() for _ in range(4)]
    print("\nTags : \n")
    print((list[0].replace("\n", "  ")))

def entry():
    print("\nType complete name>>\n")
    anime_name = (
        input("[+] Enter the name of the Anime : ").strip().title().replace(" ", "-")
    )

    print("\n")
    print(anime_name)

    search_url = "https://www.anime-planet.com/anime/" + anime_name
    source_code = requests.get(search_url)
    content = source_code.content
    soup = BeautifulSoup(content, features="html.parser")

    try:
        details(soup)
    except AttributeError:
        print("Anime info not found")

if __name__ == "__main__":
    entry()
