from window import Window
from PyQt6.QtWidgets import QApplication
import sys
import json
import yaml

if __name__ == "__main__":
    app = QApplication([sys.argv])

    with open("config.yaml", "r") as file:
        config = yaml.safe_load(file.read())

    with open("lang/{}.json".format(config["language"]), "r") as file:
        lang=json.loads(file.read())

    window = Window(lang=lang, config=config)

    with open("style/dark.css", "r") as file:
        app.setStyleSheet(file.read())

    sys.exit(app.exec())
