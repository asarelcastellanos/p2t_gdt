import requests
from bs4 import BeautifulSoup

URL = "https://smccis.smc.edu/isisdoc/web_cat_sched_20253.html"
import requests
from bs4 import BeautifulSoup

URL = "https://smccis.smc.edu/isisdoc/web_cat_sched_20253.html"

resp = requests.get(URL, timeout=15)
resp.raise_for_status()

soup = BeautifulSoup(resp.text, "lxml")
container_div = soup.find("div", id="container")
div_ids = [div["id"] for div in container_div.find_all("div", id=True)] if container_div else []
print(div_ids)
