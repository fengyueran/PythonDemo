# -*- coding:utf-8 -*-
import urllib2
import urllib
from lxml import etree
import chardet
import json
import codecs
import zlib
from bs4 import BeautifulSoup


def GetTimeByArticle(url):
    request = urllib2.Request(url)
    response = urllib2.urlopen(request)
    resHtml = response.read()
    html = etree.HTML(resHtml)
    time = html.xpath('//span[@class="tail-info"]')[1].text
    print time
    return time


def main():
    output = codecs.open('soufang.json', 'w', encoding='utf-8')

    for pn in range(1, 40, 1):

        page = pn + 1
        url = 'http://newhouse.cq.fang.com/house/s/b' + str(pn+90) + '/?ctm=1.cq.xf_search.page.'+ str(page)
        print url
        request = urllib2.Request(url)
        request.add_header('Accept-encoding', 'gzip')
        response = urllib2.urlopen(request)

        resHtml = response.read()
        gzipped = response.headers.get('Content-Encoding')
        resHtml = zlib.decompress(resHtml, 16+zlib.MAX_WBITS)

        resHtml = unicode(resHtml,'GB18030').encode('utf-8')
        # print html

        html_dom = etree.HTML(resHtml.decode('utf-8'))
        # print etree.tostring(html_dom, pretty_print=True)
        html = html_dom
        # print html

        sites = html.xpath('//li/div[@class="clearfix"]')
        # print sites
        for site in sites:
            address =  site.xpath('.//*[@class="address"]/a')[0].attrib['title'].strip()
            price = site.xpath('.//*[@class="nhouse_price"]/span/text()[last()]')
            print address
            print price
        #     # print etree.tostring(site.xpath('.//a')[0])
        #     title = site.xpath('.//a')[0].text
        #     Article_url = site.xpath('.//a')[0].attrib['href']
        #     reply_date = GetTimeByArticle('http://tieba.baidu.com' + Article_url)
        #     # strip 去掉空格
        #     jieshao = site.xpath('.//*[@class="threadlist_abs threadlist_abs_onlyline "]')[0].text.strip()
        #     author = site.xpath('.//*[@class="frs-author-name j_user_card "]')[0].text.strip()
        #     lastName = site.xpath('.//*[@class="frs-author-name j_user_card "]')[1].text.strip()
        #     print title, jieshao, Article_url, author, lastName
        #
            item = {}
        #
            item['price'] = price
            item['address'] = address

        #     item['lastName'] = lastName
        #     item['reply_date'] = reply_date
        #     print item
        #
            line = json.dumps(item, ensure_ascii=False)
            print line
            # print type(line)

            output.write(line + "\n")
        # output.close()
    print 'end'

if __name__ == '__main__':
    main()
