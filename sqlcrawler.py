import urllib2, re
def scan(vict):
    try:
        request = urllib2.Request(vict+"'")
        response = urllib2.urlopen(request)
        data = response.read()
        if "error in your SQL syntax" in data:
            print "-->  "+vict
        elif "Query failed" in data:
            print "-->  "+vict
        elif "supplied argument is not a valid MySQL result resource in" in data:
            print  "-->  "+vict
        elif "You have an error in your SQL syntax" in data:
            print "-->  "+vict
        elif "ORDER BY" in data:
            print "-->  "+vict
        elif "mysql_num_rows()" in data:
            print "-->  "+vict
        elif "SQL query failed" in data:
            print "-->  "+vict
        elif "Microsoft JET Database Engine error '80040e14'" in data:
            print "-->  "+vict
        elif "Microsoft OLE DB Provider for Oracle" in data:
            print "-->  "+vict
        elif "Error:unknown" in data:
            print "-->  "+vict
        elif "Fatal error" in data:
            print "-->  "+vict
        elif "mysql_fetch" in data:
            print "-->  "+vict
        elif "Syntax error" in data:
            print "-->  "+vict
        else:
            pass
    except:
        pass
