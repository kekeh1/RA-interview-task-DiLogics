import urllib

from bs4 import BeautifulSoup
import requests
from csv import writer
import urllib.request



def get_comment(url):

    page2 = urllib.request.urlopen(url)
    soup2 = BeautifulSoup(page2, 'html.parser')
    temps = soup2.find_all('div', class_="content")
    result = []
    if temps != None:
        num = min(3, len(temps))
        for i in range(num):
            result.append(temps[i].text)




    #description = sou p2.find('meta', attrs={'name': 'description'})['content']
    return result


url_obj = "https://forum.imacros.net/viewforum.php?f=15"


page = urllib.request.urlopen(url_obj)

# print (page)


soup = BeautifulSoup(page, 'html.parser')

lists = soup.find_all('a', class_= "topictitle")
# print (len(lists))


with open('UiPath_data.csv', 'w', encoding='utf8', newline='') as f:
    callwriter = writer(f)
    header = ['Title', 'Link', 'Description', 'Answers']
    callwriter.writerow(header)

    for i in range(len(lists)):
        Title = lists[i].text

        Link = lists[i]['href']
        c = Link[1:]
        Link = "https://forum.imacros.net" + Link[1:]

        Answers = get_comment(Link)

        info = [Title, Link, Answers]
        callwriter.writerow(info)
