import requests
from lxml import html

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36'
}


def get_word_definition(word):
    url = f'https://lexicography.online/explanatory/dal/{word[0]}/{word}'
    with requests.Session() as session:
        response = session.get(url, headers=headers)
        if response.status_code == 404:
            return f'Слово «{word}» отсутствует в словаре'
        if response.status_code == 403:
            return f'Эта функция пока не работает'
        print(response.status_code)
    site_text = response.text
    parsed_site = html.fromstring(site_text)
    xpath = '//html/body/div[1]/div/article/p[1]'
    word = parsed_site.xpath(xpath)[0].text_content()
    return word

