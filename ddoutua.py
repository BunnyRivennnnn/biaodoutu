import requests
from requests.exceptions import RequestException
from bs4 import BeautifulSoup
import re
import os

header = {
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36',
    }
charset="UTF-8"
def get_page(url):
    r = requests.get(url,headers=header,timeout=30)
    try:
        if r.status_code == 200:
            return r.text
        return None
    except RequestException:
        return None
def get_contents(html):
    soup = BeautifulSoup(html,'lxml')
    for item in soup.find('div',{'class':"page-content text-center"}).find_all('a',{'class':"col-xs-6 col-sm-3"}):
        url_pattern = re.compile(r'data-original="(.*?)"')
        urls = re.findall(url_pattern, str(item))[0]
        title_pattern = re.compile(r'alt="(.*?)"')
        title = re.findall(title_pattern, str(item))[0].replace('?', '')
        tt = []
        lists = ([urls, title])
        tt.append(lists)
        img = requests.get(urls).content
        path = os.getcwd() + '/斗图呵呵呵/' + title + '.JPG'
        with open(path, 'wb') as f:
            f.write(img)
            print(title + '【【【【卧槽，你牛逼啊，此张图片尽然下载成功了呵呵呵】】】】')
def main():
    for i in range(1, 5):
        url = 'https://www.doutula.com/photo/list/?page={page}'.format(page=i)
        html = get_page(url)
        get_contents(html)
if __name__ == '__main__':
    main()