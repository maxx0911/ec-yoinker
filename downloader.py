import os
import requests
import json

BASE_DIR = os.getcwd()

def build_filename(emoji: dict) -> str:
    nsfw_dir = "sfw" if emoji["nsfw"] == "SFW" else "nsfw"
    filename = emoji["name"]
    fileextension = 'gif' if emoji['animated'] else 'png'
    return f"{BASE_DIR}/{nsfw_dir}/{filename}.{fileextension}"

def main():
    # create necessary folders 
    # if they don't already exist

    print("Creating directories sfw and nsfw (if they don't already exist)...")
    if not os.path.exists(BASE_DIR + "/sfw"):
        os.mkdir(BASE_DIR + "/sfw")

    if not os.path.exists(BASE_DIR + "/nsfw"):
        os.mkdir(BASE_DIR + "/nsfw")

    # load emotes
    print("loading emotes...")
    with open("emotes_updated.json", "r") as Json:
        all_emotes = json.load(Json)

    if input(f"This will download {len(all_emotes)} emotes, it will take a while. Continue? [Y/n] ").lower() == "y":
        for emote in all_emotes:
            res = requests.get(emote["url"])
            filename = build_filename(emote)
            with open(
                filename,
                "wb"
            ) as EmojiFile:
                EmojiFile.write(res.content)

if __name__ == "__main__":
    main()