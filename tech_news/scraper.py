import requests
import time

import requests
import time
from requests.exceptions import Timeout

# Requisito 1
def fetch(url):
  time.sleep(1)
  try:
      response = requests.get(url, timeout=3)
      if response.status_code == 200:
          return response.text
      else:
          return None
  except Timeout:
      return None

# Requisito 2
def scrape_noticia(html_content):
    """Seu código deve vir aqui"""


# Requisito 3
def scrape_novidades(html_content):
    """Seu código deve vir aqui"""


# Requisito 4
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
