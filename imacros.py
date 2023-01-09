import urllib

from bs4 import BeautifulSoup
from csv import writer
import urllib.request


def get_comment(url):
    page2 = urllib.request.urlopen(url)
    soup2 = BeautifulSoup(page2, 'html.parser')
    temps = soup2.find_all('div', class_="content")
    result = []
    if temps is not None:
        num = min(3, len(temps))
        for j in range(num):
            result.append(temps[j].text)
    return result


url_objs = ["https://forum.imacros.net/viewforum.php?f=15", 'https://forum.imacros.net/viewforum.php?f=13', "https://forum.imacros.net/viewforum.php?f=23", "https://forum.imacros.net/viewforum.php?f=14"]

with open('imacros_data.csv', 'w', encoding='utf8', newline='') as f:
    callwriter = writer(f)
    header = ['Title', 'Link', 'Answers']
    callwriter.writerow(header)

    for url_obj in url_objs:
        page = urllib.request.urlopen(url_obj)

        soup = BeautifulSoup(page, 'html.parser')

        lists = soup.find_all('a', class_="topictitle")

        for i in range(len(lists)):
            Title = lists[i].text

            Link = lists[i]['href']
            c = Link[1:]
            Link = "https://forum.imacros.net" + Link[1:]

            Answers = get_comment(Link)

            info = [Title, Link, Answers]
            callwriter.writerow(info)
