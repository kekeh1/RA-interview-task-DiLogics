from bs4 import BeautifulSoup
import requests
from csv import writer


def get_description(url):
    headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/601.3.9 (KHTML, like Gecko) Version/9.0.2 Safari/601.3.9'}
    page2 = requests.get(url, headers=headers)
    soup2 = BeautifulSoup(page2.text, 'html.parser')
    temp = soup2.find('div', class_="_3xX726aBn29LDbsDtzr_6E _1Ap4F5maDtT1E1YuCiaO0r D3IL3FD0RFy_mkKLPwL4")
    result = ""
    if temp != None:
        description = temp.find_all('p', class_="_1qeIAgB0cPwnLhDF9XSiJM")
        if len(description) != 0:
            for i in range(len(description)):
                result = result + description[i].text



    #description = sou p2.find('meta', attrs={'name': 'description'})['content']
    return result

def get_comment(url):
    headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/601.3.9 (KHTML, like Gecko) Version/9.0.2 Safari/601.3.9'}
    page2 = requests.get(url, headers=headers)
    soup2 = BeautifulSoup(page2.text, 'html.parser')
    temps = soup2.find_all('div', class_="_3cjCphgls6DH-irkVaA0GM")
    result = []
    if temps != None:
        for temp in temps:
            description = temp.find_all('p', class_="_1qeIAgB0cPwnLhDF9XSiJM")
            temp2 = ""
            if len(description) != 0:
                for i in range(len(description)):
                    temp2 = temp2 + description[i].text
            result.append(temp2)



    #description = sou p2.find('meta', attrs={'name': 'description'})['content']
    return result


url_obj = "https://www.reddit.com/search/?q=how%20to%20web%20automation"

headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/601.3.9 (KHTML, like Gecko) Version/9.0.2 Safari/601.3.9'}
page = requests.get(url_obj, headers=headers)

# print (page)

soup = BeautifulSoup(page.content, 'html.parser')

# print (soup)

lists = soup.find_all('h3', class_="_eYtD2XCVieq6emjKBH3m")
# print (len(lists))
lists_url = soup.find_all('a', class_ = "SQnoC3ObvgnGjWt90zD9Z _2INHSNB8V5eaWp4P0rY_mE")

with open('reddit_data.csv', 'w', encoding='utf8', newline='') as f:
    callwriter = writer(f)
    header = ['Title', 'Link', 'Description', 'Answers']
    callwriter.writerow(header)

    for i in range(len(lists)):
        Title = lists[i].text
        Link = lists_url[i]['href']
        Link = "https://www.reddit.com" + Link
        Description = get_description(Link)
        Answers = get_comment(Link)

        info = [Title, Link, Description, Answers]
        callwriter.writerow(info)