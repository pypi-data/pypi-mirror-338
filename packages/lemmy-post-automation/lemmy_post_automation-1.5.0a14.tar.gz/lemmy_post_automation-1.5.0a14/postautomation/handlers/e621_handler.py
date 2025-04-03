from bs4 import BeautifulSoup

from postautomation import PostData
from postautomation.handlers.base import Handler


class E621Handler(Handler):
    def supports_domain(self, domain: str) -> bool:
        return domain == "e621.net"

    def scrape(self, url: str, document: BeautifulSoup) -> PostData:
        artists = [
            x.contents[0].replace(" (artist)", "") for x in document.find_all(
                "a",
                {"itemprop": "author"},
            ) if x.contents[0] != "conditional dnp"
        ]
        print(artists)
        img_url = document.find(
            "section", {"id": "image-container"},
        )["data-file-url"]

        return PostData(
            url,
            None,
            artists,
            img_url,
            True
        )
