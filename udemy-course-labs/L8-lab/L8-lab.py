import os
import requests

pageslist = [
    { 'name': 'wizziexd', 'url':'http://www.wizzie.pl/xd'},
    { 'name': 'wizzie', 'url': 'http://www.wizzie.pl/' },
    { 'name': 'misiunia', 'url': 'http://www.misiunia.pl/'} ]


for page in pageslist:
    filepath = '/home/wisie/sandbox/udemy-course-labs/L8-lab/' + page['name'] + '.html'
    if os.path.isfile(filepath): os.remove(filepath)    # bo uzywamy append linie nizej
    f = open(filepath, 'a')  # A = APPEND ,,,, W = OVERWRITE EXISTING CONTENT 
    content = requests.get(page['url']).text
    f.write(content)
    f.close