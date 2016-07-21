
import requests
import re
from bs4 import BeautifulSoup

all_essays = ''

r = requests.get("http://www.writingacademia.com/category/ielts-writing-task-2")
#print(r.text)
index = r.text
page_num = re.search("Page 1 of (\d+)", index)
if page_num:
    page_num = int(page_num.group(1))
for i in range(page_num):
    i += 1
    page_url = 'http://www.writingacademia.com/category/ielts-writing-task-2/page/' + str(i)
    print page_url
    r = requests.get(page_url)
    index = r.text
    essay_titles = re.findall('http://www.writingacademia.com/ielts-writing-task-2/(.+?)\"', index)
    if essay_titles:
        for i in set(essay_titles):
            print i 
            page_url = 'http://www.writingacademia.com/ielts-writing-task-2/' + i
            r = requests.get(page_url)
            page_content = r.text
            soup = BeautifulSoup(page_content, 'html.parser')
            essay_content = soup.find_all('div',class_="entry-content")[0]
            for i in essay_content.find_all('p'):
            #    print i.text
                all_essays += i.text.encode('utf-8') + '\n'
            all_essays += '\n\n'

with open("all_essays",'w') as f:
    f.write(all_essays)
