# coding: utf-8
from bs4 import BeautifulSoup
import datetime
import dateparser

# use lxml
soup = BeautifulSoup(open("git.html"), "lxml")

# get the rows of the repositories table
rows = soup.find("table", { "class": "repositories"}).find("tbody").find_all("tr")

old_plugins = []
for row in rows:
    plugin = {}
    cells = row.find_all("td")
    # plugin name is the first cell
    plugin_name = str(cells[0].get_text()).rstrip().lstrip()
    # parse the date and check if it's older than 30 days
    try:
        last_update_date = dateparser.parse(cells[4].get_text())
        if last_update_date < datetime.datetime.now()-datetime.timedelta(days=30):
            days = datetime.datetime.now() - last_update_date
            plugin["name"] = plugin_name
            plugin["last_update"] = days.days
            old_plugins.append(plugin)
    except:
        print("cant parse date")
print(old_plugins)



