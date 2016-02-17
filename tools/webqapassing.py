# -*- coding: utf-8 -*-

import xml.etree.ElementTree as ET

import requests

_BASE = 'https://webqa-ci.mozilla.com'
STAGE = _BASE + '/view/Socorro/job/socorro.stage.saucelabs/rssAll'
PROD = _BASE + '/view/Socorro/job/socorro.prod.saucelabs/rssAll'


def run():
    for url, name in ((STAGE, 'STAGE'), (PROD, 'PROD')):
        print name, u'⏱'
        xml = requests.get(url).text
        root = ET.fromstring(xml)
        ns = {
            'atom': 'http://www.w3.org/2005/Atom',
        }
        for entry in root.findall('atom:entry', ns):
            for title in entry.findall('atom:title', ns):
                if 'broken' in title.text:
                    print u'💔 \tBROKEN!'
                else:
                    print u'👍 \tAhhhh, everything seems to be fine.'
                print "({})".format(title.text)

            for link in entry.findall('atom:link', ns):
                print link.attrib['href']
            break

        print


if __name__ == '__main__':
    import sys
    sys.exit(run())
