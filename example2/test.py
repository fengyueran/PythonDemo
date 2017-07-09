from lxml import etree
import urllib2
import urllib
import json

request = urllib2.Request('http://hr.tencent.com/position.php?&start=10#a')
response =urllib2.urlopen(request)
resHtml = response.read()
output =open('tencent.json','w')

html = etree.HTML(resHtml)
result = html.xpath('//tr[@class="odd"] | //tr[@class="even"]')

for site in result:
    item={}

    name = site.xpath('./td[1]/a')[0].text
    detailLink = site.xpath('./td[1]/a')[0].attrib['href']
    catalog = site.xpath('./td[2]')[0].text
    recruitNumber = site.xpath('./td[3]')[0].text
    workLocation = site.xpath('./td[4]')[0].text
    publishTime = site.xpath('./td[5]')[0].text

    print type(name)
    print name,detailLink,catalog,recruitNumber,workLocation,publishTime
    item['name']=name
    item['detailLink']=detailLink
    item['catalog']=catalog
    item['recruitNumber']=recruitNumber
    item['publishTime']=publishTime

    line = json.dumps(item,ensure_ascii=False) + '\n'
    print line
    output.write(line.encode('utf-8'))
output.close()
