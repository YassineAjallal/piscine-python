import requests
import json
import dewiki
import sys


def send_request(subject: str) -> str:
    api_url = "https://en.wikipedia.org/w/api.php"
    params = {
        'action': 'query',
        'format': 'json',
        'titles': subject,
        'prop': 'extracts',
        'explaintext': True,
    }
    try:
        response = requests.get(api_url, params=params)
        response.raise_for_status()
        data = json.loads(response.text)
        page = next(iter(data['query']['pages'].values()))
        article_content = page['extract']
        if (len(article_content) == 0):
            raise Exception()
    except Exception:
        print('result not found')
        sys.exit()
    return (article_content)


def create_result_file(result: str, subject: str) -> None:
    try:
        f = open(subject + '.wiki', mode='w')
        f.write(result)
    except IOError as ferr:
        print(ferr)


def main() -> None:
    assert len(sys.argv) == 2, "Bad argument"
    article_content = send_request(sys.argv[1])
    article_content = dewiki.from_string(article_content)
    create_result_file(article_content, sys.argv[1])


if __name__ == "__main__":
    main()
