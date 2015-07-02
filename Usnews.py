import requests
from BeautifulSoup import BeautifulSoup
import re
import csv

csv_file = open('ranking_university_USnews.csv', 'wb', buffering=0)
writer = csv.writer(csv_file)

urls = ['http://colleges.usnews.rankingsandreviews.com/best-colleges/rankings/national-universities/data',\
        'http://colleges.usnews.rankingsandreviews.com/best-colleges/rankings/national-universities/data/page+2',\
        'http://colleges.usnews.rankingsandreviews.com/best-colleges/rankings/national-universities/data/page+3',\
        'http://colleges.usnews.rankingsandreviews.com/best-colleges/rankings/national-universities/data/page+4',\
        'http://colleges.usnews.rankingsandreviews.com/best-colleges/rankings/national-universities/data/page+5',\
        'http://colleges.usnews.rankingsandreviews.com/best-colleges/rankings/national-universities/data/page+6',\
        'http://colleges.usnews.rankingsandreviews.com/best-colleges/rankings/national-universities/data/page+7',\
        'http://colleges.usnews.rankingsandreviews.com/best-colleges/rankings/national-universities/data/page+8',\
        'http://colleges.usnews.rankingsandreviews.com/best-colleges/rankings/national-universities/data/page+9',\
        'http://colleges.usnews.rankingsandreviews.com/best-colleges/rankings/national-universities/data/page+10',\
        'http://colleges.usnews.rankingsandreviews.com/best-colleges/rankings/national-universities/data/page+11']
records = []
ranks1 = []
names = []
locations = []
for url in urls:
    r = requests.get(url)
    soup = BeautifulSoup(r.text)
    for rank in soup.findAll('span', attrs={'class': 'rankscore-bronze cluetip cluetip-stylized'}):
        ranks1.append(int(re.findall('\d+', rank.text)[0]))
    for college in soup.findAll('a', attrs={'class': 'school-name'}):
        names.append(college.text)
    for location in soup.findAll('p', attrs={'class': 'location'}):
        locations.append(location.text)

# print len(ranks), len(names), len(locations)
ranks2 = range(203, 281)
ranks = ranks1+list(ranks2)
# print ranks
for i in range(len(ranks)):
    records.append(i+1)
    records.append(ranks[i])
    records.append(names[i].encode('utf-8'))
    records.append(locations[i])
    writer.writerow(records)
    records = []
