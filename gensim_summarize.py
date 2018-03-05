#import all libraries needed to perform this program
from gensim.summarization import summarize
from bs4 import BeautifulSoup
import requests
#dict which contains all urls which we are working with
#dict key will be title of the url and value will be url link
urls = {
    'Title of url1': 'url1',
    'Title of url2': 'url2'
}
for key in urls.keys():
    url = urls[key]
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    data = soup.get_text()
    text = data
    print("PAPER URL: {}".format(url))
    print("TITLE: {}".format(key))
    print("GENERATED SUMMARY: {}".format(summarize(text)))
