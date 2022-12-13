import requests
from bs4 import BeautifulSoup
import time
import json

URL_PATH = "https://www.vz.lt/visos-naujienos"
DELAY_IN_SECONDS = 5


def checking_page_status():
    pass
    # Nezinojau ar reikia tikrint statusa atskiroje funkcijoje


def get_articles_urls():
    for number in range(2):
        print("Getting page No:", number)
        print(f'Sleeping for {DELAY_IN_SECONDS} seconds')
        time.sleep(DELAY_IN_SECONDS)
        r = requests.get(URL_PATH, params={"pageno": number})
        time.sleep(DELAY_IN_SECONDS)
        bs = BeautifulSoup(r.text)
        articles = bs.findAll(class_='one-article')
        articles_urls = [article.a.attrs['href'] for article in articles]
        return articles_urls


def save_article_content_to_json_file(articles_urls):
    for href in articles_urls[:3]:
        print(href)
        r = requests.get(href)
        article_content = BeautifulSoup(r.text)
        with open("data.json", "w+", encoding='utf-8') as f:
            json.dump(list(article_content), f, ensure_ascii=False)


def main():
    articles_urls = get_articles_urls()
    save_article_content_to_json_file(articles_urls)


if __name__ == "__main__":
    main()


# TypeError: Object of type Tag is not JSON serializable
# https://stackoverflow.com/questions/45075615/typeerror-object-of-type-tag-is-not-json-serializable
