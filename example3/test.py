from bs4 import BeautifulSoup
import urllib2
import urllib
import json

request = urllib2.Request('http://hr.tencent.com/position.php?&start=10#a')
response =urllib2.urlopen(request)
resHtml = response.read()
output =open('tencent.json','w')

html = BeautifulSoup(resHtml,'lxml')
result = html.select('tr[class="even"]')
result2 = html.select('tr[class="odd"]')
result+=result2
print len(result)

for site in result:
    item={}

    name = site.select('td a')[0].get_text()
    detailLink = site.select('td a')[0].attrs['href']
    catalog = site.select('td')[1].get_text()
    recruitNumber = site.select('td')[2].get_text()
    workLocation = site.select('td')[3].get_text()
    publishTime = site.select('td')[4].get_text()

    item['name']=name
    item['detailLink']=detailLink
    item['catalog']=catalog
    item['recruitNumber']=recruitNumber
    item['publishTime']=publishTime

    line = json.dumps(item,ensure_ascii=False) + '\n'
    print line

    output.write(line.encode('utf-8'))

output.close()
