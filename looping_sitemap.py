from bs4 import BeautifulSoup
import requests
from scrape_smash import scrape_me_your_moves
import pandas as pd

# requests the sitemap for ultimateframedata.com
r = requests.get('https://ultimateframedata.com/sitemap.xml')
xml = r.text

soup = BeautifulSoup(xml, 'lxml')
sitemapTags = soup.find_all('loc')

sitemap = []
for tags in sitemapTags:
    sitemap.append(tags.string)
mainpage = sitemap[0]
stats = sitemap[1]
character_list = sitemap[2:]


df = pd.DataFrame(columns=['character_name','movename','basedamage','startup','advantage','active_frames','total_frames','landing_lag','shield_lag','shield_stun','notes'])


for character in character_list:
    df = df.append(scrape_me_your_moves(character))

df.to_csv('/Users/jameslee/Desktop/Data_Science/webscraping/smash_movelist.csv')








