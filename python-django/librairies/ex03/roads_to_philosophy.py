from bs4 import BeautifulSoup
import sys
import requests


def parse_input(user_input: str) -> str:
    user_input = user_input.replace(' ', '_')
    return (f'/wiki/{user_input}')


def road_to_philosophy(subject: str) -> list:
    list_of_titles: list = []
    link_of_page = get_link_title(list_of_titles, subject)
    while ('Philosophy' not in list_of_titles):
        link_of_page = get_link_title(list_of_titles, link_of_page)
        if (len(link_of_page) == 0):
            raise ValueError("It leads to a dead end !")
    return (list_of_titles)


def get_link_title(list_of_titles: list, link: str) -> str:
    link_of_page: str = ''
    req = requests.get('https://en.wikipedia.org' + link)
    soup = BeautifulSoup(req.content, "html.parser")
    page_title = soup.find('span', attrs={'class': 'mw-page-title-main'}).text
    if (page_title in list_of_titles):
        raise ValueError("It leads to an infinite loop !")
    list_of_titles.append(page_title)
    p_content = soup.find('div', {'class': 'mw-content-ltr'}).findChildren('p')
    for i in p_content:
        if (i.a is not None and i.a.has_attr('href')):
            link_of_page = i.a.attrs['href']
            break
    return (link_of_page)


def main() -> None:
    assert len(sys.argv) == 2, "Bad Argument"
    user_input = parse_input(sys.argv[1])
    try:
        list_of_titles = road_to_philosophy(user_input)
        for title in list_of_titles:
            print(title)
        print(f"{len(list_of_titles) + 1} roads from \
{sys.argv[1]} to philosophy !")
    except ValueError as err:
        print(err)


if __name__ == "__main__":
    main()
