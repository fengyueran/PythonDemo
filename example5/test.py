# -*- coding:utf-8 -*-
import urllib2
import urllib
from lxml import etree
import chardet
import json
import codecs
import zlib



def main():
    output = codecs.open('soufang.json', 'w', encoding='utf-8')

    for pn in range(1, 39, 1):
        url = 'http://newhouse.cq.fang.com/house/s/b' + str(pn+900) + '/?ctm=1.cq.xf_search.page.14'
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
            name = site.xpath('.//*[@class="nlcd_name"]/a')[0].text.strip()
            address =  site.xpath('.//*[@class="address"]/a')[0].text.strip()
            district = ''
            if len(address) > 0:
                address = address.split(']', 1 );
                district = address[0].split('[', 1 )[1];
                address = address[1].strip()

            print address

            # print "".join(address[0])
            # print len(address[0].split('[', 1 ))



            price = site.xpath('.//*[@class="nhouse_price"]/span/text()[last()]')
            priceUnit = site.xpath('.//*[@class="nhouse_price"]/em/text()');
            priceUnit = "".join(priceUnit)
            price = "".join(price) + ' ' + priceUnit
            # print address
            # print name, address, price

            item = {}

            item['price'] = price
            item['district'] = district
            item['address'] = address
            line = json.dumps(item, ensure_ascii=False)
            # # print line
            #
            output.write(line + "\n")
    output.close()
    print 'end'

if __name__ == '__main__':
    main()
