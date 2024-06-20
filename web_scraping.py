import requests
from bs4 import BeautifulSoup

def get_word_definition(word):
    url = f"https://www.dictionary.com/browse/{word}"
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        definition = soup.find('span', {'class': 'one-click-content'})
        if definition:
            return definition.text.strip()
    return "Definition not found."
