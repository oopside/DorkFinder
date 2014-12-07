import urllib2, re
mailler = open("mailler.txt","w")
def mail_crawler(site):
    request = urllib2.Request(site)
    response = urllib2.urlopen(request) 
    payload = response.read()
    results = re.findall(r'[\w\.-]+@[\w\.-]+', payload)
    for result in results:
        mailler.write(result)
        mailler.write("\n")
    mailler.close()
    print "e-postalar --> mailler.txt"
