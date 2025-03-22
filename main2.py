import requests
from bs4 import BeautifulSoup
from tabulate import tabulate

url = input("input name : ")

def print_table(keys: list, values: list) -> str:
    if len(keys) != len(values):
        raise ValueError("Keys and values must have the same length.")

    table = []
    for key, value in zip(keys, values):
        table.append([key, value])
    
    return print(tabulate(
        table,
        headers=["Header", "Stats"],
        tablefmt="grid"
    ))

def main():
    URL = 'https://stalcrafthq.com/characters/RU/' + url
    HEADERS = {
        'User-Agent': (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/132.0.0.0 Safari/537.36 OPR/117.0.0.0"
        )
    }
    
    response = requests.get(URL, headers=HEADERS)
    soup = BeautifulSoup(response.content, 'html.parser')
    comps = []
    items = soup.find_all('div', class_='mud-alert mud-alert-text-normal mud-dense mud-elevation-0 info-field') # main page

    for item in items:
        title_div = item.find('div', class_='d-flex flex-column gap-1') # stats
        if title_div:
            comps.append({"title": title_div.text.strip().splitlines()})
    
    if comps and not None:
        split(comps)
    else:
        print("Wrong nickname.")
    
    def split(comps):
        keys = []
        values = []
        for comp in comps:
            comp = comp.get('title', 0)
            for item in comp:
                if ':' in item:
                    key, value = item.split(':', 1)
                    keys.append(key)
                    values.append(value)
            print_table(keys, values)
main()
input()
