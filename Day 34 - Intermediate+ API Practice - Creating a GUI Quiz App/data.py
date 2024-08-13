import requests

parameters = {
    'amount': 10,
    "difficulty": "easy",
    "type": "boolean",
}

response = requests.get(url="https://opentdb.com/api.php", params=parameters)
response.raise_for_status()

questions = response.json()
print(questions["results"])
question_data = questions["results"]
print(question_data)