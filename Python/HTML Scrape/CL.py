from lxml import html
import requests
import urllib3

urllib3.disable_warnings()

cl = requests.get('https://sfbay.craigslist.org/sfc/apa/d/san-francisco-top-floor-2-br-apt-near/7188716368.html', verify=False)
tree = html.fromstring(cl.content)

prices = tree.xpath('/html/body/section/section/h2/span/span[1]/text()')
pricesstrng = ''.join(prices)

hood = tree.xpath('/html/body/section/section/h2/span/small/text()')
hoodstrng = ''.join(hood)

address = tree.xpath('/html/body/section/section/section/section/h2/strong/text()')
address_strng = ''.join(address)
address_strng = address_strng.replace(',', '')
address_strng = address_strng.replace(' ', '+')
maplink = ('https://www.google.com/maps/place/' + address_strng)

wd = tree.xpath('/html/body/section/section/section/div/p/span[4]/text()')
wdstrng = ''.join(wd)
if wdstrng == 'w/d in unit':
    a = 'yes'
else:
    a = 'no'

datapoints = [pricesstrng, hoodstrng, maplink, a]
print()
print(datapoints)
print()


#urls = tree.xpath('/html/body/section/form/div[4]/ul/li/a/@href')

#api key = AIzaSyBoV7PpW6tPWuQJWTXfgw1J99XfOvjmxHM
#api client id = 380773912654-2snrv0td6qenlcf4qqoescedlf431l0l.apps.googleusercontent.com
#api client secret = DkC2WV0QjdDJOLpLMcbPwxAc

#cl = requests.get('https://sfbay.craigslist.org/favorites?fl=amthYnRoZmg6NzA1NjAxMDYxMCw0NDE5Njky', verify=False)
#tree = html.fromstring(cl.content)
#urls = tree.xpath('/html/body/section/form/div[4]/ul/li/a/@href')
#print(urls)
