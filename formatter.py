import json

import yarl

BASE_URL = yarl.URL("https://cdn.discordapp.com/emojis")


def main():

    print("loading emotes...")
    with open("emotes.json", "r") as Json:
        emotes = json.load(Json)

    print("building and writing URLs...")
    for obj in emotes:
        obj["url"] = str(BASE_URL / obj["id"]) + (".gif" if obj["animated"] else ".png")

    old_len = len(emotes)
    new_emotes = list({x["id"]: x for x in emotes}.values())
    new_len = len(new_emotes)
    print(f"removing {old_len - new_len} duplicates...")

    print("writing to emotes_updated.json...")
    with open("emotes_updated.json", "w") as NewJson:
        json.dump(new_emotes, NewJson, indent=3)

    if input("Write a list of URLs to url_list.txt? [Y/n] ").lower() == "y":
        print("writing a list of URLs...")
        with open("url_list.txt", "w") as UrlList:
            UrlList.writelines([obj["url"] + "\n" for obj in new_emotes])


if __name__ == "__main__":
    main()
    print("Done!")
