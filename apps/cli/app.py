import requests
from PyInquirer import prompt, print_json

questions = [
    {
        'type': 'input',
        'name': 'term',
        'message': 'What word are you looking for?',
    }
]

answers = prompt(questions)


headers = {
    'x-rapidapi-host': "mashape-community-urban-dictionary.p.rapidapi.com",
    'x-rapidapi-key': "Ki10UxsNGrmshtSSGCTX6e0tkFBFp1mvHrQjsnCV3aXUf96n42"
}

response = requests.get("https://mashape-community-urban-dictionary.p.rapidapi.com/define?term="+answers["term"], headers=headers)
body = response.json()

print(body["list"][0]["definition"])