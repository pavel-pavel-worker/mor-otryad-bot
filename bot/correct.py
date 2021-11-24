import requests
from lxml import html
from os import environ

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/96.0.4664.45 Safari/537.36 ',
    'cookie': environ['cookie'],
}


def get_correct_word(word):
    url = f'https://www.google.com/search?q={word}'
    with requests.Session() as session:
        response = session.get(url, headers=headers)
    site_text = response.text
    parsed_site = html.fromstring(site_text)
    xpath = '//*[@id="fprsl"]'
    results = parsed_site.xpath(xpath)
    if results:
        return results[0].text_content().capitalize()
    xpath = '//*[@id="taw"]/div[2]/p/a/b/i'
    results = parsed_site.xpath(xpath)
    if results:
        return results[0].text_content().capitalize()
    return 'Всё правильно'
