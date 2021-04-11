import requests

url = "https://wordsapiv1.p.rapidapi.com/words/duck"

headers = {
    'x-rapidapi-key': "e57bf9bfd6mshcce6cc62862a96fp1c186cjsn0ee4f8fc27a1",
    'x-rapidapi-host': "wordsapiv1.p.rapidapi.com"
    }

response = requests.request("GET", url, headers=headers)

print(response.text)