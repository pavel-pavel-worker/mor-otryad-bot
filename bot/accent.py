import requests
from lxml import html

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36'
}


def get_word_accent(word):
    url = f'https://xn----8sbhebeda0a3c5a7a.xn--p1ai/в-слове-{word}'
    with requests.Session() as session:
        response = session.get(url, headers=headers)
        if response.status_code == 404:
            return [f'Слово «{word}» отсутствует в словаре']
        print(response.status_code)
    site_text = response.text
    parsed_site = html.fromstring(site_text)
    xpath = '/html/body/div[1]/div/div[1]/div[@class="rule"]'
    words = [x.text_content().strip().split()[-1][:-1] for x in parsed_site.xpath(xpath)]
    return words
