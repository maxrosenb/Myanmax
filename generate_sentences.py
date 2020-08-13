import tkinter
import requests
import sqlite3
import csv
from myanmar import converter
from fpdf import FPDF 
from bs4 import BeautifulSoup


#List of urls to create CSV from, only put unicode articles, no Zawgyi!
urls = ["https://www.bbc.com/burmese/world-53765311", 
        "https://www.bbc.com/burmese/53765310", 
        "https://www.bbc.com/burmese/media-53757737",
        "https://www.bbc.com/burmese/media-53270349",
        "https://www.bbc.com/burmese/world-53752727"]

articles = []
for i, url in enumerate(urls):
    res = requests.get(url)
    html_page = res.content
    soup = BeautifulSoup(html_page, 'html.parser')
    p_text = soup.find_all("p")
    text = soup.find_all(text=True)
    output = ''
    blacklist = [
        '[document]',
        'noscript',
        'header',
        'html',
        'meta',
        'head', 
        'input',
        'script',
        'sc-component-id',
        '@media',
        'media',
        'style',
    ]

    for t in text:
        if t.parent.name not in blacklist:
            output += '{} '.format(t)
    articles.append([url, output])
    
sentences = []
#Create sentences from BFS
for article in articles:
    article_url = article[0]
    article_text = article[1]
    curr_sentence = ""
    for x in article_text:
        if x != "။":
            curr_sentence += x  
        else:
            sentences.append([curr_sentence, article_url])
            curr_sentence = ""

#Generate CSV
with open('myanmax.csv', 'w', newline='') as csvfile:
    fieldnames = ['Text', 'Url']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for i,sentence in enumerate(sentences):
        if "Do Not Sell" in sentence[0] or "BBC" in sentence[0]:
            continue
        writer.writerow({'Text': sentence[0], 'Url': sentence[1]})