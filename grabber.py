import json
import math
import time

import requests
import yarl

from .config import TOKEN

BASE_URL = yarl.URL("https://ec.emote.bot/api/v0")

emote_objects = []


def get_after() -> dict:
    if not emote_objects:
        return {}
    return {"after": emote_objects[-1]["name"]}


def main(calls: int):
    session = requests.Session()
    session.headers = {"Authorization": TOKEN}

    for i in range(calls):
        url = str(BASE_URL / "emotes" % {"limit": 250} % get_after())
        print("{}/{}: Getting {}...".format(i, calls, url))
        res = session.get(url)
        if res.status_code != 200:
            print(
                "something has gone wrong, received status {}".format(
                    res.status_code
                )
            )
            exit(1)
        # at this point, response has a list of emote objects
        # add them to emote_objects
        res_json = res.json()
        print("Adding {} emotes to the objects...".format(len(res_json)))
        emote_objects.extend(res_json)
        print("...done! {} emotes so far.".format(len(emote_objects)))
        time.sleep(5)


if __name__ == "__main__":
    amt = input("How many emotes are there total? (use ec/list) > ")
    calls = math.ceil(int(amt) / 250)
    main(calls)
    print("writing emote objects to file...")
    with open("emotes.json", "w") as Json:
        json.dump(emote_objects, Json, indent=3)
    print()
    print("All done!")
    time.sleep(10)
    exit(0)
