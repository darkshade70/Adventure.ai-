import requests


def prompt(text):
    r = requests.post(
        "https://api.deepai.org/api/text-generator",
        data={
            'text': text,
        },
        headers={'api-key': '63d85e82-3cc2-4b31-98a7-bae1b009635b'}
    )
    output = r.json()
    lines = output["output"].split("\n")
    return lines[0]


print(prompt("You walk into a dark room and find yourself face to face with a dungeon Guardian."))
