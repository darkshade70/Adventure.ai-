import requests


def gen(text):
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


# print(gen("The room appears empty but upon further investigation there is a locked vault hidden in the corner."))
