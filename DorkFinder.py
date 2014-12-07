import urllib2, re
import sqlcrawler, mailcrawler
print """DorkFinder
 _   __                   ___                  
| | / /                  / _ \                 
| |/ /  __ _ _ __ __ _  / /_\ \_   _  __ _ ____
|    \ / _` | '__/ _` | |  _  | | | |/ _` |_  /
| |\  \ (_| | | | (_| | | | | | |_| | (_| |/ / 
\_| \_/\__,_|_|  \__,_| \_| |_/\__, |\__,_/___|
                                __/ |          
                               |___/
DorkFinder & SQLCrawler & MailCrawler | karaayaz_"""
print """
    [1] DorkFinder
    [2] SQLCrawler
    [3] MailCrawler
"""
while True:
    secim = raw_input("Bir Secim Yapin: ")
    if secim == "1":
        print "Dork Finder"
        print ""
        dork = raw_input("Dork: ")
        if " " in dork:
            dork=dork.replace(" ", "+")

        def finder(dork):
            first = 1
            while first<=200:
                response = urllib2.urlopen("http://www.bing.com/search?q={}&first={}".format(dork, first))
                payload = response.read()
                results = re.findall('<h2><a(.*?)h="', payload)
                for result in results:
                    result = result.lstrip(" href=")
                    result = result.lstrip('"')
                    result = result.rstrip('" ')
                    vict = result
                    sqlcrawler.scan(vict)
                first = first + 10
        finder(dork)
        print ""
        print "Bitti.."

    elif secim == "2":
        print "SQLCrawler"
        print ""
        vict = raw_input("Site: ")
        sqlcrawler.scan(vict)
        print ""
        print "Tarama Bitti.."

    elif secim == "3":
        print "Mail Crawler"
        print ""
        site = raw_input("Site: ")
        mailcrawler.mail_crawler(site)
        print ""
        print "Tarama Bitti.."
    else:
        print "Boyle Bir Secim Bulunmamakta..."
