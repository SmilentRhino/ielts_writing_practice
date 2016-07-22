
import requests
import re
from bs4 import BeautifulSoup
import html2text
all_essays = ''

r = requests.get("http://www.ielts-mentor.com/cue-card-sample")
index = r.text
soup = BeautifulSoup(index,'html.parser')
end_of_page = soup.find('li',class_='pagination-end').a['href']
start_from = 0
while True:
    page_url = 'http://www.ielts-mentor.com/cue-card-sample?start=' + str(start_from)
    
    r = requests.get(page_url)
    index = r.text
    essays = re.findall("/cue-card-sample/.*?\"",index)
    for i in set(essays):
        essay_page = 'http://www.ielts-mentor.com/' + i
        r = requests.get(essay_page)
        index = r.text
        soup = BeautifulSoup(index,'html.parser')
        article = soup.find('div',id='main')
        text = html2text.html2text(article)
        print(text)
        break
    start_from += 20
    if end_of_page == 'http://www.ielts-mentor.com/cue-card-sample?start=' + str(start_from):
        break
    break

with open("ielts-mentor-cue-card-samples",'w') as f:
    f.write(all_essays)
