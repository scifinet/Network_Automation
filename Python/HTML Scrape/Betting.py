from lxml import html
import requests
import urllib3

urllib3.disable_warnings()
headers = {'Referer': 'https://www.oddschecker.com/','sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="99", "Google Chrome";v="99"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"macOS"','User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36', 'Accept-Encoding': 'gzip, deflate, br', 'Accept-Language': 'en-US,en;q=0.9', 'Cache-Control': 'max-age=0', 'Connection': 'keep-alive', 'Cookie': 'odds_type=traditional; odds_default_stake=10; logged_in=false; mobile_redirect=true; basket=""; cookiePolicy=false; myoc_device=YTI0MWEyNTktYjhhMS00Y2YyLWFiYjgtN2UyOTM3Zjc3NDRm; _qubitTracker=2d69ykspvzu-0l0ll0tq2-b1oykhc; qb_generic=:X92BX95:oddschecker.com; localCacheBusterSSL=1.0.31; _gid=GA1.2.1291415281.1646952547; myoc_device=YTI0MWEyNTktYjhhMS00Y2YyLWFiYjgtN2UyOTM3Zjc3NDRm; r-session-id=MWVlNTRmOWMtMDE4YS00OWMwLWIwYWQtZWMwZjBhZWNjMmQ3; _rdt_uuid=1646952551397.be639e0d-09c8-441b-9709-2dfbb707a8f8; _omappvp=4ckcFciEDGCrzUB1DWK1ggNLmrv8jRDhuCwHjkPMcK76hk545jYwMzfYDv7tZl7cbiRZ8j3JBD6Z0JPUvKPt0cRrw5S8YrKv; _hjSessionUser_1205098=eyJpZCI6ImZkNzI4MDhjLTVmZTctNWI2My1iMDY3LTUxYmMxZDZkMmNmNiIsImNyZWF0ZWQiOjE2NDY5NTI1NTE2ODYsImV4aXN0aW5nIjpmYWxzZX0=; _ga_8SVXZPTHX5=GS1.1.1646952550.1.0.1646952554.0; hideCountryBanner=true; _gcl_au=1.1.1032705023.1647018674; _fbp=fb.1.1647018676670.1744978295; all-odds-view=OddsComparison; mobile_welcome_centre=true; cacheBuster=1.0.31-.1261; bookie_bets=grid_views~8; logged_in=false; __cf_bm=_JYYpVZZNs3RYGfA8ztv8RmZdCoz0tAx.ePDInZghAI-1647027087-0-AfrWmQIbtxweNg1iO0zLsyl/19D/8LLCw6uc4EoN1ofc5EgAOPc4ACGYTEW+gt1XEV0dbQi1ygnOCh9dqVS/bJdXigSaJd1S5ezVnEnyOy/AF9GYYhlGHtm3jMcpOAIUq1wmHvm2e/4Dt6R6NByfh5oKz6erBRAmo3xuKJjmFtK6; number_access=23; session_number_access=2022-03-11+19%3A41%3A49%7E10; session-id=9006078816D83CDF7A04E8D06F3B058B; _ga_DYH22RGD1Z=GS1.1.1647021257.3.1.1647027710.0; _ga=GA1.2.1996712555.1646952547; qb_session=19:1:66:FZ+U=T&FehG=B&FfGg=M:0:X96Hfc5:0:0:0:0:oddschecker.com; qb_permanent=2d69ykspvzu-0l0ll0tq2-b1oykhc:33:29:3:2:0::0:1:0:BiKoBj:BiK6X+:A::::98.207.98.68:san%20francisco:157:united%20states:US:37.8:-122.41:san%20francisco-oak-san%20jose:807:california:5:migrated|1647027712848:FZ+U==g=CfEA=Hh&FehG==B=ChdV=Cm&FfGg==R=ChfX=Pj::X96gHNQ:X959e/W:0:0:0::0:0:oddschecker.com:0', 'Host': 'www.oddschecker.com', 'Sec-Fetch-Dest': 'document', 'Sec-Fetch-Mode': 'navigate', 'Sec-Fetch-Site': 'none', 'Sec-Fetch-User': '?1', 'Upgrade-Insecure-Requests': '1',}
session = requests.Session()

venues = requests.get('https://www.oddschecker.com/horse-racing', verify=False, headers=headers)
venues_tree = html.fromstring(venues.content)

venues_name = venues_tree.xpath('//*[@id="mc"]/section[2]/div/div/div/div[1]/div[1]/a')
venues_list = ''.join(venues_name)

print(venues_list)
#/html/body/div[1]/div[2]/div/div/div/div[2]/div/div[1]/section[2]/div/div/div/div[1]/div[1]/a
