import cookielib, mechanize, re, urllib, urllib2
acc = 'testacc'
pw = 'testpassword_for_testaccount'
login_url = 'https://ccpa.unc.edu/psp/paprd/EMPLOYEE/EMPL/h/?tab=NC_REDIRECT&TargetPage=Student'
alt_login_url = 'https://ccpa.unc.edu/psp/paprd/EMPLOYEE/UNC_CS/c/NC_CUSTOM_MENU.NC_PORTAL_STUDENT.GBL'

'''
# get proper cookies
cookie_jar = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie_jar))
urllib2.install_opener(opener)
req = urllib2.Request(login_url)
rsp = urllib2.urlopen(req)

br = mechanize.Browser()
br.set_cookiejar(cookie_jar)

data = urllib.urlencode(dict(j_username=acc, j_password=pw))

page = br.open(alt_login_url, data)
print page.read()
'''
