import requests
import json
from html.parser import HTMLParser


class Parser(HTMLParser):
    def __init__(self, *, convert_charrefs: bool = ..., tag: str) -> None:
        super().__init__(convert_charrefs=convert_charrefs)
        self.tag = None
        self.user_tag = tag

    def handle_data(self, data) -> None:
        if self.tag == self.user_tag:
            print(f"{data=}")

    def handle_starttag(self, tag, attrs) -> None:
        self.tag = tag
        if self.tag == self.user_tag:
            print(f"------------------------")
            print(f"start: <{self.tag}>")
            for attr in attrs:
                print(f"{attr}")


parser = Parser(tag=input("tag: "))

url = "https://pi.archenhold.de/service/vertretungsplan"

# post = requests.post(url="https://pi.archenhold.de/index.php?option=com_jevents&ttoption=com_jevents&typeaheadtask=gwejson&file=fetchlatestevents&path=module&folder=mod_jevents_latest&token=b217c39024b61e1468931949cf50043d", data={"json": {}})

page = requests.get("https://pi.archenhold.de/service/vertretungsplan").text

parser.feed(page)

