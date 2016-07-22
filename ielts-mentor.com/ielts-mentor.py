
import requests
import re
from bs4 import BeautifulSoup
import html2text

r = requests.get("http://www.ielts-mentor.com/cue-card-sample", timeout=20)
index = r.text
soup = BeautifulSoup(index,'html.parser')
end_of_page = soup.find('li',class_='pagination-end').a['href']
print end_of_page
start_from = 0
while True:
    page_url = 'http://www.ielts-mentor.com/cue-card-sample?start=' + str(start_from)
    
    all_essays = ''
    r = requests.get(page_url, timeout=20)
    index = r.text
    essays = re.findall("/cue-card-sample/.*?\"",index)
    for i in set(essays):
        print i
        essay_page = 'http://www.ielts-mentor.com/' + i
        r = requests.get(essay_page, timeout=20)
        index = r.text
        soup = BeautifulSoup(index,'html.parser')
        article = soup.find('div',id='main')
        text = html2text.html2text(unicode(article))
        all_essays += text.encode('utf-8') + '\n\n'

    with open("ielts-mentor-cue-card-samples",'a') as f:
        f.write(all_essays)
    if ('http://www.ielts-mentor.com' + end_of_page) == ('http://www.ielts-mentor.com/cue-card-sample?start=' + str(start_from)):
        break
    start_from += 20

