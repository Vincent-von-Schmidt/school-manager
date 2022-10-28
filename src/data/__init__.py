import json
import yaml

with open("src/data/config/config.yaml", "r") as file:
    config = yaml.safe_load(file.read())

with open("src/data/lang/{}.json".format(config["language"]), "r") as file:
    lang = json.loads(file.read())

debug = config["general"]["debug"]

def translate(text: str) -> str:
    """
    Translate text into, in config.yaml, given language. 
    If the translation is not available, 
    the missing translation will be returned in english. 
    The program will continue with the given text. 
    """
    try:
        translation = lang[text]
    
    except KeyError as error:
        translation = text
        if debug:
            print(f"translation error -> {error}")

    return translation

def safe_config() -> None:
    """
    Change the config entry in the file. 
    """
    with open("src/data/config/config.yaml", "w") as file: 
        yaml.dump(config, file, default_flow_style=False)
