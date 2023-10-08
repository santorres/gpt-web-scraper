

from bs4 import BeautifulSoup
from website_analysis.dom_analysis import HtmlLoader, UrlHtmlLoader

# Create HtmlLoader or UrlHtmlLoader based on the source type
def create_html_loader(source, source_type):
    if source_type == 'url':
        return UrlHtmlLoader(source)
    else:  # source_type == 'file'
        return HtmlLoader(source)

html_loader = create_html_loader("https://www.scrapethissite.com/pages/forms/", "url")
response = html_loader.load()

html_soup = BeautifulSoup(response, 'html.parser')
    
teams_table = html_soup.find('table', class_='table')
rows = teams_table.find_all('tr')

teams = []

for row in rows[1:]:
    team = {}
    cols = row.find_all('td')
    team['name'] = cols[0].text.strip()
    team['year'] = cols[1].text.strip()
    team['wins'] = cols[2].text.strip()
    team['losses'] = cols[3].text.strip()
    team['ot_losses'] = cols[4].text.strip()
    team['pct'] = cols[5].text.strip()
    team['gf'] = cols[6].text.strip()
    team['ga'] = cols[7].text.strip()
    team['diff'] = cols[8].text.strip()
    teams.append(team)

import json

with open('montreal_canadiens.json', 'w') as f:
    json.dump([team for team in teams if team['name'] == 'Montreal Canadiens'], f)
        