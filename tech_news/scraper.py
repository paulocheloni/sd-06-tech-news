import requests
import time


# Requisito 1
def fetch(url):
    """Pega as notícias através da URL informada"""
    try:
        time.sleep(1)
        response = requests.get(url, timeout=3)
        response.raise_for_status()
        return response.text
    except requests.exceptions.ConnectionError as error:
        print(f"Erro na requisição: {error}.")
        return None
    except requests.exceptions.ReadTimeout as error:
        print(f"Sem resposta do servidor: {error}.")
        return None
    except Exception:
        print("Erro interno.")
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
