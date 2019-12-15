import requests
r = requests.post(
    "https://api.deepai.org/api/text-generator",
    data={
        'text': 'TEXT',
    },
    headers={'api-key': 'API-KEY'}
)
output = r.json()
lines = output["output"].split("\n")
print(lines[0])